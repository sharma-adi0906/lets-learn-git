from turtle import home


class cars():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

        

Honda = cars("city", "2001", "100k")
Tata = cars("Bolt", "2004", "70k")

print("select Honda or Tata?")
select = input()
if select == "Honda":
    print("Model, Year or Price?")
    sel = input()
    if sel == "Model":
        print(Honda.model)
    elif sel == "Year":
        print(Honda.year)
    elif sel == "Price":
        print(Honda.price)
elif select == "Tata":
    print("Model, Year or Price?")
    sel = input()
    if sel == "Model":
        print(Tata.model)
    elif sel == "Year":
        print(Tata.year)
    elif sel == "Price":
        print(Tata.price)