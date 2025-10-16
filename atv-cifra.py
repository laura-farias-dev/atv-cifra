def cifrar (texto, chave):
  return algoritmo(texto, chave, fator = 1)

def decifrar (texto_cifrado, chave):
  return algoritmo(texto_cifrado, chave, fator = -1)

def algoritmo(texto, chave, fator):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789áéíóúâêôã ,;._#*\"-+"
    resultado = ""
    tam_alfabeto = len(alfabeto)

    if not texto.strip():
        raise ValueError("O texto não pode ser vazio")
    if not chave.strip():
        raise ValueError("A chave não pode ser vazia.")

    invalidos = set(c for c in texto + chave if c not in alfabeto)
    if invalidos:
      raise ValueError(f"Os seguintes caracteres inválidos foram encontrados: {''.join(invalidos)}")

    for i, c in enumerate(texto):
      pos_t = alfabeto.index(c)
      pos_k = alfabeto.index(chave[i % len(chave)])
      resultado += alfabeto[(pos_t + fator * pos_k) % tam_alfabeto]



    return resultado


if __name__ == "__main__":

  texto = input("Digite o texto a ser cifrado: ")
  chave = input("Digite a chave de cifragem: ")


  try:

    print("Texto Original: ", texto)

    texto_cifrado = cifrar(texto, chave)
    print("Texto cifrado:", texto_cifrado)

    texto_decifrado = decifrar(texto_cifrado, chave)
    print("Texto decifrado:", texto_decifrado)
  except ValueError as e:
    print(e)