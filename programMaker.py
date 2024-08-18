print("Welcome to Program Maker")

ready_program = [
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]]
          ]

print_Program = []
ready_group = []
print_group = []


programFile = input("Enter your txt file: ")
with open(programFile, 'r') as f:
    programList = f.readlines()

programList = [item.replace('\n','') for item in programList]
#print(programList)
    

Names   =  [] # Lesson Names
Days    =  [] # Number of Days
Hours   =  [] # Hours
Hours1  =  []
useless = "NO"

lessonNumber = int(programList[0])
del programList[0]

def programMaker(Day, Time):
    global useless
    Day = Day.upper()

    # Monday

    if Day+Time == "MONDAY8:30" or Day+Time == "M8":
        if ready_program[0][0] == [None]:
            ready_program[0][0] = Names[i]
        else:
            useless = "YES"
    
    if Day+Time == "MONDAY10:30" or Day+Time == "M10":
        if ready_program[0][1] == [None]:
            ready_program[0][1] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "MONDAY12:30" or Day+Time == "M12":  
        if ready_program[0][2] == [None]:
            ready_program[0][2] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "MONDAY14:30" or Day+Time == "M14":
        if ready_program[0][3] == [None]:
            ready_program[0][3] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "MONDAY16:30" or Day+Time == "M16":       
        if ready_program[0][4] == [None]:
            ready_program[0][4] = Names[i]
        else:
            useless = "YES"
    
    # Tuesday

    if Day+Time == "TUESDAY8:30" or Day+Time == "TU8":       
        if ready_program[1][0] == [None]:
            ready_program[1][0] = Names[i]
        else:
            useless = "YES"
    
    if Day+Time == "TUESDAY10:30" or Day+Time == "TU10":
        if ready_program[1][1] == [None]:
            ready_program[1][1] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "TUESDAY12:30" or Day+Time == "TU12":   
        if ready_program[1][2] == [None]:
            ready_program[1][2] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "TUESDAY14:30" or Day+Time == "TU14":
        if ready_program[1][3] == [None]:
            ready_program[1][3] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "TUESDAY16:30" or Day+Time == "TU16":
        if ready_program[1][4] == [None]:
            ready_program[1][4] = Names[i]
        else:
            useless = "YES"

    # Wednesday
    
    if Day+Time == "WEDNESDAY8:30" or Day+Time == "W8":
        if ready_program[2][0] == [None]:
            ready_program[2][0] = Names[i]
        else:
            useless = "YES"
    
    if Day+Time == "WEDNESDAY10:30" or Day+Time == "W10":
        if ready_program[2][1] == [None]:
            ready_program[2][1] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "WEDNESDAY12:30" or Day+Time == "W12":    
        if ready_program[2][2] == [None]:
            ready_program[2][2] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "WEDNESDAY14:30" or Day+Time == "W14":
        if ready_program[2][3] == [None]:
            ready_program[2][3] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "WEDNESDAY16:30" or Day+Time == "W16":
        if ready_program[2][4] == [None]:
            ready_program[2][4] = Names[i]
        else:
            useless = "YES"
    
    # Thursday

    if Day+Time == "THURSDAY8:30" or Day+Time == "TH8":
        if ready_program[3][0] == [None]:
            ready_program[3][0] = Names[i]
        else:
            useless = "YES"
    
    if Day+Time == "THURSDAY10:30" or Day+Time == "TH10":
        if ready_program[3][1] == [None]:
            ready_program[3][1] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "THURSDAY12:30" or Day+Time == "TH12":    
        if ready_program[3][2] == [None]:
            ready_program[3][2] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "THURSDAY14:30" or Day+Time == "TH14":
        if ready_program[3][3] == [None]:
            ready_program[3][3] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "THURSDAY16:30" or Day+Time == "TH16":
        if ready_program[3][4] == [None]:
            ready_program[3][4] = Names[i]
        else:
            useless = "YES"

    # Friday

    if Day+Time == "FRIDAY8:30" or Day+Time == "F8":      
        if ready_program[4][0] == [None]:
            ready_program[4][0] = Names[i]
        else:
            useless = "YES"
    
    if Day+Time == "FRIDAY10:30" or Day+Time == "F10":       
        if ready_program[4][1] == [None]:
            ready_program[4][1] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "FRIDAY12:30"  or Day+Time == "F12":  
        if ready_program[4][2] == [None]:
            ready_program[4][2] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "FRIDAY14:30" or Day+Time == "F14":       
        if ready_program[4][3] == [None]:
            ready_program[4][3] = Names[i]
        else:
            useless = "YES"

    if Day+Time == "FRIDAY16:30" or Day+Time == "F16":
        if ready_program[4][4] == [None]:
            ready_program[4][4] = Names[i]
        else:
            useless = "YES"

