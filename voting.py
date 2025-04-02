def displayResults():
        for x in votings.keys():
        #calculating the sum of voting
        sum=0
        for y in votings.keys():
            sum += int(votings[y])
        print (f'{x} : {round((100*votings[x]/sum),2)} %')

def processVoting():
    choice = input(f"Who do you vote for? 1 for {can1}, 2 for {can2} 0 for exit ")

    if choice =="1":
        votings[can1] +=1
        print(votings[can1])
    elif choice=="2":
        votings[can2] +=1
    else:
        return False


can1 = input("Name of candidate 1: ")
can2 = input("Name of candidate 2: ")

votings = {can1:0, can2:0}

for x in votings.keys():
    print (f'{x} : {votings[x]}')
while True:  
    if (processVoting()==False):
        break
    displayResults()

