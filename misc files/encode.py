import csv

disease=[]
attributes=[]
with open('D:/data/41diseases.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row['Disease'] not in disease):
             disease.append(row['Disease'])
    for row in reader:
        attributes.append(row)
            
print(disease )
print("\n \n \n")
i=0
thisdict1= {}
for word in disease:
    thisdict1[word]=i
    i=i+1
print(thisdict1)

attributes=[]
with open('D:/data/41diseases.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row['Symptom_1'] not in attributes):
            attributes.append(row['Symptom_1'])
        if(row['Symptom_2'] not in attributes):
            attributes.append(row['Symptom_2'])
        if(row['Symptom_3'] not in attributes):
            attributes.append(row['Symptom_3'])
        if(row['Symptom_4'] not in attributes):
            attributes.append(row['Symptom_4'])
        if(row['Symptom_5'] not in attributes):
            attributes.append(row['Symptom_5'])
        if(row['Symptom_6'] not in attributes):
            attributes.append(row['Symptom_6'])
        if(row['Symptom_7'] not in attributes):
            attributes.append(row['Symptom_7'])
        if(row['Symptom_8'] not in attributes):
            attributes.append(row['Symptom_8'])
        if(row['Symptom_9'] not in attributes):
            attributes.append(row['Symptom_9'])
        if(row['Symptom_10'] not in attributes):
            attributes.append(row['Symptom_10'])
        if(row['Symptom_11'] not in attributes):
            attributes.append(row['Symptom_11'])
        if(row['Symptom_12'] not in attributes):
            attributes.append(row['Symptom_12'])
        if(row['Symptom_13'] not in attributes):
            attributes.append(row['Symptom_13'])
        if(row['Symptom_14'] not in attributes):
            attributes.append(row['Symptom_14'])
        if(row['Symptom_15'] not in attributes):
            attributes.append(row['Symptom_15'])
        if(row['Symptom_16'] not in attributes):
            attributes.append(row['Symptom_16'])
        if(row['Symptom_17'] not in attributes):
            attributes.append(row['Symptom_17'])        
        
            
print("\n \n \n")
print(attributes)

i=0
thisdict2= {}
for word in attributes:
    thisdict2[word]=i
    i=i+1


print("\n \n \n")
print(thisdict2)

fields=['Disease,Symptom_1,Symptom_2,Symptom_3,Symptom_4,Symptom_5,Symptom_6,Symptom_7,Symptom_8,Symptom_9,Symptom_10,Symptom_11,Symptom_12,Symptom_13,Symptom_14,Symptom_15,Symptom_16,Symptom_17']


final_list=[[0]*134]*5000

with open('D:/data/41diseases.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
print("\n \n \n")

for x in range(1,4921):
    for y in range(18):
        var=data[x][y]
        if(var in disease):
            data[x][y]=thisdict1[var]
        if(var in attributes):
            data[x][y]=thisdict2[var]


print(data)

with open('your_file.txt', 'w') as f:
    for item in data:
        f.write("%s\n" % item)