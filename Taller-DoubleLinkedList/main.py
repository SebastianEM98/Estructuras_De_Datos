from colorama import init, Fore
init()

from Taller_DoubleLinkedList import Double_Linked_List

taller_dll = Double_Linked_List()

print(Fore.YELLOW + '************** ' + Fore.RESET + 'TALLER DOUBLE LINKED LIST' + Fore.YELLOW +' **************\n' + Fore.RESET)

taller_dll.initialize_append()
taller_dll.show_menu()

print(Fore.GREEN + '\n*** Programa finalizado con exito ***' + Fore.RESET)