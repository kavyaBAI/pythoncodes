import pandas as pd
import csv
 
df=pd.read_csv(r"C:\Users\kavya\OneDrive\Documents\form\new14.csv", usecols=['date','costinbillingcurrency'])
df1=pd.read_csv(r"C:\Users\kavya\OneDrive\Documents\form\till8 (1).csv", usecols=['date','costinbillingcurrency'])
res_dict={}
res_dict1={}
res={}
resdict={}

max_row1=len(df.index)
max_row2=len(df1.index)


for i in range(max_row1):
    row1=df.iloc[i]
    #print(row1[1])
    if row1[1] not in res_dict:
        res_dict[row1[1]] = row1[0]
    else:
        res_dict[row1[1]]+=(row1[0])
#print(res_dict) 


for i in range(max_row2):
    row2=df1.iloc[i]
    #print(row1[1])
   #counting values row by row 
    if row2[1] not in res_dict1:
        res_dict1[row2[1]] = row2[0]
    else:
        res_dict1[row2[1]]+=(row2[0])
for i in res_dict1:
    if i in res_dict:
        diff=res_dict[i]-res_dict1[i]
        res[i]=diff
for i in res_dict1:
 
 #converting dataframe file to csv file 
    resdict[i]=[i,res_dict[i],res_dict1[i],res[i]]
    # headers=['date','till14', 'till8', 'diff']
#print(resdict)
headers=['date','till14', 'till8', 'diff']
data = pd.DataFrame(resdict.values(),columns=headers)
data.to_csv("output.csv", index=False)

# df4=pd.DataFrame(resdict.items(),columns=headers)
# df.to_csv("test.csv")


      
       


#_______________________________________

# res_dict={'2023-03-07T00:00:00Z': 50499.898022491965, '2023-03-01T00:00:00Z': 50400.35626021839, '2023-03-02T00:00:00Z': 50244.941870136296, '2023-03-03T00:00:00Z': 44764.056369207385, '2023-03-06T00:00:00Z': 41132.80345473427, '2023-03-05T00:00:00Z': 15390.163638951466, '2023-03-04T00:00:00Z': 20000.928107819036, '2023-03-08T00:00:00Z': 50531.70607791524}
# res_dic1={'2023-03-08T00:00:00Z': 4141.842738922405, '2023-03-02T00:00:00Z': 50244.94186986829, '2023-03-07T00:00:00Z': 50434.035209945054, '2023-03-06T00:00:00Z': 41132.80345435097, '2023-03-04T00:00:00Z': 20000.928107446554, '2023-03-01T00:00:00Z': 50400.356260212655, '2023-03-03T00:00:00Z': 44764.056368780104, '2023-03-05T00:00:00Z': 15390.163638641156}
# res={'2023-03-08T00:00:00Z': 46389.86333899283, '2023-03-02T00:00:00Z': 2.680026227608323e-07, '2023-03-07T00:00:00Z': 65.8628125469113, '2023-03-06T00:00:00Z': 3.832974471151829e-07, '2023-03-04T00:00:00Z': 3.724817361216992e-07, '2023-03-01T00:00:00Z': 5.73345459997654e-09, '2023-03-03T00:00:00Z': 4.272806108929217e-07, '2023-03-05T00:00:00Z': 3.103104972979054e-07}
