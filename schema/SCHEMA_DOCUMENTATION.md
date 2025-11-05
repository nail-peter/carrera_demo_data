# Carrera Slot Car Track - Schema Documentation

## Overview

This document describes the actual schema extracted from the real Carrera slot car track demo data. The data comes from actual exhibitions/trade shows where participants from various companies raced on a Carrera Digital 1:32 scale slot car track.

---

## Data Files

### 1. carv2.csv - Car Information

**Purpose**: Stores information about each slot car available on the track

**Record Count**: 13 cars

**Schema**:

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `id__c` | Integer | Unique car identifier | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 123, 129 |
| `name__c` | String | Full car name/model | "Porsche 911 GT 3 R", "Audi R8 LMS GT3", "VW Bus T2b" |
| `manufacturer__c` | String | Car manufacturer | Carrera, Volkswagen |
| `scale__c` | String | Model scale | 1:32, 1:10 |
| `tyres__c` | String | Tire type | Original, hard |
| `digital_analog__c` | String | Digital or analog | digital |
| `magnets__c` | String | Has magnets | yes |
| `brakes__c` | String | Has brakes | yes, null |
| `fuel__c` | String | Fuel level (simulated) | 50%, null |
| `speed__c` | Integer | Speed setting | 1, 120, null |
| `color__c` | String | Car color | red, null |
| `decoder_type__c` | String | Decoder type | Carrera (default), typeA |
| `logo__c` | String | Logo filename | generic.png, audi.png, logo.png |
| `laps__c` | Integer | Total laps completed | 5-1775 |
| `active__c` | String | Is car active | yes |
| `timestamp__c` | Datetime | Last update timestamp | 07.05.2025 09:35:40 |
| `unix_time__c` | Long | Unix timestamp (ms) | 1746603340345 |
| `DataSource__c` | String | Data source ID | carrera_v2_6b799dd9_992f_4f07_bcd0_a3815b27c6ec |
| `DataSourceObject__c` | String | Source object type | carrera_v2_car_80687EFE |
| `KQ_id__c` | String | KQ identifier | empty |
| `interval_counter__c` | Integer | Interval counter | 1-1743 |
| `tags__c` | String | Tags (JSON array) | [] |

**Car Types**:
- **Race Cars** (9 cars): Porsche 911 GT3 R, Audi R8 LMS GT3 evo II, Lamborghini Huracan GT3 Evo2
- **Fun Cars** (3 cars): VW Bus T2b "Porsche Renndienst", "Peace and Love"
- **Custom** (2 cars): Golf GTX (special builds)

---

### 2. driverv2.csv - Driver Information

**Purpose**: Stores information about each participant/driver

**Record Count**: 128 drivers

**Schema**:

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `id__c` | String | Unique driver identifier | 2, 3, 8, 13, 15, t7, 999, kjsdhf7889H |
| `firstname__c` | String | First name | Peter, Stefan, Lewis, Tom |
| `lastname__c` | String | Last name | Nägele, Birke, Hamilton, SuperSpeed |
| `company__c` | String | Company name | Salesforce, Merck, Deutsche Bank, DHL |
| `team__c` | String | Team name | Salesforce, Tabloids Racing, null |
| `start_no__c` | String | Start number | 7, 99, 123123123, null |
| `start_no_color_background__c` | String | Number BG color (hex) | #00FF00, #bcc3bc, null |
| `start_no_color_text__c` | String | Number text color (hex) | #FFFFFF, #000000, null |
| `start_no_color_border__c` | String | Number border color (hex) | #0000FF, #3589e1, null |
| `start_no_text_style__c` | String | Text style | normal, italic |
| `name_short__c` | String | Short name/nickname | TS, TG, Mat, Wil, Dat, 123 |
| `image__c` | String | Image URL | https://example.com/driver-image.jpg, cdvfile://... |
| `active__c` | String | Is driver active | yes |
| `timestamp__c` | Datetime | Last update timestamp | 14.05.2025 08:31:49 |
| `unix_time__c` | Long | Unix timestamp (ms) | 1747204309293 |
| `DataSource__c` | String | Data source ID | carrera_v2_6b799dd9_992f_4f07_bcd0_a3815b27c6ec |
| `DataSourceObject__c` | String | Source object type | carrera_v2_driver_80687EF9 |
| `KQ_id__c` | String | KQ identifier | empty |

