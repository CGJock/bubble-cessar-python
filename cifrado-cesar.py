import colorise
def encriptador():
    word_encriptar = input("Digite la palabra a encriptar")
    encriptado_len = int(input("Digite un numero a encriptar ej: -1 para encriptar a la izquierda 1 hacia la derecha"))
    letras_codificadas = []
    palabra_final = []
    frase = list(word_encriptar)
    if word_encriptar.isalpha():
        for indice in frase:
            letras = ord(indice)
            letras_codificadas.append(letras + encriptado_len)
        for letra in letras_codificadas:
            letras = chr(letra)
            palabra_final.append(letras)
            palabra_final_map = ''.join(map(str,palabra_final))
        print(f"La palabra original {word_encriptar}, y la nueva palabra cifrada es {palabra_final_map}")
                
        
    
def decriptador():
    word_decriptar = input("Digite la palabra a decriptar: ")
    decrip_len = input("Ingrese el numero con el que se decriptara: ")
    letras_decodificar = []
    if word_decriptar.isalpha():
        for indice in word_decriptar:
            letras = ord(indice)
            letras_decodificar.append(letras + decrip_len)
            print(letras_decodificar)
    
    pass

def cesar():
    print("Bienvenido al encriptador/decriptador de mensajes")
    accion = input("Deseas encriptar o decriptar: 'ENCRIPTAR'  'DECRIPTAR'")
    if accion.lower() == "encriptar":
        encriptador()
    elif accion.lower():
        decriptador()


cesar()