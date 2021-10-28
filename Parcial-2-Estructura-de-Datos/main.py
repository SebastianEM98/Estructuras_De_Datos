from punto1 import Double_Linked_List
from punto2 import Circular_Linked_List
from punto3 import Double_Linked_List

p1 = Double_Linked_List()
p2 = Circular_Linked_List()
p3 = Double_Linked_List()

print('********** PUNTO 1 **********')

print('\nLista: ')
p1.append(2)
p1.append(5)
p1.append(10)
p1.append(17)
p1.append(26)
p1.append(37)
p1.append(50)
p1.append(65)
p1.append(82)
p1.show_elements()
p1.append_pat()


print('********** PUNTO 2 **********')

print('\nLista: ')
p2.append(4)
p2.append(11)
p2.append(18)
p2.append(25)
p2.append(46)
p2.append(53)
p2.append(60)
p2.show_elements()
p2.insert_pat()

print('********** PUNTO 3 **********')
p3.append_initialize()