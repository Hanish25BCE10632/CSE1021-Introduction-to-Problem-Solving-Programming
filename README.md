## 👨‍🎓 Student Marks Program: Easy Guide

This is a **Python program** that figures out student results. It uses marks from four places: the midterm, the final test, internal/project work, and attendance.

The program also gives useful info like the **class average**, a statistical number called **standard deviation**, and the **final letter grade**.



### ✅ What the Program Does

Here’s a simple list of the things this tool can do:

  * **Handle Many Students:** Takes marks and info for many students at once.
  * **Attendance Check:** Makes sure students came to class enough.
  * **Calculate Total Marks:** Adds up all the weighted marks correctly.
  * **Check for Failure:** Looks for reasons a student might fail the course.
  * **Give a Final Grade:** Assigns a letter grade (S, A, B, etc.).
  * **Analyze the Class:** Shows the **average** marks and the **standard deviation** for everyone.



### 🔢 How We Count the Marks (Out of 100)

We take different amounts from each test to get the full 100 final marks.

| Part of the Grade | Max Score (Input) | Counted As (Final Weight) |
| :--- | :---: | :---: |
| **Midterm Exam** | 50 marks | 30 marks |
| **Final Exam** | 100 marks | 30 marks |
| **Internal Marks** | 35 marks | 35 marks |
| **Attendance** | N/A (Based on %) | 5 marks |

#### 🛑 Failing Rules

It’s important to know the ways a student fails:

1.  **Attendance:** If the student's attendance is **under 75%**, they are **debarred** (they fail automatically, even with good marks).
2.  **Final Exam:** If the student scores **less than 40 marks** on the actual Final Exam (out of 100), they **fail** the subject.

#### Grades

The program uses the class **average** and **standard deviation** to decide the final letter grades (**S, A, B, C, D, E, F**).


### 🚀 How to Start the Program

You need two simple steps before you can run the program.

1.  **Install numpy**
    This is a helper program needed for the math (standard deviation). You only do this once.

    `pip install numpy`

2.  **Run the file**
    Use this command to start the main program:

    `python code.py`

    The program will then ask you to enter the student details.


### 📁 Project Files

  * `code.py`: The main program.
  * `README.md`: This guide.
  * `statement.md`: The paper explaining the main job/task.
