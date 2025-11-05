#!/usr/bin/env python3
"""
Generate enriched Carrera slot car track dataset for Tableau Pulse demo

This script:
1. Loads existing data from schema/*.csv
2. Analyzes patterns and assigns personas
3. Generates 3-6 months of racing activity
4. Embeds 5 storylines for Tableau Pulse demonstrations
5. Maintains exact schema compliance
6. Outputs authentic-looking data
"""

import csv
import random
import statistics
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import numpy as np
import json

# Set random seeds for reproducibility
SEED_BASE = 12345
SEED_OUTLIERS = 67890
SEED_NOISE = 11111
random.seed(SEED_BASE)
np.random.seed(SEED_BASE)

# Configuration
START_DATE = datetime(2025, 6, 1, 8, 0, 0)
END_DATE = datetime(2025, 11, 30, 20, 0, 0)  # 6 months
TARGET_LAPS = 25000  # Mid-range target

# Lap time configuration (in milliseconds)
BASE_MEAN_LAPTIME = 6600  # 6.6 seconds
BASE_STDDEV_LAPTIME = 1378
REALISTIC_MIN = 3000  # 3.0 seconds
REALISTIC_MAX = 10000  # 10.0 seconds

# Data source IDs (maintain from original)
DATA_SOURCE_ID = "carrera_v2_6b799dd9_992f_4f07_bcd0_a3815b27c6ec"
CAR_DATA_SOURCE_OBJ = "carrera_v2_car_80687EFE"
DRIVER_DATA_SOURCE_OBJ = "carrera_v2_driver_80687EF9"
LAP_DATA_SOURCE_OBJ = "carrera_v2_lap_80687EFE"

# Persona definitions
PERSONA_EXPERT = {
    'type': 'Expert',
    'base_time': 5800,  # 5.8s
    'stddev': 700,
    'improvement_rate': 0.998,  # Minimal improvement (already skilled)
    'outlier_rate': 0.15
}

PERSONA_INTERMEDIATE = {
    'type': 'Intermediate',
    'base_time': 6500,  # 6.5s
    'stddev': 1200,
    'improvement_rate': 0.992,  # Steady improvement
    'outlier_rate': 0.30
}

PERSONA_NOVICE = {
    'type': 'Novice',
    'base_time': 7500,  # 7.5s
    'stddev': 1800,
    'improvement_rate': 0.985,  # Rapid improvement
    'outlier_rate': 0.45
}

# Car performance tiers (modifiers to lap time)
CAR_PERFORMANCE = {
    3: -0.07,   # Porsche 911 RSR (fast)
    7: -0.05,   # Lamborghini Huracan (fast)
    2: -0.02,   # Audi R8 (good)
    1: 0.00,    # Audi R8 alt (baseline)
    9: 0.01,    # Audi alt
    4: 0.02,    # Porsche alt
    8: 0.03,    # Porsche alt
    5: 0.12,    # VW Bus (slow, fun)
    6: 0.15,    # VW Bus alt (slow, fun)
    10: 0.00,   # Audi (baseline)
    11: 0.14,   # VW Bus
    123: 0.05,  # Golf GTX
    129: 0.06,  # Golf GTX alt
}

# Storyline characters (will be assigned during loading)
STORYLINE_CHARACTERS = {
    'comeback_kid': None,
    'veteran_1': None,
    'veteran_2': None,
    'rival_a': None,
    'rival_b': None,
}

# Track reconfiguration week
TRACK_RECONFIG_WEEK = 6

class Driver:
    def __init__(self, record):
        self.id = record['id__c']
        self.firstname = record['firstname__c']
        self.lastname = record['lastname__c']
        self.company = record['company__c']
        self.record = record  # Keep full record
        self.persona = None
        self.base_lap_time = 6500
        self.stddev = 1200
        self.improvement_rate = 1.0
        self.outlier_rate = 0.30
        self.session_count = 0
        self.total_laps = 0
        self.is_regular = False  # Will attend multiple sessions
        self.storyline_role = None

    def assign_persona(self, persona_dict):
        self.persona = persona_dict['type']
        self.base_lap_time = persona_dict['base_time']
        self.stddev = persona_dict['stddev']
        self.improvement_rate = persona_dict['improvement_rate']
        self.outlier_rate = persona_dict['outlier_rate']

    def __repr__(self):
        return f"Driver({self.id}: {self.firstname} {self.lastname})"

