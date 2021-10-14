from colorama import init, Fore
init()

from Taller_LinkedList import Linked_List

taller_sll = Linked_List()

print(Fore.YELLOW + '************** ' + Fore.RESET + 'TALLER SINGLE LINKED LIST' + Fore.YELLOW +' **************\n' + Fore.RESET)

taller_sll.append()
taller_sll.show_menu()

print(Fore.GREEN + '\n*** Programa finalizado con exito ***' + Fore.RESET)