import pandas as pd 



def linscale(file):
   return



fileinput = str(input("Which file do you want? ")) # Just type "snakes_count_10000.csv" for the prompt
if not ".csv" in fileinput:
  fileinput += ".csv"     
data = pd.read_csv(fileinput)    # actually reads the file

columninput = ""  

print("Columns: ", end= "")
for a in data.columns:
   print(str(a), end= " ")

i = 0
print() # just for formatting
while  True:
    columninput = str(input("Which column would you like to normalize? "))
    if columninput in data.columns:
       break
    else:
       print("Please enter a valid column!")
       continue


   

    
    





#snakes_count_10000.csv
#Game Length