# Python-Pandas
In this repository, I'm going to do practice on Pandas library.

Install Pandas
    pip install pandas

Import the pandas
    import pandas as pd

Check version
    print("Pandas version: ",pd.__version__)       
         Pandas version:  2.1.0

#Numpy to pandas series
lst_num = np.random.randint(10,50,20)

#giving index from own
print("Giving index by self")
print(pd.Series(index=["A","B","c","d"],data=[1,2,3,4]))
print(pd.Series(index=[1,2,3,4],data=["A","B","c","d"]))