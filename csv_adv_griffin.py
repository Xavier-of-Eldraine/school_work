#To easily check up on dictionary status.
import pprint

def chooser():
    print("1) Yearly Breakdown \n 2) Monthly Breakdown \n 3) Quit")
    choice = input("Choice(1,2,3): ")
    choice = int(choice)
    return choice

    
def line_reader(path,header):
    collection = []
    csv_file = open(path)
    for line in csv_file.readlines():
        #Header Skipper
        if header == True:
            header = False
            continue

        #puts values into an array
        #[0] == month
        #[1] == day
        #[2] == year
        #[3] == temp
        line = line.split(",")
        line_holder= []
        for sub in line:
            line_holder.append(sub.replace("\n",""))
        collection.append(line_holder)

    
    return collection

def dict_maker(csv):
    print("Working...")
    #For each month:
    #[n]= Year
        #[0]= min
        #[1]=avg
         #[2]=max
    months = {
    1:[[0,0,0]],
    2:[[0,0,0]],
    3:[[0,0,0]],
    4:[[0,0,0]] ,
    5:[[0,0,0]],
    6:[[0,0,0]],
    7:[[0,0,0]],
    8:[[0,0,0]],
    9:[[0,0,0]],
    10:[[0,0,0]],
    11:[[0,0,0]],
    12:[[0,0,0]]}
    
    
    current_month = 1
    month_total = 0
    month_min = 99
    month_max = -99
    days = 0
    current_year = 1995
    #print(len(csv))
    for i in range(len(csv)):
        
        if (int(csv[i][2])) == current_year:

            if (int(csv[i][0])) == current_month:
                #Adds up monthly total, prepares for averaging.
                (months[current_month][current_year-1995][1])+=(float(csv[i][3]))
                month_total =  (months[current_month][current_year-1995][1])
                if current_month == 1:
                    print(month_total)
                days += 1
               # print("days,",days)
                

                #checks if less than current month min, changes if less.
                if float(csv[i][3]) < month_min:
                    (months[current_month][current_year-1995][0]) =float((csv[i][3]))
                    month_min = float(csv[i][3])

                #checks if more than current month max, changes if more.
                if float(csv[i][3]) > month_max:
                    (months[current_month][current_year-1995][2]) = float(csv[i][3])
                    month_max = float(csv[i][3])
               
            if (int(csv[i][0])) != current_month:
                if current_month == 1:
                    (months[current_month].append([0,0,0]))
               # print((months[current_month][current_year-1995][1]))
                (months[current_month][current_year-1995][1]) = ((months[current_month][current_year-1995][1]) / (days))
               # print("months average",months[current_month][current_year-1995][1])
                days = 1
                #print(days)
                current_month += 1
               # print(current_month)
                month_min = 99
                month_max = -99
                #print(months[current_month][current_year-1995][1])
                (months[current_month].append([0,0,0]))
                
        if (int(csv[i][2])) != current_year:
            #for december
            print(days)
            (months[current_month][current_year-1995][1]) = ((months[current_month][current_year-1995][1]) / days)
            current_year += 1
           #print(current_year)
            current_month = 1
            month_total = 0
           # print(csv[i][2])
        if i == (len(csv)-1):
            (months[current_month][current_year-1995][1]) = ((months[current_month][current_year-1995][1]) / days)
   # pprint.pprint(months)
    
    #tablemaker time!
    return months


def table_maker(dictionary):
    choice = input("Would you like a year or month report?(y/m):")
    if choice == 'y':
        print("Year | Min | Avg | Max")
        year = 1995
        year_min = 99
        year_max = -99
        year_average = 0
        for years in range(26):
            for months in range(12):
                temp_value = dictionary[months+1][years][1]
                year_average += temp_value
                #Checks to see if a dictionary entry is empty
                 
                null_month = (dictionary[months+1][years][1] +dictionary[months+1][years][0] +dictionary[months+1][years][2]) == 0
                if null_month == False:
                    if temp_value < year_min:
                        year_min = temp_value
            
            print("{}{:>2s}{:>1.1f}{:>3s}{:>1.1f}{:>s}".format(year,'|',year_min,"|",year_average / 12,'|'))
            year_average = 0
            year_min = 99
            year += 1


    



        
if __name__ ==  '__main__':
    header = True
    great_holder = line_reader('csv_project\MIGRNDRA.csv', header)
    #print(great_holder[0][3])
    months = dict_maker(great_holder)
   # pprint.pprint(months)
    table_maker(months)