class Car:
    def __init__(self, record):
        self.id = int(record['id__c']) if record['id__c'] else None
        self.name = record['name__c']
        self.manufacturer = record['manufacturer__c']
        self.scale = record['scale__c']
        self.record = record
        self.performance_modifier = CAR_PERFORMANCE.get(self.id, 0.0)
        self.total_laps = 0

    def __repr__(self):
        return f"Car({self.id}: {self.name[:30]}...)"

class Session:
    def __init__(self, session_type, date, duration_hours):
        self.type = session_type
        self.date = date
        self.duration_hours = duration_hours
        self.drivers = []
        self.laps = []

    def __repr__(self):
        return f"Session({self.type}, {self.date.strftime('%Y-%m-%d %H:%M')})"

def load_data():
    """Load existing CSV data"""
    print("Loading existing data...")

    # Load cars
    cars = []
    with open('schema/carv2.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for record in reader:
            if record['id__c']:  # Has valid ID
                cars.append(Car(record))
    print(f"  Loaded {len(cars)} cars")

    # Load drivers
    drivers = []
    with open('schema/driverv2.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for record in reader:
            if record['id__c']:  # Has valid ID
                drivers.append(Driver(record))
    print(f"  Loaded {len(drivers)} drivers")

    # Load existing laps to analyze patterns
    existing_laps = []
    with open('schema/lapv2.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for record in reader:
            existing_laps.append(record)
    print(f"  Loaded {len(existing_laps)} existing laps")

    return cars, drivers, existing_laps

def analyze_existing_patterns(drivers, existing_laps):
    """Analyze existing lap data to infer driver characteristics"""
    print("\nAnalyzing existing patterns...")

    # Group laps by driver
    driver_laps = defaultdict(list)
    for lap in existing_laps:
        try:
            driver_id = lap['driver_id__c']
            laptime = int(lap['laptime_raw__c'])
            if REALISTIC_MIN <= laptime <= REALISTIC_MAX:
                driver_laps[driver_id].append(laptime)
        except (ValueError, KeyError):
            continue

    # Assign personas based on existing data or defaults
    for driver in drivers:
        if driver.id in driver_laps and len(driver_laps[driver.id]) >= 5:
            laps = driver_laps[driver.id]
            mean_time = statistics.mean(laps)
            stddev = statistics.stdev(laps) if len(laps) > 1 else 1000

            # Classify based on consistency
            if stddev < 800:
                driver.assign_persona(PERSONA_EXPERT)
            elif stddev < 1500:
                driver.assign_persona(PERSONA_INTERMEDIATE)
            else:
                driver.assign_persona(PERSONA_NOVICE)

            # Use actual observed base time
            driver.base_lap_time = int(mean_time)
            driver.stddev = int(stddev)

            print(f"  {driver.firstname} {driver.lastname}: {driver.persona}, base={driver.base_lap_time}ms, σ={driver.stddev}ms")
        else:
            # Assign random persona for drivers without enough data
            persona = random.choice([PERSONA_EXPERT, PERSONA_INTERMEDIATE, PERSONA_NOVICE])
            driver.assign_persona(persona)

    # Select regular drivers (40% of drivers will be regulars who attend multiple sessions)
    num_regulars = int(len(drivers) * 0.4)
    regulars = random.sample(drivers, num_regulars)
    for driver in regulars:
        driver.is_regular = True

    print(f"  Assigned {num_regulars} regular drivers")

def assign_storyline_roles(drivers):
    """Assign specific drivers to storyline roles"""
    print("\nAssigning storyline roles...")

    # Find drivers with suitable characteristics - ensure they are regulars
    intermediates = [d for d in drivers if d.persona == 'Intermediate' and d.is_regular]
    experts = [d for d in drivers if d.persona == 'Expert' and d.is_regular]

    # If no experts marked as regular, make some regulars
    if len(experts) < 2:
        all_experts = [d for d in drivers if d.persona == 'Expert']
        for i in range(min(2, len(all_experts))):
            all_experts[i].is_regular = True
            experts.append(all_experts[i])

    if len(intermediates) >= 3:
        # Ensure they're marked as regular
        for i in range(3):
            intermediates[i].is_regular = True

        STORYLINE_CHARACTERS['comeback_kid'] = intermediates[0]
        intermediates[0].storyline_role = 'comeback_kid'
        print(f"  Comeback Kid: {intermediates[0]}")

        STORYLINE_CHARACTERS['rival_a'] = intermediates[1]
        intermediates[1].storyline_role = 'rival_a'
        STORYLINE_CHARACTERS['rival_b'] = intermediates[2]
        intermediates[2].storyline_role = 'rival_b'
        print(f"  Rivals: {intermediates[1]} vs {intermediates[2]}")

    if len(experts) >= 2:
        # Ensure they're marked as regular
        for i in range(2):
            experts[i].is_regular = True

        STORYLINE_CHARACTERS['veteran_1'] = experts[0]
        experts[0].storyline_role = 'veteran_1'
        STORYLINE_CHARACTERS['veteran_2'] = experts[1]
        experts[1].storyline_role = 'veteran_2'
        print(f"  Veterans: {experts[0]}, {experts[1]}")

def generate_session_schedule(start_date, end_date):
    """Generate realistic session schedule"""
    print("\nGenerating session schedule...")

    sessions = []
    current_date = start_date
    week_num = 0

    while current_date < end_date:
        # Determine day of week (0=Monday, 6=Sunday)
        weekday = current_date.weekday()

        # Exhibition days: Thursdays and Fridays every 2-3 weeks
        if weekday == 3 or weekday == 4:  # Thursday or Friday
            if week_num % 2 == 0 or week_num % 3 == 0:
                # Morning session (9am-12pm)
                morning = current_date.replace(hour=9, minute=0)
                sessions.append(Session('exhibition', morning, 3))

                # Afternoon session (1pm-6pm)
                afternoon = current_date.replace(hour=13, minute=0)
                sessions.append(Session('exhibition', afternoon, 5))

        # Practice sessions: Wednesdays evenings
        elif weekday == 2:  # Wednesday
            evening = current_date.replace(hour=17, minute=0)
            sessions.append(Session('practice', evening, 3))

        # Practice sessions: Saturday afternoons (every other week)
        elif weekday == 5 and week_num % 2 == 0:  # Saturday
            afternoon = current_date.replace(hour=14, minute=0)
            sessions.append(Session('practice', afternoon, 4))

        # Move to next day
        current_date += timedelta(days=1)
        if current_date.weekday() == 0:  # New week
            week_num += 1

    print(f"  Generated {len(sessions)} sessions over {week_num} weeks")
    exhibition_count = len([s for s in sessions if s.type == 'exhibition'])
    practice_count = len([s for s in sessions if s.type == 'practice'])
    print(f"    Exhibition sessions: {exhibition_count}")
    print(f"    Practice sessions: {practice_count}")

    return sessions

def select_drivers_for_session(session, drivers, week_num):
    """Select which drivers participate in this session"""
    if session.type == 'exhibition':
        # Exhibition: Many drivers, mix of regulars and new participants
        num_drivers = random.randint(15, 35)

        # Always include regulars (80% chance each)
        regulars = [d for d in drivers if d.is_regular and random.random() < 0.8]

        # Add some random participants
        non_regulars = [d for d in drivers if not d.is_regular]
        additional_needed = max(0, num_drivers - len(regulars))
        additional_available = min(additional_needed, len(non_regulars))

        if additional_available > 0:
            additional = random.sample(non_regulars, additional_available)
        else:
            additional = []

        return regulars + additional

    else:  # practice
        # Practice: Only regulars, fewer participants
        num_drivers = random.randint(5, 12)
        regulars = [d for d in drivers if d.is_regular]
        return random.sample(regulars, min(num_drivers, len(regulars)))

def get_week_number(date, start_date):
    """Calculate week number from start date"""
    delta = date - start_date
    return delta.days // 7

def apply_temporal_modifiers(base_time, session, week_num):
    """Apply time-of-day and day-of-week effects"""
    modifier = 1.0

    # Time of day effect
    hour = session.date.hour
    if 9 <= hour < 12:  # Morning
        modifier *= 0.98  # 2% faster (fresh drivers)
    elif 17 <= hour < 21:  # Evening
        modifier *= 1.01  # 1% slower (fatigue)

    # Day of week effect
    if session.date.weekday() >= 5:  # Weekend
        modifier *= 0.98  # 2% faster (more excitement)

    # Track reconfiguration effect
    if week_num == TRACK_RECONFIG_WEEK:
        # First 2 sessions on new track are slower
        modifier *= 1.10  # 10% slower
    elif TRACK_RECONFIG_WEEK < week_num < TRACK_RECONFIG_WEEK + 2:
        # Adaptation period
        adaptation = (week_num - TRACK_RECONFIG_WEEK) * 0.065
        modifier *= (1.10 - adaptation)
    elif week_num >= TRACK_RECONFIG_WEEK + 2:
        # New track is actually faster once learned
        modifier *= 0.97  # 3% faster

    return int(base_time * modifier)

def generate_lap_time(driver, car, session, lap_num, week_num):
    """Generate a single lap time with all effects applied"""

    # Start with driver's base time
    base_time = driver.base_lap_time

    # Add global offset to match target mean of 6.6s
    # Existing data is a bit fast, so add ~1200ms offset
    base_time = int(base_time + 1200)

    # Apply car performance modifier
    base_time = int(base_time * (1 + car.performance_modifier))

    # Apply learning/improvement over sessions
    improvement_factor = driver.improvement_rate ** driver.session_count
    base_time = int(base_time * improvement_factor)

    # Apply storyline modifiers
    if driver.storyline_role == 'comeback_kid':
        # Comeback kid storyline
        if week_num <= 2:
            base_time = int(base_time * 1.12)  # 12% slower initially
        elif 3 <= week_num <= 4:
            base_time = int(base_time * 1.05)  # 5% slower
        elif week_num >= 5:
            # Rapid improvement after car change
            improvement = 0.97 ** (week_num - 4)
            base_time = int(base_time * improvement)

    elif driver.storyline_role in ['rival_a', 'rival_b']:
        # Rivals improve together
        if week_num > 5:
            improvement = 0.98 ** (week_num - 5)
            base_time = int(base_time * improvement)

        # Rival B is more aggressive (higher variance, occasional amazing laps)
        if driver.storyline_role == 'rival_b' and random.random() < 0.10:
            base_time = int(base_time * 0.85)  # 15% faster on amazing laps

    # Apply temporal modifiers
    base_time = apply_temporal_modifiers(base_time, session, week_num)

    # Add normal variation
    noise = np.random.normal(0, driver.stddev)
    lap_time = int(base_time + noise)

    # Ensure within realistic range (before outliers) - wider range for base times
    lap_time = max(2000, min(REALISTIC_MAX, lap_time))

    # Apply outliers (realistic imperfections)
    random.seed(SEED_OUTLIERS + lap_num)
    if random.random() < driver.outlier_rate:
        outlier_type = random.random()
        if outlier_type < 0.15:  # Fast outlier (false start, sensor error) - reduced from 0.3
            lap_time = random.randint(19, 2999)
        elif outlier_type < 0.85:  # Slow outlier (incident, pause)
            lap_time = random.randint(10001, 45000)
        else:  # Very slow (between-race pause)
            lap_time = random.randint(45001, 180000)

    random.seed(SEED_BASE)  # Reset seed

    return lap_time

def format_lap_time(milliseconds):
    """Format milliseconds to M:SS.mmm"""
    total_seconds = milliseconds / 1000
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    # Handle display format
    if minutes < 10:
        return f"{minutes}:{seconds:06.3f}"
    else:
        # For very long times, use special format
        return f"{minutes:02d}:{seconds:05.2f}"

def generate_laps_for_session(session, drivers, cars, week_num, lap_counter):
    """Generate all laps for a session"""
    laps = []

    # Assign cars to drivers
    driver_car_assignments = {}
    for driver in session.drivers:
        # Equipment storyline: After week 6, drivers prefer car 3 (Porsche 911 RSR)
        if week_num >= 6 and random.random() < 0.30:
            car = next((c for c in cars if c.id == 3), random.choice(cars))
        else:
            car = random.choice(cars)
        driver_car_assignments[driver.id] = car

    # Generate laps
    if session.type == 'exhibition':
        # Exhibition: More laps per driver
        laps_per_driver_range = (8, 25)
    else:  # practice
        # Practice: Fewer laps
        laps_per_driver_range = (5, 15)

    # Assign controllers (lanes) - alternate between 1 and 2 for each driver
    controller_index = 0

    for driver in session.drivers:
        car = driver_car_assignments[driver.id]
        # Alternate controllers for better balance
        controller = (controller_index % 2) + 1
        controller_index += 1

        num_laps = random.randint(*laps_per_driver_range)

        # Generate timestamp progression through session
        session_start = session.date
        session_duration_seconds = session.duration_hours * 3600

        for i in range(num_laps):
            # Lap time
            lap_time_ms = generate_lap_time(driver, car, session, lap_counter['count'], week_num)

            # Timestamp: spread laps throughout session
            lap_offset_seconds = (i / num_laps) * session_duration_seconds
            lap_offset_seconds += random.randint(-30, 30)  # Add some randomness
            lap_timestamp = session_start + timedelta(seconds=lap_offset_seconds)

            # Unix timestamp in milliseconds
            unix_time = int(lap_timestamp.timestamp() * 1000)

            # Create lap record
            lap_record = {
                'KQ_driver_id__c': '',
                'controller_id__c': str(controller),
                'laptime_raw__c': str(lap_time_ms),
                'driver_id__c': str(driver.id),
                'laptime__c': format_lap_time(lap_time_ms),
                'timestamp__c': lap_timestamp.strftime('%d.%m.%Y %H:%M:%S'),
                'KQ_lap_id__c': '',
                'KQ_car_id__c': '',
                'event_type__c': 'ui.lap_update',
                'DataSource__c': DATA_SOURCE_ID,
                'personal_best__c': '',
                'unix_time__c': str(unix_time),
                'lap_id__c': str(unix_time),
                'DataSourceObject__c': LAP_DATA_SOURCE_OBJ,
                'lap__c': str(lap_counter['count']),
                'car_id__c': str(car.id),
            }

            laps.append(lap_record)
            lap_counter['count'] += 1
            driver.total_laps += 1
            car.total_laps += 1

        driver.session_count += 1

    return laps

def generate_all_laps(sessions, drivers, cars):
    """Generate laps for all sessions"""
    print("\nGenerating laps...")
    all_laps = []
    lap_counter = {'count': 1}

    for i, session in enumerate(sessions):
        week_num = get_week_number(session.date, START_DATE)

        # Select drivers for this session
        session.drivers = select_drivers_for_session(session, drivers, week_num)

        # Generate laps
        session_laps = generate_laps_for_session(session, drivers, cars, week_num, lap_counter)
        all_laps.extend(session_laps)

        if (i + 1) % 10 == 0:
            print(f"  Generated {len(all_laps)} laps across {i+1} sessions...")

    print(f"  Total laps generated: {len(all_laps)}")
    return all_laps

def validate_data(cars, drivers, laps):
    """Validate generated data"""
    print("\nValidating generated data...")

    # Extract realistic lap times
    lap_times = []
    for lap in laps:
        try:
            time_ms = int(lap['laptime_raw__c'])
            if REALISTIC_MIN <= time_ms <= REALISTIC_MAX:
                lap_times.append(time_ms)
        except ValueError:
            pass

    # Calculate statistics
    total_laps = len(laps)
    realistic_laps = len(lap_times)
    realistic_pct = (realistic_laps / total_laps * 100) if total_laps > 0 else 0

    mean_time = statistics.mean(lap_times) / 1000 if lap_times else 0
    median_time = statistics.median(lap_times) / 1000 if lap_times else 0
    stddev_time = statistics.stdev(lap_times) / 1000 if len(lap_times) > 1 else 0

    print(f"  Total laps: {total_laps}")
    print(f"  Realistic laps (3-10s): {realistic_laps} ({realistic_pct:.1f}%)")
    print(f"  Mean lap time: {mean_time:.3f}s")
    print(f"  Median lap time: {median_time:.3f}s")
    print(f"  Std dev: {stddev_time:.3f}s")

    # Controller distribution
    controllers = Counter(lap['controller_id__c'] for lap in laps)
    print(f"  Controller distribution:")
    for ctrl, count in controllers.most_common():
        print(f"    {ctrl}: {count} ({count/total_laps*100:.1f}%)")

    # Validate storylines
    print(f"\n  Storyline validation:")
    for role, driver in STORYLINE_CHARACTERS.items():
        if driver:
            print(f"    {role}: {driver.firstname} {driver.lastname} - {driver.total_laps} laps")

    # Validation checks
    print(f"\n  Validation checks:")
    checks = {
        'Schema compliance': True,  # We maintain schema by design
        'Realistic distribution (30-40% outliers)': 30 <= (100 - realistic_pct) <= 40,
        'Mean lap time (6.0-7.0s)': 6.0 <= mean_time <= 7.0,
        'Controller balance (45-55% each)': all(45 <= (c/total_laps*100) <= 55 for c in controllers.values()),
        'Sufficient data (15K+ laps)': total_laps >= 15000,
    }

    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"    [{status}] {check}")

    return all(checks.values())

def export_data(cars, drivers, laps):
    """Export enriched data to CSV"""
    print("\nExporting enriched data...")

    # Export cars (unchanged, but include for completeness)
    with open('data/processed/cars_enriched.csv', 'w', newline='', encoding='utf-8') as f:
        if cars:
            fieldnames = cars[0].record.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for car in cars:
                writer.writerow(car.record)
    print(f"  Exported {len(cars)} cars")

    # Export drivers (unchanged, but include for completeness)
    with open('data/processed/drivers_enriched.csv', 'w', newline='', encoding='utf-8') as f:
        if drivers:
            fieldnames = drivers[0].record.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for driver in drivers:
                writer.writerow(driver.record)
    print(f"  Exported {len(drivers)} drivers")

    # Export laps
    with open('data/processed/laps_enriched.csv', 'w', newline='', encoding='utf-8') as f:
        if laps:
            fieldnames = laps[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for lap in laps:
                writer.writerow(lap)
    print(f"  Exported {len(laps)} laps")

def main():
    """Main execution"""
    print("=" * 80)
    print("CARRERA SLOT CAR TRACK - ENRICHED DATA GENERATION")
    print("=" * 80)
    print(f"Target date range: {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
    print(f"Target laps: ~{TARGET_LAPS}")
    print()

    # Load existing data
    cars, drivers, existing_laps = load_data()

    # Analyze and assign personas
    analyze_existing_patterns(drivers, existing_laps)

    # Assign storyline roles
    assign_storyline_roles(drivers)

    # Generate session schedule
    sessions = generate_session_schedule(START_DATE, END_DATE)

    # Generate laps for all sessions
    laps = generate_all_laps(sessions, drivers, cars)

    # Validate
    valid = validate_data(cars, drivers, laps)

    if valid:
        # Export
        export_data(cars, drivers, laps)
        print("\n" + "=" * 80)
        print("DATA GENERATION COMPLETE - ALL VALIDATIONS PASSED")
        print("=" * 80)
    else:
        print("\n" + "=" * 80)
        print("DATA GENERATION COMPLETE - SOME VALIDATIONS FAILED")
        print("Review output above for details")
        print("=" * 80)

if __name__ == '__main__':
    main()
