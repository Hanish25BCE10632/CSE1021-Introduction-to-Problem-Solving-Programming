import numpy as np 

def calculate_attendance_marks(attendance_percentage):
    if attendance_percentage >= 96.0:
        return 5  
    elif attendance_percentage >= 91.0:
        return 4 
    elif attendance_percentage >= 86.0:
        return 3 
    elif attendance_percentage >= 81.0:
        return 2 
    elif attendance_percentage >= 76.0:
        return 1  
    elif attendance_percentage == 75.0: 
        return 0 
    else: 
        return "Debarred" 

def calculate_result(midterm_marks, final_marks, internal_marks, attendance_percentage):
    attendance_result = calculate_attendance_marks(attendance_percentage)
    
    if attendance_result == "Debarred":
        return "Debarred from Subject"

    attendance_marks = attendance_result
    
    midterm_contribution = (midterm_marks / 50.0) * 30.0
    
    # 4. Convert final marks (max 100) to 30%: 
    final_contribution = (final_marks / 100.0) * 30.0
    
    # 5. Internal marks (max 35) directly contribute 35% 
    internal_contribution = internal_marks
    
    # 7. Check if final marks are less than 40% of 100 (i.e., < 40). 
    if final_marks < 40.0:
        return "F" 

    # 6. Calculate total marks out of 100 by summing all components. 
    total_marks = (midterm_contribution + final_contribution 
                   + internal_contribution + attendance_marks)
    
    # 8. Otherwise, return the calculated total marks.
    return total_marks

def assign_grade_and_analysis(total_marks, mean, std_dev):
    grade = ""
    
    threshold_S = mean + 1.5 * std_dev
    threshold_A = mean + 0.5 * std_dev
    threshold_B = mean - 0.5 * std_dev
    threshold_C = mean - 1.0 * std_dev
    threshold_D = mean - 1.5 * std_dev
    threshold_E = mean - 2.0 * std_dev

    if total_marks >= threshold_S and total_marks >= 90.0:
        grade = "S"
        analysis = " - Exceptional Performance!" 
    elif total_marks >= threshold_A and total_marks < threshold_S:
        grade = "A"
        analysis = " - Excellent Performance!" 
    elif total_marks >= threshold_B and total_marks < threshold_A:
        grade = "B"
        analysis = " - Good Performance" 
    elif total_marks >= threshold_C and total_marks < threshold_B:
        grade = "C"
        analysis = " - Satisfactory Performance" 
    elif total_marks >= threshold_D and total_marks < threshold_C:
        grade = "D"
        analysis = " - Marginal Pass" 
    elif total_marks >= threshold_E and total_marks < threshold_D:
        grade = "E"
        analysis = " - Requires significant effort"
    else:
        grade = "F"
        analysis = " - Needs Improvement"
        
    return f"{grade}{analysis}"

def get_student_input(student_number):
    """Helper function to get all required input from the user."""
    print(f"\n--- Entering Data for Student {student_number} ---")
    
    # Input with basic validation (assuming inputs are within maximum range)
    while True:
        try:
            midterm = float(input("Enter Midterm Marks (out of 50): "))
            if 0 <= midterm <= 50: 
                break
            else: 
                print("Error: Midterm marks must be between 0 and 50.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        try:
            final = float(input("Enter Final Exam Marks (out of 100): "))
            if 0 <= final <= 100: 
                break
            else: 
                print("Error: Final marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        try:
            internal = float(input("Enter Internal Assessment Marks (out of 35): "))
            if 0 <= internal <= 35: 
                break
            else: 
                print("Error: Internal marks must be between 0 and 35.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        try:
            attendance = float(input("Enter Attendance Percentage (0-100): "))
            if 0 <= attendance <= 100: 
                break
            else: 
                print("Error: Attendance percentage must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return midterm, final, internal, attendance

def display_result(student_num, total_marks, final_grade_analysis):
    """Helper function to display results in a formatted way."""
    print("\n-------------------------------------------")
    print(f"       STUDENT {student_num} FINAL RESULT        ")
    print("-------------------------------------------")
    
    if total_marks == "Debarred from Subject":
        print("STATUS: DEBARRED")
        print("Reason: Attendance below 75%.")
    elif total_marks == "F":
        print("STATUS: F (Fail)")
        print("Reason: Final Exam score less than 40% (required minimum).")
    else:
        print(f"Total Calculated Marks (out of 100): {total_marks:.2f}")
        print(f"Final Grade & Analysis: {final_grade_analysis}")
    print("-------------------------------------------\n")

def main():
    NUM_STUDENTS = 3
    all_student_data = []
    numerical_scores = []
    
    for i in range(1, NUM_STUDENTS + 1):
        midterm_marks, final_marks, internal_marks, attendance_percentage = get_student_input(i)

        result = calculate_result(midterm_marks, final_marks, internal_marks, attendance_percentage)

        all_student_data.append({'id': i, 'result': result})

        if isinstance(result, (float, int)):
            numerical_scores.append(result)
    
    if numerical_scores:
        mean_score = np.mean(numerical_scores)
        std_dev = np.std(numerical_scores)
    else:
        mean_score = 0
        std_dev = 0

    print("\n===========================================")
    print("        CLASS PERFORMANCE SUMMARY          ")
    print("===========================================")
    print(f"Class Average (Mean): {mean_score:.2f}")
    print(f"Standard Deviation (sigma): {std_dev:.2f}")
    print(f"Minimum Passing Mark : {mean_score - 2.0 * std_dev:.2f}")
    print("===========================================")

    for data in all_student_data:
        i = data['id']
        result = data['result']
        
        final_grade_analysis = ""

        if isinstance(result, (float, int)):
            final_grade_analysis = assign_grade_and_analysis(result, mean_score, std_dev)
        
        display_result(i, result, final_grade_analysis)
        
if __name__ == "__main__":
    main()
