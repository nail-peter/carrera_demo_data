# Data Generation Strategy

## Overview

This document outlines the approach for generating and enriching the Carrera Slot Car Track demo dataset.

## Data Volume Recommendations

### Minimum for Tableau Pulse

- **Time range**: 3-6 months of historical data
- **Frequency**: Multiple race sessions per day (morning, afternoon, evening)
- **Records**: 5,000-10,000 lap records minimum
- **Dimensions**:
  - 6-10 drivers
  - 4-6 cars
  - 1-2 track configurations
  - 50-100 race sessions

### Optimal for Rich Insights

- **Time range**: 12 months for full seasonal patterns
- **Records**: 20,000-50,000 lap records
- **Dimensions**:
  - 12-15 drivers (including some who come and go)
  - 8-10 cars (different models and configurations)
  - 2-3 track configurations
  - 200-300 race sessions

---

## Data Generation Approach

### Phase 1: Base Data Structure

1. Define realistic baseline performance for each driver/car combination
2. Establish track section characteristics (difficulty, length, ideal speed)
3. Create time-based patterns (day of week, time of day effects)
4. Set up environmental factors (temperature, humidity impacts)

### Phase 2: Inject Patterns & Storylines

1. **Learning curves**: New drivers improve over time
2. **Wear and tear**: Car performance degrades, then improves after maintenance
3. **Rivalry patterns**: Certain driver pairs consistently compete
4. **Home advantage**: Some drivers excel on specific track configurations
5. **Consistency vs. volatility**: Some drivers very consistent, others erratic

### Phase 3: Add Anomalies & Outliers

1. **Positive outliers** (2% of data):
   - Perfect laps (ideal conditions + skill)
   - Post-upgrade performance spikes
   - "In the zone" exceptional sessions

2. **Negative outliers** (3% of data):
   - Near-crashes (recovery laps)
   - Technical failures
   - First-time track attempts
   - Adverse conditions

### Phase 4: Correlation Building

Design correlated patterns:

| Metric A | Metric B | Correlation | Reason |
|----------|----------|-------------|---------|
| Average Speed | Lap Time | Strong Negative (-0.85) | Faster = better time |
| Pit Stop Count | Final Position | Moderate Negative (-0.55) | More stops = worse position |
| Track Temperature | Lap Time | Moderate Positive (0.45) | Heat affects grip |
| Driver Experience | Consistency | Strong Positive (0.75) | Experience = stability |
| Battery Voltage | Top Speed | Strong Positive (0.80) | Power affects speed |

---

## Storyline Templates

### Storyline 1: The Comeback Kid

**Character**: Driver "Alex Chen"

**Arc**:
- Week 1-2: Poor performance (learning new car)
- Week 3-4: Gradual improvement
- Week 5: Car upgrade/tuning
- Week 6-8: Dramatic improvement
- Week 9-12: Consistent top-3 finisher

**Data patterns**:
- Lap times decrease by 15% over period
- Consistency improves (lower std deviation)
- Creates clear "trend change alert"

---

### Storyline 2: The Veteran's Consistency

**Character**: Driver "Morgan Silva"

**Arc**:
- Consistently good performance
- Small performance degradation mid-season (car wear)
- Returns to form after maintenance
- Always finishes top-5, rarely wins

**Data patterns**:
- Low variance in lap times
- Predictable forecasts
- Few outliers
- "Reliable contributor" pattern

---

### Storyline 3: The Rivalry

**Characters**: "Jordan Lee" vs. "Taylor Park"

**Arc**:
- Both start strong
- Trade victories throughout season
- Close lap times (within 0.1s)
- Different strategies (one more aggressive, one more consistent)

**Data patterns**:
- Correlated improvements
- "Concentrated contribution" to wins
- Alternating "top driver" status

---

### Storyline 4: Equipment Matters

**Focus**: Red Lightning Car Model

**Arc**:
- Consistently outperforms other models
- Multiple drivers succeed with this car
- Clear correlation between car choice and performance

**Data patterns**:
- "Top contributor" at car model level
- "Concentrated contribution" alert
- Cross-driver consistency with this car

---

### Storyline 5: Track Evolution

**Focus**: Learning the new track layout

**Arc**:
- Track reconfiguration in Week 6
- All drivers struggle initially
- Lap times improve as drivers learn
- Different sections show different learning curves

**Data patterns**:
- Clear "trend change alert" at Week 6
- Period-over-period shows degradation then improvement
- "Current trend" shows learning curve

---

## Environmental Variables

### Time-based Patterns

**Time of Day**:
- Morning (9am-12pm): Cooler, better grip, faster times (-2%)
- Afternoon (12pm-5pm): Warmer, slower times (baseline)
- Evening (5pm-9pm): Cooling down, moderate times (-1%)

**Day of Week**:
- Weekdays: Regular practice, moderate performance
- Weekends: Higher competition, better effort, more spectators (+3% performance)

