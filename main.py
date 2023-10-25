import pandas as pd 


def scale(file, col):
   """determines which scaling alg to use"""
   
def clipping(sd, df, feature_name):
  """
  Returns clipped dataset such that a provided feature is within sd standard deviations of feature
  """
  if sd <= 0.0:
    raise ValueError("Standard deviation must be a positive value.")
  if feature_name not in df.columns:
    raise ValueError("Feature name is invalid, please provide a string.")

  pre_clipping_size = float(df.shape[0])

  feature_min = df[feature_name].mean() - df[feature_name].std()
  feature_max = df[feature_name].mean() + df[feature_name].std()

  if feature_max >= df[feature_name].max() and feature_min <= df[feature_name].min():
    print("No data will be clipped, all data is within", sd, "standard deviations of mean.")
    return df;

  if feature_min > df[feature_name].max() or feature_max < df[feature_name].min():
    raise ValueError("All data will be deleted if clipped to provided specifications.")
  new_df = df.loc[df[feature_name] >= feature_min and df[feature_name] <= feature_max]
  after_clipping_size = float(new_df.shape[0])
  percent_clipped = 100.0 * (pre_clipping_size - after_clipping_size)/pre_clipping_size
  print(str(percent_clipped) + "% of data clipped.")
  return new_df
def clipping_max(max, df, feature_name):
  """
  Returns clipped dataset such that a provided feature is below or equal to a provided value
  """
  if max >= df[feature_name].max():
    print("No data will be clipped, all data is below max value")
    return df;
  if max < df[feature_name].min():
    raise ValueError("All data will be clipped if clipped to provided specifications.")
  if feature_name not in df.columns:
    raise ValueError("Feature name is invalid, please provide a string.")
  pre_clipping_size = float(df.shape[0])

  new_df = df.loc[df[feature_name] <= max]
  after_clipping_size = float(new_df.shape[0])
  percent_clipped = 100.0 * (pre_clipping_size - after_clipping_size)/pre_clipping_size
  print(str(percent_clipped) + "% of data clipped.")
  return new_df

def clipping_min(min, df, feature_name):
  """
  Returns clipped dataset such that a provided feature is above or equal to a provided value
  """
  if min <= df[feature_name].min():
    print("No data will be clipped, all data is below max value")
    return df;
  if min > df[feature_name].max():
    raise ValueError("All data will be clipped if clipped to provided specifications.")
  if feature_name not in df.columns:
    raise ValueError("Feature name is invalid, please provide a string.")
  pre_clipping_size = float(df.shape[0])

  new_df = df.loc[df[feature_name] >= min]
  after_clipping_size = float(new_df.shape[0])
  percent_clipped = 100.0 * (pre_clipping_size - after_clipping_size)/pre_clipping_size
  print(str(percent_clipped) + "% of data clipped.")
  return new_df
   
def logScale(file, col):
   """
   Takes in a csv file, col to be scaled
   Edits the dataframe directly and returns nothing
   """


def linscale(file, col, max, min):
   """ 
    Takes in a csv file, col to be scaled, max value and min value in the file and col
    Edits the dataframe directly and returns nothing
   """



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
