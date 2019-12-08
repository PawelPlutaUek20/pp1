import statistics
class Stats():
    def __init__(self):
        self.tab = []
    def add_to_tab(self):
        number = int(input("Podaj liczbe: "))
        self.tab.append(number)
    def show_tab(self):
        print(*tab, sep=', ')
    def show_stats(self):
        print(f'Biggest number: {max(self.tab)}\nSmallest number: {min(self.tab)}\nArithmetic average: {statistics.mean(self.tab)}\nMedian: {statistics.median(self.tab)}')
st = Stats()
for _ in range(5):
    st.add_to_tab()
st.show_stats()