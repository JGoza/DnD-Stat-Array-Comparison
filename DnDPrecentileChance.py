import csv

# Numbers from AnyDice https://anydice.com/program/7b8c
# Make sure to put the Standard_Dist_4d6_Drop_Lowest_6_times.csv in the same folder as this file
coolDice = []

def makeDiceList():
    file = open("Standard_Dist_4d6_Drop_Lowest_6_times.csv","r")
    file.readline()

    for line in file:
        die = line.strip().split(",")
        #               Total Rolled, Percent Chance
        coolDice.append([int(die[0]), die[1]])
    file.close()
   
   
def compareRoll():
    roll = int(input("What was your total roll? "))
    
    lowPercent = 0
    topPercent = 0
    
    for x in range(roll-18):
        lowPercent += float(coolDice[x][1])
        
    topPercent = 100 - lowPercent
    print("Your roll of {} was better than {:.2f}% of rolls and was in the top {:.2f}%".format(roll, lowPercent, topPercent))
    
    
def main():
    makeDiceList()
    compareRoll()

if __name__ == '__main__':
    main()