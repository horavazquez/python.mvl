def cuentaPalabras(cadena):
    cadena = cadena.lower()
    diccionario = {}
    lista = cadena.split()
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabra_mas_repetida(dwords):
    max_frec = 0
    max_word = ""
    wordlist = []
    for palabra, frec in dwords.items():
        if frec >= max_frec: 
            if frec > max_frec:  
                wordlist = []
            max_word = palabra
            max_frec = frec
            wordlist.append((max_word, max_frec))        
    return wordlist


texto=input("Ingresa una cadea de caracteres: ")
resultado = cuentaPalabras(texto)
print("Frecuencia de palabras:", resultado)

print ("Palabra mas repetida", palabra_mas_repetida(resultado))
