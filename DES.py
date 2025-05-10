#Geração de Chaves

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
    ep = [3, 0, 1, 2, 1, 2, 3, 0]
    nova_chave = []
    before = ""
    reverter_chave= ""
    
    for i in ep:
        before += str(i)
    
    for i in range(len(ep)):
        nova_chave.append(before[ep[i]])
        
    nova_chave_esquerda = nova_chave[:4]
    for i in range(nova_chave_esquerda):
        reverter_chave = nova_chave_esquerda[i]

        
        
    return reverter_chave
    
    

bloco_de_dados = 11010111
chave_inicial = 1010000010
nova_chave_p10 = permutacao_p10(chave_inicial)
nova_chave_p10= divisao_deslocamento_p10(nova_chave_p10)
nova_chave_p8 = permutacao_p8(nova_chave_p10) #p8 k1
print(nova_chave_p8)
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
feistel = rodada_feistel(chave_direita_ip)
print(feistel)