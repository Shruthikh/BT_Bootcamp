def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    if average >= 60:
        grade = "First Class"
    elif average >= 50:
        grade = "Second Class"
    elif average >= 35:
        grade = "Pass Class"
    else:
        grade = "Fail"

    return total, average, grade


if __name__ == "__main__":
    try:
        name = input("Enter student name: ")
        m1 = float(input("Enter marks 1: "))
        m2 = float(input("Enter marks 2: "))
        m3 = float(input("Enter marks 3: "))

        if m1 < 0 or m2 < 0 or m3 < 0:
            print("Invalid marks")
        else:
            total, avg, grade = calculate_result(m1, m2, m3)
            print("Total =", total)
            print("Average =", avg)
            print("Class =", grade)
    except ValueError:
        print("Error: Enter numeric marks.")
