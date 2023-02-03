#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ioanna Protopapadaki MSBA


# In[ ]:


data= []

with open("/Users/ioannaprotopapadaki/Downloads/Students.txt", "r") as file:
    next(file)
    for i in file:
        ID, Last_Name, First_Name, Grad_Year, Grad_Term, Degree = i.strip().split("\t")
        data.append({
            "#": ID,
            "Last_Name": Last_Name,
            "First_Name": First_Name,
            "Grad_Year": Grad_Year,
            "Grad_Term": Grad_Term,
            "Degree": Degree })


while True:

    print("Please select one of the following types of reports:")
    print("1.Display all student records")
    print("2.Display students whose last name begins with a certain string")
    print("3.Display students whose first name begins with a certain string")
    print("4.Display all records for students whose graduating year is a certain year")
    print("5.Display all records for students whose graduating term is a certain term")
    print("6.Display a summary report of number and percent of students in each program,\n"
          "for students graduating on/after a certain year")
    print("7.The program will terminate")
    choice= input("Choose an option from the above, by typing a number from 1-7: ")

    print()

    if choice== "1":
        print("%-15s%-20s%-20s%-20s%-20s%-20s" % ("Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term","Degree Program"))
        
        for a in data:
            print("%-15s%-20s%-20s%-20s%-20s%-20s" % (a["#"],a["Last_Name"],a["First_Name"],a["Grad_Year"],a["Grad_Term"],a["Degree"]))
   
    elif choice== "2":
        string= input("Please enter the string that student's last name begins: ")
        print("%-15s%-20s%-20s%-20s%-20s%-20s" % ("Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term","Degree Program"))
        
        for a in data:
            if a["Last_Name"].lower().startswith(string.lower()):
                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (a["#"],a["Last_Name"],a["First_Name"],a["Grad_Year"],a["Grad_Term"],a["Degree"]))
  
    elif choice== "3":
        string= input("Please enter the string that student's first name begins: ")
        print("%-15s%-20s%-20s%-20s%-20s%-20s" % ("Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term","Degree Program"))
        
        for a in data:
            if a["First_Name"].lower().startswith(string.lower()):
                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (a["#"],a["Last_Name"],a["First_Name"],a["Grad_Year"],a["Grad_Term"],a["Degree"]))


    elif choice== "4":
        Grad_Year = input("Please enter student's graduation year from 2019 to 2021: ")
        print("%-15s%-20s%-20s%-20s%-20s%-20s" % ("Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term","Degree Program"))

        for a in data:
            if a["Grad_Year"] == Grad_Year:
                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (a["#"],a["Last_Name"],a["First_Name"],a["Grad_Year"],a["Grad_Term"],a["Degree"]))

    elif choice== "5":
        sem = input("Please enter student's graduation term. Term can be: fall, spring or summer: ")
        print("%-15s%-20s%-20s%-20s%-20s%-20s" % ("Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term","Degree Program"))

        for a in data:
            if a["Grad_Term"].lower()== sem.lower():
                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (a["#"],a["Last_Name"],a["First_Name"],a["Grad_Year"],a["Grad_Term"],a["Degree"]))
  
    elif choice== "6":
        degree_program = [s["Degree"] for s in data]
        student_count = {}
        
        for p in degree_program:
            student_count[p] = student_count.get(p, 0) + 1
        print("%-15s%-20s%-15s" % ("Program", "No. of Student", "Percentage"))
       
        for b, c in student_count.items():
            print("%-15s%-20s%-15.2f" % (b, c, (100 * c) / len(data)))
            
        count = 0
        year = int(input("Please enter a year to get a display of the number of students graduating on/after this certain year: "))

        for a in data:
            if int(a["Grad_Year"]) >= year:
                count += 1
        print(f"The number of students who graduate on or after {year} is {count}!")

    elif choice== "7":
        print("Program will terminate!")
        break

    else:
        print("Invalid infomation given. Please enter a valid number from 1-7.")

    print()

