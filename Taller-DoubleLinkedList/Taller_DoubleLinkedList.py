from colorama import init, Fore
init()

class Double_Linked_List:
  class Node:
    #Metodo inicializador de la clase Nodo
    def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None
  #Metodo inicializador de la clase Double_Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0


  #Metodo que muestra el menu de opciones
  def show_menu(self):
    option_menu = 0
    while option_menu != 3:
      try:
        option_menu = int(input(Fore.YELLOW + '\nSeleccione una opción:' + Fore.RESET + '\n1. ' + Fore.CYAN + 'Eliminar nodo' + Fore.RESET + '\n2. ' + Fore.CYAN + 'Invertir la lista' + Fore.RESET + '\n3. ' + Fore.CYAN + 'Invertir la lista elevando valores al cuadrado' + Fore.RESET + '\n4. ' + Fore.CYAN + 'Salir\nTu respuesta ' + Fore.YELLOW + '>>> ' + Fore.RESET))

        if option_menu == 1:
          self.remove()

        elif option_menu == 2:
          self.reverse()

        elif option_menu == 3:
          self.reverse_pow()
        
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
  def initialize_append(self):
    while True:
      try:
        cant_node = int(input(Fore.CYAN + '\n     Cantidad de nodos a crear: ' + Fore.RESET + Fore.YELLOW + '\n      >>> ' + Fore.RESET))
        for node_item in range(cant_node):
          value = int(input(Fore.CYAN + '\n     Ingrese el valor del nodo: ' + Fore.RESET))
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
          else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
          self.length += 1
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print(Fore.RED + '\n*** Se esperaba un numero ***' + Fore.RESET)


  #Metodo para eliminar un nodo por indice ingresado por el usuario
  def remove(self):
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
    if index == 0:
      self.shift()
      print(Fore.GREEN + '\n*** Eliminado con exito ***' + Fore.RESET)
      self.show_elements()
    elif index == self.length-1:
      self.pop()
      print(Fore.GREEN + '\n*** Eliminado con exito ***' + Fore.RESET)
      self.show_elements()
    else:
      prev_node = self.get(index-1)
      next_node = self.get(index+1)
      prev_node.next = next_node
      next_node.prev = prev_node
      self.length -= 1
      print(Fore.GREEN + '\n*** Eliminado con exito ***' + Fore.RESET)
      self.show_elements()

  
  #Metodo para invertir la lista
  def reverse(self):
    prev_node = None
    current_node = self.head
    self.head.prev = None
    while current_node != None:
      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node
      current_node = current_node.prev
    self.head = prev_node.prev
    print(Fore.GREEN + '\n*** Lista invertida ***' + Fore.RESET)
    self.show_elements()


  #Metodo para invertir la lista elevando los valores al cuadrado
  def reverse_pow(self):
    prev_node = None
    current_node = self.head
    self.head.prev = None
    while current_node != None:
      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node
      current_node.value = current_node.value ** 2
      current_node = current_node.prev
    self.head = prev_node.prev
    print(Fore.GREEN + '\n*** Lista invertida elevando al cuadrado ***' + Fore.RESET)
    self.show_elements()


  #Metodo para obtener el valor de un nodo a partir del indice
  def get(self, index):
    if index == 0:
      return self.head
    elif index == self.length-1:
      return self.tail
    elif not(index >= self.length or index < 0):
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
      delete_node.prev = None
      self.length -= 1


  #Metodo para eliminar el ultimo elemento de la lista
  def pop(self):
    if self.length == 0 or self.length == 1:
      self.head = None
      self.tail = None
    else:
      current_node = self.tail
      temp = current_node.prev
      temp.next = None
      temp = None
      self.tail = current_node.prev
      self.length -= 1