**Driver Types**:
- **Exhibition Participants** (125 drivers): Real people from companies at trade shows
- **Fun/Famous Names** (3 drivers): Lewis Hamilton, Michael Schumacher, Kiki Räikkönen

**Top Companies**:
1. Salesforce: 18 drivers
2. Merck: 4 drivers
3. Deutsche Bank: 3 drivers
4. Others: Allianz, DHL, Siemens, Mercedes-Benz, etc.

---

### 3. lapv2.csv - Lap Records

**Purpose**: Stores individual lap time records for each driver/car combination

**Record Count**: 4,440 laps

**Schema**:

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `lap_id__c` | Long | Unique lap identifier (timestamp-based) | 1747239238700 |
| `driver_id__c` | Integer | Reference to driver ID | 42, 102, 112, 113 |
| `car_id__c` | Integer | Reference to car ID | 3, 7, 1, 2, 4, 5, 6 |
| `controller_id__c` | String | Controller/lane number | 1, 2, controller1, ctrl-007 |
| `lap__c` | Integer | Lap number for this session | 1-1481 |
| `laptime_raw__c` | Integer | Lap time in milliseconds | 421-16744567 |
| `laptime__c` | String | Formatted lap time | 0:05.689, 0:07.003, 09:39:96 |
| `event_type__c` | String | Event type | ui.lap_update, browser.lap_update, lap, new_lap |
| `personal_best__c` | Boolean | Is personal best | True, False, empty |
| `timestamp__c` | Datetime | Lap timestamp | 27.05.2025 17:03:01 |
| `unix_time__c` | Long | Unix timestamp (ms) | 1748358180720 |
| `DataSource__c` | String | Data source ID | carrera_v2_6b799dd9_992f_4f07_bcd0_a3815b27c6ec |
| `DataSourceObject__c` | String | Source object type | carrera_v2_lap_80687EFE |
| `KQ_driver_id__c` | String | KQ driver identifier | empty |
| `KQ_lap_id__c` | String | KQ lap identifier | empty |
| `KQ_car_id__c` | String | KQ car identifier | empty |

**Lap Time Statistics** (Realistic range 3-10 seconds):

- **Count**: 2,921 laps (65.8% of total)
- **Range**: 3.076s - 9.997s
- **Mean**: 6.600s
- **Median**: 6.194s
- **Std Dev**: 1.378s

**Data Quality Notes**:
- 65.8% of laps are realistic (3-10 seconds)
- Remaining 34.2% includes:
  - Very fast times (<3s): False starts, sensor errors
  - Very slow times (>10s): Pauses, incidents, recovery laps
  - Extremely slow (>60s): Between-race pauses, technical issues

**Controllers**:
- Controller 1: 2,401 laps
- Controller 2: 2,031 laps
- *(Indicates 2-lane track configuration)*

**Date Range**:
- Primary dates: May 14, 2025 and May 27, 2025 (exhibition days)
- Full range: April 28, 2025 to April 25, 2026 (361 days)
- Most data concentrated in 2-3 exhibition days

---

## Relationships

```
Driver (driverv2.csv)
  └─── has many ───> Lap (lapv2.csv)
                      └─── references ───> Car (carv2.csv)

driver_id__c in lapv2.csv → id__c in driverv2.csv
car_id__c in lapv2.csv → id__c in carv2.csv
```

**Foreign Keys**:
- `lapv2.driver_id__c` → `driverv2.id__c`
- `lapv2.car_id__c` → `carv2.id__c`

**Note**: Not all drivers have laps, not all cars have been used

---

## Data Source Context

### Real-World Context

This data comes from **actual Carrera Digital slot car track exhibitions** at trade shows and corporate events. The data characteristics reflect real usage:

1. **Exhibition Format**:
   - Two-lane digital track (controller 1 and 2)
   - 1:32 scale Carrera Digital cars
   - Multiple sessions throughout exhibition days
   - Participants from various companies racing against each other

2. **Participant Profile**:
   - Corporate employees from exhibition attendees
   - Mix of experience levels (first-timers to racing enthusiasts)
   - Companies include Salesforce customers and partners

3. **Data Collection**:
   - Automated from Carrera Digital track system
   - Real-time lap time recording
   - Includes false starts, incidents, and pauses (realistic!)
   - Some manual entries (browser.lap_update events)

### Data Characteristics for Demo Generation

When generating enriched data, maintain these characteristics:

