#extract facial expression data from raw data and create csv files
import pandas as pd

for i in range(1,26):
    if i==3:
        continue  #---this code block for experimental block 1(3) and 2(21)
    file=open(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP-working\datasets\swell dataset\raw data\facial expressions\1\Participant %s_Analysis 1.txt"%str(i),"r")
    
    # read the content of the file opened
    content = file.readlines()
    #total number of lines
    number_of_lines = len(content)
    print("number of lines : ",number_of_lines)
    
    # read 9th line from the file
    print("nineth line")
    print(content[8])

    # read 10th line from the file
    print("tenth line")
    print(content[9])

    # read 10th line from the file
    print("last line")
    print(content[number_of_lines-1])
    print("this is %s participant data"%str(i))

    header=content[8]
    header = header.replace('\n','')
    #convert tab separated strig elements to list
    header_list=header.split("\t")
    
    total_data_string_list=[]
    total_data_list=[]
    for j in range(9,number_of_lines):
        data=content[j]
        data = data.replace('\n','')
        #convert tab separated strig elements to list
        data_list=data.split("\t")
        total_data_string_list.append(data)
        total_data_list.append(data_list)
    
    #create pandas data frame from list
    
    df = pd.DataFrame (total_data_list, columns = header_list)
    
    df['PP']='PP'+str(i)
    df['Block']=1   # for block is 1
    #df['Block']=2  # for block is 2
    #df['Block']=3  # for block is 3

    #save pd data frame to a csv file
    df.to_csv(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP\ENTC_17_FYP_26\stress_data_collection\facial_expression\PP%s_facial_expression_1.csv"%str(i),index=False)
    
    