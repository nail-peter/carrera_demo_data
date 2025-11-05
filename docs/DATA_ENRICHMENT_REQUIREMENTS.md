# Data Enrichment Requirements

## Overview

This document outlines how to enrich and expand the existing Carrera slot car track data while:
1. **Maintaining the exact same schema**
2. **Keeping realistic characteristics** (looks like it came from the track)
3. **Adding storylines** for engaging Tableau Pulse demonstrations
4. **Embedding patterns** for all 12 Tableau Pulse insight types

---

## Key Principles

### 1. Maintain Authenticity

**The data must look like it came directly from the slot car track**:

✅ **DO**:
- Use realistic lap times (mean ~6.6s, median ~6.2s)
- Include false starts and errors (~35% outliers)
- Maintain 2-lane track structure (controller 1 and 2)
- Keep exhibition/event context (concentrated activity on specific days)
- Use real company names and plausible driver names
- Preserve timestamp formats and data source IDs

❌ **DON'T**:
- Create perfect, synthetic-looking data
- Remove all errors (errors are realistic!)
- Generate uniform distributions
- Add fields or change schema
- Create impossible lap times (<1s, all identical, etc.)

### 2. Expand Timeline

**Current data**: Primarily 2 exhibition days (May 14 & 27, 2025)

**Enriched data**: 3-6 months of continuous activity
- Multiple exhibition days per month
- Practice sessions between exhibitions
- Mix of busy days and quiet days
- Seasonal patterns (if 6+ months)

**Why**: Tableau Pulse needs temporal data for trending, forecasting, and period-over-period analysis

### 3. Add Metrics (Within Existing Schema)

While keeping the schema unchanged, we can **infer and calculate** additional metrics from existing fields:

| Metric | Calculation | Purpose |
|--------|-------------|---------|
| Consistency Score | Std dev of lap times per driver | Driver skill indicator |
| Improvement Rate | Lap time change over time | Learning curves |
| Car Performance Index | Mean lap time per car | Equipment correlation |
| Session Activity | Laps per day/hour | Temporal patterns |
| Personal Best Improvement | Delta from previous PB | Progress tracking |
| Controller Balance | Lap count per controller | Track fairness |

### 4. Embed Storylines

Create 5-7 narrative arcs visible in the data:

1. **The Learner**: Driver improves 15% over 8 weeks
2. **The Veteran**: Consistently top-3, rarely wins
3. **The Rivals**: Two drivers trading victories
4. **The Comeback**: Poor start, then dramatic improvement
5. **Equipment Advantage**: Specific car model consistently faster
6. **Track Learning**: All drivers improve after track reconfiguration
7. **Company Competition**: Inter-company rivalry patterns

---

## Data Volume Targets

### Minimum for Tableau Pulse

| Entity | Current | Target (Minimum) | Target (Optimal) |
|--------|---------|------------------|------------------|
| Time Range | 2 days (concentrated) | 3 months | 6 months |
| Laps | 4,440 | 15,000+ | 30,000+ |
| Drivers | 128 | 40-60 active | 80-120 total |
| Cars | 13 (9 used) | 8-10 active | 12-15 total |
| Sessions | ~6 | 60-100 | 150-200 |
| Daily Activity | 2 peak days | 2-4 days/week | 3-5 days/week |

**Rationale**:
- **60+ data points per metric**: Needed for reliable forecasting
- **Multiple drivers per car**: Shows equipment correlation
- **Regular activity**: Enables trend detection
- **Variety in conditions**: Supports cross-metric analysis

---

## Enrichment Strategy

### Phase 1: Extend Timeline (3-6 months)

**Approach**: Generate additional exhibition and practice sessions

**Session Types**:

1. **Exhibition Days** (2-4 per month):
   - High activity: 200-400 laps per day
   - Many participants: 20-40 drivers
   - Peak hours: 9am-6pm
   - Mix of experience levels
   - Example dates: First and third Thursday/Friday each month

2. **Practice Sessions** (1-2 per week):
   - Medium activity: 50-150 laps per session
   - Fewer participants: 5-15 drivers
   - Shorter duration: 2-4 hours
   - Regulars only (subset of drivers)
   - Example times: Wednesday evenings, Saturday afternoons

3. **Setup/Testing** (occasional):
   - Low activity: 10-30 laps
   - Staff only: 2-5 designated drivers
   - Track configuration testing
   - Car tuning and calibration

**Date Distribution Pattern**:
```
Week 1: Mon (setup), Thu (exhibition), Fri (exhibition)
Week 2: Wed (practice)
Week 3: Thu (exhibition), Fri (exhibition), Sat (practice)
Week 4: Wed (practice)
```

