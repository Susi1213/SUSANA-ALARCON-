def calcular_descuento(monto_total , porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento , monto_final


# Llamada a la función proporcionando solo el monto total de la compra
monto_compra1 = 100
descuento1 , monto_final1 = calcular_descuento ( monto_compra1 )
print ( f"Monto de compra: ${monto_compra1}" )
print ( f"Descuento aplicado: ${descuento1}" )
print ( f"Monto final a pagar: ${monto_final1}" )

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra2 = 400
porcentaje_descuento2 = 15
descuento2 , monto_final2 = calcular_descuento ( monto_compra2 , porcentaje_descuento2 )
print ( "\nLlamada con monto y porcentaje personalizado:" )
print ( f"Monto de compra: ${monto_compra2}" )
print ( f"Porcentaje de descuento: {porcentaje_descuento2}%" )
print ( f"Descuento aplicado: ${descuento2}" )
print ( f"Monto final a pagar: ${monto_final2}" )
