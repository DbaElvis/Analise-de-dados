exp = [2200,2350,2600,2130,2190]



print("In feb this much extra was spent compared to jan:",exp[1]-exp[0]) # 150



print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150



print("Did I spent 2000$ in any month? ", 2000 in exp) # False



exp.append(1980)
print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]



exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]



exp.lshift()
print("Apos remocao: ",exp)