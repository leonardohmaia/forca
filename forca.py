import random

def jogar_forca():
    palavras = ["python", "programacao", "linguagem", "computador", "desenvolvimento"]
    palavra = random.choice(palavras)
    letras_corretas = []
    tentativas = 6

    while True:
        letra = input("Digite uma letra: ")
        if letra in palavra:
            letras_corretas.append(letra)
        else:
            tentativas -= 1

        palavra_descoberta = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])
        print(f"Palavra: {palavra_descoberta}")
        print(f"Tentativas restantes: {tentativas}")

        if palavra_descoberta == palavra:
            print("Você venceu!")
            break
        elif tentativas == 0:
            print(f"Fim de jogo. A palavra era: {palavra}")
            break

if __name__ == "__main__":
    jogar_forca()
