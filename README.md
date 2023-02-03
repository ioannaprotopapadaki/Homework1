# Homework1
## STUDENT QUERY TOOL
The "student query tool" is a tool the user can use to get a summary of student reports based on the given text file (student.txt).

The student.txt file contains information for master's students who graduated between 2019 and 2021 from different master's programs. The file contains 101 lines and six columns, and each observation represents the characteristics of 100 students. In detail, the columns from the text file are the following:

1.	Student_ID: A unique number for each student (unique identifier)
2.	Last Name: Student’s last name 
3.	First Name: Student’s first name
4.	Graduating Year: The year the student has graduated from school. Year counting from 2019 up to 2021
5.	Graduating Term: The term the student has graduated from school. Terms can be Fall, Spring, or Summer
6.	Degree Program: The master program that its student is taking. Master programs have 13 different categories: MSA, MSSD, MSBA, MSGF, MSIT, MSM, MSMI, MSMM, MST, MSSC, MBA, MBAP,MBAE

Based on the text file, a tool has been created that can display the followings:
-	All student records
-	Students whose last name begins with a certain string (case insensitive) 
-	Students whose first name begins with a certain string (case insensitive) 
-	Students whose graduating year is a certain year 
-	Students whose graduating term is a certain term 
-	A summary report of number and percent of students in each program, for students graduating on/after a certain year 
 
How to use the program

Once the user installs python and downloads the text file mentioned above, we need to open the text file. Python provides a built-in function for reading/opening files.

*Make sure you insert the correct file path in X as shown below*
with open (“X/Students.txt”, “r”) #Draft
with open(“/Users/ioannaprotopapadaki/Downloads/Students.txt”, “r”) #Example

The program is created to let the user select what student report they need to search for. If by mistake, they open the program or do not need any further analysis, a fifth option has been added for terminating the program.

Upon running the code, the program asks the user to select one of the following student report options:
1.	All student records
2.	Students whose last name begins with a certain string 
3.	Students whose first name begins with a certain string 
4.	Students whose graduating year is a certain year 
5.	Students whose graduating term is a certain term
6.	A summary report of number and percent of students in each program, for students graduating on/after a certain year 
7.	Program terminates
The user can enter a number from 1 to 7. For all numbers from 1 to 6 the user gets a table with the student’s id, number, name, surname, graduation year and term, and degree program. The program continually asks the user to insert a new number to get a summary report, and it is terminated only if the user selects the number 7. 

Based on the number chosen, the program works as follows:

If they type 1, they will get a summary table with all the records for the 100 master students.

If they type 2, a second question will pop-up asking the user to insert the string where their last name begins. When the user inserts the asking letter, a summary table will appear with all the students whose surnames start from the given letter.

If they type 3, a second question will pop-up asking the user to insert the string where their first name begins. When the user inserts the asking letter, a summary table will appear with all the students whose names start from the given letter.

If they type 4, a second question will pop-up asking from the user to insert the year of graduation between 2019 and 2021. When the user enters the year, a summary table with all the users who graduated this year will appear.

If they type 5, a second question will pop-up asking the user to insert the term of graduation. They can choose between the fall, the spring, or the summer term. When the user enters the term, a summary table with all the students who graduated the given term will appear.

If they type 6, they will first get a summary report of the number and percent of students in each program, while a second question will appear asking the user to insert the year and get the number of students who graduated on or after that year. Finally, when the user enters the year, a message will appear mentioning the total number of graduate students for the given year.

If they type 7, the program will terminate by greeting them.

If they enter invalid numbers or invalid data types, the program will keep working, and the user can retry.
