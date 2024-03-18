#Derrick Zhang Comp3005 A3Q1
import psycopg2
from datetime import date

try:
    connection = psycopg2.connect(
        dbname="a3q1",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Connected to database!")
except psycopg2.Error as e:
    print("Unable to connect to database:", e)

cursor = connection.cursor()

#function to get all students
def getAllStudents():
    cursor.execute("SELECT * FROM students")
    allStudents = cursor.fetchall()
    print(allStudents)
    return allStudents

def addStudent(id, fName, lName, email, date):
    insertQuery = "INSERT INTO students (student_id, first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s, %s)"
    toInsert = (id, fName, lName, email, date)
    cursor.execute(insertQuery, toInsert)


addStudent(5, "john", "john", "john_john@john.ca", date(1992, 3, 18))

students = getAllStudents()


