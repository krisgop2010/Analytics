#Read the file
file = open("C:\\DataSets\\SampleCrimeData.csv", "r+")
#print(file)

#Get the header
header = file.readline()[0:-1]
headerColumns = header.split(",")
#rint(headerColumns)
#Process other elements
data = file.readlines()
file.close()

#Parse the data
#remove newline and store in data1
data1 = []
for element in data:
    if(element[-1] == '\n'):
       data1.append(element[0:-1])
    else:
        data1.append(element)
#create list for district
list_district = []
for element in data1:
    list_district.append(element.split(',')[9])

#print("district list  is: ",list_district)

#create unique list of districts
list_uniq_districts = []
for element in list_district:
    if (element in list_uniq_districts):
        pass
    else:
        list_uniq_districts.append(element)
#print("Unique District List is: ",list_uniq_districts)

#count No of crimes against each district
#for element in list_uniq_districts:
 #   count_Crimes = list_district.count(element)
 #   print("District Code         No of Crimes")
 #   print("%s                      %d" %(element,count_Crimes))

combined_list = []

#count No of crimes against each district with sorting
for element in list_uniq_districts:
    count_Crimes = list_district.count(element)
    tup1 = (element,count_Crimes)
    #print(tup1)
    combined_list.append(tup1)
    
#print("List of unique distrcit is: ", list_uniq_districts)
#print("List of count is:", count_List)
print("combined List is - without sorting:", combined_list)
combined_list.sort(key = lambda x:x[1],reverse = True)
print("combined List is - with sorting:", combined_list)
for item in combined_list:
    print("District Code         No of Crimes")
    print("%s                    %d" %(item[0],item[1]))
