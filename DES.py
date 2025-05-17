#Geração de Chaves

# Matrizes
S0 = [
  [1, 0, 3, 2],
  [3, 2, 1, 0],
  [0, 2, 1, 3],
  [3, 1, 3, 2]
]
S1 = [
  [0, 1, 2, 3],
  [2, 0, 1, 3],
  [3, 0, 1, 0],
  [2, 1, 0, 3]
]
# --------------------------------------------------------------

def permutacao_p10(chave_ini):
    chave_ini_str = str(chave_ini)
    p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    nova_chave = []
    for i in range(len(p10)):
        nova_chave.append(chave_ini_str[p10[i]])
    print(nova_chave)    
    return nova_chave

def divisao_deslocamento_p10(chave):
    chave_esquerda = chave[:5]
    chave_direita = chave[5:]
    print(chave_esquerda)    
    print(chave_direita)    

    chave_ref = chave_esquerda[1:]
    chave_ref.append(chave_esquerda[0])
    chave_esquerda = chave_ref

    chave_ref = chave_direita[1:]
    chave_ref.append(chave_direita[0]) 
    chave_direita = chave_ref

    return chave_esquerda + chave_direita

def permutacao_p8(chave):
    p8 = [5,2,6,3,7,4,9,8]
    nova_chave = []
    for i in range(len(p8)):
        nova_chave.append(chave[p8[i]])
    print(nova_chave)    
    return nova_chave

def divisao_deslocamento_duplo_p10(chave):
    chave = divisao_deslocamento_p10(chave)
    chave = divisao_deslocamento_p10(chave)
    chave_esquerda = chave[:5]
    chave_direita = chave[5:]
    print(chave_esquerda)    
    print(chave_direita)    

    chave_ref = chave_esquerda[1:]
    chave_ref.append(chave_esquerda[0])
    chave_esquerda = chave_ref

    chave_ref = chave_direita[1:]
    chave_ref.append(chave_direita[0]) 
    chave_direita = chave_ref

    return chave

def permutacao_inicial(bloco_de_dados):
    block = str(bloco_de_dados)
    ip = [1,5,2,0,3,7,4,6]
    nova_chave = []
    
    for i in range(len(ip)):
        nova_chave.append(block[ip[i]])
        
    divisão = nova_chave[:2]
        
    return nova_chave


def rodada_feistel(chave_direita_ip):
    ep = "30121230"
    chave_inteira_ip = ""
    for i in ep:
        chave_inteira_ip += chave_direita_ip[int(i)]

    return chave_inteira_ip

def xor_comparador(chave_k, chave_ep):
    chave_k_string = ""
    for c in chave_k:
        chave_k_string += c

    chave_k = chave_k_string
    chave_ep = str(chave_ep)

    chave_final_xor = ""

    for i in range(len(chave_k)):
        if chave_k[i] == chave_ep[i]:
            chave_final_xor += "0"
        else:
            chave_final_xor += "1"
    return chave_final_xor

def binario_deciaml(valor_binario):
    dicionario_binario = {"00":"0", "01":"1", "10":"2", "11":"3"}
    return dicionario_binario[valor_binario]

def decimal_binario(valor_decimal):
    dicionario_decimal = {0:"00", 1:"01", 2:"10", 3:"11"}
    return dicionario_decimal[valor_decimal]

def s_boxes(chave_xor):
    str(chave_xor)
    s0 = chave_xor[:4]
    s1 = chave_xor[4:]

    soma_externa_s0 = s0[0]+s0[3]
    soma_interna_s0 = s0[1]+s0[2]
    soma_externa_s1 = s1[0]+s1[3]
    soma_interna_s1 = s1[1]+s1[2]

    soma_externa_s0 = binario_deciaml(soma_externa_s0)
    soma_interna_s0 = binario_deciaml(soma_interna_s0)
    soma_externa_s1 = binario_deciaml(soma_externa_s1)
    soma_interna_s1 = binario_deciaml(soma_interna_s1)
    
    numero_matriz_s0 = S0[int(soma_externa_s0)][int(soma_interna_s0)]
    numero_matriz_s1 = S1[int(soma_externa_s1)][int(soma_interna_s1)]

    valor_s0 = decimal_binario(numero_matriz_s0)
    valor_s1 = decimal_binario(numero_matriz_s1)
    valor_final = valor_s0+valor_s1
    return valor_final 

def permutacao_p4(valor_s_box):
    p4 = [1,3,2,0]
    valor_final = ""
    for n in p4:
        valor_final += valor_s_box[n]
    return valor_final

def rodada_feistel_rodada_2_k2(chave):
    ep = "30121230"
    chave_lista = []
    for c in ep:
        chave_lista.append(chave[int(c)])
    return chave_lista 

def permutacao_inversa(chave):
    ip = "30246175"
    ip_final = ""
    for c in ip:
        ip_final += chave[int(c)]
    return ip_final


def encriptar_des(bloco_de_dados, chave_inicial):
    nova_chave_p10 = permutacao_p10(chave_inicial)
    nova_chave_p10= divisao_deslocamento_p10(nova_chave_p10)
    chave_k1 = permutacao_p8(nova_chave_p10) #p8 k1
    print(chave_k1)
    print("-----------------------------------------------------------")
    nova_chave_p10_k2 = divisao_deslocamento_duplo_p10(nova_chave_p10)
    nova_chave_p8_k2 = permutacao_p8(nova_chave_p10_k2) #k2
    print(nova_chave_p8_k2)
    print("-----------------------------------------------------------")
    nova_chave_ip = permutacao_inicial(bloco_de_dados)
    print(nova_chave_ip)
    print("-----------------------------------------------------------")

    chave_esquerda_ip = nova_chave_ip[:4]
    print(chave_esquerda_ip)
    chave_direita_ip = nova_chave_ip[:4]
    print(chave_direita_ip)
    print(chave_esquerda_ip)
    print("-----------------------------------------------------------")
    ep_R = rodada_feistel(chave_direita_ip)
    print(ep_R)

    xor_k1_epR = xor_comparador(chave_k1, ep_R)

    valor_s_boxes = s_boxes(xor_k1_epR)
    valor_s_boxes_p4 = permutacao_p4(valor_s_boxes)
    print(valor_s_boxes_p4)

    l_xor_p4 = xor_comparador(chave_esquerda_ip, valor_s_boxes_p4)

    #Troca de metades
    chave_esquerda_ip = chave_direita_ip
    chave_direita_ip = l_xor_p4

    print("-----------------------------------------------------------")
    #Para k2
    print(chave_direita_ip)
    ep_R_k2 = rodada_feistel_rodada_2_k2(chave_direita_ip)
    print(ep_R_k2)

    xor_k2_epR = xor_comparador(nova_chave_p8_k2, ep_R_k2)

    valor_s_boxes_k2 = s_boxes(xor_k2_epR)
    valor_s_boxes_p4_k2 = permutacao_p4(valor_s_boxes_k2)
    print(valor_s_boxes_p4_k2)

    l_xor_p4_k2 = xor_comparador(chave_esquerda_ip, valor_s_boxes_p4_k2)
    chave_esquerda_ip = l_xor_p4_k2

    final_antes_de_ip = chave_esquerda_ip + chave_direita_ip
    print(final_antes_de_ip)

    print("-----------------------------------------------------------")

    ip_inverso = permutacao_inversa(final_antes_de_ip)
    print(ip_inverso)

# Adicione o valor do bloco de dados e da chave de dados de 8 bits
bloco_de_dados = 11010111
chave_inicial = 1010000010
encriptar_des(bloco_de_dados, chave_inicial)
