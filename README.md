# Athlete Performance Correlation Analyzer

A Python sports analytics project that explores relationships between training load, athlete wellness, readiness and performance measures.

## Objective

The project investigates relationships between:

- Training load
- Sleep quality
- Wellness
- Readiness
- 10-m sprint performance
- Countermovement jump performance
- Strength performance

The system creates a composite performance index and performs correlation analysis.

## Data Flow

```text
Training Load
      +
Wellness
      +
Readiness
      +
Sleep
      +
Sprint
      +
Jump
      +
Strength
      ↓
Performance Index
      ↓
Correlation Analysis
      ↓
Visualization
      ↓
Sports Performance Insights
```

## Dataset

The sample dataset contains observations from four athletes.

### Variables

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Testing date |
| Training_Load | Training load in arbitrary units |
| Sleep_Quality | Subjective sleep-quality score |
| Wellness_Score | Overall wellness score |
| Readiness_Score | Readiness percentage |
| Sprint_10m | 10-m sprint time |
| CMJ_Height | Countermovement jump height |
| Strength_Index | Standardized strength measure |

## Performance Index

A simple composite performance index is created from sprint, jump and strength measures.

Sprint performance is directionally reversed because lower sprint time represents better performance.

The resulting components are averaged to create:

```text
Performance Index
```

This index is an educational data-analysis metric and is not a validated universal athlete-performance score.

## Correlation Analysis

The project calculates Pearson correlation coefficients between:

- Training load
- Sleep
- Wellness
- Readiness
- Sprint performance
- Jump performance
- Strength
- Performance index

Correlation values range from:

```text
-1 to +1
```

## Interpretation

Positive correlation:

```text
One variable tends to increase as another increases.
```

Negative correlation:

```text
One variable tends to decrease as another increases.
```

A correlation does not demonstrate causation.

## Technologies

- Python
- Pandas
- Matplotlib
- CSV
- Data validation
- Feature engineering
- Correlation analysis
- Data visualization

## Installation

```bash
pip install pandas matplotlib
```

## Running the Project

Place the Python script and CSV dataset in the same directory.

Run:

```bash
python athlete_performance_correlation.py
```

## Generated Outputs

```text
performance_analysis.csv
correlation_matrix.csv
correlation_matrix.png
load_vs_performance.png
readiness_vs_performance.png
```

## Sports Science Applications

The workflow can be adapted for:

- Strength and conditioning
- Athlete monitoring
- Performance testing
- Training-load analysis
- Readiness monitoring
- Longitudinal performance analysis
- Sports analytics research

## Limitations

The dataset is synthetic.

Correlation analysis is observational and does not establish causality.

The composite Performance Index is created for educational programming purposes.

Real athlete monitoring should account for:

- Individual baselines
- Measurement reliability
- Smallest worthwhile change
- Test-retest reliability
- Training history
- Competition schedule
- Athlete context
- Statistical uncertainty

## Future Development

- Add more athletes
- Add more testing sessions
- Add effect sizes
- Add confidence intervals
- Add regression models
- Add rolling correlations
- Add individual athlete baselines
- Add GPS metrics
- Add heart-rate metrics
- Add force-plate variables
- Add velocity-based training data
- Add machine-learning models
- Build an interactive dashboard

## Skills Demonstrated

```text
Python
   ↓
Pandas
   ↓
Data Validation
   ↓
Feature Engineering
   ↓
Correlation Analysis
   ↓
Visualization
   ↓
Sports Performance Analytics
```

## Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

## License

MIT License