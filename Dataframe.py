import pandas as pd

ddd = pd.DataFrame([("SSDD",555,"SI","45945"),
                    ("FGH",5681,"NO","45948"),
                    ("BNM",4567,"SI","45963")]
                    , columns=["DATO1","DATO2","DATO3","DATO4"])

print (ddd)

df = pd.read_csv("./BIGDATA.csv",sep=",")
print(df.head(5))


import pywhatkit
