import tkinter as tk
from tkinter import filedialog
from collections import deque

class MTND:
    def __init__(self):
        self.conjunto_estados = []
        self.conjunto_estados_finais = []
        self.transicoes = []
        self.fita = None
        self.estado_inicial = None

class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def gerar_arvore_recursivamente(self, transicoes, estado_atual, fita, pos_fita, profundidade_max, profundidade_atual):
        if profundidade_atual < profundidade_max:
            transicoes_possiveis = [transicao for transicao in transicoes if transicao[0] == estado_atual and transicao[1] == fita[pos_fita]]
            for transicao in transicoes_possiveis:

                fita_n = list(fita)
                fita_n = list(fita)
                fita_n[pos_fita] = transicao[2]
                fita_n = ''.join(fita_n)

                aux = int(pos_fita)
                if transicao[3] == 'l':
                    if aux > 0:
                        pos_fita_n = int(aux) - 1
                    else:
                        pos_fita_n = 0
                elif transicao[3] == 'r':
                    if aux < len(fita_n):
                        pos_fita_n = int(aux) + 1
                    else:
                        pos_fita_n = len(fita_n) - 1
                else:
                    pos_fita_n = aux

                filho = No(transicao[4])
                self.adicionar_filho(filho)
                filho.gerar_arvore_recursivamente(transicoes, transicao[4], fita_n, pos_fita_n, profundidade_max, profundidade_atual + 1)
            
    def imprimir_arvore(self, nivel):
        print("  " * nivel + str(self.valor))
        for filho in self.filhos:
            filho.imprimir_arvore(nivel + 1)

def chave_de_ordenacao(tupla):
    return (tupla[0], tupla[1], tupla[4])

def busca_em_largura(raiz):
    fila = deque([(raiz, [])])

    while fila:
        no_atual, caminho_atual = fila.popleft()
        caminho_atual = caminho_atual + [no_atual.valor]

        if no_atual.valor.startswith("halt"):
            return caminho_atual

        fila.extend((filho, caminho_atual) for filho in no_atual.filhos)

    return

maquina_lida = MTND()

def ler_arquivo():
    filepath = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])

    if filepath:
        try:
            with open(filepath, 'r') as file:
                conjunto_estados = []
                conjunto_estados_finais = []
                transicoes = []
                transicoes_fita_2 = []
                fita_2 = []

                for linha in file.readlines():
                    linha = linha.strip()
                    if not linha.startswith(';') and linha:

                        if linha.startswith('!'):
                            fita = linha.split()[1]
                        else:
                            estado_origem = linha.split()[0]
                            charactere_na_fita = linha.split()[1]
                            novo_charactere = linha.split()[2]
                            movimentacao = linha.split()[3]
                            estado_destino = linha.split()[4]

                            nova_transicao = (estado_origem, charactere_na_fita, novo_charactere, movimentacao, estado_destino)

                            if nova_transicao not in transicoes:
                                transicoes.append(nova_transicao)

                            if estado_origem == "0":
                                estado_inicial = estado_origem

                            if estado_origem not in conjunto_estados:
                                conjunto_estados.append(estado_origem)

                            if estado_destino not in conjunto_estados:
                                conjunto_estados.append(estado_destino)

                            if estado_destino.startswith("halt") and estado_destino not in conjunto_estados_finais:
                                conjunto_estados_finais.append(estado_destino)
                
                maquina_lida.conjunto_estados = sorted(conjunto_estados)
                maquina_lida.estado_inicial = estado_inicial
                maquina_lida.conjunto_estados_finais = conjunto_estados_finais
                maquina_lida.transicoes = sorted(transicoes, key=chave_de_ordenacao)
                maquina_lida.fita = fita

                for estado in maquina_lida.conjunto_estados:
                    transicoes_possiveis = [transicao for transicao in transicoes if transicao[0] == estado]

                    if len(transicoes_possiveis) == 1:
                        n_tupla = (estado, '1', '_', 'r', transicoes_possiveis[0][-1])
                        transicoes_fita_2.append(n_tupla)
                    elif len(transicoes_possiveis) > 1:
                        for indice, transicao in enumerate(transicoes_possiveis):
                           n_tupla = (estado, indice + 1, '_', 'r', transicao[4]) 
                           transicoes_fita_2.append(n_tupla)

                raiz = No(maquina_lida.estado_inicial)
                raiz.gerar_arvore_recursivamente(maquina_lida.transicoes, maquina_lida.estado_inicial, maquina_lida.fita, 0, 20, 0)
                caminho = busca_em_largura(raiz)

                for i in range(len(caminho) - 1):
                    atual_estado = caminho[i]
                    prox_estado = caminho[i + 1]
                    
                    for transicao in transicoes_fita_2:
                        if transicao[0] == atual_estado and transicao[4] == prox_estado:
                            fita_2.append(transicao[1])
                
                fita_2 = ''.join(map(str,fita_2))
                print(fita_2)

                print(caminho)
                
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
    else:
        print("Nenhum arquivo selecionado")

# Cria a janela principal
root = tk.Tk()
root.title("Leitor de Arquivo .txt")

# Define a largura e altura da janela
largura = 200
altura = 200
resolucao_tela = f"{largura}x{altura}"
root.geometry(resolucao_tela)

# Cria um botão para selecionar o arquivo
btn_selecionar_arquivo = tk.Button(root, text="Selecionar Arquivo", command=ler_arquivo)
btn_selecionar_arquivo.pack(pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()