# BrewCost
# Calculadora de costos de producción de cerveza artesanal

print("=" * 40)
print("            BREWCOST")
print("Calculadora de Costos de Producción")
print("=" * 40)

lote = input("Nombre del lote: ")

litros = float(input("Litros producidos: "))

malta = float(input("Costo total de la malta ($): "))
lupulo = float(input("Costo total del lúpulo ($): "))
levadura = float(input("Costo de la levadura ($): "))

costo_total = malta + lupulo + levadura
costo_litro = costo_total / litros

ingredientes = {
    "Malta": malta,
    "Lúpulo": lupulo,
    "Levadura": levadura
}

ingrediente_mas_costoso = max(ingredientes, key=ingredientes.get)
ingrediente_menos_costoso = min(ingredientes, key=ingredientes.get)

print("\n" + "=" * 40)
print("               RESUMEN")
print("=" * 40)

print(f"Lote: {lote}")
print(f"Producción: {litros:.0f} litros")
print(f"Costo total: ${costo_total:.2f}")
print(f"Costo por litro: ${costo_litro:.2f}")
print(f"Ingrediente más costoso: {ingrediente_mas_costoso}")
print(f"Ingrediente menos costoso: {ingrediente_menos_costoso}")