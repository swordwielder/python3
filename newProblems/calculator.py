points = 0
def computeScore(answers):
    if year <= 4:
        points = points + year
def main():
    year = int(input("What year are you?(1,2,3,4):"))
    age = input(int("How old are you?:"))
    probation = input("Are you currently on probation? (Yes or No):")
    time = input(int("Are you Part-time or Full-time?(0 or 1):"))
    GPA = input(float("What is your GPA?:"))
    computeScore(answers[year,age,probation,time,GPA])
    return computeScore


if __name__ == "__main__":
    main()
