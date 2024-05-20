portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Ingrese su salario anual: "))
portion_saved = float(input("Ingrese la porcion de salario a ahorrar: "))
total_cost  = float(input("Ingrese el costo de la casa de sus sueños: "))

while current_savings < (total_cost*portion_down_payment) :
    current_savings+= current_savings * r/12
    current_savings+=(annual_salary/12 * portion_saved)
    months+=1

print ("La cantidad de meses es:", months)