class Circular_Linked_List:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    

  #Metodo para mostrar los elementos que conforman nuestra lista
  def show_elements(self):
    array = []
    current_node = self.head
    pivote = True
    count = self.length
    while count != 0:
      if pivote != False or current_node != self.head:
        array.append(current_node.value)
        current_node = current_node.next
        pivote = False
        count -= 1
      else:
        break
    return print(array)


  #Metodo para agregar elemento al final de la lista circular
  def append(self, value):
    new_node = self.Node(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.next = self.head
      self.tail = new_node
    self.length += 1
      

  #Metodo para Consultar valor de un nodo a partir del inicie
  def get(self, index):
    if index == self.length-1:
      return self.tail
    if index == 0:
      return self.head
    elif not(index >= self.length or index < 0):
      current_node = self.head
      count = 0
      while count != index:
        current_node = current_node.next
        count += 1
      return current_node
    else:
      print('indice por fuera de los limites')
      return None


  #Metodo para insertar nodo en determinada posicion de la lista circular
  def insert(self, index, value):
    if index == self.length:
      self.append(value)
    elif index == 0:
      self.prepend(value)
    elif not(index >= self.length or index < 0):
      new_node = self.Node(value)
      prev_node = self.get(index-1)
      next_node = prev_node.next
      prev_node.next = new_node
      new_node.next = next_node
      self.length += 1
    else:
      print('indice por fuera de los limites')


  #Metodo 9: Eliminar un elemento determinado por indice
  def remove(self, index):
    if index == 0:
      self.shift()
    elif index == self.length-1:
      self.pop()
    elif not(index >= self.length or index < 0):
      prev_node = self.get(index-1)
      next_node = self.get(index+1)
      prev_node.next = next_node
      self.length -= 1
    else:
      print('indice por fuera de los limites')


  #Metodo para inicializar la lista agregando valores al final
  def insert_pat(self):
    while True:
      try:
        cant_node = 2
        index = 4
        get_index = 3
        for node_item in range(cant_node):
          value = int(input(f'\nIngrese el valor del nodo que cumpla con el patron para la posicion {index}: '))
          current_node = self.get(get_index)
          if value == current_node.value + 7:
            self.insert(index, value)
            get_index += 1
            index += 1
            self.show_elements()
          else:
            intentos = 3
            while intentos != 0:
              print(f'El valor no cumple con el patron, le quedan {intentos} intentos')
              value = int(input(f'\nIngrese el valor del nodo que cumpla con el patron para la posicion {index}: '))
              if value == current_node.value + 7:
                self.insert(index, value)
                get_index += 1
                index += 1
                self.show_elements()
                break
              else:
                intentos -= 1
            if intentos == 0:
              print('Inténtalo en una próxima ocasión')
              break
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print('\n*** Se esperaba un numero ***')