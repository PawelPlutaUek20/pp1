import random
class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(array):
        print(*array,sep=', ')
        
    @staticmethod
    def metoda1(liczba_elementow_tablicy,wartosc_elementow_tablicy):
        list = []
        for _ in range(liczba_elementow_tablicy):
            list.append(wartosc_elementow_tablicy)
        return list
    
    @staticmethod
    def metoda2(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        return [random.randint(wartosc_od,wartosc_do) for _ in range(liczba_elementow_tablicy)]
    
    @staticmethod
    def metoda3(tablica,wartość_od,wartość_do):
        list = []
        for _ in tablica:
            if _ in range(wartość_od,wartość_do+1):
                list.append(_)
        return len(list)
    
my_array = [4,1,8,7,2]
#Arrays.print_in_col(my_array)