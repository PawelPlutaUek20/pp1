import math
# Sumuje liczby nturalne parzyste z przedziału <from_n,to_n>
def sum_even(from_m,to_n):
    sum = 0
    if (type(from_m) != int and type(from_m) != float) or (type(to_n) != int and type(to_n) != float):
        return 0
    for i in range(math.ceil(from_m),math.floor(to_n+1)):
        if to_n+1<0 :
            return 0
        if from_m <0 and from_m<to_n+1:
            from_m+=1
        elif i%2 == 0: # liczba parzysta
            sum += i
    return sum

def main():
    m = "jeden"
    n = "osiem"
    print(f"Suma liczb naturalnych parzystych z przedziału <{m},{n}> wynosi {sum_even(m,n)}")

if __name__ == "__main__":
    main()