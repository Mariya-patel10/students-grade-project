# Student Grade Calculator

A simple Python program that takes a student's name and marks as input and returns their grade along with an encouraging message.

---

## Project Overview

This project was built as part of Week 2 of the Python internship program. The goal was to apply core Python concepts like conditional statements, loops, functions, and input validation in a real-world scenario — a student grade calculator.

The program:
- Accepts a student's name and marks (0–100)
- Validates the input and re-prompts if invalid
- Calculates the grade using if-elif-else logic
- Displays a result with a personalized message

---

## Grading Logic

| Marks Range | Grade |
|-------------|-------|
| 90 – 100    | A     |
| 80 – 89     | B     |
| 70 – 79     | C     |
| 60 – 69     | D     |
| 0 – 59      | F     |

---

## Project Structure

```
grade_project/
├── grade_calculator.py   # Main program
├── test_cases.txt        # All test cases with results
├── README.md             # Project documentation
└── screenshots.png          # Program output screenshot
```

---

## Setup Instructions

**Requirements:** Python 3.x (no external libraries needed)

1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the program:

```bash
python grade_calculator.py
```

---

## Functions Used

### `get_grade(marks)`
Takes marks as input and returns a tuple containing the grade letter and an encouraging message based on the grading logic.

### `get_marks()`
Handles user input for marks. Uses a `while` loop to keep asking until a valid integer between 0 and 100 is entered. Also handles non-numeric input using `try-except`.

### `main()`
Entry point of the program. Collects the student's name, calls `get_marks()` and `get_grade()`, then prints the final result.

---

## Sample Output

```
===== Student Grade Calculator =====

Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍
```

---

## What I Learned

- How to use `if-elif-else` for multi-condition logic
- Using `while` loops for input validation
- Writing reusable functions in Python
- Handling exceptions with `try-except`
- Breaking a problem into smaller functions before coding
