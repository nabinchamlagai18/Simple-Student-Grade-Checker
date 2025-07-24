
subjects = ("Math", "Science", "English", "History")

# Grade boundaries (A, B, C, D, F)
grades = ["A", "B", "C", "D", "F"]

# Welcome message
print("Welcome to the Grade Checker!")
print("Available subjects:", subjects)

# Ask user to enter a subject
subject = input("Enter the subject name: ")

# Check if the subject is valid
if subject in subjects:
    # Ask for score
    try:
        score = int(input("Enter the score (0-100): "))

        # Validate score range
        if score < 0 or score > 100:
            print("Invalid score! Please enter a number between 0 and 100.")
        else:
            # Grade checking using if-elif-else
            if score >= 90:
                grade = grades[0]  # A
            elif score >= 80:
                grade = grades[1]  # B
            elif score >= 70:
                grade = grades[2]  # C
            elif score >= 60:
                grade = grades[3]  # D
            else:
                grade = grades[4]  # F
            
            # Output the result
            print(f"Subject: {subject}")
            print(f"Score: {score}")
            print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for score.")
else:
    print("Invalid subject! Please choose from the available list.")
