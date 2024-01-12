import os
def first():  #Menu Bar
    print("1. ADD")
    print("2. SHOW")
    print("3. SEARCH")
    print("4. UPDATE")
    print("5. DELETE")
    print("6. EXIT")


def Add():    # Add data in our File (Name "new")
    name = input("Enter student name: ")
    subject = input("Enter student subject: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student_data = f"name : {name}\nsubject : {subject}\nrol no : {roll_number}\nmarks : {marks}\n"
    file = open("new.txt","a")
    file.write(student_data)
    file.close()

    print("Student added successfully!")
    Students_Managment()
            
        
def Show():  # To see data of our File
    f = open("new.txt","r")
    print(f.read())
    Students_Managment()
            

def Search():  # To Search Particular data of Our File
    print("1. search by name")
    print("2. search by subject")
    print("3. search by roll number")
    print("4. search by marks")
    type_search = int(input("enter choice from (1-4): "))
    f = open("new.txt","r")
    if type_search == 1:  # Searching Name
        name = input("enter name to search: ")
        
        for i in f:
            if name in i:
                print(i)
                break
            else:
                print("not found")   
            
    elif type_search == 2: # Searching Subject
        subject = input("enter subject to search: ")
        f = open("new.txt","r")
        for i in f:
            if subject in i:
                print(i)
                break
            else:
                print("not found")
    elif type_search == 3:  # Searching Roll No.
        roll_number = input("enter roll no to search: ")
        for i in f:
            if roll_number in i:
                print(i)
                break
            else:
                print("not found")
    elif type_search == 4: # Searching Marks
        marks = input("enter marks to search: ")
        f = open("new.txt","r")
        for i in f:
            if marks in i:
                print(i)
                break
            else:
                print("not found")
    else:
        print("invalid input!")
    Students_Managment()
def Update():  # Updating Our Data
    line= int(input("enter line number: "))
    data = input("enter new data: ")
    f = open("new.txt","r")
    g = f.readlines()    
    if 0 <= line < len(g):
        g[line] = f"{data}\n"
        f = open("new.txt","w")
        f.writelines(g)
        f.close()
        print("updated successfully")
    else:
        print("Invalid Input!")
    Students_Managment()

def Delete():  # Delete Data From Our File
    print("1. for delete file")
    print("2. for delete a line in a file")
    opt = int(input("enter option range(1-2)"))
    
    if opt == 1:# Deleting Complete File
        os.remove("new.txt")
        print("file removed successfully")
    elif opt ==2:# Deleting a Particular data
        
        line = int(input("enter line number: "))
        try:

            f = open("new.txt",'r')
            g = f.readlines()
            if 0 <= line < len(g):
              del g[line]
              f = open("new.txt","w")
              f.writelines(g)
              f.close()
              print(f"line {line} deleted successfully")
            else:
                print("Invalid Line Number")
        except FileNotFoundError:
            print("File Not Found.")
    else:
        print("Inavlid option")
    Students_Managment()

def Students_Managment():  # Starting Our Managment System
    first()  #opening Menu Bar
    option = int(input("Enter value from (1-6): "))
    if option == 1: # Adding Values
        Add()
    elif option == 2: # Showing Values
        Show()
    elif option == 3: # Searching Values
        Search()
    elif option == 4: # Updating Values
        Update()
    elif option == 5: # Deleting Values
        Delete()
    elif option == 6: # Closing Managment System
        print("Exiting student managemnt system. Thank You")
    else:
        print("Enter a valid value!")
        Students_Managment()
Students_Managment()