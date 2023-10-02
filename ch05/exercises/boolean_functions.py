user_score = float(input("What was your exam score?:"))

def percentage_to_letter(score=0):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def is_passing(letter=None):
    if letter == "A" or letter == "B" or letter == "C":
        is_passing = True
    else:
        is_passing = False
    return is_passing

letter_grade = percentage_to_letter(user_score)
passed = is_passing(letter_grade)

if passed is True:
    print("You passed with a score of", letter_grade)
elif passed is False:
    print("You failed with a score of", letter_grade)