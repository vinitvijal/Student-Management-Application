import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="student_mangement"
)

cursor = db.cursor()

# StudentDetails Table - Name, Addmission Number auto increment, Contact Number, Email, Address, Class, DOB, Date of Admission, Fathers Name and Mothers Name
# StudentMarks Table - Admission Number foreign key, Subject, Marks Obtained, Total Marks, Date of Exam, Test Number


def AddNewStudent():
    print("Enter the following details to add a new student")
    name = input("Name: ")
    contactNumber = input("Contact Number: ")
    email = input("Email: ")
    address = input("Address: ")
    classOfStudent = input("Class: ")
    dob = input("Date of Birth(YY-MM-DD): ")
    dateOfAdmission = input("Date of Admission(YY-MM-DD): ")
    fathersName = input("Fathers Name: ")
    mothersName = input("Mothers Name: ")

    cursor.execute("INSERT INTO StudentDetails(Name, ContactNumber, Email, Address, Class, DOB, DateOfAdmission, FathersName, MothersName) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, contactNumber, email, address, classOfStudent, dob, dateOfAdmission, fathersName, mothersName))

    db.commit()

    print("Student Details Added Successfully")


def AddStudentMarks():
    print("Enter the following details to add a new student")
    admissionNumber = input("Admission Number: ")
    subject = input("Subject: ")
    marksObtained = input("Marks Obtained: ")
    totalMarks = input("Total Marks: ")
    dateOfExam = input("Date of Exam(YY-MM-DD): ")
    testNumber = input("Test Number: ")

    cursor.execute("INSERT INTO StudentMarks(AdmissionNumber, Subject, MarksObtained, TotalMarks, DateOfExam, TestNumber) VALUES(%s, %s, %s, %s, %s, %s)", (admissionNumber, subject, marksObtained, totalMarks, dateOfExam, testNumber))

    db.commit()

    print("Student Marks Added Successfully")

def ViewStudentDetails(admissionNumber = None):
    print("Enter the following details to view a student")

    if(admissionNumber == None):
        admissionNumber = input("Admission Number: ")
    

    cursor.execute("SELECT * FROM StudentDetails WHERE AdmissionNumber = %s", (admissionNumber,))

    studentDetails = cursor.fetchone()

    print(studentDetails)

def ViewStudentMarks(AdmissionNumber = None):
    print("Enter the following details to view a student")
    if(AdmissionNumber == None):
        admissionNumber = input("Admission Number: ")

    cursor.execute("SELECT * FROM StudentMarks WHERE AdmissionNumber = %s", (admissionNumber,))
    studentMarks = cursor.fetchall()

    for marks in studentMarks:
        print(marks)
    
def EditStudentMarks():
    print("Enter the following details to edit a student")
    admissionNumber = input("Admission Number: ")


    print("Which field do you want to edit?")
    print("""
        1. Marks Obtained
        2. Total Marks
        3. Date of Exam
        4. Test Number
    """)

    userChoice = input("Enter your choice: ")
    if(userChoice == "1"):
        marksObtained = input("Marks Obtained: ")
        testNumber = input("Test Number: ")
        subject = input("Subject: ")
        cursor.execute("UPDATE StudentMarks SET MarksObtained = %s WHERE AdmissionNumber = %s AND TestNumber = %s AND Subject = %s", (marksObtained, admissionNumber, testNumber, subject)) 
    elif(userChoice == "2"):
        totalMarks = input("Total Marks: ")
        testNumber = input("Test Number: ")
        subject = input("Subject: ")
        cursor.execute("UPDATE StudentMarks SET TotalMarks = %s WHERE AdmissionNumber = %s AND TestNumber = %s AND Subject = %s", (totalMarks, admissionNumber, testNumber, subject))
    elif(userChoice == "3"):
        dateOfExam = input("Date of Exam(YY-MM-DD): ")
        testNumber = input("Test Number: ")
        subject = input("Subject: ")
        cursor.execute("UPDATE StudentMarks SET DateOfExam = %s WHERE AdmissionNumber = %s AND TestNumber = %s AND Subject = %s", (dateOfExam, admissionNumber, testNumber, subject))
    elif(userChoice == "4"):
        testNumber = input("Old Test Number: ")
        newTestNumber = input("New Test Number: ")
        subject = input("Subject: ")
        dateOfExam = input("Date of Exam(YY-MM-DD): ")
        cursor.execute("UPDATE StudentMarks SET TestNumber = %s, DateOfExam = %s WHERE AdmissionNumber = %s AND TestNumber = %s AND Subject = %s", (newTestNumber, dateOfExam, admissionNumber, testNumber, subject))
    else:
        print("Invalid Choice")



def EditStudentDetails():
    print("Enter the following details to edit a student")
    admissionNumber = input("Admission Number: ")
    
    ViewStudentDetails(admissionNumber)

    print("Which field do you want to edit?")
    print("""
    1. Name
    2. Contact Number
    3. Email
    4. Address
    5. Class
    6. DOB
    7. Date of Admission
    8. Fathers Name
    9. Mothers Name
    """)
    userChoice = input("Enter your choice: ")

    if(userChoice == "1"):
        name = input("Name: ")
        cursor.execute("UPDATE StudentDetails SET Name = %s WHERE AdmissionNumber = %s", (name, admissionNumber))
    elif(userChoice == "2"):
        contactNumber = input("Contact Number: ")
        cursor.execute("UPDATE StudentDetails SET ContactNumber = %s WHERE AdmissionNumber = %s", (contactNumber, admissionNumber))
    elif(userChoice == "3"):
        email = input("Email: ")
        cursor.execute("UPDATE StudentDetails SET Email = %s WHERE AdmissionNumber = %s", (email, admissionNumber))
    elif(userChoice == "4"):
        address = input("Address: ")
        cursor.execute("UPDATE StudentDetails SET Address = %s WHERE AdmissionNumber = %s", (address, admissionNumber))
    elif(userChoice == "5"):
        classOfStudent = input("Class: ")
        cursor.execute("UPDATE StudentDetails SET Class = %s WHERE AdmissionNumber = %s", (classOfStudent, admissionNumber))
    elif(userChoice == "6"):
        dob = input("Date of Birth(YY-MM-DD): ")
        cursor.execute("UPDATE StudentDetails SET DOB = %s WHERE AdmissionNumber = %s", (dob, admissionNumber))
    elif(userChoice == "7"):
        dateOfAdmission = input("Date of Admission(YY-MM-DD): ")
        cursor.execute("UPDATE StudentDetails SET DateOfAdmission = %s WHERE AdmissionNumber = %s", (dateOfAdmission, admissionNumber))
    elif(userChoice == "8"):
        fathersName = input("Fathers Name: ")
        cursor.execute("UPDATE StudentDetails SET FathersName = %s WHERE AdmissionNumber = %s", (fathersName, admissionNumber))
    elif(userChoice == "9"):
        mothersName = input("Mothers Name: ")
        cursor.execute("UPDATE StudentDetails SET MothersName = %s WHERE AdmissionNumber = %s", (mothersName, admissionNumber))
    else:
        print("Invalid Choice")


    print("Student Details Updated Successfully")

def DeleteStudentDetails():
    print("Enter the following details to delete a student")
    admissionNumber = input("Admission Number: ")
    cursor.execute("DELETE FROM StudentDetails WHERE AdmissionNumber = %s", (admissionNumber,))
    print("Student Details Deleted Successfully")
    cursor.execute("DELETE FROM StudentMarks WHERE AdmissionNumber = %s", (admissionNumber,))
    print("Student Marks Deleted Successfully")

def main():
    while True:
        print("""
        Welcome to Student Management System
        1. Add Student Details(New Student)
        2. Add Student Marks(Teachers)
        3. Edit Student Details(Admin)
        4. Edit Student Marks(Admin)
        5. View Student Details(Admin)
        6. View Student Marks(Admin)
        7. Delete Student Details(Admin)
            """)
        userChoice = input("Enter your choice: ")
        if(userChoice == "1"):
            AddNewStudent()
        elif(userChoice == "2"):
            AddStudentMarks()
        elif(userChoice == "3"):
            EditStudentDetails()
        elif(userChoice == "4"):
            EditStudentMarks()
        elif(userChoice == "5"):
            ViewStudentDetails()
        elif(userChoice == "6"):
            ViewStudentMarks()
        elif(userChoice == "7"):
            DeleteStudentDetails()
        elif(userChoice == "8"):
            cursor.close()
            db.close()
            print("Exiting...")
            break
        else:
            print("Invalid Choice")




main()  