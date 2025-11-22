# Student Result Calculator

This is a simple Python program that calculates student results based on
midterm marks, final exam marks, internal marks, and attendance.

It also calculates the class average, standard deviation, and gives grades.

## What this program does

* Takes input for many students
* Checks attendance
* Calculates marks
* Checks fail conditions
* Gives total marks
* Gives a final grade
* Shows a short analysis
* Shows class average and standard deviation

## How the marks are counted

* Midterm: out of 50 → counted as 30 marks
* Final exam: out of 100 → counted as 30 marks
* Internal marks: out of 35 → added directly
* Attendance: gives 0 to 5 marks
* If attendance is below 75% → student is debarred
* If final marks < 40 → student fails

## Grades

Grades are given using mean and standard deviation:

* S
* A
* B
* C
* D
* E
* F

## How to run

1. Install Python
2. Install numpy

``` pip install numpy ```

3. Run the file

``` python code.py ```

4. Enter student details when asked.

## Files in this project

* `code.py` → main program
* `README.md` → simple guide
* `statement.md` → explanation of the task
