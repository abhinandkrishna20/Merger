# 📂 File Merger and Folder Cleaner

This Python script moves all files from subfolders within a specified source folder into a single destination folder, skips the script file itself, and removes any empty subfolders afterward.

## 🔧 Features

- ✅ Moves all files from subdirectories to a single folder
- ✅ Automatically avoids moving the script file
- ✅ Prevents overwriting by renaming duplicate files
- ✅ Deletes empty folders after moving files
- ✅ Cross-platform compatible (Windows, macOS, Linux)

## 📁 Project Structure



project/
├── merge20.py             # The Python script
├── some\_subfolder/
│   ├── file1.txt
│   └── file2.txt
└── merged\_files/          # Created automatically by the script

## 🚀 How It Works

- The script walks through all folders starting from the current working directory.
- All files (except the script file) are moved to a folder called `merged_files`.
- If a file with the same name already exists in the destination, it appends a number to avoid overwriting.
- After moving the files, it deletes any empty folders.

## 🧪 Example Usage

### Run the script with Python:

```bash
python merge20.py
````

* The script uses the **current working directory** as the source folder.
* It creates or uses a subfolder named `merged_files` to store all the files.
* The script file (`merge20.py`) is skipped to prevent it from being moved or altered.

## ⚠️ Notes

* Make sure to name the script file correctly in the `script_name` variable:

  ```python
  script_name = "merge20.py"
  ```
* Files already in the `merged_files` directory will not be moved or duplicated.

## 📌 Requirements

No external libraries are needed. It uses only Python's standard library:

* `os`
* `shutil`

## 📄 License

This project is licensed under the MIT License.


