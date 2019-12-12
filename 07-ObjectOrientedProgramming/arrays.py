import random
class Arrays():
    
    sign = ","
    
    @staticmethod
    def separator(new_sign):
        Arrays.sign = new_sign

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(list):
        print(*list,sep=f'{Arrays.sign} ')
        
    @staticmethod
    def metoda1(liczba_elementow_tablicy,wartosc_elementow_tablicy):
        list = []
        for _ in range(liczba_elementow_tablicy):
            list.append(wartosc_elementow_tablicy)
        print(*list,sep=f'{Arrays.sign} ')
    
    @staticmethod
    def metoda2(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        list = [random.randint(wartosc_od,wartosc_do) for _ in range(liczba_elementow_tablicy)]
        print(*list,sep=f'{Arrays.sign} ')
    
    @staticmethod
    def metoda3(tablica,wartość_od,wartość_do):
        list = []
        for _ in tablica:
            if _ in range(wartość_od,wartość_do+1):
                list.append(_)
        print(len(list))
    
my_array = [4,1,8,7,2]
#Arrays.print_in_col(my_array)