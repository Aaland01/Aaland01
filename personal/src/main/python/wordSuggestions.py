import random
# Does not really work
# Was supposed to give out suggestions of a word 
# based on assumptions of which letters are places correctly through several iterations

length = 9
correct_Letters = "DERALN"
possible = "CB"
# QWX
typ = "NARDL"
order =   "****A**E*"
knowledge = {
    "D" : "220002200",
    "E" : "222002012",
    "R" : "200202202",
    "L" : "222200200", 
    "A" : "202012002",
    "N" : "200002202"
}

def suggestions(position : int, knowledge : dict):
    if position < 0 or position >= length: 
        print(f"Ended at pos: {position}")
        return newKnowledge
    checklist = []
    for letter in knowledge.keys():
        if isinstance(knowledge[letter], tuple):
            checklist.append("0")
        else:
            checklist.append(knowledge[letter][position])
    print(checklist)
    index = 0
    for code in checklist:
        if code=="1":
            print("Hit 1")
            suggestions(position + 1,newKnowledge)
        elif code=="2":
            print("Hit 2")
            # Check next letterposition with altered knowledge
            currentLetter = list(newKnowledge.keys())[index]
            print(currentLetter)
            newKnowledge[currentLetter] = (position, "1")
            suggestions(position + 1,newKnowledge)
    return newKnowledge
            
#suggestions(0, knowledge)
def randomizeStuff():
    for i in range(10):
        mid = typ
        midPossible = list(possible)
        randLetter1 = midPossible[random.randint(0,len(midPossible)-1)]
        midPossible.remove(randLetter1)
        randLetter2 = midPossible[random.randint(0,len(midPossible)-1)]
        mid += randLetter1 + randLetter2
        mid.join(possible[random.randint(0,len(possible)-1)])
        s = ''.join(random.sample(mid,len(mid)))
        s = s[:4] + "A" + s[4:6] + "E" + s[6:]
        print(s)
# randomizeStuff()
newKnowledge = knowledge
print(suggestions(0, newKnowledge))