let say we have list of directories in that many files will be there we have to count how many files are to do that we can manually but it is lot of work using python we can do this.
example:we have path="c://users/kavya/documents"
  in this "in this documents i have lot of other directories in those dirctories u have many images url u have to download  u have to count them"
  
  import os
  import pandas as pd
  res={}
  path=r"c://users/kavya/documents"
  dir_names=os.listdir(path)
  for names in dir_names:
    in_path=path +str(names)    //c://users/kavya/documents/armc //also we can write in_path=os.path.join(path,names)
    len_path=len(in_path)
    res[names]=[len_path]
  df=pd.DataFrame(res)
  df.to_csv("output.csv",index=False)
    
    
    
  
