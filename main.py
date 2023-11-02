import math
import pandas as pd 


def scale(df, feature_name):
   """
   determines which scaling method to use
   """

   
def clipping(sd, df, feature_name):
  """
  Returns clipped dataset such that a provided feature is within sd standard deviations of feature
  """
  if sd <= 0.0:
    raise ValueError("Standard deviation must be a positive value.")
  if feature_name not in df.columns:
    raise ValueError("Feature name is invalid, please provide a string.")

  pre_clipping_size = float(df.shape[0])

  feature_min = df[feature_name].mean() - df[feature_name].std()  # I did not change this, but I believe that you need to multiply "df[feature_name].std()" by "sd" to get the correct feature min/max - Adit
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
   
def log_scale(df, feature_name):
   """
   Takes in a dataframe, feature to be scaled and returns logScaled dataset
   """
   if feature_name not in df.columns:
    raise ValueError("Feature name is invalid, please provide a string.")
   
   original_sd = df[feature_name].std()
   original_mean = df[feature_name].mean()
   new_df = df
   
   new_df[feature_name] = new_df[feature_name].apply(lambda x: math.log(x))

   print("-"*20)
   print("Standard Deviation:", original_sd, "-->", new_df[feature_name].std())
   print("Mean:", original_mean, "-->", new_df[feature_name].mean())
   print("-"*20)
   
   return new_df





def range_scale(df, feature_name, max, min):
   """ 
   Takes in a dataframe, feature to be scaled, max value and min value to range scale to
   Returns dataframe scaled to range
   """
   if feature_name not in df.columns:
     raise ValueError("Feature name is invalid, please provide a string.")
   
   if max < min:
     temp = min
     min = max
     max = temp
   
   new_df = df
   x_min = new_df[feature_name].min()
   x_max = new_df[feature_name].max()
   
   if x_max == max and x_min == min:
     print("Data is already scaled to range: (" + min, "-", max + ")")
     return df
   # two lines just so your eyes don't die trying to read the math
   new_df[feature_name] = new_df[feature_name].apply(lambda x: ((x - x_min) / (x_max - x_min)))
   new_df[feature_name] = new_df[feature_name].apply(lambda x: x * (max - min) + min) 
   
   print("-"*20)
   print ("Scaled from (" + x_min, "-", x_max + ") to (" + min, "-", max + ")")
   print("-"*20)
   return new_df



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
