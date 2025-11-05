# Enhanced Q&A (Discover) - Advanced Capabilities 🚀

## Overview

Enhanced Q&A (Discover) is Tableau Pulse's advanced conversational AI feature that enables natural language exploration of metrics with cross-metric intelligence and correlation analysis.

---

## Cross-Metric Intelligence & Correlation Analysis

Enhanced Q&A goes beyond single-metric analysis to reveal relationships across groups of metrics:

### Core Capabilities

- **Cross-metric reasoning**: Synthesizes insights across multiple metrics to detect co-movements and correlations
- **Common contributors analysis**: Identifies shared drivers across different metrics
- **Correlated metrics insights**: Suggests metrics that move together in interesting ways (coming soon)
- **Multi-metric trend analysis**: Reveals connections where "vitals of business happen"

### Carrera Demo Application

Our dataset will support cross-metric analysis such as:
- Lap time performance correlated with car maintenance schedules
- Driver improvement rates vs. practice session frequency
- Track temperature impact across speed, lap time, and incident rates
- Pit stop efficiency relationship to final race position

---

## Supported Statistical Insight Types 📊

The system can answer questions about these advanced analytics:

| Insight Type | Description | Carrera Demo Example |
|--------------|-------------|---------------------|
| **Period-over-Period Change (POPC)** | How metrics changed vs. previous periods | Weekend vs. weekday lap times |
| **Unusual Change Detection** | Flags unexpectedly high/low values based on trends | Sudden lap time improvement after car tuning |
| **Trend Analysis** | Detects steady patterns or new emerging trends | Driver learning curve over first month |
| **Top/Bottom Contributors** | Highlights which values drive the most change | Which drivers improved lap times most |
| **Top Drivers & Detractors** | Shows which values changed most between periods | Track sections with biggest time changes |
| **Outliers** | Finds extreme values that stand out | Exceptionally fast or slow laps |
| **Pace to Goal** | Predicts if you're on track | Progress toward championship goals (coming soon) |

---

## Advanced Question Types for Carrera Demo 💡

### Multi-Metric Exploration Questions

**Template Questions:**
- "How are our campaign metrics performing across regions?"
- "What's driving the correlation between customer acquisition and churn rates?"
- "Which marketing channels show the strongest relationship to revenue growth?"
- "How do our top-performing products relate to customer satisfaction scores?"

**Adapted for Carrera Slot Car Track:**

✅ **Performance Analysis:**
- "How are our racing performance metrics trending across different drivers?"
- "What's driving the correlation between lap times and pit stop frequency?"
- "Which car models show the strongest relationship to race wins?"
- "How do top-performing drivers' speeds relate to their consistency scores?"

✅ **Cross-Metric Insights:**
- "Show me the relationship between track temperature and average lap times"
- "How does car maintenance frequency correlate with race position?"
- "Which factors contribute most to both speed and consistency?"
- "What's the connection between practice session attendance and race performance?"

✅ **Equipment & Performance:**
- "How do different car configurations impact lap times and reliability?"
- "Which car models perform best across speed and consistency metrics?"
- "Show me the correlation between battery voltage and top speed across all races"
- "How does lane position affect both lap times and overtake success?"

---

### Dynamic Filtering & Scope Refinement

**Template Questions:**
- "Show me sales performance, but focus on our top-performing products"
- "Let's just look at the Northeast region for these metrics"
- "How does this compare to last quarter for our enterprise customers?"

**Adapted for Carrera Racing:**

✅ **Driver Focus:**
- "Show me lap time performance, but focus on our top 3 drivers"
- "Let's just look at the weekend races for these metrics"
- "How does performance compare to last month for rookie drivers?"

✅ **Condition-Based Filtering:**
- "Show me all metrics during high-temperature conditions"
- "Focus on evening race sessions when analyzing speed trends"
- "Compare performance only for races with large crowds"

✅ **Equipment Filtering:**
- "Analyze lap times for the Red Lightning car model only"
- "Show me metrics for cars that have had recent maintenance"
- "Focus on Track Configuration A when comparing driver performance"

---

### Cross-Dimensional Analysis

**Template Questions:**
- "Break down these metrics by customer segment and region"
- "Which product categories are driving the increase in our key metrics?"
- "Show me performance across different time granularities"

**Adapted for Carrera Racing:**

