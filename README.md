# 📊 Student Report Generator

This Python program processes student data and generates a comprehensive report in JSON format. It reads data from multiple sources, combines them, and writes a final `report.json`.

## 💡 Features

- Reads student names from `students.txt`
- Loads grades from `grades.csv`
- Checks attendance from `attendance.txt`
- Adds activity points from `activities.json`
- Detects missing grades and low attendance
- Option to add new student data interactively
- Outputs final report as `report.json`

## 🗂️ File Descriptions

| File            | Description                              |
|-----------------|------------------------------------------|
| `script.py`     | Main script for running the program      |
| `allfunctions.py` | All helper functions (data loading, processing, writing) |
| `students.txt`  | List of student names                    |
| `grades.csv`    | Student grades (math, english, science)  |
| `attendance.txt`| Student attendance (out of 20 days)      |
| `activities.json` | Activity points (JSON format)         |
| `report.json`   | Output report with complete student info |

## 🛠️ How to Use

1. Run `script.py`
2. When prompted, choose whether to add new student data.
3. Program will process everything and generate `report.json`

## 📌 Requirements

- Python 3.x
- No extra libraries needed (uses built-in `csv`, `json`, etc.)

---

## 📍 Example Output (in `report.json`)
```json
{
  "Alice": {
    "math": "90",
    "english": "85",
    "science": "88",
    "average_grades": 87.67,
    "low_attendance": false,
    "activity_points": 10
  },
  ...
}
