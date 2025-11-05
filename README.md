# Carrera Slot Car Track - Tableau Pulse Demo Dataset

## Project Overview

This project creates a rich, realistic demo dataset for a Carrera Slot Car Track exhibition/showcase, optimized for Tableau Pulse demonstrations, particularly Pulse Discover and Enhanced Q&A features.

## Purpose

- Primary: Demonstrate Tableau Pulse capabilities in an engaging, visual context
- Secondary: Showcase Tableau's analytics features using relatable racing data
- Context: Trade shows, expos, fairs, and live demonstrations

## Project Structure

```
/
├── docs/                    # Documentation and design notes
├── schema/                  # Database schemas and data models
├── data/                    # Generated datasets
│   ├── raw/                # Source/seed data
│   └── processed/          # Enriched, storyline-enhanced data
├── scripts/                # Data generation and enrichment scripts
└── tableau/                # Tableau workbooks and configurations
```

## Tableau Pulse Optimization

This dataset is designed to showcase all 12 Tableau Pulse insight types:

### Enabled Insight Types

1. **Period Over Period Change** - Compare race performance across time periods
2. **Correlated Metrics** - Analyze relationships (e.g., speed vs. lap time, pit stops vs. position)
3. **Record-level Outliers** - Detect exceptional lap times and performance anomalies
4. **Forecast** - Predict race outcomes and maintenance needs
5. **Current Trend** - Track performance trends over racing sessions
6. **Trend Change Alert** - Flag sudden performance changes
7. **Unexpected Values** - Identify anomalous results beyond historical ranges
8. **Goal and Threshold Breakdown** - Track progress toward race time goals
9. **Top Drivers** - Identify best performing entities
10. **Top Detractors** - Highlight underperforming entities
11. **Concentrated Contribution Alert** - Detect dominance patterns
12. **Top/Bottom Contributors** - Rank performance across dimensions

### Data Characteristics

The dataset includes:

- **Time-series data**: Continuous tracking across race sessions and time periods
- **Clear dimensions**: Drivers, cars, track sections, race types, time periods
- **Multiple metrics**: Lap times, speeds, positions, pit stops, penalties, etc.
- **Hierarchies**: Date hierarchies, track section hierarchies, performance categories
- **Relatable stories**: Built-in narratives that make demos engaging and memorable

## Next Steps

1. Define detailed schema based on real requirements
2. Receive example data for enrichment
3. Build storylines into the data
4. Generate comprehensive dataset
5. Create Tableau Pulse configuration

## Status

🔄 **Bootstrapping Phase** - Awaiting schema and example data input
