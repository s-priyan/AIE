#extract body postures data from raw data and create csv files
import pandas as pd

for i in range(1,26):
    '''if i==18 or i==19:
        continue'''    #Block 1
    '''if i==2 or i==18:
        continue'''  #Block 2

    if i==1:
        continue  #Block 3

    file=open(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP-working\datasets\swell dataset\raw data\body postures\Kinect Studio Capture PP%s_3.txt"%str(i),"r")
    
    # read the content of the file opened
    content = file.readlines()
    #total number of lines
    number_of_lines = len(content)
    print("number of lines : ",number_of_lines)

    print("this is %s participant data"%str(i))

    header=content[0]
    #convert tab separated strig elements to list
    header_list=header.split("\t")
    header_list=header_list[:-1]

    total_data_string_list=[]
    total_data_list=[]
    for j in range(1,number_of_lines):
        data=content[j]
        #convert tab separated strig elements to list
        data_list=data.split("\t")
        data_list=data_list[:-1]
        total_data_string_list.append(data)
        total_data_list.append(data_list)
    print("len of total data string list:",len(total_data_string_list))
    print("len of total data list:",len(total_data_list))

    df = pd.DataFrame (total_data_list, columns = header_list)

    df['PP']='PP'+str(i)
    #df['Block']=1   # for block is 1
    #df['Block']=2  # for block is 2
    df['Block']=3  # for block is 3

    #save pd data frame to a csv file
    df.to_csv(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP\ENTC_17_FYP_26\stress_data_collection\body_postures\PP%s_body_postures_3.csv"%str(i),index=False)
