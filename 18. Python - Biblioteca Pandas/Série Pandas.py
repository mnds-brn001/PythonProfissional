import pandas as pd

a = [1, 7, 2]

# myvar= pd.Series(a)
# myvar= pd.Series(a, index=["x", "y", "z"])
# print(myvar[0])
# print(myvar)
# print(myvar["y"])

# calorias= {"dia1":420, "dia2": 380, "dia3": 390}
# myvar=pd.Series(calorias)
# myvar=pd.Series(calorias, index=["dia1", "dia2"])
# print(myvar)

data={
    "calorias": [420, 380, 390],
    "duraçao": [50, 40, 45]
}
myvar= pd.DataFrame(data)
print(myvar)