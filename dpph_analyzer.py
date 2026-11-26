import re
import pandas as pd
import matplotlib.pyplot as plt


def calculate_inhibition(control, sample):
    """Calculate DPPH percentage inhibition from absorbance readings."""
    if control <= 0:
        raise ValueError("Control absorbance must be greater than zero.")
    if sample < 0:
        raise ValueError("Sample absorbance cannot be negative.")

    return ((control - sample) / control) * 100


def safe_filename(name):
    """Convert a sample name into a filename-safe label."""
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", name.strip())
    return cleaned.strip("_") or "sample"


def get_positive_float(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or (value == 0 and not allow_zero):
                print("Please enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("\n=== DPPH Antioxidant Analyzer v1.0 ===\n")

    control = get_positive_float("Enter control absorbance: ")
    sample_name = input("Enter plant extract/sample name: ").strip() or "Sample"

    while True:
        try:
            count = int(input("How many concentrations will you enter? "))
            if count <= 0:
                print("Enter at least one concentration.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    results = []

    for i in range(count):
        print(f"\nReading {i + 1}")
        concentration = get_positive_float("Concentration (µg/mL): ")
        sample_absorbance = get_positive_float("Sample absorbance: ", allow_zero=True)
        inhibition = calculate_inhibition(control, sample_absorbance)
        results.append({
            "Concentration (µg/mL)": concentration,
            "Sample Absorbance": sample_absorbance,
            "Inhibition (%)": inhibition
        })

    df = pd.DataFrame(results).sort_values("Concentration (µg/mL)")
    print("\n=== DPPH Analysis Results ===")
    print(df.to_string(index=False, formatters={"Inhibition (%)": "{:.2f}".format}))

    filename = safe_filename(sample_name)
    csv_file = f"{filename}_dpph_results.csv"
    graph_file = f"{filename}_dpph_graph.png"

    df.to_csv(csv_file, index=False)

    plt.figure(figsize=(8, 5))
    plt.plot(
        df["Concentration (µg/mL)"],
        df["Inhibition (%)"],
        marker="o",
        linestyle="-"
    )
    plt.xlabel("Concentration (µg/mL)")
    plt.ylabel("DPPH Inhibition (%)")
    plt.title(f"DPPH Antioxidant Activity - {sample_name}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(graph_file, dpi=300)
    plt.show()

    print(f"\nCSV saved as: {csv_file}")
    print(f"Graph saved as: {graph_file}")
    print("\nNote: This tool calculates direct percentage inhibition only.")
    print("It does not perform blank correction, replicate statistics, or IC50 estimation.")


if __name__ == "__main__":
    main()
