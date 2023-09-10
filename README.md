# Python-Pandas
In this repository, I'm going to do practice on Pandas library.

# Install Pandas
    pip install pandas

# Import the pandas
    import pandas as pd

# Check version
    print("Pandas version: ",pd.__version__)       
         Pandas version:  2.1.0

# Pandas Series
    # Numpy to pandas series
    lst_num = np.random.randint(10,50,5)
    pd.Series(lst_num)  
        Numpy to Pandas:
            0     28
            1     32
            2     13
            3     47
            4     35

    # Giving index from own
    print("Giving index by self")
    print(pd.Series(index=["A","B","c","d"],data=[1,2,3,4]))
    print(pd.Series(index=[1,2,3,4],data=["A","B","c","d"]))
            Giving index by self
                A    1
                B    2
                c    3
                d    4
                dtype: int64
                1    A
                2    B
                3    c
                4    d
                dtype: object

    # accessing the data by index number and index slicing
        data_numpy = np.random.randint(10,50,20)
        data_index = pd.Series(data_numpy)
        #Accessing data by using index number data_index[index-value]
        print(data_index[5])

        # Accessing data by using index slicing data_index[start : end]"
        print(data_index[3:8])

        # Accessing data by using index slicing using last index data_index[start : - end]"
        print(data_index[3:-2])

    # Aggregate function 
        print("Aggregate function")
        print(data_index.agg([min,max,sum])) #This may generate warning, so we have used direct min, max, sum function from series directly
        print(pd.Series.min(data_index))
        print(pd.Series.max(data_index))
        print(pd.Series.sum(data_index))

    # Series absolute function
        print("Absolute function")
        print(data_index.abs())
                Absolute function
                    0    47
                    1    46
                    2    29
                    3    29
                    4    40
                    5    30

    # Series between function -> retrun the value between the range (start, end)
    sr1 = pd.Series([1,2,3,4,5])
    print("Between the series")
    print(sr1.between(2,6))
        Between the series
            0    False
            1     True
            2     True
            3     True
            4     True

    # String function in series
    str_series = pd.Series(["Mahesh ", "ritvika  ", "hridyansh", "  Jadugar"])
        print("Lower function:")
        print(str_series.str.lower())
        Lower function:
                    0      mahesh
                    1    ritvika
                    2    hridyansh
                    3      jadugar
        print("Upper function:")
        print(str_series.str.upper())
        Upper function:
                    0      MAHESH
                    1    RITVIKA
                    2    HRIDYANSH
                    3      JADUGAR
                
    # Length function
        print("length of array of each element")
        for i in str_series:
            print(i,len(i))

    # Return boolean value

    print("Startwith()",str_series1.str.startswith("I"))
        Startwith() 
            0    False
            1     True
            2    False
    print("Endwith()",str_series1.str.endswith("g"))
        Endwith() 
            0     True
            1    False
            2     True
    print("find()",str_series1.str.find("rain"))     
        find() 
            0   -1
            1   -1
            2    0

    # Convert pd to list
    print("Pandas series to List",str_series1.to_list())
        Pandas series to List ['Rain@is@happening', "I'm in Hyderabad", 'rain happening from morning']

