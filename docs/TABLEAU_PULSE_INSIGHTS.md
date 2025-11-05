# Tableau Pulse Insights - Design Guide

## Overview

This document outlines how to structure the Carrera Slot Car Track dataset to maximize Tableau Pulse's analytical capabilities.

## Tableau Pulse Insight Types & Data Requirements

### 1. Period Over Period Change (Always Enabled)

**What it detects**: Compares metric values between two time periods

**Data requirements for Carrera demo**:
- Time dimension with regular intervals (race sessions, days, weeks)
- Metrics that change over time (lap times, average speeds, positions)
- Example storyline: "Weekend performance vs. weekday performance"

**Demo storylines**:
- Compare morning vs. afternoon race sessions
- Week-over-week performance trends
- Pre-maintenance vs. post-maintenance performance

---

### 2. Correlated Metrics (Tableau+ feature)

**What it detects**: Identifies relationships between different metrics

**Data requirements**:
- Multiple related metrics (up to 5 correlation candidates)
- Sufficient data points to establish patterns

**Demo storylines**:
- **Positive correlation**: Higher average speed → Better lap times
- **Negative correlation**: More pit stops → Lower final position
- **No correlation**: Driver age → Performance (to show non-relationships)

**Metrics to correlate**:
- Lap time vs. average speed
- Pit stop duration vs. race position
- Track temperature vs. lap time
- Number of overtakes vs. final position
- Battery voltage vs. speed

---

### 3. Record-level Outliers

**What it detects**: Extremely high or low values for individual records

**Data requirements**:
- Record identifier field (unique lap ID, race ID)
- Metrics with occasional extreme values

**Demo storylines**:
- Exceptionally fast lap (driver hitting perfect line)
- Unusually slow lap (near-crash recovery)
- Extreme speed readings (car malfunction)

**Implementation**:
- Insert 2-3% outlier records
- Document reasons (car upgrades, track conditions, errors)

---

### 4. Forecast (Tableau+ feature)

**What it detects**: Projects expected values with confidence ranges

**Data requirements**:
- Historical time-series data
- Sufficient data points for pattern detection
- Regular time intervals

**Demo storylines**:
- Predict next race session lap times
- Forecast maintenance needs based on usage patterns
- Project season championship standings

---

### 5. Current Trend

**What it detects**: Rate of change, direction, and fluctuations

**Data requirements**:
- Time-series data showing directional movement
- Enough data points to establish trend

**Demo storylines**:
- Driver improving over time (learning curve)
- Car degrading over race season (wear and tear)
- Track conditions affecting all drivers

---

### 6. Trend Change Alert

**What it detects**: New trends that vary significantly from current trend

**Data requirements**:
- Established baseline trend
- Sudden significant changes in pattern

**Demo storylines**:
- Sudden performance improvement after car tuning
- Performance drop after track reconfiguration
- Weather impact causing trend shift

---

### 7. Unexpected Values

**What it detects**: Metrics higher or lower than expected range

**Data requirements**:
- Historical baseline to establish expected ranges
- Occasional values outside normal distribution

**Demo storylines**:
- Lap time unexpectedly fast (new racing line discovered)
- Power consumption unexpectedly low (technical issue)
- Crowd size unexpectedly high (special event)

---

### 8. Goal and Threshold Breakdown

**What it detects**: Progress toward defined goals

**Data requirements**:
- Defined goals or thresholds
- Breakdown by dimensions

**Demo storylines**:
- Target lap time: < 3.5 seconds
- Goal: Complete 100 laps without incident
- Threshold: Maintain speed > 150 km/h on straights

---

### 9. Top Drivers

**What it detects**: Dimension members that changed most in same direction as metric

**Data requirements**:
- Dimensional data (drivers, cars, tracks)
- Change data showing movement

**Demo storylines**:
- Which drivers improved most this month?
- Which cars contributed most to speed increases?
- Which track sections saw biggest time improvements?

---

### 10. Top Detractors