**Seasonal** (if using full year):
- Spring/Fall: Optimal temperatures
- Summer: Higher temperatures, slightly slower
- Winter: Heating system, consistent indoor conditions

### Condition-based Patterns

**Track Temperature**:
- 18-22°C: Optimal (baseline)
- 23-26°C: Slightly slower (+0.05s per lap)
- <18°C: Reduced grip (+0.03s per lap)

**Crowd Size**:
- Small (<20): Practice atmosphere
- Medium (20-50): Normal event
- Large (50+): Special event, drivers perform better (-2% lap times)

---

## Data Quality Rules

### Realism Constraints

1. **Lap Time Ranges**:
   - Minimum realistic lap time: 3.0s
   - Maximum before considered "failed": 8.0s
   - Typical range: 3.2-4.5s

2. **Speed Ranges**:
   - Minimum: 80 km/h (slow sections)
   - Maximum: 250 km/h (straightaways)
   - Average: 140-180 km/h

3. **Pit Stop Rules**:
   - Minimum duration: 2s
   - Maximum duration: 15s
   - Typical: 3-5s
   - Frequency: 0-2 per race

### Consistency Rules

1. **Driver Skill Levels**:
   - Expert: σ = 0.05s (very consistent)
   - Intermediate: σ = 0.15s
   - Novice: σ = 0.30s (high variance)

2. **Car Reliability**:
   - High reliability: <1% technical issues
   - Medium: 2-3% issues
   - Low: 5-8% issues

3. **Improvement Rates**:
   - Novice improvement: 10-15% over first month
   - Intermediate: 5-8% over first month
   - Expert: 2-3% (already optimized)

---

## Technical Implementation Notes

### Random Seed Strategy

Use fixed random seeds for reproducibility:
- Base patterns: Seed 12345
- Outlier injection: Seed 67890
- Environmental noise: Seed 11111

### Distribution Types

1. **Lap Times**: Log-normal distribution (right-skewed)
2. **Speeds**: Normal distribution within range constraints
3. **Pit Stops**: Poisson distribution (discrete events)
4. **Outliers**: Manual injection at specific points

### Validation Checks

After generation, validate:
- [ ] All insight types can be demonstrated
- [ ] Correlations exist as designed
- [ ] Storylines are detectable visually
- [ ] No impossible values (negative times, etc.)
- [ ] Sufficient data for forecasting
- [ ] Clear dimension hierarchies

---

## Enhanced Q&A (Discover) Integration

### Critical Requirements for Q&A Success

To ensure all Enhanced Q&A features work optimally, the dataset must support:

#### 1. Cross-Metric Analysis Chains

Design interconnected metric groups that answer multi-metric questions:

**Performance Chain**:
- Practice Session Attendance → Lap Time Improvement → Race Position → Win Rate
- *Example Q&A*: "How does practice frequency correlate with race performance across drivers?"

**Equipment Chain**:
- Maintenance Frequency → Car Reliability Score → Race Completion Rate → Average Position
- *Example Q&A*: "Show me the relationship between car maintenance and race outcomes"

**Environmental Chain**:
- Track Temperature → Tire Grip Index → Lap Times → Speed Metrics
- *Example Q&A*: "What's the connection between track conditions and performance metrics?"

**Strategy Chain**:
- Pit Stop Count → Total Pit Time → Time Lost → Final Position
- *Example Q&A*: "How do pit stop strategies impact race results?"

#### 2. Common Contributors Design

Structure data so multiple metrics share obvious common drivers:

**Example**: Track Section "Hairpin Turn"
- Drives slowest lap time segments ✓
- Drives highest incident rates ✓
- Drives most lane change attempts ✓
- *Q&A can identify this section as common contributor across metrics*

**Example**: Driver "Alex Chen" (during improvement period)
- Top contributor to average speed increases ✓
- Top contributor to lap time improvements ✓
- Top contributor to consistency gains ✓
- *Q&A can highlight as key driver of multiple positive trends*

#### 3. Dimensional Breakdown Hierarchies

Create clear hierarchies that support drill-down questions:

**Time Hierarchy**:
```
Year → Quarter → Month → Week → Day → Session → Lap
```
- Supports: "Show me performance over time at different granularities"

**Location Hierarchy**:
```
Track Configuration → Lane → Section → Segment
```
- Supports: "Break down lap times by track location"

**Driver Hierarchy**:
```
Experience Level → Team → Individual Driver
```
- Supports: "Compare performance across driver experience levels"

**Equipment Hierarchy**:
```
Car Model → Individual Car → Configuration → Component
```
- Supports: "Analyze performance by car type and configuration"

#### 4. Scope Refinement Patterns

Ensure filters work naturally with conversational queries:

**Time-based Scopes**:
- "Last 7 days", "This month", "Q3", "Last quarter", "This season"
- Generate date ranges that align with common business questions

