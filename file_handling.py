# f = open("myfile.txt", "w")   # will create new file if myfile.txt doesn't exist
# f.write("This is a single line\n")
# f.writelines("This is a multi-line\n" \
#     "=== Sample text line 1 ===\n" \
#     "=== Sample text line 2 ===\n" \
#     "=== Sample text line 3 ===\n"
#     )
# with open("myfile.txt") as f:
#     f.writelines(
#     "This is a multi-line\n" \
#     "=== Sample text line 1 ===\n" \
#     "=== Sample text line 2 ===\n" \
#     "=== Sample text line 3 ===\n"
#     )

# f = open("myfile.txt", "r")
# print(f.read())
# f.close()      # Close the file after opened it using open function

# with open("myfile.txt") as f:
    # print(f.readline())  # read a single line
    # print(f.read())      # read multiple lines
    # print(f.readlines()) # read multiple lines
    # for line in f:
    #     print(line)      # Another way of priting lines

# f = open("newfile.txt", "x") # Generate error since newfile.txt already exists
# f.write("This is a demo text")

# f = open("newfile.txt", "a") # open file in append mode
# f.write("\nThis is newly added line")

# import os
# if os.path.exists("newfile1.txt"):
#     os.rename("newfile1.txt", "newfile2.txt")   # Rename file
# else:
#     print("File not found")

# if os.path.exists("newfile2.txt"):
#     os.remove("newfile2.txt")        # Remove file
# else:
#     print("File not found")
# os.mkdir("myDir")                   # Create new directory
# os.rmdir("myDir")                     # Delete the directory


# import csv

# with open("person.csv","x",newline='') as file:
#     file.write("Name Age Address")

# with open("person.csv","w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "Location"])
#     writer.writerow(["Ashik",27,"Kochi"])

# with open("person.csv","r",newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# pip install pandas
# import pandas as pd

# Read data from csv using pandas
# import pandas as pd

# pd.read_csv("people.csv")


# Write data to csv using pandas

# import pandas as pd

# creating a data frame
# df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])

# writing data frame to a CSV file
# df.to_csv('person.csv')

# Compress data to zip file
# import zipfile

# with zipfile.ZipFile("zippedFile","w") as zipFile:
#     zipFile.write("person.csv")
#     zipFile.write("records.xlsx")

#extract data and list the contents
# import os
# with zipfile.ZipFile("zippedFile","r") as extZip:
#     extZip.extractall("extractedFile")
#     extracted_files = extZip.namelist()  # list the files inside the zip

    # for file in extracted_files:
    #     print(file)                     #print the file name inside the zip
    #     print(os.path.join("extractedFile", file))         #print file name with full path




    