**✅ Keep**:
- Lap time distribution (mean ~6.6s, median ~6.2s, std dev ~1.4s)
- Mix of realistic and unrealistic times (65% realistic ratio)
- Two-lane track structure (controller 1 and 2)
- Company/corporate context
- Exhibition/event day concentration
- Mix of race cars and fun cars
- Variety in driver experience levels

**✅ Add for Tableau Pulse**:
- Storylines (improvement arcs, rivalries, etc.)
- Intentional correlations (car performance, driver learning, etc.)
- Seasonal/temporal patterns
- Environmental factors (simulated track conditions)
- Additional metrics (speed, incidents, pit stops - if extending schema)

---

## Data Generation Guidelines

### Lap Time Generation

**Realistic Lap Times** (65% of data):
```python
# Base realistic lap time: 3.0-10.0 seconds (3000-10000 ms)
base_mean = 6600  # milliseconds
base_stddev = 1378  # milliseconds

# Use log-normal distribution for slight right skew
import numpy as np
mu = np.log(base_mean)
sigma = 0.21  # Tuned for realistic spread

lap_time_ms = int(np.random.lognormal(mu, sigma))
lap_time_ms = max(3000, min(10000, lap_time_ms))  # Clamp to range
```

**Outlier Times** (35% of data):
```python
# Fast outliers (10%): False starts, sensor issues
if random.random() < 0.10:
    lap_time_ms = random.randint(19, 2999)

# Slow outliers (25%): Pauses, incidents, recovery
elif random.random() < 0.25:
    lap_time_ms = random.randint(10001, 60000)
    # Occasionally very slow (between-race pauses)
    if random.random() < 0.05:
        lap_time_ms = random.randint(60000, 300000)
```

### Driver Skill Levels

**Infer from existing lap time consistency**:
```python
# Calculate driver's lap time standard deviation
driver_laps = get_laps_for_driver(driver_id)
realistic_laps = [l for l in driver_laps if 3000 <= l <= 10000]
driver_stddev = np.std(realistic_laps)

if driver_stddev < 800:
    skill_level = "Expert"  # Very consistent
elif driver_stddev < 1500:
    skill_level = "Intermediate"
else:
    skill_level = "Novice"  # High variance
```

### Time Format

Lap times are stored in two formats:

1. **Raw milliseconds** (`laptime_raw__c`): Integer value
   - Example: 5689 = 5.689 seconds

2. **Formatted string** (`laptime__c`): "M:SS.mmm" format
   - Example: "0:05.689" = 5.689 seconds
   - Example: "09:39:96" = 9 minutes 39.96 seconds (likely data error or special format)

```python
def format_lap_time(ms):
    """Format milliseconds to M:SS.mmm"""
    total_seconds = ms / 1000
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:06.3f}"
```

### Timestamp Format

**String format**: `DD.MM.YYYY HH:MM:SS`
- Example: "27.05.2025 17:03:01"

**Unix timestamp**: Milliseconds since epoch
- Example: 1748358180720

```python
from datetime import datetime

dt = datetime.strptime("27.05.2025 17:03:01", "%d.%m.%Y %H:%M:%S")
unix_ms = int(dt.timestamp() * 1000)
```

### ID Generation

**Driver IDs**: Mix of sequential integers and custom strings
- Mostly integers: 2, 3, 8, 13, 15, etc.
- Some custom: "t7", "999", "kjsdhf7889H"

**Car IDs**: Sequential integers 1-123, 129

**Lap IDs**: Use unix timestamp in milliseconds
- Ensures uniqueness
- Matches existing pattern

---

## Next Steps

1. ✅ Schema extracted and documented
2. ⏳ Design data enrichment strategy
3. ⏳ Create data generation scripts
4. ⏳ Add storylines and patterns for Tableau Pulse
5. ⏳ Validate generated data
6. ⏳ Create Tableau Pulse metric definitions

---

## Appendix: Sample Records

### Sample Car Record
```csv
id__c,name__c,manufacturer__c,scale__c,laps__c,active__c
3,Porsche 911 RSR,Carrera,1:32,1775,yes
```

### Sample Driver Record
```csv
id__c,firstname__c,lastname__c,company__c,active__c
2,Peter,Nägele,Salesforce,yes
```

### Sample Lap Record
```csv
lap_id__c,driver_id__c,car_id__c,controller_id__c,laptime_raw__c,laptime__c,timestamp__c
1748358180720,112,7,2,5043,0:05.043,27.05.2025 17:03:06
```
