import random
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    self.up = None
    self.down = None

    

class DLL:
  
  def __init__ (self):
    self.head = Node("-")
    
    

  def crearMatriz (self,n):
    current = self.head
    i = 1
    while i <=n:
      curd = current
      j = 1
      while j <=n:
        # valor = random.randint(0,1)
        # if valor == 0:
        #   nodo = Node(j)
        #   current.down = nodo
        # else:
        num = random.randint(0,1)
        if num == 0:
          jos = curd.down = Node("+")
          jos.up = curd
          curd = jos
          j+=1
        else:
          jos = curd.down = Node("-")
          jos.up = curd
          curd = jos
          j+=1

    #   valorf = random.randint(0,1)
    #   if valorf == 0:
    #       nodo = Node(i)
    #   else:
      num = random.randint(0,1)
      if num == 0:
        aj = current.next = Node("-")
        aj.prev = current

        current = aj
        i+=1
      else:
        aj = current.next = Node("+")
        aj.prev = current

        current = aj
        i+=1
        
  
  
  
  def Unir_next(self):
    unir = self.head

    while unir.next != None:
      #print("unir")
      unir2 = unir.down
      unir_frente = unir.next.down
      while unir2 != None:
        if unir_frente != None:
          unir2.next = unir_frente
          unir2 = unir2.down
          unir_frente = unir_frente.down
        
        else:
          break

      unir = unir.next


  def unir_prev(self):

     unir = self.head

     while unir.next != None:

       unir2 = unir.down
       unir_izq = unir.next.down

       while unir2 != None:
         if unir_izq != None:

           unir_izq.prev = unir2
           unir_izq = unir_izq.down
           unir2 = unir2.down
        
         else:
           break

       unir = unir.next

  
  def posicionar(self,lista,player):
    i = 0
    j = 0
    current = self.head

    

    while current.down != None:
      current2 = current
    

      while current !=None:
        if i == lista[0] and j ==lista[1]:
          if current.value == "D":
            current.value += "-"+player
          else: 
            current.value = player
        
        i += 1
        current = current.next
      
      current2 = current2.down

      current = current2

      j +=1
      i = 0

      print("\n")


  def mover_alien(self):
    current = self.head

    x = 0
    y = 0

    while current.next != None:
      current2 = current

      while current2.down != None:

        if current2.value == "A":


    
  
  def Traverse(self):

    
    current = self.head

    

    while current.down != None:
      current2 = current
    

      while current !=None:
        print(current.value, ", ", end = "")

        current = current.next
      
      current2 = current2.down

      current = current2

      print("\n")
      
      







      
  

      
    
  
      

      # unir = self.head.next
      
      # unir_izq = unir.prev.down
      # while unir2 != None:
      #   unir_izq = unir.prev.down
      #   if unir_izq != None:
      #     unir2.prev = unir_izq
      #     unir2 = unir2.down
      #     unir_izq = unir_izq.down
      #   else:
      #     break

      
  # def mostrar (self):
  #   current = self.head
  #   while current.next != None:
  #     curd = current.down
  #     while curd != None:
  #       print(curd.value, ", ", end = "")
  #       curd = curd.down
  #     current = current.next

LL= DLL()
n = int(input("ingrese el tamaño de la matriz"))
LL.crearMatriz(n)
#LL.head.down.value
#LL.mostrar()
# print(LL.head.value)
#print(LL.head.next.down.value)

LL.Unir_next()
LL.unir_prev()
LL.Traverse()
def posocion_Depredador():
  x = random.randint(0,2)
  y = random.randint(0,2)

  posicion = [x,y]
  print(f"Posicion en x = {x} , y = {y}")

  return posicion
def posicion_Alien():
  x = int(input("Ingrese una posicon en X entre 0 y 2: "))
  y = int(input("Ingrese una posicon en y entre 0 y 2; "))

  posicion = [x,y]
  print(f"Posicion en x = {x} , y = {y}")

  return posicion

def mover_jugador(posicion_alien,n, ll):
  opcion = 0
  posicion_nueva = posicion_alien
  print(posicion_alien)
  
  while opcion != 5:
    print("ingrese 1 para mover a la derecha")
    print("ingrese 2 para mover a la izquierda")
    print("ingrese 3 para mover hacia arriba")
    print("ingrese 4 para mover hacia abajo")
    print("ingrese 5 para salir")
    opcion = int(input("ingrese hacia donde se quiere mover"))
    if opcion == 1:
      if posicion_alien[0]+1 == n:
        print("no puedes mover hacia la derecha")
      else:
        posicion_alien[0] = posicion_alien[0]+1
        ll.posicionar(posicion_nueva," ")
        ll.posicionar(posicion_alien,"A")
        ll.Traverse()
        print(posicion_nueva)
        print(posicion_alien)
        print(posicion_nueva[0]+1)
        return posicion_nueva
      
      if opcion == 2:
        if posicion_alien[1]-1 == -1:
          print("no puedes mover hacia la izquierda")
        else:
          posicion_nueva[1] = posicion_alien[1]+1
          return posicion_nueva
        
      if opcion == 4:
        if posicion_alien[0]+1 == n:
          print("no puedes mover hacia abajo")
        else:
          posicion_nueva[0] = posicion_alien[0]+1
          return posicion_nueva  
        
      if opcion == 3:
        if posicion_alien[0]-1 == -1:
          print("no puedes mover hacia arriba")
        else:
          posicion_nueva[0] = posicion_alien[0]+1
          return posicion_nueva  
                     
    print(1)

    
 
posicion =posocion_Depredador()
depredador="D"
LL.posicionar(posicion,depredador)

posicion_alien = posicion_Alien()
Alien = "A"
LL.posicionar(posicion_alien,Alien)
LL.Traverse()
#LL.mostrar()




print(LL.head.value)
print(LL.head.down.value)
print(LL.head.down.down.value)
print()
print(LL.head.next.value)
print(LL.head.next.down.value)
print(LL.head.next.down.down.value)
print()
print(LL.head.next.next.value)
print(LL.head.next.next.down.value)
print(LL.head.next.next.down.down.value)
print()

print(LL.head.next.next.next.value)
mover_jugador(posicion_alien, n, LL)