✅ **Multi-Dimensional Breakdowns:**
- "Break down lap time performance by driver experience level and track configuration"
- "Which car models are driving the improvement in our race metrics?"
- "Show me speed performance across different times of day and days of week"

✅ **Hierarchical Analysis:**
- "Compare performance by driver, then by car model, then by track section"
- "Break down incidents by track configuration, lane, and section"
- "Show pit stop efficiency by session type, driver, and car"

✅ **Temporal Cross-Sections:**
- "How do morning vs. evening sessions compare across all drivers?"
- "Show me weekly performance trends broken down by car model"
- "Compare month-over-month improvements by driver experience level"

---

## Current Limitations to Consider ⚠️

Based on customer feedback, these areas need attention when designing the demo:

### Issues with Correlations

- **Correlation definition difficulties**: May have trouble with correlations defined in metric definitions
- **Explicit correlation queries**: Enhanced Q&A sometimes can't use correlations even when explicitly asking about both metrics

**Demo Mitigation Strategy:**
- Include correlation candidates in metric definitions
- Prepare fallback questions that work around correlation limitations
- Have both direct metric queries and correlation queries ready

### Data Consistency Challenges

- **Category creation**: May create non-existing categories on the fly
- **Data matching issues**: Some metric breakdowns show data that doesn't match detail links
- **Variability**: Results can vary between identical questions asked back-to-back

**Demo Mitigation Strategy:**
- Use clean, well-defined dimension values with no ambiguity
- Test questions multiple times before live demos
- Have consistent naming conventions across all dimensions
- Avoid edge cases or ambiguous dimension values

### Scope Limitations

- **Metrics Layer only**: Operates on the Metrics Layer, not total published data sources
- **Active metrics only**: Only functions for metrics that have been created and actively followed
- **Single data source**: Limited to single data source per query

**Demo Implications:**
- All key metrics must be pre-defined in Tableau Pulse
- Demo account should have metrics actively followed
- Design dataset as single cohesive data source
- Cannot demonstrate cross-data-source queries

---

## Best Practices for Carrera Demo Dataset 🎯

### Optimal Data Scenarios

Our Carrera dataset includes all recommended patterns:

✅ **Time-Series Data**:
- Lap times, speeds, positions evolving over race sessions and days
- Driver performance trending over weeks and months
- Car reliability metrics tracked across maintenance cycles

✅ **Clear Dimensions**:
- Driver (Name, ID, Experience Level, Team)
- Car (Model, ID, Configuration, Maintenance Status)
- Track (Configuration, Section, Lane)
- Time (Date, Time of Day, Session Type, Week, Month)
- Conditions (Temperature, Weather, Crowd Size)

✅ **Aggregated Business Metrics**:
- Average lap time
- Top speed
- Consistency score (standard deviation)
- Win rate
- Incident rate
- Pit stop efficiency

✅ **Related Metric Groups**:
Metrics that naturally correlate:
- **Performance Chain**: Practice attendance → Lap time improvement → Race position
- **Equipment Chain**: Maintenance frequency → Car reliability → Race completion rate
- **Environmental Chain**: Track temperature → Tire grip → Lap times
- **Strategy Chain**: Pit stop count → Total pit time → Final position

---

## Question Types That Work Best

### ✅ Trend & Performance Questions

**Examples for Carrera:**
- "How are our lap time metrics trending across all drivers?"
- "Show me speed performance over the last month"
- "Which drivers have improving trends in consistency?"
- "How is average lap time changing by track configuration?"

### ✅ Comparative Analysis Questions

**Examples for Carrera:**
- "How did weekend racing compare to weekday sessions?"
- "Compare Q3 performance to Q2 across all drivers"
- "Show me how Red Lightning car compares to Blue Thunder"
- "How do morning sessions compare to evening sessions for lap times?"

### ✅ Change Detection Questions

**Examples for Carrera:**
- "Which drivers are driving the improvement in average lap times?"
- "What's causing the decrease in incident rates?"
- "Show me which track sections have unusual lap time changes"
- "Which cars are contributing most to speed increases?"

### ✅ Breakdown Analysis Questions

**Examples for Carrera:**
- "Show lap time performance by driver and track configuration"
- "Break down incident rate by track section and time of day"
- "Display pit stop efficiency by driver experience level and session type"
- "How does speed vary by car model, lane, and track section?"

---

## Scenarios to Avoid ❌

Based on best practices, our dataset will NOT include:

