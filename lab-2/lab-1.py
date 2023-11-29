file_path = 'score2.txt'

with open(file_path, 'r') as file:
    scores = dict()
    for line in file:
        data = line.strip().split()
        number = data[1]
        fname = data[2]
        lname = data[3]
        points = int(data[4])

        fullName = fname + ' ' + lname
        if fullName in scores:  # för att här coden betyder att dic ska chika om den personen redan finns ska addera value om inte ska lägga den som key
            scores[fullName] += points
        else:
            scores[fullName] = points

maxPoint = max(scores.values())
duktigast = [person for person, points in scores.items() if points == maxPoint]

print(scores)
print(
    f"The person(s) with the most points is/are: {', '.join(duktigast)} with {maxPoint} points.")
