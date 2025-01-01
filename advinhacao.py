import os 
import random 
os.system ("cls")

palavras = ["amor", "jogos","ano","maria"]


palavra_escolhida = random.choice(palavras)
tentativa = 6
array = list(palavra_escolhida)
letras_adivinhadas = ['_'] * len(palavra_escolhida)



while (tentativa > 0 ):
    print("Palavra: ", " ".join(letras_adivinhadas))
    letra = input ("digite uma letra:").lower()
    os.system()

    if letra in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_adivinhadas[i] = letra
        print("Boa! Você acertou uma letra.")

    else:
        tentativa -= 1
        print ("Vish, você errou a letra. Tente novamente...")
        print (tentativa)

    
    if ''.join(letras_adivinhadas) == palavra_escolhida:
        print("Parabens, você acertou a palavra secreta")
        print (tentativa)
        break


if tentativa == 0:
    print("você perdeu")
    

    