#W2D1- TExt file handling - introduction

#step  : impoort the csv (comma separated value) library
import csv

total_records = 0 #the total number of records (rows) in the file

#step 2 :
#connecting to the file's path - switch \  to /
#-----connected to file------- 
print(f"{name:10} \t {number:3} \t {color}")
 #HEADER PRINT
print("---------------------")
with open("text_files/simple.csv") as csvfile:
    #indent 1 level! ( new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)
     #loop through every record (row) in the file
    for record in file:
            #add +1 to total_records
            total_records += 1

            #print (record) 
            print(record) #the list view of each record (row)

            name = record[0]
            number = record[1]
            color = record [2]

            print(f"{name:10} \t {number:3} \t {color}")
#-----disconnected from file-----------------------------
print(f"\nTOTAL RECORDS: {total_records}\n")