import pandas as pd
import matplotlib.pyplot as plt


print("=" * 80)
print("          ATHLETE PERFORMANCE CORRELATION ANALYZER")
print("=" * 80)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("athlete_performance_data.csv")

data["Date"] = pd.to_datetime(data["Date"])

data = data.sort_values(
    ["Athlete", "Date"]
).reset_index(drop=True)


# ------------------------------------------
# Data Validation
# ------------------------------------------

print("\n" + "=" * 80)
print("DATA VALIDATION")
print("=" * 80)

print(f"Rows       : {len(data)}")
print(f"Columns    : {len(data.columns)}")
print(f"Missing values : {data.isnull().sum().sum()}")


# ------------------------------------------
# Calculate Performance Change
# ------------------------------------------

data["Sprint_Change_%"] = (
    data.groupby("Athlete")["Sprint_10m"]
    .pct_change()
    * 100
)

data["Jump_Change_%"] = (
    data.groupby("Athlete")["CMJ_Height"]
    .pct_change()
    * 100
)

data["Strength_Change_%"] = (
    data.groupby("Athlete")["Strength_Index"]
    .pct_change()
    * 100
)


# ------------------------------------------
# Create Performance Index
# ------------------------------------------

data["Sprint_Score"] = (
    data["Sprint_10m"].max()
    / data["Sprint_10m"]
) * 100

data["Jump_Score"] = (
    data["CMJ_Height"]
    / data["CMJ_Height"].max()
) * 100

data["Strength_Score"] = (
    data["Strength_Index"]
    / data["Strength_Index"].max()
) * 100


data["Performance_Index"] = (
    data["Sprint_Score"]
    + data["Jump_Score"]
    + data["Strength_Score"]
) / 3


# ------------------------------------------
# Display Dataset
# ------------------------------------------

print("\n" + "=" * 80)
print("ATHLETE PERFORMANCE DATA")
print("=" * 80)

print(
    data.to_string(
        index=False
    )
)


# ------------------------------------------
# Correlation Variables
# ------------------------------------------

correlation_variables = [
    "Training_Load",
    "Sleep_Quality",
    "Wellness_Score",
    "Readiness_Score",
    "Sprint_10m",
    "CMJ_Height",
    "Strength_Index",
    "Performance_Index"
]


# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

correlation_matrix = data[
    correlation_variables
].corr()


print("\n" + "=" * 80)
print("CORRELATION MATRIX")
print("=" * 80)

print(
    correlation_matrix.round(2).to_string()
)


# ------------------------------------------
# Performance Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Observations=("Athlete", "count"),
        Average_Load=("Training_Load", "mean"),
        Average_Wellness=("Wellness_Score", "mean"),
        Average_Readiness=("Readiness_Score", "mean"),
        Average_Sprint=("Sprint_10m", "mean"),
        Average_CMJ=("CMJ_Height", "mean"),
        Average_Strength=("Strength_Index", "mean"),
        Average_Performance=("Performance_Index", "mean")
    )
    .reset_index()
)


print("\n" + "=" * 80)
print("ATHLETE PERFORMANCE SUMMARY")
print("=" * 80)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Load":
                "{:.1f}".format,

            "Average_Wellness":
                "{:.1f}".format,

            "Average_Readiness":
                "{:.1f}".format,

            "Average_Sprint":
                "{:.2f}".format,

            "Average_CMJ":
                "{:.1f}".format,

            "Average_Strength":
                "{:.1f}".format,

            "Average_Performance":
                "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Strongest Correlations
# ------------------------------------------

performance_correlations = (
    correlation_matrix["Performance_Index"]
    .drop("Performance_Index")
    .sort_values(
        key=abs,
        ascending=False
    )
)


print("\n" + "=" * 80)
print("CORRELATIONS WITH PERFORMANCE INDEX")
print("=" * 80)

print(
    performance_correlations.round(3)
)


# ------------------------------------------
# Best Performance Observation
# ------------------------------------------

best_performance = data.loc[
    data["Performance_Index"].idxmax()
]


print("\n" + "=" * 80)
print("BEST PERFORMANCE OBSERVATION")
print("=" * 80)

print(
    f"Athlete : {best_performance['Athlete']}"
)

print(
    f"Date : {best_performance['Date'].date()}"
)

print(
    f"Performance Index : "
    f"{best_performance['Performance_Index']:.2f}"
)

print(
    f"Sprint : "
    f"{best_performance['Sprint_10m']:.2f} s"
)

print(
    f"CMJ : "
    f"{best_performance['CMJ_Height']:.1f} cm"
)

print(
    f"Strength Index : "
    f"{best_performance['Strength_Index']:.1f}"
)


# ------------------------------------------
# Visualization 1
# Training Load vs Performance
# ------------------------------------------

plt.figure(figsize=(9, 6))

plt.scatter(
    data["Training_Load"],
    data["Performance_Index"]
)

plt.title(
    "Training Load vs Performance Index"
)

plt.xlabel(
    "Training Load (AU)"
)

plt.ylabel(
    "Performance Index"
)

plt.tight_layout()

plt.savefig(
    "load_vs_performance.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Visualization 2
# Readiness vs Performance
# ------------------------------------------

plt.figure(figsize=(9, 6))

plt.scatter(
    data["Readiness_Score"],
    data["Performance_Index"]
)

plt.title(
    "Readiness vs Performance Index"
)

plt.xlabel(
    "Readiness Score (%)"
)

plt.ylabel(
    "Performance Index"
)

plt.tight_layout()

plt.savefig(
    "readiness_vs_performance.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Visualization 3
# Correlation Matrix
# ------------------------------------------

plt.figure(figsize=(10, 8))

plt.imshow(
    correlation_matrix,
    aspect="auto"
)

plt.colorbar(
    label="Correlation"
)

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title(
    "Athlete Performance Correlation Matrix"
)

plt.tight_layout()

plt.savefig(
    "correlation_matrix.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Export Results
# ------------------------------------------

data.to_csv(
    "performance_analysis.csv",
    index=False
)

correlation_matrix.to_csv(
    "correlation_matrix.csv"
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

print("Files created:")
print("1. performance_analysis.csv")
print("2. correlation_matrix.csv")
print("3. correlation_matrix.png")
print("4. load_vs_performance.png")
print("5. readiness_vs_performance.png")

print("\n" + "=" * 80)
print("TRAIN • MONITOR • TEST • ANALYZE • PERFORM")
print("=" * 80)