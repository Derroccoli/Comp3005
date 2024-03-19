#Derrick Zhang Comp3005 A3Q1
import psycopg2
from datetime import date

#connection code
try:
    #try to start a connection using credentials to my local pg4 server
    connection = psycopg2.connect(
        dbname="a3q1",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Connected to database!")
    #exception if we dont connect to database
except psycopg2.Error as e:
    print("Unable to connect to database:", e)

#create a cursor, this is used to execute queries
cursor = connection.cursor()

#function to get all students
def getAllStudents():
    try:
        #execute the query and store the values in a variable, then print it
        cursor.execute("SELECT * FROM students")
        allStudents = cursor.fetchall()
        print(allStudents)
        return allStudents
    except e:
        print("Something went wrong, unable to get all")

#function to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        #setup a query and execute it
        insertQuery = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        toInsert = (first_name, last_name, email, enrollment_date)
        cursor.execute(insertQuery, toInsert)
    except e:
        print("invalid data")

#function to update an email
def updateStudentEmail(student_id, new_email):
    try:
        #setup the update query and execute it
        updateQuery = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(updateQuery, (new_email, student_id))
    except e:
        print("invalid student id or email")

#function to delete a student
def deleteStudent(student_id):
    try:
        #execute the delete query
        deleteQuery = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(deleteQuery, (student_id,))
    except e:
        print("invalid student id")

#simulate all 4 actions
print("Add student")

addStudent("Bob", "Bob", "Bob_Bob@Bob.ca", date(1992, 3, 18))
print()
students = getAllStudents()

print("Update student email to BobChangedEmail@gmail.com")

updateStudentEmail(19, "BobChangedEmail@gmail.com")
print()
students = getAllStudents()

print("Delete the newly added student")

deleteStudent(19)
print()
students = getAllStudents()
