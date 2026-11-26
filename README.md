# DPPH Antioxidant Analyzer

A beginner-friendly Python command-line tool for calculating percentage DPPH radical inhibition from absorbance readings, displaying results in a table, and exporting a CSV file and graph.

**Author:** Paul Rousseau S.  
**Version:** 1.0  
**Project status:** Educational portfolio project

## Features

- Calculates percentage inhibition from control and sample absorbance.
- Accepts multiple concentrations.
- Displays results using a Pandas table.
- Exports results to CSV.
- Saves a concentration-versus-inhibition graph as a 300 dpi PNG image.
- Checks common invalid inputs.

## Formula

% Inhibition = ((A_control - A_sample) / A_control) × 100

Where:
- `A_control` is the control absorbance.
- `A_sample` is the sample reaction absorbance.

## Requirements

- Python 3.10 or newer
- pandas
- matplotlib

## Installation

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the program

```bash
python dpph_analyzer.py
```

Enter the control absorbance, sample/extract name, number of concentrations, and each concentration with its sample absorbance.

The program creates:
- `<sample>_dpph_results.csv`
- `<sample>_dpph_graph.png`

These files are saved in the folder from which the program is run.

## Example test data (illustrative only)

For a control absorbance of `0.800`:

| Concentration | Sample absorbance | Inhibition |
|---:|---:|---:|
| 25 µg/mL | 0.600 | 25% |
| 50 µg/mL | 0.400 | 50% |
| 100 µg/mL | 0.200 | 75% |

These values are software test examples, not experimental findings.

## Scientific limitations

Version 1.0 calculates direct percentage inhibition from the values entered by the user. It does **not** currently perform blank correction, replicate averaging, statistical testing, curve fitting, or IC50 estimation. For real laboratory work, use an appropriate validated DPPH protocol, suitable blanks and controls, and replicate measurements. Review data quality and calculations before using results in academic work.

## Future improvements

- Blank correction
- Replicate handling and mean/standard deviation
- Dose-response curve fitting and IC50 estimation
- Importing experimental readings from CSV

## License

No license has been added yet. Add an appropriate open-source license if you want to define reuse and distribution permissions.
