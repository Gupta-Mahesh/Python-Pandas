
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