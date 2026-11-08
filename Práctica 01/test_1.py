from string.templatelib import convert

nombre = "Fabian"
salario = 3200
edad = "34"
compañia = "emp"

print(type(nombre))
print(type(salario))
print(type(edad))
print(type(compañia))

edad_num = int(edad)
if edad_num > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
bono_final = salario**2 +  (salario*10)/100
print(bono_final)