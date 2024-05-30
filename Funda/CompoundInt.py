import csv

def compoundInt(principal, rate, years):
    return principal * (1+rate) ** years

data=[]
with open("data.csv",newline="") as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        row["Compound Interest"] = compoundInt(float(row["Principal"]),float(row["Rate"]),float(row["Years"]))
        data.append(row)

print(data)
header = ["Principal","Rate","Years","Compound Interest"]
with open("dataout.csv",mode="w",newline="") as csvout:
    writer = csv.DictWriter(csvout,fieldnames=header)
    writer.writeheader()
    for row in data:
        writer.writerow(row)



