import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root"
)

cursor = db.cursor()

# cursor.execute("SHOW DATABASES")

# for db in cursor:
#     print(db)

cursor.execute("CREATE DATABASE IF NOT EXISTS student_mangement")

cursor.execute("USE student_mangement")

# Table Creation of StudentDetails Table - Name, Addmission Number auto increment, Contact Number, Email, Address, Class, DOB, Date of Admission, Fathers Name and Mothers Name

cursor.execute("Create Table StudentDetails(Name VARCHAR(255), AdmissionNumber INT AUTO_INCREMENT PRIMARY KEY, ContactNumber INT, Email VARCHAR(255), Address VARCHAR(255), Class VARCHAR(255), DOB DATE, DateOfAdmission DATE, FathersName VARCHAR(255), MothersName VARCHAR(255))")


# Table Creation of StudentMarks Table - Admission Number foreign key, Subject, Marks Obtained, Total Marks, Date of Exam, Test Number

cursor.execute("Create Table StudentMarks(AdmissionNumber INT, FOREIGN KEY(AdmissionNumber) REFERENCES StudentDetails(AdmissionNumber), Subject VARCHAR(255) NOT NULL, MarksObtained INT NOT NULL, TotalMarks INT NOT NULL, DateOfExam DATE NOT NULL, TestNumber INT NOT NULL)")

cursor.close()