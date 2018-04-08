def main():
    print("Selecciona la opcion deseada")
    print("1.)Decimal a binario")
    print("2.)Decimal a hexadecimal")
    print("3.)Binario a decimal")
    print("4.)Binario a Hexadecimal")
    print("5.)Hexadecimal a binario")
    print("6.)Hexadecimal a decimal")
    seleccion = input()
    numero = input("ingresa el numero a convertir :")
    if seleccion == '1':
        res = DecimalABase(2,int(numero))
        print(res)
    elif seleccion == "2":
        res = DecimalABase(16,int(numero))
        print(res)
    elif seleccion == "3":
        res = BaseADecimal (2,numero)
        print(res)
    elif seleccion == "4":
        temp = BaseADecimal(2,numero)
        res = DecimalABase(16,temp)
        print(res)
    elif seleccion == "5":
        temp = BaseADecimal (16,numero)
        res = DecimalABase(2,temp)
        print(res)
    elif seleccion == "6":
        temp = BaseADecimal(16,numero)
        res = DecimalABase(10,temp)
        print(res)

def DecimalABase(base,numero):
    resultado = ""
    while numero > 0:
        residuo=numero % base
        numero =numero // base
        if residuo == 10:
            resultado = "A" + resultado
        elif residuo == 11:
            resultado = "B" + resultado
        elif residuo == 12:
            resultado = "C" + resultado
        elif residuo == 13:
            resultado = "D" + resultado
        elif residuo == 14:
            resultado = "E" + resultado
        elif residuo == 15:
            resultado = "F" + resultado
        else:
            resultado = str(residuo) + resultado
    return resultado

def BaseADecimal (base,numero):
    cuantosDigitos = len(numero)
    exponente = 0
    resultado = 0

    for i in range(cuantosDigitos,0,-1):
        digito = numero[i-1]
        if digito.upper() == "A":
            resultado += 10*(base**exponente)
        elif digito.upper() == "B":
            resultado += 11 * (base ** exponente)
        elif digito.upper() == "C":
            resultado += 12 * (base ** exponente)
        elif digito.upper() == "D":
            resultado += 13 * (base ** exponente)
        elif digito.upper() == "E":
            resultado += 14 * (base ** exponente)
        elif digito.upper() == "F":
            resultado += 15 * (base ** exponente)
        else:
            resultado += int(digito) * (base**exponente)
            exponente += 1
    return resultado
