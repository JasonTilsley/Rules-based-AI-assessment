class rulesAI:
    def __init__(self):
        self.rules={
            '1s',1,
            '2y',1,
            '3e',1,
            '3y',1,
            '5f',1,
            '5c',1,
            '6n',1,
            '9w',1,
            '11b',1,
            '16w',1,
            '16e',1,
            '20w',1,
            '22w',1,
        }
    def PoisonCheck(self, atribute):
        matches=0
        for rule in self.rules:
            for i in range(1, len(atribute)):
                check=str(str(i)+atribute[i])
                if check in self.rules:
                    matches+=1#I originally wanted to have it test if two or more valid features appeared, but since I got an error for putting a dictionary in another dictionary I instead decided to assign a value to each relevant possible attribute and sum the values to determine if it was toxic or not.
        matches/=11
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