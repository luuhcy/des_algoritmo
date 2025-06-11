#!/usr/bin/env python3
SBOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}
def string_em_bits(text):
    bits_final = ''
    for char in text:
        #ord transforma string em ascii
        valor_em_ascii = ord(char)
        ascii_em_binario = bin(valor_em_ascii)[2:]  # Remove o prefixo '0b'

        #Coloca 0s para manter 8 bits se houver menos
        while len(ascii_em_binario) < 8:
            ascii_em_binario = '0' + ascii_em_binario

        bits_final += ascii_em_binario
    return bits_final

def definicao_nibbles(bits):
    lista_nibbles = []
    i = 0
    while i < len(bits):
        nibble_string = bits[i:i+4]  # Pega 4 bits
        nibble_string_em_inteiro = int(nibble_string, 2)  # Converte de binário para inteiro
        lista_nibbles.append(nibble_string_em_inteiro)
        i = i + 4

    if (len(lista_nibbles) < 4):
        i = len(lista_nibbles)
        while i < 4:
            lista_nibbles.append(0)
            i += 1
    return lista_nibbles

def matriz_de_nibbles(nibble):
    matriz = [[nibble[0],nibble[1]],[nibble[2],nibble[3]]]
    return matriz

def matriz_em_nibbles(matriz):
   nibbles = [matriz[0][0],matriz[0][1],matriz[1][0],matriz[1][1],]
   return nibbles

def add_round_key(matriz_mensagem, matriz_chave):
    round = [
        [matriz_mensagem[0][0] ^ matriz_chave[0][0], matriz_mensagem[0][1] ^ matriz_chave[0][1]],
        [matriz_mensagem[1][0] ^ matriz_chave[1][0], matriz_mensagem[1][1] ^ matriz_chave[1][1]]
    ]
    return round

def substituicao_nibbles_sbox(matriz):
    novos_nibbles = [
        [SBOX[matriz[0][0]], SBOX[matriz[0][1]]],
        [SBOX[matriz[1][0]], SBOX[matriz[1][1]]]
    ]
    return novos_nibbles

def inverter_segunda_linha_matriz(state):
    matriz_invertida = [
        [state[0][0], state[0][1]],
        [state[1][1], state[1][0]]
    ]
    return matriz_invertida


mensagem = "A"
msg_em_bits = string_em_bits(mensagem)
print("MSG: String em bits: ", msg_em_bits)
msg_bits_em_nibbles = definicao_nibbles(msg_em_bits)
print("MSG: Definição dos Nibbles: ", msg_bits_em_nibbles)
matriz_msg = matriz_de_nibbles(msg_bits_em_nibbles)
print("MSG: Nibbles -> Matriz: ", matriz_msg)

chave = "k"
chave_em_bits = string_em_bits(chave)
print("CHAVE: String em bits: ", chave_em_bits)
bits_em_nibbles = definicao_nibbles(chave_em_bits)
print("CHAVE: Definição dos Nibbles: ", bits_em_nibbles)
matriz_chave = matriz_de_nibbles(bits_em_nibbles)
print("CHAVE: Nibbles -> Matriz: ", matriz_chave)

round_key = add_round_key(matriz_msg, matriz_chave)
print(round_key)
