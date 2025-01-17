import numpy as np
import pandas as pd

for k in range(1,26):
    for l in range(1,4):
        if ((k==1) or (k==2 and l==2) or (k==2 and l==3) or (k==3 and l==1) or (k==4 and l==1) or (k==6 and l==3) or (k==7 and l==3)
        or (k==8 and l==2)  or (k==9 and l==1) or (k==9 and l==3) or (k==17 and l==1) or (k==17 and l==3) or (k==18) or (k==19 and l==1)
        or (k==21 and l==2)):
            continue
        else:
            facial_data=pd.read_csv(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP\ENTC_17_FYP_26\stress_data_collection\updated_dataset_1\facial_expression\PP%s_facial_expression_%s.csv"%(str(k),str(l)))
            posture_data=pd.read_csv(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP\ENTC_17_FYP_26\stress_data_collection\updated_dataset_1\body postures\PP%s_body_postures_%s.csv"%(str(k),str(l)))

            print(facial_data.shape)
            print(posture_data.shape)

            x=int(posture_data.shape[0]/5)
            df1 = pd.DataFrame()

            for i in range(0,x*5):
                if i%5==4:
                    continue
                else:
                    df1.loc[i,posture_data.columns]=posture_data.loc[i,posture_data.columns]

            drop_columns=['PP','Block']
            print(df1.shape)
            df1.drop(drop_columns,axis=1,inplace=True)
            print(df1.shape)

            df1_reset=df1.reset_index(drop=True)   #modified body posture dataframe

            facial_sample=facial_data.shape[0]
            posture_sample=df1_reset.shape[0]
            print(facial_sample)
            print(posture_sample)

            if facial_sample>=posture_sample:
                df2=facial_data[:posture_sample]
                df2_reset=df2.reset_index(drop=True)
                print(df2_reset.shape)
                print(df1_reset.shape)
                df_concat = pd.concat([df1_reset,df2_reset],axis=1)
                
            else:
                df1_reset=df1_reset[:facial_sample]
                df2_reset=facial_data.reset_index(drop=True)
                print(df2_reset.shape)
                print(df1_reset.shape)
                df_concat = pd.concat([df1_reset,df2_reset],axis=1)

            print(df_concat.shape)
            #save pd data frame to a csv file
            df_concat.to_csv(r"C:\Users\sivaluxan\Desktop\FYP-2021\FYP\ENTC_17_FYP_26\stress_data_collection\updated_dataset_1\combine\PP%s_combine_%s.csv"%(str(k),str(l)),index=False)
