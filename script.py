from allfunctions import listofstudent, completedata, required_subject
from allfunctions import read_students,read_grades,read_activity,read_attendance,write_report,input_data
import time
if __name__ == "__main__":
    userinput = input("Do you want to add more data ? [Yes/No] : ")
    if userinput == "Yes":
        nameinput = input("Enter his/her name")
        mathgrade = int(input("Enter his/her math grade : "))
        englishgrade = int(input("Enter his/her english grade : "))
        sciencegrade = int(input("Enter his/her science grade : "))
        attendance = int(input("Enter his/her attendance point : "))
        activity = int(input("Enter his/her activity point : "))
        input_data(nameinput, mathgrade, englishgrade, sciencegrade, attendance, activity)
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
    else:
        print("I'll take that as a no !")
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