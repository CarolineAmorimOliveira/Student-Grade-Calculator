def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Welcome to the Student Grade Calculator!")
    num_students = int(input("How many students do you want to grade? "))

    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")
        grades = []

        for j in range(3):
            grade = float(input(f"Enter grade {j+1} for {name}: "))
            grades.append(grade)

        avg = calculate_average(grades)
        letter = letter_grade(avg)
        print(f"{name}'s average is {avg:.2f}, which is a letter grade of {letter}")


if __name__ == "__main__":
    main()