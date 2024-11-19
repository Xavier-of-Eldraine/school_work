"""
Griffin Stover
11/18/24
CRN:
Class: CIS 216
Time Estimate:
"""

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

class CSVBase:
    #For each array below the index is equal to the year
    MONTH_AVG = [0]

    MONTH_MIN = [0]

    MONTH_MAX = [0]

    YEAR = 1995
    def __init__(self,filea,num):
        self.num = num
        self.file = filea
    
    def average(self):
        month_total = 0
        days = 0
        for i in range(len(self.file)):
            if int(self.file[i][0]) == int(self.num):
                month_total += float(self.file[i][3])
                days += 1
            if int(self.file[i][2]) != self.YEAR:
                    self.MONTH_AVG[self.YEAR-1995] = month_total / days
                    self.YEAR += 1
                    self.MONTH_AVG.append(0)
                    days = 0
                    month_total = 0
                
        print(self.MONTH_AVG)

    def minimum(self):
        for i in range:
            pass
        return



    def run(self):
        print(self.file)

class Month(CSVBase):

    pass


#Reads file
header = True
filecsv = line_reader("CSV_Project\MIGRNDRA.csv",header)

#print(filecsv)

for i in range(12):
    
#csv_runner = CSVBase(filecsv)


#csv_runner.average()


