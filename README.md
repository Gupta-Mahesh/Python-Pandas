# Python-Pandas
In this repository, Practice on the Pandas library.

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
            This method allows you to apply a function or a list of function names to be executed along one of the axis of the DataFrame, default 0, which is the index (row) axis.
        
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

# DataFrame
    Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

   # Crearing dataframe 
    data_frame1 = pd.DataFrame(data=[["Mahesh", "Kumar", "Gupta"],["Ritvika","Singh","Gautam"]],columns=["First","Middle","Last"])
    print(data_frame1)
                First   Middle  Last
            0   Mahesh  Kumar   Gupta
            1  Ritvika  Singh  Gautam
   # Creating data from list
    # 1D list to pd dataframe
        lst = ["Python", "Swift", "C++", "Java", "C#"]
        pd_df_list = pd.DataFrame(lst)
        print(pd_df_list)
                        0
                0  Python
                1   Swift
                2     C++
                3    Java
                4      C#

   # 2D list to pd dataframe
        lst_2d = [["Python", 10],["Java",11],["C#",12]]
        df_2d = pd.DataFrame(lst_2d)
        print(df_2d)
                        0   1
                0  Python  10
                1    Java  11
                2      C#  12

   # Creating dataframe from dict   [Keys will show as column name]
        lst_dict = {"Name":["Mahesh","Suresh","Dinesh","Makhanchu"],
                    "Age": [32,         25,     60,     55]}
        df_dict = pd.DataFrame(lst_dict)
        print(df_dict)  
                        Name  Age
                0     Mahesh   32
                1     Suresh   25
                2     Dinesh   60
                3  Makhanchu   55
   # loc function  here need to pass row index and coumn name

        print(df_dict1.loc[1:2])        [Rows index]
                        Name   Age     Qualification    Address
                    1  Suresh   25         BCA          Banglore
                    2  Dinesh   60        B.tech        Delhi
        print(df_dict1.loc[1:2, "Age":"Qualification"]) [Rows index, col names]

                        Age     Qualification
                    1   25           BCA
                    2   60        B.tech
   # iloc here need to pass row index and coumn index
        print(df_dict1.iloc[:1,:1])     #[row,col]
                    Name
                0  Mahesh
        Selecting specific row and column
        df_dict1.iloc[[0,2],[1,2]]      [[first , sec rows],[first, sec col]]
               Age    Qualification
            0   32           MCA
            2   60        B.tech
   
   # Slicing using condition
        num_df = pd.DataFrame(data=[10,22,32,24,65,55,75,85,95,102,115],columns=["num"])
        print(num_df.loc[num_df["num"]>24])
            Output: print only value > 24
                    num
                2    32
                4    65
                5    55
                6    75
                7    85
                8    95
                9   102
                10  115

   # Creating a new data frame
        list_df =[[10,22,32],[55,75,85],[54,65,77],[12,32,65]]
        num_df1 = pd.DataFrame(list_df,columns=["num1","num2","num3"])
        print("Complete data frame")
        print(num_df1)

            Output:  Complete data frame
                    num1  num2  num3
                0    10    22    32
                1    55    75    85
                2    54    65    77
                3    12    32    65

   # Checking condition if col num1 >10 print num1 and num2 col values
        print("Data frame after condition")
        print(num_df1.loc[num_df1["num1"]>10, ["num1", "num2"]])            
            Output: Data frame after condition
                    num1  num2
                1    55    75
                2    54    65
                3    12    32

   # Adding the column in data frame
        ls_add = [41,54,65,87]
        num_df1["num4"] =ls_add
        print("added col num4")
        print(num_df1)
            added col num4
                num1  num2  num3  num4
            0    10    22    32    41
            1    55    75    85    54
            2    54    65    77    65
            3    12    32    65    87

        ls_add1 = pd.Series([31,65,85,99])
        num_df1["num5"] =ls_add1
        print("adding col num5 using series")
        print(num_df1)

            Output: adding col num5 using series
                    num1  num2  num3  num4  num5
                0    10    22    32    41    31
                1    55    75    85    54    65
                2    54    65    77    65    85
                3    12    32    65    87    99

   # adding some value in col num1 
     Here the value 10 will add in complete col1 and saving in new col num6
        num_df1["num6"] = num_df1["num1"]+10
        print(num_df1)
            Output:
                    num1  num2  num3  num4  num5  num6
                0    10    22    32    41    31    20
                1    55    75    85    54    65    65
                2    54    65    77    65    85    64
                3    12    32    65    87    99    22

   # Deleing the col
        del num_df1["num3"]
        print("del col num3")
        print(num_df1)
            Output: del col num3
                num1  num2  num4  num5  num6
            0    10    22    41    31    20
            1    55    75    54    65    65
            2    54    65    65    85    64
            3    12    32    87    99    22

   # addition of rows
        df_row = pd.DataFrame([[11,22,33,44,55],[54,55,66,77,88]],columns=["num1","num2","num4","num5","num6"])
        #num_df1 = num_df1.append(df_row)
        con_df = pd.concat([num_df1,df_row],axis=0).reset_index()
        print("Appended rows")
        print(con_df)

            Appended rows
                index  num1  num2  num4  num5  num6
            0      0    10    22    41    31    20
            1      1    55    75    54    65    65
            2      2    54    65    65    85    64
            3      3    12    32    87    99    22
            4      0    11    22    33    44    55
            5      1    54    55    66    77    88

   # Droping the row & col 
        temp_df = con_df
        print("Droping row 4 and 5")
        temp_df = temp_df.drop([4,5],axis=0)
        print(temp_df)
            Output: Droping row
                index  num1  num2  num4  num5  num6
            0      0    10    22    41    31    20
            1      1    55    75    54    65    65
            2      2    54    65    65    85    64
            3      3    12    32    87    99    22
    
        print("Droping column num2 and num4")
        temp_df = temp_df.drop(["num2","num4"],axis=1)
        print(temp_df)
            Output: Droping column
                index  num1  num5  num6
            0      0    10    31    20
            1      1    55    65    65
            2      2    54    85    64
            3      3    12    99    22

