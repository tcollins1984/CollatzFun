#The collatz algorithm ends when you hit a powewr of 2.  All subsequent steps will
#be to divide by 2 until you reach one.  
#The only way to initally "hit" a power of 2 is by taking an oddd number X and performing 3X + 1.
#Let's look at the first 100 powers of 2 and see if they will ever be that power of 2 which ends
#the algorigthm when by being reached from an odd number

#We'll create a dataframe in pandas to show the power of 2 that ends the algorithm and the odd number which
#will land us there. We'll also have a brief text description saying whether or not that particular power of 2 is a terminal number

import pandas as pd
max_power = 100
pwr2 = []
for i in range(0,max_power+1):
    pwr2.append(2**i)

#Let's all each element of pwrd Ni. Since it must be reached by running an odd number X through 3X+1,
#we can find out if this is so by inverting the function (Ni - 1)/3 = X

#Since X must be a whole number, we know that Ni is reached through the application
# of the 3X + 1 algorith when (Ni - 1)%3 = 0

cc = []
for n in range(0,len(pwr2)):
    if (pwr2[n]-1)%3 == 0:
            cc.append([pwr2[n],(pwr2[n]-1)/3,'will converge form here'])
    else:
            cc.append([pwr2[n], 'na','cannot be reached by 3n + 1'])
number = []
odd = []
result = []
for i in range(0,len(cc)):
    number.append(cc[i][0])
    odd.append(cc[i][1])
    result.append(cc[i][2])
powerTwo = pd.DataFrame({"2 to the Index":number, "Corresponding Odd if Any":odd,"Result":result})
print(powerTwo)

#use the following code to print to csv file in the directory of your choice
#powerTwo.to_csv('CollatzTerminalNumbers.csv')