**Condition-based Scopes**:
- "High temperature sessions" (>24°C)
- "Weekend races" (Saturday-Sunday)
- "Large crowd events" (>50 spectators)
- "Morning sessions" (before noon)

**Performance-based Scopes**:
- "Top performing drivers" (top 25%)
- "Recent maintenance" (within 14 days)
- "Competitive races" (position changes >5)

#### 5. Metric Correlation Candidates

For each primary metric, define 3-5 correlation candidates:

**Primary Metric: Lap Time**
- Correlation Candidates:
  1. Average Speed (strong negative)
  2. Track Temperature (moderate positive)
  3. Pit Stop Count (moderate positive)
  4. Driver Experience Level (moderate negative)
  5. Car Maintenance Days Since (weak positive)

**Primary Metric: Race Position**
- Correlation Candidates:
  1. Lap Time Consistency (strong negative)
  2. Total Pit Time (moderate positive)
  3. Starting Position (moderate positive)
  4. Overtake Success Rate (strong negative)
  5. Incident Count (moderate positive)

### Data Generation Rules for Q&A

#### Rule 1: Avoid Ambiguity

❌ **Bad**: Dimension values with typos or variations
- "Red Lightning", "red lightning", "RedLightning", "Red Ltng"

✅ **Good**: Consistent, clean values
- Always: "Red Lightning"

#### Rule 2: Create Obvious Patterns

Make correlations and patterns detectable:

✅ **Strong correlation example**:
```python
# When track_temp increases, lap_time increases proportionally
lap_time_base = 3.5
temp_effect = (track_temp - 20) * 0.02  # 0.02s per degree above 20°C
lap_time = lap_time_base + temp_effect + small_random_noise
```

✅ **Common contributor example**:
```python
# "Hairpin Turn" section affects multiple metrics negatively
if track_section == "Hairpin Turn":
    lap_segment_time *= 1.4  # Slower
    incident_probability *= 2.5  # More incidents
    overtake_attempts *= 1.8  # More attempts
```

#### Rule 3: Support Dynamic Filtering

Ensure dimensional values support natural filtering:

✅ **Time filters**:
- Include metadata: is_weekend, time_of_day_category, season
- Enable questions like: "Show me weekend performance"

✅ **Performance filters**:
- Include rankings: driver_rank_this_month, car_percentile
- Enable questions like: "Focus on top 3 drivers"

✅ **Condition filters**:
- Include categories: temp_category (cool/normal/hot), crowd_size_category
- Enable questions like: "Only analyze hot weather sessions"

#### Rule 4: Sufficient Data for Trend Detection

**Minimum Requirements**:
- At least 30 data points per metric for basic trends
- At least 60 data points for seasonal patterns
- At least 90 data points for reliable forecasting
- At least 10 data points per dimensional category

**Example**:
```python
# For driver "Alex Chen" to show learning trend
# Need: 60+ laps across 8+ weeks
# Frequency: 2-3 sessions per week, 3-4 laps per session
```

#### Rule 5: Validate Q&A Questions During Generation

After generating data, test these questions:

**Must Work** (Basic functionality):
- [ ] "Show me lap time trends"
- [ ] "Which driver has the fastest average?"
- [ ] "Compare morning vs evening sessions"
- [ ] "Break down by car model"

**Should Work** (Core features):
- [ ] "What's driving the improvement in lap times?"
- [ ] "How do pit stops correlate with race position?"
- [ ] "Show unexpected performance changes"
- [ ] "Which track sections are slowest?"

**Nice to Have** (Advanced features):
- [ ] "How do track temperature and car model both affect lap times across different drivers?"
- [ ] "Which factors are common contributors to speed and consistency?"
- [ ] "Show me performance for top 3 drivers during weekend races with large crowds"

---

## Validation Checks (Updated)

After generation, validate:
- [ ] All insight types can be demonstrated
- [ ] Correlations exist as designed (test with scatter plots)
- [ ] Storylines are detectable visually
- [ ] No impossible values (negative times, etc.)
- [ ] Sufficient data for forecasting (60+ points per metric)
- [ ] Clear dimension hierarchies work in drill-downs
- [ ] **Enhanced Q&A questions return expected results**
- [ ] **Cross-metric analysis reveals designed patterns**
- [ ] **Common contributors are correctly identified**
- [ ] **Dynamic filtering works with natural language scopes**
- [ ] **Dimensional breakdowns align with hierarchies**

---

## Next Steps

1. Receive actual schema from user
2. Map schema to these patterns and Q&A requirements
3. Review example data to understand format
4. Build data generation scripts with Q&A validation
5. Generate and validate dataset
6. Test all demo questions from ENHANCED_QA_DISCOVER.md
7. Create Tableau Pulse configuration guide
8. Build demo question playbook
