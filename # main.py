# main.py

def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    maior, menor = divmod(x, 10**m)
    maior2, menor2 = divmod(y, 10**m)
    
    x1 = karatsuba(menor, menor2)
    x2 = karatsuba((menor + maior), (menor2 + maior2))
    x3 = karatsuba(maior, maior2)
    
    return (x3 * 10**(2*m)) + ((x2 - x3 - x1) * 10**m) + x1

if __name__ == "__main__":
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    xy = karatsuba(x, y)
    print(f"Resultado da multiplicação karatsuba: {xy}")
