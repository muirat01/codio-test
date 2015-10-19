__author__ = 'muirat01'
#To change this template use Tools | Templates.

Distance = 100
SpeedOfRunner = 0
MStoMPH = 2.24
SpeedLimit = 20

NameOfRunner = input("Name of Runner: \n")
TimeTaken = float(input("Time Taken: "))

SpeedOfRunner = Distance / TimeTaken

SpeedInMPH = SpeedOfRunner * MStoMPH

print (NameOfRunner + " ran the 100M race in: " + str(round(SpeedInMPH,2)) + "MPH")