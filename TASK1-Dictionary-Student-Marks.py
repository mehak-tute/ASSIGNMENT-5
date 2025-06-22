try:
    Student = {'Alice': '50', 'Bob': '80', 'Olivia': '76', 'Mehak': '80'}

    name = input("Enter the student's name: ")
    marks = Student[name]
    print("{}'s marks: {} ".format(name,marks))

except KeyError :
    print ("Student not found.")