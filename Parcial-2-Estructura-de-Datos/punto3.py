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
  

  #Metodo para mostrar los elementos de la lista
  def show_elements(self):
    array = []
    current_node = self.head
    while current_node != None:
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)


  #Metodo para agregar elemento al final de la lista
  def append(self, value):
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


  #Metodo apra eliminar el ultimo elemento de la lista
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


  #Metodo 6:Consultar valor de un nodo a partir del indice ingresado por el usuario
  def get(self, index):
    if index == 0:
      print(self.head.value)
      return self.head
    elif index == self.length-1:
      print(self.tail.value)
      return self.tail
    elif not(index >= self.length or index < 0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      print(current_node.value)
      return current_node
    else:
      print('indice por fuera de los limites')
      return None

  
  #Metodo 10: Eliminar un elemento por valor
  def remove_value(self, value):
      if self.head.value == value:
        self.shift()
      elif self.tail.value == value:
        self.pop()
      else:
        tmp = self.head.next
        tmp_next = tmp.next
        tmp_prev = self.head
        while tmp.next != None:
          if tmp.value == value:
            tmp_prev.next = tmp_next
            tmp_next.prev = tmp_prev
            tmp.next = None
            tmp.prev = None
            break
          tmp = tmp.next
          tmp_next = tmp_next.next
          tmp_prev = tmp_prev.next
        self.length -= 1


  #Metodo para inicializar la lista agregando valores al final
  def append_initialize(self):
    while True:
      try:
        cant_node = 6
        i = 0
        for node_item in range(cant_node):
          value = int(input(f'\nIngrese el valor del nodo para la posicion {i}: '))
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
            i += 1
          else:
            self.append(value)
            i += 1
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print('\n*** Se esperaba un numero ***')