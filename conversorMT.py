import tkinter as tk
from tkinter import filedialog

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
            print(transicoes_possiveis)
            for transicao in transicoes_possiveis:

                fita_n = list(fita)
                print(fita_n)
                fita_n = list(fita)
                fita_n[pos_fita] = transicao[2]
                fita_n = ''.join(fita_n)
                print(fita_n)

                aux = int(pos_fita)
                if transicao[3] == 'l':
                    pos_fita_n = int(aux) - 1 if aux > 0 else 0
                elif transicao[3] == 'r':
                    pos_fita_n = int(aux) + 1
                print(pos_fita_n)

                filho = No(transicao[4])
                print(filho.valor)
                self.adicionar_filho(filho)
                filho.gerar_arvore_recursivamente(transicoes, transicao[4], fita_n, pos_fita_n, profundidade_max, profundidade_atual + 1)
            
    def imprimir_arvore(self, nivel):
        print("  " * nivel + str(self.valor))
        for filho in self.filhos:
            filho.imprimir_arvore(nivel + 1)

maquina_lida = MTND()

def ler_arquivo():
    # Abre a caixa de diálogo para selecionar o arquivo
    filepath = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])

    # Verifica se o usuário selecionou um arquivo
    if filepath:
        # Tenta abrir o arquivo
        try:
            with open(filepath, 'r') as file:
                # Cria um array para armazenar as primeiras palavras únicas
                conjunto_estados = []
                conjunto_estados_finais = []
                transicoes = []

                # Lê as linhas do arquivo, ignorando aquelas que começam com ";" ou são vazias
                for linha in file.readlines():
                    linha = linha.strip()
                    if not linha.startswith(';') and linha:

                        if linha.startswith('!'):
                            fita = linha.split()[1]
                        else:
                            # Adiciona a primeira palavra ao array (se ainda não estiver presente)
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

                            # Checa se o estado de origem da transicao ja foi adicionado ao array, se nao foi a adiciona
                            if estado_origem not in conjunto_estados:
                                conjunto_estados.append(estado_origem)

                            # Checa se o estado de destino da transicao ja foi adicionado ao array, se nao foi a adiciona
                            if estado_destino not in conjunto_estados:
                                conjunto_estados.append(estado_destino)

                            # Checa se o estado de destino da transicao ja foi adicionado ao array, se nao foi a adiciona
                            if estado_destino.startswith("halt") and estado_destino not in conjunto_estados_finais:
                                conjunto_estados_finais.append(estado_destino)
                
                maquina_lida.conjunto_estados = conjunto_estados
                maquina_lida.estado_inicial = estado_inicial
                maquina_lida.conjunto_estados_finais = conjunto_estados_finais
                maquina_lida.transicoes = transicoes
                maquina_lida.fita = fita

                print("Conjunto de estados:")
                print(maquina_lida.conjunto_estados)

                print("Estado inicial:")
                print(maquina_lida.estado_inicial)

                print("Conjunto de estados finais:")
                print(maquina_lida.conjunto_estados_finais)

                print("transicoes:")
                print(maquina_lida.transicoes)

                print("fita:")
                print(maquina_lida.fita)

                raiz = No(maquina_lida.estado_inicial)
                raiz.gerar_arvore_recursivamente(maquina_lida.transicoes, maquina_lida.estado_inicial, maquina_lida.fita, 0, 3, 0)
                raiz.imprimir_arvore(0)
                
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