### Phase 2: Create Driver Personas

**Strategy**: Assign characteristics to existing and new drivers

**Persona Types**:

1. **The Expert** (10-15% of drivers):
   - Consistent lap times: σ = 600-800ms
   - Mean lap time: 5.5-6.2s
   - Rare improvements (already skilled)
   - Low outlier rate: 15%
   - Example: Experienced Salesforce staff, racing enthusiasts

2. **The Intermediate** (40-50% of drivers):
   - Moderate consistency: σ = 1000-1400ms
   - Mean lap time: 6.2-7.0s
   - Steady improvements: 5-10% over time
   - Normal outlier rate: 30%
   - Example: Most corporate participants

3. **The Novice** (30-40% of drivers):
   - High variance: σ = 1500-2000ms
   - Mean lap time: 7.0-8.5s
   - Rapid improvements: 10-15% first month
   - High outlier rate: 45%
   - Example: First-time participants, casual drivers

4. **The Irregular** (5-10% of drivers):
   - Inconsistent attendance (1-2 sessions only)
   - Unknown skill level initially
   - May be any persona type
   - Example: Trade show visitors, one-time participants

**Implementation**:
```python
# Assign persona to each driver
personas = {
    'Peter Nägele': {'type': 'Expert', 'base_time': 5800, 'stddev': 700},
    'Stefan Birke': {'type': 'Intermediate', 'base_time': 6500, 'stddev': 1200},
    # ... etc
}
```

### Phase 3: Embed Car Performance Characteristics

**Strategy**: Make certain cars consistently faster/slower

**Car Performance Tiers**:

1. **Tier A - Fast** (2-3 cars):
   - Base lap time modifier: -8% to -5%
   - Examples: Porsche 911 GT3 R, Audi R8 LMS (specific models)
   - Used by top performers

2. **Tier B - Standard** (4-5 cars):
   - Base lap time modifier: -3% to +3%
   - Examples: Most race cars
   - General use

3. **Tier C - Fun/Novelty** (2-3 cars):
   - Base lap time modifier: +10% to +15%
   - Examples: VW Bus models (heavier, slower)
   - Used for fun races, handicap events

**Correlation Setup**:
```python
car_modifiers = {
    3: -0.07,  # Porsche 911 RSR (fast)
    7: -0.05,  # Lamborghini Huracan (fast)
    2: -0.02,  # Audi R8 (good)
    1: 0.00,   # Audi R8 alt (baseline)
    4: 0.02,   # Porsche alt (slight slower)
    5: 0.12,   # VW Bus (much slower, fun)
    6: 0.15,   # VW Bus alt (much slower, fun)
}

# Apply to driver's base time
actual_lap_time = driver_base_time * (1 + car_modifiers[car_id])
```

### Phase 4: Add Temporal Patterns

**Strategy**: Create day/time-based performance variations

**Patterns to Embed**:

1. **Time of Day Effect**:
   - Morning (9am-12pm): Optimal performance (-2%)
     - *Reason: Fresh drivers, cooler track*
   - Afternoon (12pm-5pm): Baseline (0%)
   - Evening (5pm-9pm): Slight fatigue (+1%)
     - *Reason: Driver fatigue after long exhibition day*

2. **Day of Week Effect**:
   - Weekdays: Normal activity
   - Weekends: +15% more spectators → +2% better performance
     - *Reason: More energy, crowd excitement*

3. **Learning Curve** (for novices):
   - First session: Baseline
   - Sessions 2-5: -2% per session (rapid learning)
   - Sessions 6-10: -1% per session (slower learning)
   - Sessions 10+: -0.5% per session (plateau)

4. **Track Condition Variation** (simulated):
   - Normal: 95% of time
   - "Hot track": 3% of time, +3% lap times
   - "Slippery": 2% of time, +5% lap times, more outliers

### Phase 5: Create Storylines

**Implementation**: Apply specific patterns to selected drivers

#### Storyline 1: "The Comeback Kid"

**Character**: Select 1-2 intermediate drivers

**Arc**:
- Weeks 1-2: Below average performance (7.5s mean)
- Week 3: First signs of improvement (7.0s)
- Week 4: Car upgrade (switch to Tier A car)
- Weeks 5-8: Rapid improvement (6.2s → 5.8s)
- Weeks 9+: Consistently top-3 finisher

