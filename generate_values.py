# This is a python file to generate the values for various employers
# Manually inputting values from random.org is kinda a pain
# Also manually inputting lots of qualities is also a pain
# I had to manually input subjects and it was kind of a pain
# So to save me from this pain, I'll create a whole new program
# This might save me time, it might not, this file generates the values after the subjects for employer lists

from random import randint

# Qualities that Employers want
qualities = ["friendly", "positive", "fluent", "confident", "honest", "humble", "courteous", "trustworthy",
             "honorable", "creative thinking", "original", "inventive", "productive", "adventurous",
             "agreeable", "ambitious", "bright", "considerate", "enthusiastic", "helpful",
             "loyal", "reliable", "sensible", "sincere"]


# Loop for each employer
for i in range(11):

    temp = []
    temp2 = []
    print("[", end=", ")

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

    # Employer qualities
    print("[")
    for i in range(10):
        value = randint(0, len(qualities) - 1)
        temp2.append(qualities[value])
        print(qualities[value], end=", ")
    
    print("], ", end=", ")


    print("]", end=", ")
    print()