❌ **Highly granular data**:
- Not minute-by-minute sensor readings
- Not frame-by-frame position tracking
- Instead: Aggregated lap-level and session-level metrics

❌ **Static, one-time datasets**:
- Not single-event data
- Not one-off special races
- Instead: Continuous multi-month time series

❌ **Unstructured or free-form text**:
- Not free-form race notes
- Not unstructured commentary
- Instead: Categorical dimensions with clear values

❌ **Complex organizational hierarchies**:
- Not deep nested team structures
- Not complex reporting relationships
- Instead: Simple, clear dimension hierarchies

---

## Pre-Configured Demo Questions

### Beginner-Level Questions (Easy wins)

1. "Show me lap time trends for the last month"
2. "Which driver has the fastest average lap time?"
3. "How many races did we have last week?"
4. "What's the average speed across all drivers?"

### Intermediate-Level Questions (Show capabilities)

1. "How do lap times compare between morning and evening sessions?"
2. "Which track sections have the slowest average times?"
3. "Show me lap time performance broken down by car model"
4. "What's driving the improvement in race completion rates?"

### Advanced-Level Questions (Wow factor)

1. "What's the correlation between pit stop frequency and final race position across all drivers?"
2. "Show me how track temperature affects lap times and speed across different car models"
3. "Which drivers improved most in lap time consistency, and how does that relate to their practice session attendance?"
4. "Break down performance by driver experience level and car configuration, focusing on weekend races with large crowds"

### Cross-Metric Analysis Questions (Showcase 2025 features)

1. "How are lap time, speed, and consistency metrics performing across all drivers?"
2. "What's the relationship between car maintenance frequency and both reliability and performance metrics?"
3. "Which factors are common contributors to both fast lap times and high consistency scores?"
4. "Show me the connection between environmental conditions and multiple performance metrics"

---

## Demo Preparation Checklist

### Before the Demo:

- [ ] All metrics defined and actively followed in Tableau Pulse
- [ ] Test each question at least 3 times to ensure consistency
- [ ] Have fallback questions ready for each category
- [ ] Know which questions showcase which features
- [ ] Understand current limitations and have workarounds ready
- [ ] Data loaded with clear, unambiguous dimension values
- [ ] Time range includes sufficient history for trend analysis
- [ ] Correlations validated and working

### During the Demo:

- [ ] Start with simple questions to build confidence
- [ ] Progress to more complex cross-metric queries
- [ ] Show dynamic filtering and scope refinement
- [ ] Demonstrate breakdown analysis
- [ ] Highlight AI-generated insights
- [ ] Use natural, conversational phrasing
- [ ] Let the audience suggest questions (if comfortable)

### Demo Flow Recommendation:

1. **Opening** (2 min): Simple trend question to warm up
2. **Core Features** (5 min): Demonstrate 3-4 key insight types
3. **Cross-Metric** (3 min): Show advanced correlation analysis
4. **Interactive** (3 min): Take audience questions or show filtering
5. **Closing** (2 min): Advanced multi-metric query as finale

---

## Technical Requirements for Dataset

To support all Enhanced Q&A features, ensure:

### Data Structure Requirements

- [ ] At least 3-6 months of continuous time-series data
- [ ] Minimum 5,000 records for reliable trend detection
- [ ] Clear primary keys and relationships
- [ ] No null values in critical dimension fields
- [ ] Consistent date/time formatting
- [ ] Standardized dimension value naming

### Metric Requirements

- [ ] 8-12 core metrics defined
- [ ] 3-5 correlation candidates per metric
- [ ] Mix of aggregation types (SUM, AVG, COUNT, etc.)
- [ ] Clear metric names and descriptions
- [ ] Appropriate time granularity settings

### Dimension Requirements

- [ ] 4-6 primary dimensions
- [ ] 2-3 levels of hierarchy where applicable
- [ ] Consistent categorical values (no typos)
- [ ] Meaningful dimension names
- [ ] No overly large cardinality (< 100 values per dimension ideal)

---

## Next Steps

1. ✅ Receive actual schema from user
2. ⏳ Map schema to these Q&A requirements
3. ⏳ Design specific metrics for Tableau Pulse
4. ⏳ Generate dataset with Q&A patterns in mind
5. ⏳ Create metric definitions document
6. ⏳ Build demo question script
7. ⏳ Test all questions in Tableau Pulse
8. ⏳ Create demo playbook