**Data Pattern**:
```python
if driver == COMEBACK_KID and week <= 2:
    lap_time *= 1.12  # 12% slower initially
elif driver == COMEBACK_KID and 3 <= week <= 4:
    lap_time *= 1.05  # 5% slower
elif driver == COMEBACK_KID and week >= 5:
    improvement_rate = 0.97 ** (week - 4)  # Exponential improvement
    lap_time *= improvement_rate
```

**Tableau Pulse Insights**:
- ✓ Trend Change Alert (Week 4-5 shift)
- ✓ Unusual Values (Week 5 sudden improvement)
- ✓ Top Drivers (Weeks 6-8 climbing rankings)
- ✓ Correlated Metrics (Car change + performance improvement)

#### Storyline 2: "The Veteran"

**Character**: Select 2-3 expert drivers

**Arc**:
- Consistently good performance (5.8-6.0s mean)
- Very low variance (σ = 600ms)
- Always finishes top-5
- Rarely wins (beaten by aggressive drivers with outliers)
- Predictable, reliable

**Data Pattern**:
```python
if driver == VETERAN:
    base_time = 5900  # Fast baseline
    stddev = 600  # Very consistent
    outlier_rate = 0.10  # Rare errors
```

**Tableau Pulse Insights**:
- ✓ Current Trend (Flat, consistent line)
- ✓ Forecast (High confidence, narrow bands)
- ✓ Top Contributors (Reliable top performer)
- ✓ Concentrated Contribution (Part of dominant group)

#### Storyline 3: "The Rivalry"

**Characters**: Select 2 drivers of similar skill

**Arc**:
- Both intermediate-to-expert level
- Trade victories throughout season
- Lap times within 0.2s of each other
- Different strategies: One consistent, one aggressive
- Drive improvements in each other

**Data Pattern**:
```python
# Driver A: Consistent
rival_a_base = 6200
rival_a_stddev = 800

# Driver B: Aggressive (higher variance, occasional amazing laps)
rival_b_base = 6300  # Slightly slower average
rival_b_stddev = 1200  # Higher variance
rival_b_outlier_boost = 0.10  # 10% chance of amazing lap (-15%)

# Correlated improvements
if week > 5:
    improvement = 0.98 ** week  # Both improve together
    rival_a_base *= improvement
    rival_b_base *= improvement
```

**Tableau Pulse Insights**:
- ✓ Correlated Metrics (Both drivers improve together)
- ✓ Top Drivers/Detractors (Trade positions)
- ✓ Period-over-Period (Week-by-week competition)

#### Storyline 4: "Equipment Matters"

**Focus**: Specific car (e.g., Porsche 911 RSR, car_id=3)

**Arc**:
- Car consistently 7% faster than average
- Multiple drivers succeed with this car
- Drivers notice pattern, request this car
- Eventually creates "concentrated contribution" alert

**Data Pattern**:
```python
# Car 3 (Porsche 911 RSR) advantage
if car_id == 3:
    lap_time *= 0.93  # 7% faster

# Increase usage over time as drivers notice
if week >= 6:
    prob_choose_car3 = 0.30  # 30% of drivers request it
else:
    prob_choose_car3 = 0.11  # Normal distribution
```

**Tableau Pulse Insights**:
- ✓ Correlated Metrics (Car choice → Lap time)
- ✓ Concentrated Contribution (One car dominates wins)
- ✓ Top Contributors (Car 3 drives performance)

#### Storyline 5: "Track Learning Event"

**Focus**: Track reconfiguration at Week 6

**Arc**:
- Week 1-5: Normal performance
- Week 6 day 1: Track reconfigured (+10% lap times)
- Week 6-7: All drivers adapt
- Week 8+: New normal (-3% from original due to better layout)

**Data Pattern**:
```python
if week < 6:
    track_modifier = 1.00  # Baseline
elif week == 6 and session <= 2:
    track_modifier = 1.10  # 10% slower on new track
elif 6 <= week < 8:
    # Linear adaptation
    adaptation = (week - 6) * 0.065  # Gradual improvement
    track_modifier = 1.10 - adaptation
else:  # week >= 8
    track_modifier = 0.97  # Actually faster after learning

lap_time *= track_modifier
```

**Tableau Pulse Insights**:
- ✓ Trend Change Alert (Week 6 sudden change)
- ✓ Unexpected Values (Week 6 lap times)
- ✓ Period-over-Period (Pre vs. post reconfiguration)
- ✓ Common Contributors (All drivers affected)

---

## Data Generation Workflow

### Step 1: Prepare Base Data

