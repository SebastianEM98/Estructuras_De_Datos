from math import sqrt
from colorama import init, Fore
init()

class Linked_List:
  class Node:
    #Metodo inicializador de la clase Nodo
    def __init__(self, value):
      self.value = value
      self.next = None
  #Metodo inicializador de la clase Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  

  #Metodo que muestra el menu de opciones
  def show_menu(self):
    option_menu = 0
    while option_menu != 4:
      try:
        option_menu = int(input(Fore.YELLOW + '\nSeleccione una opción:' + Fore.RESET + '\n1. ' + Fore.CYAN + 'Añadir nodo con raiz cuadrada' + Fore.RESET + '\n2. ' + Fore.CYAN + 'Eliminar nodo y añadirlo al final elevado al cuadrado' + Fore.RESET + '\n3. ' + Fore.CYAN + 'Invertir la lista' + Fore.RESET + '\n4. ' + Fore.CYAN + 'Salir\nTu respuesta ' + Fore.YELLOW + '>>> ' + Fore.RESET))

        if option_menu == 1:
          self.new_node_sqrt()

        elif option_menu == 2:
          self.new_node_pow()

        elif option_menu == 3:
          self.reverse()
          
        elif option_menu == 4:
          break
        
        else:
          print(Fore.RED + '\n*** Ingrese una opcion valida ***' + Fore.RESET)

      except ValueError:
        print(Fore.RED + '\n*** Se esperaba un numero ***' + Fore.RESET)


  #Metodo para mostrar los elementos que conforman la lista
  def show_elements(self):
    array = []
    current_node = self.head
    while current_node != None:
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)


  #Metodo para inicializar la lista agregando valores al final
  def append(self):
    while True:
      try:
        cant_node = int(input(Fore.CYAN + '\n     Cantidad de nodos a crear: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
        for node_item in range(cant_node):
          value = int(input(Fore.CYAN + '\n     Ingrese el valor del nodo: ' + Fore.RESET))
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
          else:
            self.tail.next = new_node
            self.tail = new_node
          self.length += 1
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print(Fore.RED + '\n*** Se esperaba un numero ***' + Fore.RESET)


  #Metodo para agregar un elemento al inicio de la lista
  def prepend(self, value):
    new_node = self.Node(value)
    #Si la lista no contiene elementos, la cabeza y cola pasan a valer lo mismo
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    #Actualizamos el tamaño de la lista
    self.length += 1


  #Metodo para consultar valor de un nodo a partir del indice
  def get(self, index):
    if index == self.length -1:
      return self.tail
    if index == 0:
      return self.head
    elif not(index >= self.length or index <0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      return current_node
    else:
      return None


  #Metodo para eliminar el primer elemento de la lista
  def shift(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      self.length -= 1
      return delete_node.value


  #Metodo para eliminar el ultimo elemento de la lista
  def pop(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      #Recorremos toda la lista para identificar el ultimo elemento
      current_node = self.head
      new_tail = current_node
      while current_node.next != None:
        new_tail = current_node
        current_node = current_node.next
      self.tail = new_tail
      self.tail.next = None
      self.length -= 1
      return current_node.value


  #Metodo para eliminar un elemento dada la posicion
  def remove(self, index):
    if index == 0:
      return self.shift()
    elif index == self.length-1:
      return self.pop()
    elif not(index >= self.length or index < 0):
      preview_node = self.get(index-1)
      delete_node = preview_node.next
      preview_node.next = delete_node.next
      delete_node.next = None
      self.length -= 1
      return delete_node.value
    else:
      return None
    

  #Metodo del PUNTO 1
  def new_node_sqrt(self):
    while True:
      try:
        index = int(input(Fore.CYAN + '\n     Ingrese el indice: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
        while True:
          if index < 0 or index+1 > self.length:
            print(Fore.RED + '\n*** Indice por fuera de los limites ***' + Fore.RESET)
            index = int(input(Fore.CYAN + '\n     Ingrese el indice: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
          else:
            break
        break
      except ValueError:
        print(Fore.RED + '\n*** Se esperaba un numero ***' + Fore.RESET)
    new_node = self.get(index)
    node_sqrt = float(sqrt(new_node.value))
    print(Fore.YELLOW + '\n     Raiz cuadrada de '+  Fore.RESET , new_node.value, Fore.YELLOW + 'es: ' + Fore.RESET, node_sqrt)
    node_n = self.Node(node_sqrt)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
      print(Fore.GREEN + '\n*** Agregado con exito ***' + Fore.RESET)
      self.show_elements()
    else:
      self.tail.next = node_n
      self.tail = node_n
      print(Fore.GREEN + '\n*** Agregado con exito ***' + Fore.RESET)
      self.show_elements()
    self.length +=1


  #Metodo del PUNTO 2
  def new_node_pow(self):
    while True:
      try:
        index = int(input(Fore.CYAN + '\n     Ingrese el indice: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
        while True:
          if index < 0 or index+1 > self.length:
            print(Fore.RED + '\n*** Indice por fuera de los limites ***' + Fore.RESET)
            index = int(input(Fore.CYAN + '\n     Ingrese el indice: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
          else:
            break
        break
      except ValueError:
        print(Fore.RED + '\n*** Se esperaba un numero ***' + Fore.RESET)
    new_node = self.get(index)
    delete_node = self.remove(index)
    node_pow = pow(new_node.value, 2)
    print(Fore.YELLOW + '\n     Valor elimidado:  '+  Fore.RESET , delete_node)
    print(Fore.YELLOW + '\n     El numero '+  Fore.RESET , new_node.value, Fore.YELLOW + 'elevado al cuadrado es: ' + Fore.RESET, node_pow)
    node_n = self.Node(node_pow)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
      print(Fore.GREEN + '\n*** Agregado con exito ***' + Fore.RESET)
      self.show_elements()
    else:
      self.tail.next = node_n
      self.tail = node_n
      print(Fore.GREEN + '\n*** Agregado con exito ***' + Fore.RESET)
      self.show_elements()
    self.length += 1


  #Metodo para invertir la lista. Punto 3
  def reverse(self):
    reverse_nodes = None
    current_node= self.head
    self.tail = current_node
    while current_node != None:
      next = current_node.next
      current_node.next = reverse_nodes
      reverse_nodes = current_node
      current_node = next
    self.head = reverse_nodes
    print(Fore.GREEN + '\n*** Lista invertida ***' + Fore.RESET)
    self.show_elements()
    return self.head