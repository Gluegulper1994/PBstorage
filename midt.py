print("My midterm project is to create a data sheet on my phone battery and having python read the data. I also had the idea for the user to be able to change variables on the chart to suit their needs.")
import matplotlib.pyplot as plt
file=open("Midt Phone Battery.csv") #file must be comma seperated val
data = [] #set data as an empty list
name=input("What is your name?")
print("Please ensure you have edited the Midt Phone Battery.csv file to accuracy for your phone", name)

next(file)
for line in file:
    data.append(line)

while True:
    print1=input("")
    print("What would you like to know about your phone battery", end= " ")
    print(name,end="")
    print("? Please remember to only enter numbers.")

    print("1. Max Voltage \n2. Max Current \n3. Min Voltage \n4. Chart of battery usage \n5. Max Capacity of Batt \n6. Battery Type \nType end to end program")
    
    if print1=='1':
        print("Max voltage is", end=" ")
        print(data[1].split(",")[0])
        
    if print1=='2':
        print("The Max current of the battery is", end=" ")
        print(data[1].split(",")[1])
        
    if print1=='3':
        print("The minimum voltage of your battery should be", end=" ")
        print(data[1].split(",")[2])
    
    if print1=='4':
        print("Here is a chart of all the data on your phone battery over one day of usage.")
        file2=open("Midt Phone Battery.csv")
        next(file2) #skip first line
        
        for i in file2: # for loop to print out entire chart as well as the file being opened with the variable "i"
            data1=i.split(",")[3]
            data2=i.split(",")[4]
            print(data1,end=' ') # end function sets it so the line is no longer skipped when read
            print(data2)
        file2.close
        
        cont=input("Would you like to make a graph for all of this data? Y/N?")
        
        if cont =="Y":
            file2=open("Midt Phone Battery.csv")
            next(file2)
            for i in file2:

                data1=i.split(",")[3]
                data2=int(i.split(",")[4][0:2])

                print(data1)
                print(data2)
                plt.rc('font',size=5)
                plt.xlabel("Time")
                plt.ylabel("Percentage")
                plt.title("Percentage over time")
                plt.scatter(data1,data2)
            plt.show()
        elif cont=="N":
            print("That's okay! Any input to return to main console.")

        else:
            print("User input invalid, any input to return to main console.")

    if print1=='5':
        print("Your Max battery capacity is", end=" ")
        print(data[1].split(",")[5])
    
    if print1=='6':
        print("Your battery type is",end=" ")
        print(data[1].split(",")[6])
    

    if print1=='end':
        print('Program ended.')
        break
