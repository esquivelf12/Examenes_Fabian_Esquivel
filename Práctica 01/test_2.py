#Caso reporte

#Matemáticas: 17, Ciencia: 14, Historia: 15
#Cada curso tiene un peso diferente en la nota final:
#Matemáticas: 40%, Ciencia: 30%, Historia: 30%

mate = 17
cien = 14
hist = 15
pond_mat = 0.4
pond_cien = 0.30
pond_hist = 0.30


nota_pond = ((mate * pond_mat) + (cien * pond_cien) + (hist * pond_hist))
resultado = round(nota_pond,1)
print("La nota final es:", resultado)
if resultado >= 13:
    print("¿Aprobado?: Sí")
    print("El estudiante obtuvo una nota final de 15.5 y su estado final es: Aprobado")
