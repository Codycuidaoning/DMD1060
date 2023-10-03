investment = 10000
x = int(input("Enter number of years: "))
for i in range(x):
    yearly_interest = investment * 0.05
    investment = investment + yearly_interest
print(i)
print(investment)

