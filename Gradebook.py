#Name - Aark Bharti
#Section-B
#Roll No.- 2501350046

import csv

# ---------------------- TASK 3 ---------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2
    else:
        return scores[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

# ---------------------- MAIN PROGRAM ---------------------------
def manual_input():
    marks = {}
    n = int(input("How many students? "))
    for i in range(n):
        name = input("Enter name: ")
        score = int(input("Enter marks: "))
        marks[name] = score
    return marks

def csv_input():
    marks = {}
    filename = input("Enter CSV file name: ")
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            marks[row[0]] = int(row[1])
    return marks

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def count_grade_distribution(grades):
    dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        dist[g] += 1
    return dist

def main():
    print("===== WELCOME TO GRADEBOOK ANALYZER =====")
    
    while True:
        print("\n1. Manual Input")
        print("2. CSV Input")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            marks = manual_input()
        elif choice == "2":
            marks = csv_input()
        else:
            print("Goodbye!")
            break

        # Statistics
        avg = calculate_average(marks)
        med = calculate_median(marks)
        mx = find_max_score(marks)
        mn = find_min_score(marks)

        print("\n--- STATISTICS ---")
        print("Average:", avg)
        print("Median:", med)
        print("Max Score:", mx)
        print("Min Score:", mn)

        # Grades
        grades = assign_grades(marks)
        dist = count_grade_distribution(grades)

        print("\n--- GRADE DISTRIBUTION ---")
        for g, c in dist.items():
            print(g, ":", c)

        # Pass / Fail (Task 5)
        passed = [name for name, m in marks.items() if m >= 40]
        failed = [name for name, m in marks.items() if m < 40]

        print("\nPassed Students:", passed)
        print("Failed Students:", failed)

        # Table Output (Task 6)
        print("\n--- FINAL TABLE ---")
        print("Name\tMarks\tGrade")
        print("-----------------------------")
        for name in marks:
            print(f"{name}\t{marks[name]}\t{grades[name]}")

        again = input("\nRun again? (y/n): ")
        if again.lower() != "y":
            break

# Run main program
main()