#print(lessonNumber)
for i in range(0,lessonNumber):
    lessonName = programList[0]
    del programList[0]
    Names.append(lessonName)

for i in range(0,lessonNumber):
    day_number = int(programList[0])
    del programList[0]
    Days.append(day_number)   

    for j in range(0,day_number):
         #day_hour = input(f"Enter Day and Hour for {Names[i]} Day {j+1} group 1: ")
         Hours.append(programList[0])
         Hours1.append(programList[0])

         del programList[0]

    for k in range(0,len(Hours1)):
        hours = Hours1[k]
        Day = hours.split()[0]
        Time = hours.split()[1]

        #print(Day)
        #print(Time)
        #print(Names[i])

        programMaker(Day, Time)
        

    Hours1.clear()
  

#print(ready_program)

def readyProgram(program):
    print_Program.append(program)

def printProgram(program):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    timeslots = ["8:30-10:20", "10:30-12:20", "12:30-14:20", "14:30-16:20", "16:30-17:20"]
    # Print header
    print(" ".join(f"{day:<12}" for day in days))
    print("-" * 64)
    # Print time slots and schedule
    for i, timeslot in enumerate(timeslots):
        schedule = [program[day][i] if isinstance(program[day][i], str) else "" for day in range(len(days))]
        print(" ".join(f"{entry:<12}" for entry in schedule)+f"| {timeslots[i]}")        

if useless == "YES":
    ready_program = [
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]],  
          ]
    useless = "NO"
else:
    readyProgram(ready_program)
    for i in range(0,len(Names)):
        ready_group.append(f"Lesson {Names[i]}: Group 1")
    print_group.append(", ".join(ready_group))
    #print(print_group)
    ready_group = []


ready_program = [
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]],  
          ]

#print(Days)
#print(Hours)

# Lesson 1 

Hours2 = [] # Lesson 1 Group 2,3,4... Hours (Temporary)
groupNumber2 = 1 # Lesson 1 No. Of Groups

# Lesson 2

Hours3 = [] # Lesson 1 Group 2,3,4... Hours
Hours4 = [] # All Hours (Temporary)
Hours5 = [] # Lesson 2 Group 2,3,4... Hours (Temporary)
Hours6 = [] # All Hours except Lesson 1 and 2 Hours (Temporary)

groupNumber3 = 1 # Lesson 1 No. of Groups (Temporary)
groupNumber4 = 1 # Lesson 2 No. of Groups

# Lesson 3

Hours7 = [] # Lesson 2 Group 2,3,4... Hours 
Hours8 = [] # Lesson 3 Group 2,3,4... Hours (Temporary)
Hours9 = [] # All Hours except Lesson 1 , 2 and 3 Hours (Temporary)
Hours10 = [] # All Hours (Temporary)
Hours11 = [] # Lesson 2 Group 2,3,4... Hours (Temporary)

groupNumber5 = 1 # Lesson 3 No. of Groups
groupNumber6 = 1 # Lesson 2 No of. Groups (Temporary)

# Lesson 4

Hours12 = [] # Lesson 3 Group 2,3,4... Hours (Temporary)
Hours13 = [] # Lesson 4 Group 2,3,4... Hours (Temporary)
Hours14 = [] # All Hours (Temporary)
Hours15 = [] # All Hours except Lesson 1 , 2 , 3 and 4 Hours (Temporary)
Hours16 = [] # Lesson 3 Group 2,3,4... Hours

groupNumber7 = 1 # Lesson 3 No. of Groups (Temporary)
groupNumber8 = 1 # Lesson 4 No. of Groups

# Lesson 5

Hours17 = [] # Lesson 5 Group 2,3,4... Hours (Temporary)
Hours18 = [] # All Hours (Temporary)
Hours19 = [] # All Hours except Lesson 1 , 2 , 3 , 4 and 5 Hours (Temporary)
Hours20 = [] # Lesson 4 Group 2,3,4... Hours
Hours21 = [] # Lesson 4 Group 2,3,4... Hours (Temporary)

groupNumber9 = 1 # Lesson 5 No. of Groups
groupNumber10 = 1 # Lesson 4 No. of Groups (Temporary)

# Lesson 6

Hours22 = [] # Lesson 5 Group 2,3,4... Hours (Temporary)
Hours23 = [] # Lesson 6 Group 2,3,4... Hours (Temporary)
Hours24 = [] # All Hours (Temporary)
Hours25 = [] # All Hours except Lesson 1 , 2 , 3 , 4 and 5 Hours (Temporary)
Hours26 = [] # Lesson 5 Group 2,3,4... Hours

