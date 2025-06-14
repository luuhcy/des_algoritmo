# =======================================
# IMPLEMENTAÇÃO DO S-DES - SOCORRO DEUS
# =======================================

# Matrizes S-Box
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

# --- Funções Auxiliares ---
def binario_decimal(valor_binario):
    """Converte um valor binário (2 bits) para decimal"""
    return {"00": "0", "01": "1", "10": "2", "11": "3"}[valor_binario]

def decimal_binario(valor_decimal):
    """Converte um valor decimal (0-3) para binário (2 bits)"""
    return {0: "00", 1: "01", 2: "10", 3: "11"}[valor_decimal]

# --- Funções de Permutação ---
def permutacao(chave, tabela):
    """Aplica permutação usando a tabela especificada"""
    return ''.join([chave[int(i)] for i in tabela])

def permutacao_p10(chave):
    """Permutação P10: 3,5,2,7,4,10,1,9,8,6 (índices começando em 0)"""
    return permutacao(chave, [2,4,1,6,3,9,0,8,7,5])

def permutacao_p8(chave):
    """Permutação P8: 6,3,7,4,8,5,10,9 (índices começando em 0)"""
    return permutacao(chave, [5,2,6,3,7,4,9,8])

def permutacao_inicial(bloco):
    """Permutação Inicial (IP): 2,6,3,1,4,8,5,7"""
    return permutacao(bloco, [1,5,2,0,3,7,4,6])

def permutacao_inversa(bloco):
    """Permutação Inversa (IP⁻¹): 4,1,3,5,7,2,8,6"""
    return permutacao(bloco, [3,0,2,4,6,1,7,5])

def permutacao_p4(bloco):
    """Permutação P4: 2,4,3,1"""
    return permutacao(bloco, [1,3,2,0])

# --- Funções de Deslocamento ---
def deslocamento_circular(chave, shifts=1):
    """Realiza o deslocamento circular (left shift)"""
    return chave[shifts:] + chave[:shifts]

# --- Funções da Rodada Feistel ---
def expansao_permutacao(bloco):
    """Expansão/Permutação: 4,1,2,3,2,3,4,1"""
    return permutacao(bloco, [3,0,1,2,1,2,3,0])

def xor(bits1, bits2):
    """Operação XOR bit a bit"""
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2))

def s_boxes(bloco):
    """Aplica as S-Boxes S0 e S1"""
    s0 = bloco[:4]
    s1 = bloco[4:]
    
    linha_s0 = int(binario_decimal(s0[0] + s0[3]))
    coluna_s0 = int(binario_decimal(s0[1] + s0[2]))
    s0_result = decimal_binario(S0[linha_s0][coluna_s0])
    
    linha_s1 = int(binario_decimal(s1[0] + s1[3]))
    coluna_s1 = int(binario_decimal(s1[1] + s1[2]))
    s1_result = decimal_binario(S1[linha_s1][coluna_s1])
    
    return s0_result + s1_result

def rodada_feistel(esquerda, direita, subchave):
    """Rodada de Feistel completa """
    ep = expansao_permutacao(direita)
    xor_result = xor(ep, subchave)
    sbox_result = s_boxes(xor_result)
    p4_result = permutacao_p4(sbox_result)
    nova_esquerda = xor(esquerda, p4_result)
    return nova_esquerda, direita

# --- Geração de Subchaves ---
def gerar_subchaves(chave_principal):
    """Geração das subchaves K1 e K2"""
    p10 = permutacao_p10(chave_principal)
    
    esquerda = deslocamento_circular(p10[:5])
    direita = deslocamento_circular(p10[5:])
    
    k1 = permutacao_p8(esquerda + direita)
    
    esquerda = deslocamento_circular(esquerda, 2)
    direita = deslocamento_circular(direita, 2)
    
    k2 = permutacao_p8(esquerda + direita)
    
    return k1, k2

# --- Cifração S-DES ---
def cifrar_sdes(bloco, chave_principal):
    """Cifração S-DES completa"""
    k1, k2 = gerar_subchaves(chave_principal)
    
    ip = permutacao_inicial(bloco)
    
    esquerda, direita = ip[:4], ip[4:]
    
    nova_esquerda, nova_direita = rodada_feistel(esquerda, direita, k1)
    
    esquerda, direita = nova_direita, nova_esquerda
    
    nova_esquerda, nova_direita = rodada_feistel(esquerda, direita, k2)
    
    resultado = nova_esquerda + nova_direita
    
    cifrado = permutacao_inversa(resultado)
    
    return cifrado

# --- Decifração S-DES ---
def decifrar_sdes(cifrado, chave_principal):
    """Decifração S-DES completa (ordem inversa das chaves)"""
    k1, k2 = gerar_subchaves(chave_principal)
    
    ip = permutacao_inicial(cifrado)
    
    esquerda, direita = ip[:4], ip[4:]
    
    nova_esquerda, nova_direita = rodada_feistel(esquerda, direita, k2)
    
    esquerda, direita = nova_direita, nova_esquerda
    
    nova_esquerda, nova_direita = rodada_feistel(esquerda, direita, k1)
    
    resultado = nova_esquerda + nova_direita
    
    decifrado = permutacao_inversa(resultado)
    
    return decifrado

# --- Modo ECB ---
def modo_ECB(mensagem, chave, cifrar=True):
    """Implementação do modo ECB"""
    blocos = mensagem.split()
    if not blocos:
        return ""
        
    resultados = []
    funcao = cifrar_sdes if cifrar else decifrar_sdes
    
    for bloco in blocos:
        resultado = funcao(bloco, chave)
        resultados.append(resultado)
    
    return ' '.join(resultados)

