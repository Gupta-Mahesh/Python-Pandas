
import pandas as pd
import numpy as np

#check the version of pandas
print("Pandas version: ",pd.__version__)

#Creating the series
#list to pandas
lst = [1,2,3,6,4,5,8,9]
print("List to pandas series:")
print(pd.Series(lst))

#numpy to pandas series
lst_num = np.random.randint(10,50,20)
print("Numpy to Pandas:")
print(pd.Series(lst_num))

#giving index from own
print("Giving index by self")
print(pd.Series(index=["A","B","c","d"],data=[1,2,3,4]))
print(pd.Series(index=[1,2,3,4],data=["A","B","c","d"]))


#series through dictonary
steps_walk={"day1":1000,"day2":1500,"day3":2000,"day4":2500}
print("Dict to pandas series")
print(pd.Series(steps_walk))


#repeat series
print("Repeate")
print(pd.Series(17).repeat(3)) #same index shows for all repeated element
print(pd.Series(17).repeat(5).reset_index(drop=True)) 


#accessing the date by index number
data_numpy = np.random.randint(10,50,6)
data_index = pd.Series(data_numpy)
print("Accessing data by using index number data_index[index-value]")
print(data_index[5])

print("Accessing data by using index slicing data_index[start : end]")
print(data_index[3:8])

print("Accessing data by using index slicing data_index[start : - end]")
print(data_index[3:-2])


#Aggregate function 
print("Aggregate function")
print(data_index.agg([min,max,sum]))
print(pd.Series.min(data_index))
print(pd.Series.max(data_index))
print(pd.Series.sum(data_index))


#Series absolute function
print("Absolute function")
print(data_index.abs())


# Series between function
sr1 = pd.Series([1,2,3,4,5])
print("Between the series")
print(sr1.between(2,5))

# String function in series
str_series = pd.Series(["Mahesh ", "ritvika  ", "hridyansh", "  Jadugar"])

##Upper and Lower Function

print("Upper and lower case")
print("Lower function:")
print(str_series.str.lower())
print("Upper function:")
print(str_series.str.upper())

print("length of array of each element")
for i in str_series:
    print(i,len(i))

##Strip function which will remove unwanted spaces
str_series = str_series.str.strip()
print("Length after strip function")
for i in str_series:
    print(i,len(i))


##Split function
str_series1 = pd.Series(["Rain@is@happening","I'm in Hyderabad","rain happening from morning"])
print("Split function")
print(str_series1.str.split("@"))

print("Replace function")
print(str_series1.str.replace("@"," "))

#return boolean value

print("Startwith()",str_series1.str.startswith("I"))
print("Endwith()",str_series1.str.endswith("g"))
print("find()",str_series1.str.find("rain"))


#convert pd to list

print("Pandas series to List",str_series1.to_list())
