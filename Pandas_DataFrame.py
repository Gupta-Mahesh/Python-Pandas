import pandas as pd

#creating data frame

data_frame1 = pd.DataFrame(data=[["Mahesh", "Kumar", "Gupta"],["Ritvika","Singh","Gautam"]],columns=["First","Middle","Last"])
print(data_frame1)

# 1D list to pd dataframe
lst = ["Python", "Swift", "C++", "Java", "C#"]
pd_df_list = pd.DataFrame(lst)
print("Pandas data frame from list 1D")
print(pd_df_list)

# 2D list to pd dataframe
lst_2d = [["Python", 10],["Java",11],["C#",12]]
df_2d = pd.DataFrame(lst_2d)
print("2D Dataframe")
print(df_2d)

# Creating dataframe from dict
lst_dict = {"Name":["Mahesh","Suresh","Dinesh","Makhanchu"],
            "Age": [32,         25,     60,     55]}
df_dict = pd.DataFrame(lst_dict)
print("Dict to dataframe")
print(df_dict)

lst_dict1 = {   
            "Name":["Mahesh","Suresh","Dinesh","Makhanchu"],
            "Age": [32,         25,     60,     55],
            "Qualification": ["MCA","BCA","B.tech","Nothing"],
            "Address":["Hyd","Banglore","Delhi","Mumbai"]
            }
df_dict1 = pd.DataFrame(lst_dict1)
print("Keys and Values are working as column name and it's value")
print(df_dict1)
print("Selecting only Name and Age")
print(df_dict1[["Name","Age"]])

#loc function  here need to pass row index and coumn name
print("Loc from 1:2")
print("Row 1 to 2 rows will print")
print(df_dict1.loc[1:2])
print("Row 1 to 2 rows will print and coulum only Age and Qualification")
print(df_dict1.loc[1:2, "Age":"Qualification"])


#iloc function here need to pass row index and coumn index

print(df_dict1.iloc[:1,:1])     #[row,col]
print(df_dict1.iloc[:,:-2])

#Seleting specific row and column
print(df_dict1.iloc[[0,2],[1,2]])


#Slicing using condition
num_df = pd.DataFrame(data=[10,22,32,24,65,55,75,85,95,102,115],columns=["num"])
print(num_df.loc[num_df["num"]>24])

list_df =[[10,22,32],[55,75,85],[54,65,77],[12,32,65]]
num_df1 = pd.DataFrame(list_df,columns=["num1","num2","num3"])
print("Complete data frame")
print(num_df1)
print("Data frame after condition")
print(num_df1.loc[num_df1["num1"]>10, ["num1", "num2"]])            #checking condition if col num1 >10 print num1 and num2 col values


#Adding the column in data frame
ls_add = [41,54,65,87]
num_df1["num4"] =ls_add
print("added col num4")
print(num_df1)

ls_add1 = pd.Series([31,65,85,99])
num_df1["num5"] =ls_add1
print("adding col num5 using series")
print(num_df1)

#adding some value in col num1          the value 10 will add in complete col
num_df1["num6"] = num_df1["num1"]+10
print(num_df1)

#Deleing the col
del num_df1["num3"]
print("del col num3")
print(num_df1)

#addition of rows
df_row = pd.DataFrame([[11,22,33,44,55],[54,55,66,77,88]],columns=["num1","num2","num4","num5","num6"])
#num_df1 = num_df1.append(df_row)
con_df = pd.concat([num_df1,df_row],axis=0).reset_index()
print("Appended rows")
print(con_df)

temp_df = con_df
print("Droping row 4 and 5")
temp_df = temp_df.drop([4,5],axis=0)
print(temp_df)

print("Droping column num2 and num4")
temp_df = temp_df.drop(["num2","num4"],axis=1)
print(temp_df)