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


  #Metodo para gregar elemento al final de la lista
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


  #Metodo para inicializar la lista agregando valores al final
  def append_pat(self):
    while True:
      try:
        cant_node = 1
        for node_item in range(cant_node):
          current_node = self.head
          patron = 3
          while current_node != None:
            current_node = current_node.next
            patron += 2
          value = int(input('\nIngrese el valor del nodo que cumpla con el parton para la ultima posicion: '))
          while True:
            if value == self.tail.value + patron:
              self.append(value)
              self.show_elements()
              break
            else:
              print('El valor no cumple con el patron')
              value = int(input('\nIngrese el valor del nodo que cumpla con el parton para la ultima posicion: '))
              if value == self.tail.value + patron:
                self.append(value)
                self.show_elements()
                break
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print('\n*** Se esperaba un numero ***')