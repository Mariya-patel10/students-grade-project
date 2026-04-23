def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent! You're at the top of your class! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! A little more focus and you'll get there! 💪"
    elif marks >= 60:
        return "D", "You passed! But there's room to improve. Don't give up! 📚"
    else:
        return "F", "Don't worry, failures are stepping stones. Study hard! 🔥"

def get_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("===== Student Grade Calculator =====\n")
    name = input("Enter student name: ").strip()
    marks = get_marks()
    grade, message = get_grade(marks)

    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

main()