```python
# Load existing data
cars = load_csv('schema/carv2.csv')
drivers = load_csv('schema/driverv2.csv')
existing_laps = load_csv('schema/lapv2.csv')

# Analyze existing patterns
analyze_driver_skills(existing_laps)
analyze_car_usage(existing_laps)
```

### Step 2: Define Timeline

```python
# Generate session schedule
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 10, 31)  # 6 months

sessions = generate_session_schedule(
    start_date,
    end_date,
    exhibition_days_per_month=3,
    practice_days_per_week=2
)
```

### Step 3: Assign Personas

```python
# Assign characteristics to drivers
for driver in drivers:
    driver.persona = assign_persona(driver)
    driver.base_lap_time = calculate_base_time(driver.persona)
    driver.stddev = calculate_stddev(driver.persona)
    driver.improvement_rate = calculate_improvement_rate(driver.persona)
```

### Step 4: Generate Laps

```python
for session in sessions:
    # Select drivers for this session
    active_drivers = select_drivers_for_session(
        session.type,
        session.date,
        drivers
    )

    # Assign cars
    for driver in active_drivers:
        car = assign_car(driver, session, storyline_rules)

        # Generate laps for this driver/car combo
        num_laps = random.randint(*session.lap_range)

        for lap_num in range(num_laps):
            lap_time = generate_lap_time(
                driver=driver,
                car=car,
                session=session,
                lap_num=lap_num,
                storylines=active_storylines
            )

            create_lap_record(driver, car, lap_time, session)
```

### Step 5: Apply Storylines

```python
# Apply storyline modifications to generated data
apply_comeback_kid_storyline(laps, selected_drivers[0])
apply_veteran_storyline(laps, selected_drivers[1:3])
apply_rivalry_storyline(laps, selected_drivers[3:5])
apply_equipment_storyline(laps, cars[2])  # Porsche 911 RSR
apply_track_learning_storyline(laps, week=6)
```

### Step 6: Add Realistic Noise

```python
# Add false starts, errors, pauses (maintain ~35% outlier ratio)
for lap in laps:
    if random.random() < 0.35:
        lap.laptime_raw__c = generate_outlier_time(
            lap.laptime_raw__c,
            outlier_type=random.choice(['fast', 'slow', 'very_slow'])
        )
```

### Step 7: Validate and Export

```python
# Validate generated data
validate_schema_compliance(laps)
validate_realistic_distributions(laps)
validate_storyline_detectability(laps)
validate_tableau_pulse_requirements(laps)

# Export to CSV (same schema)
export_csv(cars, 'data/processed/cars_enriched.csv')
export_csv(drivers, 'data/processed/drivers_enriched.csv')
export_csv(laps, 'data/processed/laps_enriched.csv')
```

---

## Validation Criteria

### 1. Schema Compliance

✅ **Required**:
- All columns match original schema exactly
- Data types match (String, Integer, Long, Datetime)
- Formats match (timestamp format, laptime format)
- No new columns added

### 2. Realistic Distributions

✅ **Required**:
- Mean lap time: 6.0-7.0s (realistic range)
- Median lap time: 5.8-6.8s
- Std dev: 1.2-1.6s (overall population)
- Outlier ratio: 30-40%
- Controller balance: 45-55% each

### 3. Storyline Detectability

✅ **Required**:
- Comeback Kid: Visible trend change in line chart
- Veteran: Predictable forecast with narrow confidence bands
- Rivalry: Cross-tabulation shows alternating winners
- Equipment: Significant difference in car model performance (p < 0.05)
- Track Learning: Clear before/after pattern

### 4. Tableau Pulse Requirements

✅ **Required** (from ENHANCED_QA_DISCOVER.md):
- At least 60 data points per key metric
- Clear correlations (r > 0.6 for designed correlations)
- Common contributors identifiable across metrics
- Temporal patterns for trending
- Dimensional hierarchies functional

---

## Next Steps

1. ✅ Schema documented
2. ✅ Enrichment requirements defined
3. ⏳ Build data generation script
4. ⏳ Generate enriched dataset
5. ⏳ Validate against criteria
6. ⏳ Create Tableau Pulse metric definitions
7. ⏳ Test Enhanced Q&A questions

---

## Notes for Data Generation Script

**Language**: Python 3.8+

**Key Libraries**:
- `pandas`: Data manipulation
- `numpy`: Statistical distributions
- `datetime`: Timestamp handling
- `csv`: CSV I/O

**Output Format**: CSV files with exact same schema as input

**Reproducibility**: Use fixed random seeds for consistent storylines

**Performance**: Target ~30,000 laps should generate in < 5 minutes
