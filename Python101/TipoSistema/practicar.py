# Luis quire abrir su pizzeria
#FrontEnd se tiene Fitmap

# 1. Visualizar que quieres hacer.
# 2. Dividir en tareas pequeñas las tareas grandes.
# 3. Aplica lógica en todos los pasos.

# Declarar las variables y llamando las librerias

cliente: str = "Carlos"
basePizza: str = "Delgada"
PizzaTamanio: int = 14
ingredientes: str = "jamon"
extraQueso: bool = True
precio: float = 89.50

# Alternativa 1 - usando Funciones con print

print(f"Se recibe la orden de: {cliente}")
print(f"Pizza base: {basePizza}, tamaño: {PizzaTamanio} pugadas y de ingredientes: {ingredientes}")
print(f"se requiere con extra queso: {extraQueso}")
print(f"La cuenta es de: {precio}")

# Alternativa 2 - Strings formateados

detalleOrden: str = f"""

print(f"Se recibe la orden de: {cliente}")
print(f"Pizza base: {basePizza}, tamaño: {PizzaTamanio} pugadas y de ingredientes: {ingredientes}")
print(f"se requiere con extra queso: {extraQueso}")
print(f"La cuenta es de: {precio}")
"""

# Alternativa 3 - Usando el f string en print

print(f"""se recibe orden de: {cliente}, pizza base: {basePizza}, tamaño: {PizzaTamanio}, pulgadas, ingredientes: {ingredientes}, con extraqueso?: {extraQueso}, la cuenta es de: ${precio})"""
