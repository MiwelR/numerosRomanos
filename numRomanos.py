simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 =('V', 'D', 'L')
restas = ('CD', 'CM', 'XL', 'XC', 'IV', 'IX')

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido")
    else:
        raise ValueError(f"parámetro {simbolo} debe ser un string")

def orden_magnitud(caracter):
    valor = simbolo_a_entero(caracter)
    return len(str(valor))

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parámetro {romano} debe ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = ""
    orden_magnitud_global = 0
    orden_magnitud_letra = 0
    ha_habido_resta = False

    for letra in romano:
        orden_magnitud_letra = orden_magnitud(letra)
        if letra == valor_anterior:
            # SUMA REPETICIÓN
            orden_magnitud_global = orden_magnitud_letra
            if letra in tipo_5:
                raise ValueError(f"Demasiados simbolos de tipo: {letra}")
            elif c_repes >= 2:
                raise ValueError(f"Has repetido '{letra}' demasiadas veces")
            elif ha_habido_resta:
                raise ValueError(f"No es posible sumar {letra} a un valor inferior")
            c_repes += 1
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            # RESTA
            if valor_anterior + letra not in restas:
                raise ValueError(f"No están permitidas restas de este tipo: {valor_anterior + letra}")
            elif c_repes > 0:
                raise ValueError("Resta tras repeticion no permitida")
            elif ha_habido_resta:
                raise ValueError("No puede realizar dos veces la misma resta")

            ha_habido_resta = True
            suma -= 2 * simbolo_a_entero(valor_anterior)
            c_repes = 0
        else:
            # SUMA
            if orden_magnitud_global > orden_magnitud_letra:
                ha_habido_resta = False

            if ha_habido_resta:
                raise ValueError("Demasiadas restas")

            orden_magnitud_global = orden_magnitud_letra
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra    
    return suma

# Funciones para conversión de números enteros a romanos:

def descomponer(numero):
    if not isinstance(numero, int):
        raise SyntaxError(f"{numero} no es un número natural")

    l = []
    for n in str(numero):
        l.append(int(n))
    return l
'''
# DESCOMPOSICIÓN USANDO ENTEROS

def descomponer(numero):
    l = []
    for pot in (1000, 100, 10):
        l.append(numero // pot)
        numero %= pot

    
    l.append(numero)

    return l
'''

millares = ('M',)
centenas = ('C', 'D', 'M')
decenas = ('X', 'L', 'C')
unidades = ('I', 'V', 'X')
ordenes = [unidades, decenas, centenas, millares]

def convertir(ordenes_magnitud):
    contador = 0
    resultado = []
    for orden in ordenes_magnitud[::-1]:
        resultado.append(procesar_simbolo(orden, ordenes[contador]))
        contador += 1

    return ''.join(reversed(resultado))


def procesar_simbolo(s, clave):
    if s == 9:
        return clave[0] + clave[2]
    elif s >= 5:
        return clave[1] + clave[0] * (s-5)
    elif s == 4:
        return clave[0] + clave[1]
    else:
        return clave[0] * s


def entero_a_romano(numero):
    if not isinstance(numero, int):
        raise SyntaxError(f"{numero} no es un número natural")

    if numero < 1 or numero > 3999:
        raise OverflowError(f"{numero} ha de estar entre 1 y 3999")

    ordenes_de_magnitud = descomponer(numero)
    romano = convertir(ordenes_de_magnitud)
    return romano