groupNumber11 = 1 # Lesson 6 No. of  Groups
groupNumber12 = 1 # Lesson 5 No. of Groups (Temporary)

#

#answer = input(f"Lesson {Names[0]} has 2. group? ")
answer = programList[0]
del programList[0]
a=2

while answer.upper() == "YES":  
    groupNumber2 += 1
    x=0
    for i in range(0,Days[0]):
         #day_hour = input(f"Enter Day and Hour for {Names[0]} Day {i+1} group {a}: ")
         Hours2.append(programList[0])
         Hours3.append(programList[0])
         #print(Hours2)
         del programList[0]
    
    for i in range(0,len(Names)):
        if i != 0 and i != len(Names):
            for k in range(0,Days[i]):
                Hours2.append(Hours[Days[0]+k+x])
                #print(Hours2)
            x = x + Days[i]

        for j in range(0,len(Hours2)):
                hours = Hours2[j]
                Day = hours.split()[0]
                Time = hours.split()[1]

                programMaker(Day, Time)
        
        #print(Hours2)
        Hours2.clear()

        
    if useless == "YES":
        ready_program = [
            [[None],[None],[None],[None],[None]], 
            [[None],[None],[None],[None],[None]], 
            [[None],[None],[None],[None],[None]], 
            [[None],[None],[None],[None],[None]], 
            [[None],[None],[None],[None],[None]],  
            ]

    else:
        readyProgram(ready_program)
        for i in range(0,len(Names)):
            if i == 0:
                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber2}")
            if i != 0:
                ready_group.append(f"Lesson {Names[i]}: Group 1")
        print_group.append(", ".join(ready_group))
        #print(print_group)
        ready_group = []

    ready_program = [
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]], 
           [[None],[None],[None],[None],[None]],  
          ]
    useless = "NO"

    #answer = input(f"Lesson {Names[0]} has {a+1}. group? ")
    answer = programList[0]
    del programList[0]
    a = a + 1

