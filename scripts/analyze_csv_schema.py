#!/usr/bin/env python3
"""
Analyze the existing CSV schema and data patterns from the Carrera slot car track
"""
import csv
import statistics
from collections import Counter, defaultdict
from datetime import datetime

def analyze_cars(filename):
    """Analyze car data"""
    print("=" * 80)
    print("CAR DATA ANALYSIS")
    print("=" * 80)

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        cars = list(reader)

    print(f"\nTotal cars: {len(cars)}")
    print("\nCar names:")
    for i, car in enumerate(cars, 1):
        print(f"  {i}. [{car['id__c']}] {car['name__c']}")

    print("\nManufacturers:")
    manufacturers = Counter(car['manufacturer__c'] for car in cars if car['manufacturer__c'])
    for mfr, count in manufacturers.most_common():
        print(f"  {mfr}: {count}")

    print("\nScales:")
    scales = Counter(car['scale__c'] for car in cars if car['scale__c'])
    for scale, count in scales.items():
        print(f"  {scale}: {count}")

    return cars

def analyze_drivers(filename):
    """Analyze driver data"""
    print("\n" + "=" * 80)
    print("DRIVER DATA ANALYSIS")
    print("=" * 80)

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        drivers = list(reader)

    print(f"\nTotal drivers: {len(drivers)}")

    print("\nSample drivers (first 10):")
    for i, driver in enumerate(drivers[:10], 1):
        name = f"{driver['firstname__c']} {driver['lastname__c']}"
        company = driver['company__c'] if driver['company__c'] else 'N/A'
        print(f"  {i}. [{driver['id__c']}] {name} - {company}")

    print("\nCompanies (top 10):")
    companies = Counter(driver['company__c'] for driver in drivers if driver['company__c'])
    for company, count in companies.most_common(10):
        print(f"  {company}: {count}")

    return drivers

def analyze_laps(filename):
    """Analyze lap data"""
    print("\n" + "=" * 80)
    print("LAP DATA ANALYSIS")
    print("=" * 80)

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        laps = list(reader)

    print(f"\nTotal lap records: {len(laps)}")

    # Extract lap times (in milliseconds)
    lap_times = []
    for lap in laps:
        try:
            if lap['laptime_raw__c'] and lap['laptime_raw__c'].strip():
                time_ms = int(lap['laptime_raw__c'])
                if time_ms > 0:
                    lap_times.append(time_ms)
        except (ValueError, KeyError):
            pass

    if lap_times:
        print(f"\nValid lap times: {len(lap_times)}")
        print(f"  Min: {min(lap_times)/1000:.3f}s ({min(lap_times)}ms)")
        print(f"  Max: {max(lap_times)/1000:.3f}s ({max(lap_times)}ms)")
        print(f"  Mean: {statistics.mean(lap_times)/1000:.3f}s")
        print(f"  Median: {statistics.median(lap_times)/1000:.3f}s")

        # Realistic lap times (3-10 seconds = 3000-10000ms)
        realistic = [t for t in lap_times if 3000 <= t <= 10000]
        if realistic:
            print(f"\nRealistic lap times (3-10s): {len(realistic)} ({len(realistic)/len(lap_times)*100:.1f}%)")
            print(f"  Min: {min(realistic)/1000:.3f}s")
            print(f"  Max: {max(realistic)/1000:.3f}s")
            print(f"  Mean: {statistics.mean(realistic)/1000:.3f}s")
            print(f"  Median: {statistics.median(realistic)/1000:.3f}s")
            print(f"  Std Dev: {statistics.stdev(realistic)/1000:.3f}s")

    # Controllers
    print("\nControllers:")
    controllers = Counter(lap['controller_id__c'] for lap in laps if lap['controller_id__c'])
    for ctrl, count in controllers.most_common():
        print(f"  {ctrl}: {count}")

    # Event types
    print("\nEvent types:")
    events = Counter(lap['event_type__c'] for lap in laps if lap['event_type__c'])
    for event, count in events.most_common():
        print(f"  {event}: {count}")

    # Drivers in laps
    print("\nUnique drivers in laps:")
    driver_ids = set(lap['driver_id__c'] for lap in laps if lap['driver_id__c'])
    print(f"  {len(driver_ids)} unique drivers")

    # Cars in laps
    print("\nUnique cars in laps:")
    car_ids = set(lap['car_id__c'] for lap in laps if lap['car_id__c'])
    print(f"  {len(car_ids)} unique cars")

    # Date range
    timestamps = []
    for lap in laps:
        if lap['timestamp__c']:
            try:
                # Parse format: "14.05.2025 18:13:59"
                ts = datetime.strptime(lap['timestamp__c'], "%d.%m.%Y %H:%M:%S")
                timestamps.append(ts)
            except:
                pass

    if timestamps:
        print(f"\nDate range:")
        print(f"  Earliest: {min(timestamps)}")
        print(f"  Latest: {max(timestamps)}")
        print(f"  Span: {(max(timestamps) - min(timestamps)).days} days")

    return laps

if __name__ == '__main__':
    cars = analyze_cars('schema/carv2.csv')
    drivers = analyze_drivers('schema/driverv2.csv')
    laps = analyze_laps('schema/lapv2.csv')

    print("\n" + "=" * 80)
    print("SCHEMA EXTRACTION COMPLETE")
    print("=" * 80)
