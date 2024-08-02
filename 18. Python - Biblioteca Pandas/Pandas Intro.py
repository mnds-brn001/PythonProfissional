import pandas as pd

print(pd.__version__)

mydataset= {
    "carros":["BMW","Volvo", "Ford"],
    "passageiros":[3, 7, 2]
}

myvar=pd.DataFrame(mydataset)
print(myvar)