# --- Modo CBC ---
def modo_CBC(mensagem, chave, iv, cifrar=True):
    """Implementação do modo CBC"""
    blocos = mensagem.split()
    if not blocos:
        return ""
    
    resultados = []
    feedback = iv
    funcao = cifrar_sdes if cifrar else decifrar_sdes
    
    for bloco in blocos:
        if cifrar:
            bloco_xor = xor(bloco, feedback)
            cifrado = funcao(bloco_xor, chave)
            resultados.append(cifrado)
            feedback = cifrado
        else:
            decifrado = funcao(bloco, chave)
            bloco_xor = xor(decifrado, feedback)
            resultados.append(bloco_xor)
            feedback = bloco 
    
    return ' '.join(resultados)

# --- Testes ---
if __name__ == "__main__":
    CHAVE = "1010000010"
    BLOCO_TEXTO = "11010111"
    MENSAGEM = "11010111 01101100 10111010 11110000"
    IV = "01010101"

    print("\n" + "="*50)
    print("RESULTADOS FINAIS S-DES")
    print("="*50 + "\n")

    # --- Parte I: Cifração de um bloco com detalhamento ---
    print("\n[PARTE I] CIFRACAO DE UM BLOCO (11010111)")
    
    # Geração de subchaves
    k1, k2 = gerar_subchaves(CHAVE)
    print(f"\n1. GERACAO DE SUBCHAVES:")
    print(f"   Chave principal (10 bits): {CHAVE}")
    print(f"   Subchave K1 (8 bits): {k1}")
    print(f"   Subchave K2 (8 bits): {k2}")

    # Processo de cifração
    ip = permutacao_inicial(BLOCO_TEXTO)
    L0, R0 = ip[:4], ip[4:]
    print(f"\n2. PERMUTACAO INICIAL (IP):")
    print(f"   Bloco original: {BLOCO_TEXTO}")
    print(f"   Apos IP (8 bits): {ip}")
    print(f"   Divisao: L0={L0}, R0={R0}")

    # Rodada 1
    print(f"\n3. RODADA 1 (USANDO K1):")
    ep = expansao_permutacao(R0)
    xor_k1 = xor(ep, k1)
    sbox = s_boxes(xor_k1)
    p4 = permutacao_p4(sbox)
    L1 = xor(L0, p4)
    R1 = R0
    print(f"   E/P(R0): {ep}")
    print(f"   E/P(R0) XOR K1: {xor_k1}")
    print(f"   Saida S-Boxes: {sbox}")
    print(f"   P4: {p4}")
    print(f"   L1 = L0 XOR P4: {L1}")
    print(f"   R1 mantido: {R1}")

    # Troca
    L1, R1 = R1, L1
    print(f"\n4. TROCA DE METADES:")
    print(f"   L1 (apos troca): {L1}")
    print(f"   R1 (apos troca): {R1}")

    # Rodada 2
    print(f"\n5. RODADA 2 (USANDO K2):")
    ep = expansao_permutacao(R1)
    xor_k2 = xor(ep, k2)
    sbox = s_boxes(xor_k2)
    p4 = permutacao_p4(sbox)
    L2 = xor(L1, p4)
    R2 = R1
    print(f"   E/P(R1): {ep}")
    print(f"   E/P(R1) XOR K2: {xor_k2}")
    print(f"   Saida S-Boxes: {sbox}")
    print(f"   P4: {p4}")
    print(f"   L2 = L1 XOR P4: {L2}")
    print(f"   R2 mantido: {R2}")

    # Final
    resultado = L2 + R2
    cifrado = permutacao_inversa(resultado)
    print(f"\n6. PERMUTACAO FINAL (IP-1):")
    print(f"   Antes de IP-1: {resultado}")
    print(f"   Bloco cifrado: {cifrado}")

    # Decifração
    decifrado = decifrar_sdes(cifrado, CHAVE)
    print(f"\n7. DECIFRACAO:")
    print(f"   Bloco decifrado: {decifrado}")
    print(f"   Verificacao: {'DEU CERTO' if BLOCO_TEXTO == decifrado else 'É TRISTE :('}")

    # --- Parte II: Modos de Operação ---
    print("\n\n[PARTE II] MODOS DE OPERACAO")
    
    # ECB
    cifrado_ecb = modo_ECB(MENSAGEM, CHAVE, cifrar=True)
    decifrado_ecb = modo_ECB(cifrado_ecb, CHAVE, cifrar=False)
    print(f"\n1. MODO ECB:")
    print(f"   Mensagem original: {MENSAGEM}")
    print(f"   Texto cifrado:     {cifrado_ecb}")
    print(f"   Texto decifrado:   {decifrado_ecb}")
    print(f"   Verificacao ECB: {'DEU CERTO' if MENSAGEM == decifrado_ecb else 'É TRISTE :('}")

    # CBC
    cifrado_cbc = modo_CBC(MENSAGEM, CHAVE, IV, cifrar=True)
    decifrado_cbc = modo_CBC(cifrado_cbc, CHAVE, IV, cifrar=False)
    print(f"\n2. MODO CBC (IV={IV}):")
    print(f"   Mensagem original: {MENSAGEM}")
    print(f"   Texto cifrado:     {cifrado_cbc}")
    print(f"   Texto decifrado:   {decifrado_cbc}")
    print(f"   Verificacao CBC: {'DEU CERTO' if MENSAGEM == decifrado_cbc else 'É TRISTE :('}")
