# This is a python file to generate the values for various employers
# Manually inputting values from random.org is kinda a pain
# Also manually inputting lots of qualities is also a pain
# I had to manually input subjects and it was kind of a pain
# So to save me from this pain, I'll create a whole new program
# This might save me time, it might not, this file generates the values after the subjects for employer lists
# Edit: It saved me time
# Noticed that code isn't perfect as it could generate multiple of the same quality but that's fine

from random import randint

# Qualities that Employers want
qualities = ["friendly", "positive", "fluent", "confident", "honest", "humble", "courteous", "trustworthy",
             "honorable", "creative thinking", "original", "inventive", "productive", "adventurous",
             "agreeable", "ambitious", "bright", "considerate", "enthusiastic", "helpful",
             "loyal", "reliable", "sensible", "sincere"]


# Loop for each employer
for i in range(11):

    # Get the 5 values after the subjects
    for i in range(5):
        value = randint(1,10)
        print(value, end=", ")

    # True or False
    willingnessToLearn = randint(0,1)
    toLearn = False
    if willingnessToLearn == 0:
        print("False", end=", ")
    else:
        print("True", end=", ")

    temp = []

    # Employer qualities
    print("[", end="")
    for i in range(20):
        value = randint(0, len(qualities) - 1)
        # fixes duplicates
        temp.append(qualities[value])
        temp = list(set(temp))
        s = "'" + temp[-1] + "'"


    for i in range(6):
        s = "'" + temp[i] + "'"
        if i == 5:
            print(s, end="")
        else:
            print(s, end=", ")

    print("]", end="")
    print()





