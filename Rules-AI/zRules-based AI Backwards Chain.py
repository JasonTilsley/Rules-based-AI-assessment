class rulesAI:
    def __init__(self):
        self.rules={
            '3e',1,
            '4t',1,
            '5y',1,
            '5p',1,
            '5f',1,
            '5m',1,
            '9w',1,
            '11u',1,
            '16e',1,#I chose to only test colour below the ring as if I tested both there would be a high chance of excessive weighting towards red stalks
            '20w',1,
        }
    def PoisonCheck(self, atribute):
        matches=0
        for rule in self.rules:
            for i in range(1, len(atribute)):
                check=str(str(i)+atribute[i])
                if check in self.rules:
                    matches+=1#I originally wanted to have it test if two or more valid features appeared, but since I got an error for putting a dictionary in another dictionary I instead decided to assign a value to each relevant possible attribute and sum the values to determine if it was toxic or not.
        matches/=11#for some reason, the value of matches was being multiplied by 11 so I'm reversing it here
        if matches<2:
            print("There is a decent likelihood of this mushroom being edible")
            return "e"
        else:
            print("There are decent odds of this mushroom being toxic")
            return "p"



MushFile=open("agaricus-lepiota.data","rt")
AI=rulesAI()
tries=0
success=0
FP=0
TP=0
FN=0
TN=0
results={}
for line in MushFile:
    lineA=line.strip()
    Mush=lineA.split(',')
    Mush[len(Mush)-1].strip()
    print(Mush)
    x=AI.PoisonCheck(Mush)
    print(x)
    print(Mush[0])
    if x==Mush[0]:
        print("Correct")
        tries+=1
        success+=1
        if Mush[0]=="e":
            TP+=1#The goal is to identify what mushrooms can be eaten, so a non-poisionous mushroom is listed as a positive
        else:
            TN+=1
    else:
        print("Incorrect")
        tries+=1
        if Mush[0]=="e":
            FN+=1
        else:
            FP+=1
print(tries)
print(success)
print ("True Positives: ", TP)
print ("True Negatives: ", TN)
print ("False Positives: ", FP)
print ("False Negatives: ", FN)
print("accuracy = ", success/tries)
print("precision = ", TP/(TP+FP))
print ("recall = ", TP/(TP+FN))
print ("F1 score = ", 2*(((TP/(TP+FP))*(TP/(TP+FN)))/((TP/(TP+FP))+(TP/(TP+FN)))))