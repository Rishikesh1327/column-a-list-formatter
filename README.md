# 📋 Column A Formatter (Excel & CSV) – Google Colab Utility

<img width="1536" height="1024" alt="Row to List" src="https://github.com/user-attachments/assets/24b69b9e-8f0b-4672-979b-8ad3688ccb74" />

## 📌 Description

This Python utility is designed for **Google Colab users** who need a **simple, fast, and reliable** way to extract and format values from a file.

The script allows users to:
- Upload an **Excel (.xlsx / .xls)** or **CSV (.csv)** file using a **click-to-upload** interface
- Automatically read **only Column A**
- Skip the **first row (header)** and process data starting from **A2 onward**
- Remove blank values and duplicate entries
- Format the output as a clean Python list with a fixed number of values per line

This tool is especially useful when working with **MAC IDs, device IDs, site IDs, or any identifier-based automation workflows**.

---

## ⚙️ How the Code Works

1. **File Upload**
   - Opens a file chooser in Google Colab
   - User selects an Excel or CSV file (no file paths required)

2. **Automatic File Detection**
   - `.xlsx / .xls` files are read using `pandas.read_excel()`
   - `.csv` files are read using `pandas.read_csv()`

3. **Column & Row Handling**
   - Always selects **Column A**
   - Skips the first row (assumed header)
   - Reads data from **A2:A until the last row**

4. **Data Cleaning**
   - Removes empty cells
   - Converts values to a string
   - Removes duplicate entries

5. **Formatted Output**
   - Prints values as a Python list
   - User can control how many values appear per line

---

## 🧠 Use Cases

This script is ideal for:

- Preparing **MAC ID lists** for automation scripts
- Formatting identifiers for **Python, Google Apps Script, or SQL**
- Quickly cleaning data exported from Excel or Google Sheets
- Eliminating manual copy-paste and formatting errors
- Analysts and automation engineers working in **Google Colab**

---

## 🚀 Benefits

- ✔ No file paths or Google Drive mounting required
- ✔ Supports both **Excel and CSV** files
- ✔ One-click file upload
- ✔ Header-independent (always reads A2:A)
- ✔ Automatically removes duplicates
- ✔ Clean, readable, and reusable output
- ✔ Beginner-friendly and production-safe

---

## 🧪 Example Output

```python
List = [
    'C4D8D581D97C', 'A1B2C3D4E5F6', '112233445566',
    '778899AABBCC', 'FFEEDDCCBBAA',
]
