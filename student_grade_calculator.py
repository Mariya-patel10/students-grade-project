# Grade Calculator Program

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! Keep improving! 🙂"
    elif marks >= 60:
        return "D", "You passed! Work harder next time! 💪"
    else:
        return "F", "Don't give up! Try again! 🔄"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run program
main()
