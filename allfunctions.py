import json
import csv
import time

listofstudent = []
completedata = {}
required_subject = ["math", "english","science"]
def read_students(file_path):
    with open(file_path, "r") as f:
        readertxt = f.readlines() #Already has list of students
        for student in readertxt:
            listofstudent.append(student.strip())

def read_grades(file_path):

    with open(file_path,"r") as f:
        readercsv = csv.DictReader(f)
        averagegrades = 0
        for row in readercsv:
            if row["name"] in listofstudent:
                completedata[row["name"]] = {}
                for subject in required_subject:
                    if subject not in row or not row[subject]:
                        completedata[row["name"]][subject] = None
                        completedata[row["name"]]["missing_grades"] = True
                    else:
                        completedata[str(row["name"])][subject] = row[subject]
                        averagegrades += int(row[subject])

                averagegrades /= 3
                averagegrades = round(averagegrades, 2)
                try:
                    if completedata[row["name"]]["missing_grades"] == True:
                        completedata[row["name"]]["average_grades"] = averagegrades
                except KeyError: #Already checked above, if it exists it wont throw error if not, it will and here we
                    completedata[row["name"]]["missing_grades"] = False
                    completedata[row["name"]]["average_grades"] = averagegrades
                averagegrades = 0

        for student in listofstudent:
            if student not in completedata:
                completedata[student] = {
                    "absence": False
                }
def read_attendance(file_path):
    with open(file_path, "r") as f:
        reader = f.readlines()
        for attendance in reader:
            name, count = attendance.strip().split(": ")
            attendance_percent = int(count) / 20 * 100
            if name in completedata:
                completedata[name]["attendance_percent"] = attendance_percent
                completedata[name]["attendance"] = int(count)
                if attendance_percent < 75:
                    completedata[name]["low_attendance"] = True
                elif attendance_percent >= 75:
                    completedata[name]["low_attendance"] = False

def read_activity(file_path):
    with open(file_path, "r") as f:
        reader = json.load(f)
        for student in reader:
            if student in completedata:
                completedata[student]["activity_points"] = reader[student]
            elif student not in completedata:
                completedata[student] = reader[student]

def write_report(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def input_data(name, math, english, science, attendance, activity_points):
    with open("students.txt", "a", newline="") as f:
        f.writelines(f"\n{name}")

    with open("grades.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, math, english, science])
    print("Added !")

    with open("attendance.txt", "a", newline="") as f:
        f.writelines(f"\n{name}: {attendance}")
    
    with open("activities.json", "r") as f:
        data = json.load(f)
    data[name] = activity_points
    with open("activities.json", "w") as f:
        json.dump(data, f, indent=4)

def processing():
    print("Processing Students name...")
    read_students("students.txt")
    time.sleep(3)

    print("Processing grades...")
    read_grades("grades.csv")
    time.sleep(3)

    print("Processing attendance...")
    read_attendance("attendance.txt")
    time.sleep(3)

    print("processing activity points...")
    read_activity("activities.json")
    time.sleep(3)

    print("Inputting data...")
    time.sleep(5)
    write_report("report.json", completedata)
        
    print("Finished ! You now may look at report.json !")