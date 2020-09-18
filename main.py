import gspread
from oauth2client.service_account import ServiceAccountCredentials
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# Setting up the api's and their links
# This project uses the google sheet api (which is connected to the google forms)
# An adjective extractor library to extract adjectives from the extended response
# This is done by nltk
# Then we have the synonyms library to get synonyms for each adjective

# Adjectives & Synonyms will be a multidimensional array, each sublist is each person's adjectives in their response
adjectives = []
synonyms = []

# Google sheets api set up
scope = ['https://spreadsheets.google.com/feeds', "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Students (Responses)").sheet1

person = sheet.row_values(sheet.row_count)
# for every response to the survey
words = person[11].split(" ")

# Whole thing checks if any words are adjectives and gets their synonyms
for w in words:
    if wn.synsets(w):

        tmp = wn.synsets(w)[0].pos()
        if tmp == "a":
            print(w, ":", tmp)
            wSynonym = dictionary.synonym(w)
            synonyms += wSynonym

print(synonyms)

# Start of employers lists
# These are fake companies (some are based on real companies), you can tell from the names
# Some of the subjects for some of the employers aren't super realistic, but others are
# I just put in what came to mind for variety, Also locations are also fictional
# A proper version would have actual employers with actual locations and what not
# The values in the list are based on the spreadsheet questions
# Values are randomised externally (not in the website for consistency) using random.org, so they're not real values

employer1 = [2020, "computerland", "Belait", True, ["English", "History", "Business", "Computer Science"], 1, 5, 6, 4, 6, True, ['honest', 'confident', 'adventurous', 'productive', 'original', 'courteous']]
employer2 = [2020, "novideo", "Belait", False, ["Maths", "Computer Science", "Business", "Economics", "Physics"], 2, 5, 10, 8, 10, False, ['positive', 'creative thinking', 'reliable', 'confident', 'agreeable', 'considerate']]
employer3 = [2020, "ayyyymd", "Brunei-Muara", False, ["Maths", "Computer Science", "Business", "Economics", "Physics"], 4, 10, 3, 3, 10, True, ['positive', 'honest', 'reliable', 'confident', 'agreeable', 'adventurous']]
employer4 = [2020, "shintel", "Temburong", False, ["Maths", "Computer Science", "Business", "Economics", "Physics"], 7, 4, 9, 10, 10, False, ['positive', 'reliable', 'confident', 'considerate', 'adventurous', 'original']]
employer5 = [2020, "Bdope", "Tutong", True, ["Art", "Psychology", "Business", "Economics"], 2, 8, 4, 4, 5, True, ['positive', 'honest', 'creative thinking', 'reliable', 'confident', 'agreeable']]
employer6 = [2020, "Lavinci", "Brunei-Muara", True, ["Art", "English", "Psychology", "Economics"], 7, 2, 2, 10, 10, True, ['positive', 'creative thinking', 'reliable', 'confident', 'agreeable', 'considerate']]
employer7 = [2020, "yCircle", "Belait", False, ["Maths", "Physics", "Computer Science"], 3, 7, 6, 2, 9, False, ['loyal', 'reliable', 'agreeable', 'considerate', 'enthusiastic', 'courteous']]
employer8 = [2020, "Shell", "Brunei-Muara", False, ["Economics", "Business", "Geography"], 6, 2, 1, 9, 10, True, ['positive', 'confident', 'agreeable', 'productive', 'fluent', 'sincere']]
employer9 = [2020, "Pear", "Tutong", True, ["Computer Science", "Physics", "Business"], 9, 3, 5, 2, 10, True, ['honest', 'confident', 'considerate', 'adventurous', 'productive', 'enthusiastic']]
employer10 = [2020, "Wacdonalds", "Belait", False, ["Psychology", "English", "Geography", "Economics", "Drama"], 10, 10, 1, 5, 10, True, ['honest', 'creative thinking', 'reliable', 'considerate', 'original', 'trustworthy']]
employer11 = [2020, "WagyuQueen", "Belait", False, ["Psychology", "English", "Geography", "Economics"], 1, 4, 8, 10, 3, False, ['positive', 'honest', 'confident', 'adventurous', 'considerate', 'productive']]

employers = []
employers.append(employer1)
employers.append(employer2)
employers.append(employer3)
employers.append(employer4)
employers.append(employer5)
employers.append(employer6)
employers.append(employer7)
employers.append(employer8)
employers.append(employer9)
employers.append(employer10)
employers.append(employer11)


employersWeightingScores = {}
for i in range(11):
    employersWeightingScores[i] = 0.1

# Weighting Algorithm Part
# There are some arbitary values that I've decided to use for the weight
# like how location is worth 5 and virtual work is worth 2.
# Also the higher the weight for the employers, the better
# It's like the employers score

i = 0
for employer in employers:
    weight = float(0)
    #Location
    userLocation = person[2]
    if userLocation == employer[2]:
        weight += 5

    #VirtualWork

    if person[3] == employer[3]:
        weight += 2

    #Subjects

    usersubjects = person[4].split(', ')
    for user_subject in usersubjects:
        for employer_subject in employer[4]:
            if user_subject == employer_subject:
                weight += 1.5

    #Teamwork skills

    # If an employer has a 2 for importance on teamwork, then it'll have a weight of 0.4 per point that the user has.
    # If an employer has a 9 for importance on teamwork, then it'll have a weight of 1.8 per point that the user has.
    # Ie it dictates how important the employer values teamwork and future skills
    weight += float(person[5]) * (float(employer[5]) * 0.1)

    #Creativity

    weight += float(person[6]) * (float(employer[6]) * 0.1)

    #Organization skills

    weight += float(person[7]) * (float(employer[7]) * 0.1)

    #Problem Solving Skills

    weight += float(person[8]) * (float(employer[8]) * 0.1)

    #General Computer Skills

    weight += float(person[9]) * (float(employer[9]) * 0.1)

    #Willingness to learn

    if person[10] == False and employer[10] == True:
        weight -= 3
    elif person[10] == True and employer[10] == True:
        weight += 3

    #Qualities
    for employerquality in employer[11]:
        for userquality in synonyms:
            if userquality == employerquality:
                weight += 0.5

    employersWeightingScores[i] = weight
    i += 1

# sort employers weighting score
sortedRankings = sorted(employersWeightingScores, key=employersWeightingScores.get)
sortedRankings.reverse()
for i in range(11):
    employerName = employers[sortedRankings[i]][1]
    print(str(i+1) + ": " + employerName)




