# POS-Entropy-Calculator
This repository provides a simple Python tool for calculating the __entropy of Part-of-Speech (POS) distributions__ for each word in a dataset. Entropy is used as an indicator of __potential POS labeling inconsistency__, which is especially useful for corpus cleaning, dataset validation, and linguistic analysis.

## ✨ Features
* Reads an Excel dataset containing Word and POS columns
* Automatically groups POS tags for each word
* Computes entropy using Shannon’s Information Theory
* Saves the output to data/entropy_results.xlsx
* Helps detect ambiguous or inconsistently labeled words

## 📊 What Is Entropy Used For?
Entropy measures the uncertainty or variability in POS assignments:
* __Low entropy (0.0)__ → The word has consistent POS labeling
* __High entropy__ → The word appears with multiple POS tags; may indicate:
    * Annotation inconsistency
    * True linguistic ambiguity
    * Dataset noise

Example:

| Word	| POS Tags  | Entropy |
|-------|-----------|---------|
| makan	| VERB (100%)	| 0.0 |
| baik	| ADJ (60%), ADV (40%)  | > 0.9 |
| yang	| SC (98%), PRON (2%)   | low but non-zero |

## 📂 Folder Structure
```powershell
project/
│
├── data/
│   ├── revised.xlsx           # Input file
│   ├── entropy_results.xlsx   # Output file (auto-generated)
│
├── pos_entropy.py             # Main script (your program)
└── README.md
```

## 📥 Input Format
The Excel file must contain at least two columns:

| Word	| POS |
|-------|-----|
| makan	| VERB |
| makan	| NOUN |
| cukup	| ADV |
| cukup | ADJ |

Case sensitivity for words is preserved.

## 🚀 How to Use
__1. Install dependencies__
```bash
pip install pandas numpy openpyxl
```

__2. Run the script__
```bash
python pos_entropy.py
```

The script will:
* Process `data/revised.xlsx`
* Compute entropy per word
* Save the output to:
```bash
data/entropy_results.xlsx
```

## 🧠 How Entropy Is Calculated

Shannon Entropy formula:
$$
H = - \sum_{i=1}^{n} p_i \log_2(p_i)
$$

Where:
* $p_i$ is the probability of POS tag i for the word
* Entropy = 0 if the word has only one unique POS tag

## 📘 Example Output
| Word	| Entropy |
|-------|---------|
| makan	| 0.00 |
| bisa	| 0.72 |
| baik	| 0.91 |
| cukup	| 0.99 |

## 🛠 Code Reference
The main functions are:
* `calculate_entropy(pos_counts)` → computes entropy
* `process_pos_entropy(file_path)` → loads data, aggregates POS counts, and exports results

See the full source in `pos_entropy.py`.

## 📄 License
This project is open-source. You may modify and use it for research or academic purposes.