class cancion:
  def __init__(self, titulo, precio):
    self.titulo = titulo
    self.precio = precio

  def __str__(self):
    return f"{self.titulo} - ${self.precio:,.0f}"

class lista_reproduccion:
   def __init__(self, nombre_cliente):
    self.canciones = []
    self.nombre_cliente = nombre_cliente

   def agregar_cancion(self, cancion):
    self.canciones.append(cancion)
  
   def mostrar_lista(self):
    print(f"Lista de reproducción de {self.nombre_cliente}:")
    for cancion in self.canciones:
      print(cancion)

   def total_compra(self):
    total = sum(cancion.precio for cancion in self.canciones)
    print(f"total de la compra: ${total:,.0f}")


c1 = cancion("rock and roll", 8000)
c2 = cancion("balada romantica", 7000)
c3 = cancion("salsa", 12000)

lista_David = lista_reproduccion("David")

lista_David.agregar_cancion(c1)
lista_David.agregar_cancion(c2)
lista_David.agregar_cancion(c3)

lista_David.mostrar_lista()

lista_David.total_compra()