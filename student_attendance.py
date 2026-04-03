students=[]

def add_student(name,attendance):
    students.append({
        "name":name,
        "attendance":attendance
    })
    print("Student Added")
    return

def view_students():
    if not students:
        print("There is no student in list")
        return
    

    for  i,student in enumerate(students,start=1):
         print(i,student["name"],"-",student["attendance"])

def search_student(name):
    for i,student in enumerate(students,start=1):
        if student["name"]==name:
            print(i,"-",student["name"],"-",student["attendance"])
            return
        print("Not Founded")

def present_count():
    count=0
    print("Present List:\n")
    for i,student in enumerate(students,start=1):
        if student["attendance"]=="present":
            count+=1
            print(i,"-",student["name"],"-",student["attendance"])
        
    if count==0:
        print("There Is No Student Present")
    else:
        print("Total Present:",count)
        

while True:
    print("1/ add student")
    print("2/ view students")
    print("3/ search student")
    print("4/ total present")
    print("5/ exit")

    user=input("Enter your choice").lower()

    if user=="5" or user =="exit":
        print("Program ended")
        break

    elif user=="1" or user=="add student":
        name=input("Enter name of student")
        attendance=input("Student is whether present or absent?")
        add_student(name,attendance)
    
    elif user=="2" or user=="view students":
        view_students()
    
    elif user=="3" or user=="search student":
        name=input("Enter name of student you want to search")
        search_student(name)

    elif user=="4" or user=="total present":
        present_count()

    else:
        print("Invalid Choice")