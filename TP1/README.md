# Trabalho de Implementação 1 – S-DES (Simplified DES)

Este repositório contém a implementação completa do algoritmo **S-DES (Simplified DES)**, desenvolvido como parte do trabalho da disciplina de Segurança Computacional.

O S-DES é uma versão simplificada do algoritmo DES original, usado para fins educacionais. Ele permite compreender os princípios básicos de cifragem por blocos de forma prática e didática.

## 📚 Sobre o S-DES

O algoritmo utiliza:

- **Chave principal:** 10 bits  
- **Blocos de dados:** 8 bits  
- **Rodadas:** 2 rodadas de Feistel

### ⚙️ Etapas do S-DES

1. **Geração de Subchaves (K1 e K2)**  
   - Permutação P10  
   - Deslocamento circular simples  
   - Permutação P8 → Gera K1  
   - Deslocamento circular duplo  
   - Permutação P8 → Gera K2

2. **Permutação Inicial (IP)**  
   - Reorganiza os bits do bloco antes das rodadas.

3. **Rodadas de Feistel (2 vezes)**  
   - Função F com subchave  
   - XOR com metade esquerda  
   - Troca das metades após a primeira rodada

4. **Permutação Final (IP⁻¹)**  
   - Reorganiza os bits para gerar o bloco final cifrado.