**What it detects**: Members that changed most in opposite direction

**Data requirements**:
- Same as Top Drivers but showing negative impact

**Demo storylines**:
- Which drivers' performance declined?
- Which cars lost the most speed?
- Which factors led to slower lap times?

---

### 11. Concentrated Contribution Alert

**What it detects**: Small number of entities representing 50%+ of contribution

**Data requirements**:
- Metrics where concentration is possible
- Dimensional breakdown

**Demo storylines**:
- 2 out of 8 drivers winning 80% of races (dominance)
- One car model winning most races
- Single track section causing most incidents

---

### 12. Top/Bottom Contributors

**What it detects**: Highest and lowest performing dimension members

**Data requirements**:
- Dimensional data with performance metrics
- Time range for comparison

**Demo storylines**:
- Fastest drivers this week
- Slowest track sections
- Most reliable cars vs. most problematic cars

---

## Data Best Practices for Tableau Pulse

### Optimal Data Characteristics

✅ **Time-series data**: Events that evolve over time
✅ **Aggregated metrics**: Key business numbers (lap times, speeds, positions)
✅ **Clear dimensions**: Well-defined categories (drivers, cars, tracks, sessions)
✅ **Clean and structured**: Consistent formatting, validated data
✅ **Regular intervals**: Consistent time periods for better trending

### Data to Avoid

❌ **Highly granular data**: Minute-by-minute logs (too detailed)
❌ **Single point-in-time**: One-off surveys or static datasets
❌ **Irregular intervals**: Inconsistent time periods
❌ **Messy dimensions**: Inconsistent naming or categories

---

## Enhanced Q&A (Discover) Optimization

### 2025 Features to Leverage

1. **Cross-metric analysis**: Design questions comparing multiple metrics
   - "How does speed correlate with lap time across different drivers?"
   - "Compare top drivers' pit stop strategies"

2. **Conversational queries**: Natural language questions
   - "Which driver improved the most last week?"
   - "Show me unexpected performance changes"

3. **Multi-language support**: Ensure dimension names are clear in English
   - Use descriptive names: "Driver Name" not "drv_nm"
   - Avoid abbreviations in key fields

---

## Recommended Carrera Dataset Structure

### Core Dimensions

1. **Time**: DateTime, Date, Time of Day, Session ID, Week, Month, Season
2. **Driver**: Driver ID, Name, Age, Experience Level, Team
3. **Car**: Car ID, Model, Color, Manufacturer, Configuration
4. **Track**: Track ID, Section, Configuration, Lane
5. **Event**: Event Type (Race, Practice, Qualifying, Exhibition)
6. **Conditions**: Weather, Temperature, Humidity, Crowd Size

### Core Metrics

1. **Performance**: Lap Time, Average Speed, Top Speed, Position
2. **Operations**: Pit Stops, Pit Duration, Lane Changes, Overtakes
3. **Reliability**: Incidents, Crashes, Technical Issues, Battery Level
4. **Engagement**: Spectator Count, Audience Reactions, Photo Opportunities

### Calculated Metrics (for correlation)

- Speed/Time ratio
- Consistency score (std dev of lap times)
- Improvement rate
- Reliability index

---

## Storytelling Elements

### Narrative Arcs to Build Into Data

1. **The Underdog**: Driver who starts poorly but improves dramatically
2. **The Veteran**: Experienced driver with consistent performance
3. **The Rookie**: New driver with erratic but improving results
4. **The Rivalry**: Two drivers with competing strategies
5. **The Equipment Factor**: One car consistently outperforming
6. **The Track Evolution**: Performance changes as drivers learn the track
7. **The Maintenance Impact**: Clear before/after maintenance patterns
8. **The Event Effect**: Special events drawing larger crowds and better performance

---

## Next Steps

1. Map real schema to these requirements
2. Identify which insight types to prioritize
3. Design specific storylines for demo scenarios
4. Generate data with intentional patterns
5. Validate with Tableau Pulse