else:
    if lessonNumber > 1:
        #answer1 = input(f"Lesson {Names[1]} has 2. group? ")
        answer1 = programList[0]
        del programList[0]
        a=2
        while answer1.upper() == "YES":  
            num = 0
            groupNumber4 += 1


            for i in range(0,Days[1]):
                #day_hour = input(f"Enter Day and Hour for {Names[1]} Day {i+1} group {a}: ")
                #Hours4[Days[0]+i]=day_hour
                Hours5.append(programList[0])
                Hours7.append(programList[0])
               #print(Hours4)

                del programList[0]

            for group in range(0,groupNumber2):
                

                for i in range(0,len(Hours)):
                    Hours6.append(Hours[i])
                #print(Hours6)
                for i in range(0,Days[0]):
                    del Hours6[0]
                #print(Hours6)
                for i in range(0,Days[1]):
                    del Hours6[0]
                #print(Hours6)


                for i in range(0,lessonNumber):


                    if i == 0:
                        if groupNumber3 == 1: # GOOD
                            for j in range(0,Days[0]):
                                Hours4.append(Hours[j])
                        
                        elif groupNumber3 != 1:
                            for j in range(0,Days[0]):
                                Hours4.append(Hours3[j+num])
                            num = num + Days[0]
                                            
                    if i == 1: # GOOD
                        for j in range(0,Days[1]):
                            Hours4.append(Hours5[j])
                    
                    if i != 0 and i != 1: # GOOD
                        for j in range(0,Days[i]):
                            Hours4.append(Hours6[0])
                            del Hours6[0]
                            #print(Hours4)

                    for j in range(0,len(Hours4)): #GOOD
                        hours = Hours4[j]
                        Day = hours.split()[0]
                        Time = hours.split()[1]

                        programMaker(Day, Time)
                    
                    Hours4.clear()

                if useless == "YES":
                        ready_program = [
                            [[None],[None],[None],[None],[None]], 
                            [[None],[None],[None],[None],[None]], 
                            [[None],[None],[None],[None],[None]], 
                            [[None],[None],[None],[None],[None]], 
                            [[None],[None],[None],[None],[None]],  
                            ]

                else:
                    readyProgram(ready_program)
                    for i in range(0,len(Names)):
                        if i == 0:
                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber3}")
                        if i == 1:
                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber4}")
                        if i != 0 and i != 1:
                            ready_group.append(f"Lesson {Names[i]}: Group 1")
                    print_group.append(", ".join(ready_group))
                    #print(print_group)
                    ready_group = []

                ready_program = [
                        [[None],[None],[None],[None],[None]], 
                        [[None],[None],[None],[None],[None]], 
                        [[None],[None],[None],[None],[None]], 
                        [[None],[None],[None],[None],[None]], 
                        [[None],[None],[None],[None],[None]],  
                        ]
                useless = "NO"

                groupNumber3 += 1

            Hours5.clear()
            groupNumber3 = 1
                        
        

            #answer1=input(f"Lesson {Names[1]} has {a+1}. group? ")
            answer1 = programList[0]
            del programList[0]
            a = a + 1

        else:
            if lessonNumber > 2:
                #answer2 = input(f"Lesson {Names[2]} has 2. group? ")
                answer2 = programList[0]
                del programList[0]
                a = 2
                while answer2.upper() == "YES":
                    num1 = 0 
                    groupNumber5 += 1                  

                    for i in range(0,Days[2]):
                        #day_hour = input(f"Enter Day and Hour for {Names[2]} Day {i+1} group {a}: ")
                        Hours8.append(programList[0])
                        Hours16.append(programList[0])

                        del programList[0]
                    
                    for i in range(0,len(Hours7)):
                        Hours11.append(Hours7[i])
                    
                    
                    for group1 in range(0, groupNumber4):
                        num = 0

                        for group in range(0,groupNumber2):
                

                            for i in range(0,len(Hours)):
                                Hours9.append(Hours[i])
                            #print(Hours6)
                            for i in range(0,Days[0]):
                                del Hours9[0]
                            #print(Hours6)
                            for i in range(0,Days[1]):
                                del Hours9[0]
                            #print(Hours6)
                            for i in range(0,Days[2]):
                                del Hours9[0]


                            for i in range(0,lessonNumber):

                                if i == 0:
                                    if groupNumber3 == 1: # GOOD
                                        for j in range(0,Days[0]):
                                            Hours10.append(Hours[j])
                                    
                                    elif groupNumber3 != 1:
                                        for j in range(0,Days[0]):
                                            Hours10.append(Hours3[j+num])
                                        num = num + Days[0]
                                                        
                                if i == 1: # GOOD
                                    if groupNumber6 == 1:
                                        for j in range(0,Days[1]):
                                            Hours10.append(Hours[j+Days[0]])

                                    elif groupNumber6 != 1:
                                        for j in range(0,Days[1]):
                                            Hours10.append(Hours11[j])
                                
                                if i == 2: 
                                    for j in range(0,Days[2]):
                                        Hours10.append(Hours8[j])
                                
                                if i != 0 and i != 1 and i != 2: # GOOD
                                    for j in range(0,Days[i]):
                                        Hours10.append(Hours9[0])
                                        del Hours9[0]
                                        #print(Hours4)
                                
                                #print(Hours10)
                                for j in range(0,len(Hours10)): #GOOD
                                    hours = Hours10[j]
                                    Day = hours.split()[0]
                                    Time = hours.split()[1]

                                    programMaker(Day, Time)
                                
                                Hours10.clear()

                            if useless == "YES":
                                    ready_program = [
                                        [[None],[None],[None],[None],[None]], 
                                        [[None],[None],[None],[None],[None]], 
                                        [[None],[None],[None],[None],[None]], 
                                        [[None],[None],[None],[None],[None]], 
                                        [[None],[None],[None],[None],[None]],  
                                        ]

                            else:
                                readyProgram(ready_program)
                                for i in range(0,len(Names)):
                                    if i == 0:
                                        ready_group.append(f"Lesson {Names[i]}: Group {groupNumber3}")
                                    if i == 1:
                                        ready_group.append(f"Lesson {Names[i]}: Group {groupNumber6}")
                                    if i == 2:
                                        ready_group.append(f"Lesson {Names[i]}: Group {groupNumber5}")
                                    if i != 0 and i != 1 and i != 2:
                                        ready_group.append(f"Lesson {Names[i]}: Group 1")
                                print_group.append(", ".join(ready_group))
                                #print(print_group)
                                ready_group = []

                            ready_program = [
                                    [[None],[None],[None],[None],[None]], 
                                    [[None],[None],[None],[None],[None]], 
                                    [[None],[None],[None],[None],[None]], 
                                    [[None],[None],[None],[None],[None]], 
                                    [[None],[None],[None],[None],[None]],  
                                    ]
                            useless = "NO"

                            groupNumber3 += 1

                        
                        groupNumber3 = 1
                        groupNumber6 += 1

                        if group1 != 0:
                            for i in range(0,Days[1]):
                                del Hours11[0]
                    
                    groupNumber6 = 1
                    Hours8.clear()


                    #answer2=input(f"Lesson {Names[2]} has {a+1}. group? ")
                    answer2 = programList[0]
                    del programList[0]
                    a = a + 1
                    

                else:
                    if lessonNumber > 3:
                        #answer3 = input(f"Lesson {Names[3]} has 2. group? ")
                        answer3 = programList[0]
                        del programList[0]
                        a=2
                        while answer3.upper() == "YES":
                        
                            num1 = 0    
                            groupNumber8 += 1             

                            for i in range(0,Days[3]):
                                #day_hour = input(f"Enter Day and Hour for {Names[3]} Day {i+1} group {a}: ")
                                Hours13.append(programList[0])
                                Hours20.append(programList[0])

                                del programList[0]
                            
                            for i in range(0,len(Hours16)):
                                Hours12.append(Hours16[i])
                            
                            for group2 in range(0, groupNumber5):
                            
                                for i in range(0,len(Hours7)):
                                    Hours11.append(Hours7[i])
                                                               
                                for group1 in range(0, groupNumber4):
                                    num = 0

                                    for group in range(0,groupNumber2):
                            

                                        for i in range(0,len(Hours)):
                                            Hours15.append(Hours[i])

                                        for i in range(0,Days[0]):
                                            del Hours15[0]
                                        for i in range(0,Days[1]):
                                            del Hours15[0]
                                        for i in range(0,Days[2]):
                                            del Hours15[0]
                                        for i in range(0,Days[3]):
                                            del Hours15[0]


                                        for i in range(0,lessonNumber):

                                            if i == 0:
                                                if groupNumber3 == 1: # GOOD
                                                    for j in range(0,Days[0]):
                                                        Hours14.append(Hours[j])
                                                
                                                elif groupNumber3 != 1:
                                                    for j in range(0,Days[0]):
                                                        Hours14.append(Hours3[j+num])
                                                    num = num + Days[0]
                                                                    
                                            if i == 1: # GOOD
                                                if groupNumber6 == 1:
                                                    for j in range(0,Days[1]):
                                                        Hours14.append(Hours[j+Days[0]])

                                                elif groupNumber6 != 1:
                                                    for j in range(0,Days[1]):
                                                        Hours14.append(Hours11[j])
                                            
                                            if i == 2:
                                                if groupNumber7 == 1:
                                                    for j in range(0,Days[2]):
                                                        Hours14.append(Hours[j+Days[0]+Days[1]])
                                                elif groupNumber7 != 1:
                                                    for j in range(0,Days[2]):
                                                        Hours14.append(Hours12[j])
                                            
                                            if i == 3:
                                                for j in range(0,Days[3]):
                                                    Hours14.append(Hours13[j])
                                            
                                            if i != 0 and i != 1 and i != 2 and i != 3: # GOOD
                                                for j in range(0,Days[i]):
                                                    Hours14.append(Hours15[0])
                                                    del Hours15[0]
                                                    #print(Hours4)
                                            
                                            #print(Hours10)
                                            for j in range(0,len(Hours14)): #GOOD
                                                hours = Hours14[j]
                                                Day = hours.split()[0]
                                                Time = hours.split()[1]

                                                programMaker(Day, Time)
                                            
                                            Hours14.clear()

                                        if useless == "YES":
                                                ready_program = [
                                                    [[None],[None],[None],[None],[None]], 
                                                    [[None],[None],[None],[None],[None]], 
                                                    [[None],[None],[None],[None],[None]], 
                                                    [[None],[None],[None],[None],[None]], 
                                                    [[None],[None],[None],[None],[None]],  
                                                    ]

                                        else:
                                            readyProgram(ready_program)
                                            for i in range(0,len(Names)):
                                                if i == 0:
                                                    ready_group.append(f"Lesson {Names[i]}: Group {groupNumber3}")
                                                if i == 1:
                                                    ready_group.append(f"Lesson {Names[i]}: Group {groupNumber6}")
                                                if i == 2:
                                                    ready_group.append(f"Lesson {Names[i]}: Group {groupNumber7}")
                                                if i == 3:
                                                    ready_group.append(f"Lesson {Names[i]}: Group {groupNumber8}")
                                                if i != 0 and i != 1 and i != 2 and i != 3:
                                                    ready_group.append(f"Lesson {Names[i]}: Group 1")
                                            print_group.append(", ".join(ready_group))
                                            #print(print_group)
                                            ready_group = []

                                        ready_program = [
                                                [[None],[None],[None],[None],[None]], 
                                                [[None],[None],[None],[None],[None]], 
                                                [[None],[None],[None],[None],[None]], 
                                                [[None],[None],[None],[None],[None]], 
                                                [[None],[None],[None],[None],[None]],  
                                                ]
                                        useless = "NO"

                                        groupNumber3 += 1

                                    
                                    groupNumber3 = 1
                                    groupNumber6 += 1

                                    if group1 != 0:
                                        for i in range(0,Days[1]):
                                            del Hours11[0]
                                
                                if group2 != 0:
                                    for i in range(0,Days[2]):
                                        del Hours12[0]
                                
                                groupNumber7 += 1
                                
                                groupNumber6 = 1
                                #Hours12.clear()

                            groupNumber7 = 1
                            Hours13.clear()


                            #answer3=input(f"Lesson {Names[3]} has {a+1}. group? ")
                            answer3 = programList[0]
                            del programList[0]
                            a = a + 1
                        
                        else:
                            if lessonNumber > 4:
                                #answer4 = input(f"Lesson {Names[4]} has 2. group? ")
                                answer4 = programList[0]
                                del programList[0]
                                a=2
                                while answer4.upper() == "YES":
                                    groupNumber9 += 1

                                    for i in range(0,Days[4]):
                                        #day_hour = input(f"Enter Day and Hour for {Names[4]} Day {i+1} group {a}: ")
                                        Hours17.append(programList[0])
                                        Hours26.append(programList[0])

                                        del programList[0]

                                    for i in range(0, len(Hours20)):
                                        Hours21.append(Hours20[i])

                                    for group3 in range(0, groupNumber8):              
                                        
                                        for i in range(0,len(Hours16)):
                                            Hours12.append(Hours16[i])
                                        
                                        for group2 in range(0, groupNumber5):
                                        
                                            for i in range(0,len(Hours7)):
                                                Hours11.append(Hours7[i])
                                                                        
                                            for group1 in range(0, groupNumber4):
                                                num = 0

                                                for group in range(0,groupNumber2):
                                        

                                                    for i in range(0,len(Hours)):
                                                        Hours19.append(Hours[i])

                                                    for i in range(0,Days[0]):
                                                        del Hours19[0]
                                                    for i in range(0,Days[1]):
                                                        del Hours19[0]
                                                    for i in range(0,Days[2]):
                                                        del Hours19[0]
                                                    for i in range(0,Days[3]):
                                                        del Hours19[0]
                                                    for i in range(0,Days[4]):
                                                        del Hours19[0]


                                                    for i in range(0,lessonNumber):

                                                        if i == 0:
                                                            if groupNumber3 == 1: # GOOD
                                                                for j in range(0,Days[0]):
                                                                    Hours18.append(Hours[j])
                                                            
                                                            elif groupNumber3 != 1:
                                                                for j in range(0,Days[0]):
                                                                    Hours18.append(Hours3[j+num])
                                                                num = num + Days[0]
                                                                                
                                                        if i == 1: # GOOD
                                                            if groupNumber6 == 1:
                                                                for j in range(0,Days[1]):
                                                                    Hours18.append(Hours[j+Days[0]])

                                                            elif groupNumber6 != 1:
                                                                for j in range(0,Days[1]):
                                                                    Hours18.append(Hours11[j])
                                                        
                                                        if i == 2:
                                                            if groupNumber7 == 1:
                                                                for j in range(0,Days[2]):
                                                                    Hours18.append(Hours[j+Days[0]+Days[1]])
                                                            elif groupNumber7 != 1:
                                                                for j in range(0,Days[2]):
                                                                    Hours18.append(Hours12[j])
                                                        
                                                        if i == 3:
                                                            if groupNumber10 == 1:
                                                                for j in range(0,Days[3]):
                                                                    Hours18.append(Hours[j+Days[0]+Days[1]+Days[2]])
                                                            elif groupNumber10 != 1:
                                                                for j in range(0,Days[3]):
                                                                    Hours18.append(Hours21[j])
                                                        
                                                        if i == 4:
                                                            for j in range(0,Days[4]):
                                                                Hours18.append(Hours17[j])
                                                        
                                                        if i != 0 and i != 1 and i != 2 and i != 3 and i != 4: # GOOD
                                                            for j in range(0,Days[i]):
                                                                Hours18.append(Hours19[0])
                                                                del Hours19[0]
                                                                #print(Hours4)
                                                        
                                                        #print(Hours10)
                                                        for j in range(0,len(Hours18)): #GOOD
                                                            hours = Hours18[j]
                                                            Day = hours.split()[0]
                                                            Time = hours.split()[1]

                                                            programMaker(Day, Time)

                                                        Hours18.clear()

                                                    if useless == "YES":
                                                            ready_program = [
                                                                [[None],[None],[None],[None],[None]], 
                                                                [[None],[None],[None],[None],[None]], 
                                                                [[None],[None],[None],[None],[None]], 
                                                                [[None],[None],[None],[None],[None]], 
                                                                [[None],[None],[None],[None],[None]],  
                                                                ]

                                                    else: 
                                                        readyProgram(ready_program)
                                                        for i in range(0,len(Names)):
                                                            if i == 0:
                                                                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber3}")
                                                            if i == 1:
                                                                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber6}")
                                                            if i == 2:
                                                                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber7}")
                                                            if i == 3:
                                                                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber10}")
                                                            if i == 4:
                                                                ready_group.append(f"Lesson {Names[i]}: Group {groupNumber9}")
                                                            if i != 0 and i != 1 and i != 2 and i != 3 and i != 4:
                                                                ready_group.append(f"Lesson {Names[i]}: Group 1")
                                                        print_group.append(", ".join(ready_group))
                                                        #print(print_group)
                                                        ready_group = []

                                                    ready_program = [
                                                            [[None],[None],[None],[None],[None]], 
                                                            [[None],[None],[None],[None],[None]], 
                                                            [[None],[None],[None],[None],[None]], 
                                                            [[None],[None],[None],[None],[None]], 
                                                            [[None],[None],[None],[None],[None]],  
                                                            ]
                                                    useless = "NO"

                                                    groupNumber3 += 1

                                                
                                                groupNumber3 = 1
                                                groupNumber6 += 1

                                                if group1 != 0:
                                                    for i in range(0,Days[1]):
                                                        del Hours11[0]
                                            
                                            if group2 != 0:
                                                for i in range(0,Days[2]):
                                                    del Hours12[0]
                                            
                                            groupNumber7 += 1
                                            
                                            groupNumber6 = 1
                                            #Hours12.clear()

                                        if group3 != 0:
                                            for i in range(0, Days[3]):
                                                del Hours21[0]
                                        
                                        groupNumber10 += 1

                                        groupNumber7 = 1
                                    
                                    Hours17.clear()
                                    groupNumber10 = 1


                                    #answer4=input(f"Lesson {Names[4]} has {a+1}. group? ")
                                    answer4 = programList[0]
                                    del programList[0]
                                    a = a + 1

                                else:
                                    if lessonNumber > 5:
                                        #answer5 = input(f"Lesson {Names[5]} has 2. group? ")
                                        answer5 = programList[0]
                                        del programList[0]
                                        a=2
                                        while answer5.upper() == "YES":
                                            groupNumber11 += 1

                                            for i in range(0,Days[5]):
                                                #day_hour = input(f"Enter Day and Hour for {Names[5]} Day {i+1} group {a}: ")
                                                #day_hour = programList[0]
                                                Hours23.append(programList[0])
                                                #Hours23.append(day_hour)

                                                del programList[0]

                                            for i in range(0, len(Hours26)):
                                                    Hours22.append(Hours26[i])

                                            for group4 in range(0, groupNumber9):

                                                for i in range(0, len(Hours20)):
                                                    Hours21.append(Hours20[i])

                                                for group3 in range(0, groupNumber8):              
                                                    
                                                    for i in range(0,len(Hours16)):
                                                        Hours12.append(Hours16[i])
                                                    
                                                    for group2 in range(0, groupNumber5):
                                                    
                                                        for i in range(0,len(Hours7)):
                                                            Hours11.append(Hours7[i])
                                                                                    
                                                        for group1 in range(0, groupNumber4):
                                                            num = 0

                                                            for group in range(0,groupNumber2):
                                                    

                                                                for i in range(0,len(Hours)):
                                                                    Hours25.append(Hours[i])

                                                                for i in range(0,Days[0]):
                                                                    del Hours25[0]
                                                                for i in range(0,Days[1]):
                                                                    del Hours25[0]
                                                                for i in range(0,Days[2]):
                                                                    del Hours25[0]
                                                                for i in range(0,Days[3]):
                                                                    del Hours25[0]
                                                                for i in range(0,Days[4]):
                                                                    del Hours25[0]
                                                                for i in range(0,Days[5]):
                                                                    del Hours25[0]


                                                                for i in range(0,lessonNumber):

                                                                    if i == 0:
                                                                        if groupNumber3 == 1: # GOOD
                                                                            for j in range(0,Days[0]):
                                                                                Hours24.append(Hours[j])
                                                                        
                                                                        elif groupNumber3 != 1:
                                                                            for j in range(0,Days[0]):
                                                                                Hours24.append(Hours3[j+num])
                                                                            num = num + Days[0]
                                                                                            
                                                                    if i == 1: # GOOD
                                                                        if groupNumber6 == 1:
                                                                            for j in range(0,Days[1]):
                                                                                Hours24.append(Hours[j+Days[0]])

                                                                        elif groupNumber6 != 1:
                                                                            for j in range(0,Days[1]):
                                                                                Hours24.append(Hours11[j])
                                                                    
                                                                    if i == 2:
                                                                        if groupNumber7 == 1:
                                                                            for j in range(0,Days[2]):
                                                                                Hours24.append(Hours[j+Days[0]+Days[1]])
                                                                        elif groupNumber7 != 1:
                                                                            for j in range(0,Days[2]):
                                                                                Hours24.append(Hours12[j])
                                                                    
                                                                    if i == 3: 
                                                                        if groupNumber10 == 1:
                                                                            for j in range(0,Days[3]):
                                                                                Hours24.append(Hours[j+Days[0]+Days[1]+Days[2]])
                                                                        elif groupNumber10 != 1:
                                                                            for j in range(0,Days[3]):
                                                                                Hours24.append(Hours21[j])
                                                                    
                                                                    if i == 4: 
                                                                        if groupNumber12 == 1:
                                                                            for j in range(0,Days[4]):
                                                                                Hours24.append(Hours[j+Days[0]+Days[1]+Days[2]+Days[3]])
                                                                        elif groupNumber12 != 1:
                                                                            for j in range(0,Days[4]):
                                                                                Hours24.append(Hours22[j])
                                                                    
                                                                    if i == 5:
                                                                        for j in range(0,Days[5]):
                                                                            Hours24.append(Hours23[j])
                                                                    
                                                                    if i != 0 and i != 1 and i != 2 and i != 3 and i != 4 and i != 5: # GOOD
                                                                        for j in range(0,Days[i]):
                                                                            Hours24.append(Hours25[0])
                                                                            del Hours25[0]
                                                                            #print(Hours4)
                                                                    
                                                                    #print(Hours10)
                                                                    for j in range(0,len(Hours24)): #GOOD
                                                                        hours = Hours24[j]
                                                                        Day = hours.split()[0]
                                                                        Time = hours.split()[1]

                                                                        programMaker(Day, Time)

                                                                    Hours24.clear()

                                                                if useless == "YES":
                                                                        ready_program = [
                                                                            [[None],[None],[None],[None],[None]], 
                                                                            [[None],[None],[None],[None],[None]], 
                                                                            [[None],[None],[None],[None],[None]], 
                                                                            [[None],[None],[None],[None],[None]], 
                                                                            [[None],[None],[None],[None],[None]],  
                                                                            ]

                                                                else: 
                                                                    readyProgram(ready_program)
                                                                    for i in range(0,len(Names)):
                                                                        if i == 0:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber3}")
                                                                        if i == 1:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber6}")
                                                                        if i == 2:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber7}")
                                                                        if i == 3:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber10}")
                                                                        if i == 4:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber12}")
                                                                        if i == 5:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group {groupNumber11}")
                                                                        if i != 0 and i != 1 and i != 2 and i != 3 and i != 4 and i != 5:
                                                                            ready_group.append(f"Lesson {Names[i]}: Group 1")
                                                                    print_group.append(", ".join(ready_group))
                                                                    #print(print_group)
                                                                    ready_group = []

                                                                ready_program = [
                                                                        [[None],[None],[None],[None],[None]], 
                                                                        [[None],[None],[None],[None],[None]], 
                                                                        [[None],[None],[None],[None],[None]], 
                                                                        [[None],[None],[None],[None],[None]], 
                                                                        [[None],[None],[None],[None],[None]],  
                                                                        ]
                                                                useless = "NO"

                                                                groupNumber3 += 1

                                                            
                                                            groupNumber3 = 1
                                                            groupNumber6 += 1

                                                            if group1 != 0:
                                                                for i in range(0,Days[1]):
                                                                    del Hours11[0]
                                                        
                                                        if group2 != 0:
                                                            for i in range(0,Days[2]):
                                                                del Hours12[0]
                                                        
                                                        groupNumber7 += 1
                                                        
                                                        groupNumber6 = 1
                                                        #Hours12.clear()

                                                    if group3 != 0:
                                                        for i in range(0, Days[3]):
                                                            del Hours21[0]
                                                    
                                                    groupNumber10 += 1

                                                    groupNumber7 = 1

                                                if group4 != 0:
                                                    for i in range(0, Days[4]):
                                                        del Hours22[0]
                                                
                                                groupNumber10 = 1

                                                groupNumber12 += 1

                                            groupNumber12 = 1
                                            Hours23.clear()

                                            #answer5=input(f"Lesson {Names[5]} has {a+1}. group? ")
                                            answer5 = programList[0]
                                            del programList[0]
                                            a = a + 1



print("Your all possible programs: ")
for i in range(0,len(print_Program)):
    printProgram(print_Program[i])
    print(print_group[i])
    

print(f"\nYou have {len(print_Program)} possible program")