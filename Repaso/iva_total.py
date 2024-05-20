def iva_total(monto_sin_iva, porcentaje_iva=21):
    iva = monto_sin_iva * (porcentaje_iva / 100)
    total_con_iva = monto_sin_iva + iva
    return total_con_iva
monto = float(input("Ingresa el monto sin IVA: "))
porcstr= input("Ingresa el porcentaje de IVA (opcional, presiona Enter para usar el 21% por defecto): ")
if porcstr == "":
    porcentaje = None
else:
    porcentaje = float(porcstr)

if porcentaje:
    total = iva_total(monto, porcentaje)
else:total = iva_total(monto)
print(f"El total con IVA es: ${total:.2f}")
