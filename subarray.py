import random

# Função para calcular a soma dos elementos de um subarray
def calculaSoma(subArray):
    soma = 0
    for i in range(len(subArray)):
        soma += subArray[i]
    return soma

# Função para encontrar o maior subarray contíguo em um array dado
def maiorSubArray(array, posEsq, posDir):
    # Caso base: quando há apenas um elemento no array
    if posEsq == posDir:
        return array[posEsq], [array[posEsq]]

    # Encontre o ponto médio do array
    meioArray = (posEsq + posDir) // 2

    # Recursivamente encontre o maior subarray na metade esquerda
    maiorSubEsq, subArrayEsq = maiorSubArray(array, posEsq, meioArray)
    # Recursivamente encontre o maior subarray na metade direita
    maiorSudDir, subArrayDir = maiorSubArray(array, meioArray + 1, posDir)

    # Inicialização de variáveis para encontrar o maior subarray no meio
    maiorSubEsqMeio = float('-inf')
    soma = 0
    indiceEsq = meioArray

    # Encontre o maior subarray na metade esquerda do meio
    for i in range(meioArray, posEsq - 1, -1):
        soma += array[i]
        if soma > maiorSubEsqMeio:
            maiorSubEsqMeio = soma
            indiceEsq = i

    maiorSubDirMeio = float('-inf')
    soma = 0
    indiceDir = meioArray + 1

    # Encontre o maior subarray na metade direita do meio
    for i in range(meioArray + 1, posDir + 1):
        soma += array[i]
        if soma > maiorSubDirMeio:
            maiorSubDirMeio = soma
            indiceDir = i

    # Combine os resultados das metades esquerda e direita para encontrar o maior subarray no meio
    maiorSubMeio = maiorSubEsqMeio + maiorSubDirMeio

    # Determine qual subarray tem a soma máxima entre as três opções
    if maiorSubMeio >= maiorSubEsq and maiorSubMeio >= maiorSudDir:
        subArrayMeio = array[indiceEsq:indiceDir+1]  # Subarray do meio
        return maiorSubMeio, subArrayMeio
    elif maiorSubEsq >= maiorSudDir:
        return maiorSubEsq, subArrayEsq  # Maior subarray na metade esquerda
    else:
        return maiorSudDir, subArrayDir  # Maior subarray na metade direita

# Criação do array com valores definidos pelo usuário
array = []
lenArray = int(input('Qual a quantidade de números do array: '))
for i in range(lenArray):
    array.append(int(input(f'Insira o número da posição {i}: ')))

print(array)

# Encontre o maior subarray e imprima os resultados
maxSubArray, subArray = maiorSubArray(array, 0, len(array)-1)
print("Maior soma subarray contíguo:", maxSubArray)
print("Subarray correspondente:", subArray)
