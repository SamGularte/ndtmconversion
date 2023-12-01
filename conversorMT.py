import tkinter as tk
from tkinter import filedialog

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
                        # Adiciona a primeira palavra ao array (se ainda não estiver presente)
                        estado_origem = linha.split()[0]
                        charactere_na_fita = linha.split()[1]
                        novo_charactere = linha.split()[2]
                        movimentacao = linha.split()[3]
                        estado_destino = linha.split()[4]

                        nova_transicao = (estado_origem, charactere_na_fita, novo_charactere, movimentacao, estado_destino)

                        if nova_transicao not in transicoes:
                            transicoes.append(nova_transicao)

                        # Checa se o estado de origem da transicao ja foi adicionado ao array, se nao foi a adiciona
                        if estado_origem not in conjunto_estados:
                            conjunto_estados.append(estado_origem)

                        # Checa se o estado de destino da transicao ja foi adicionado ao array, se nao foi a adiciona
                        if estado_destino not in conjunto_estados:
                            conjunto_estados.append(estado_destino)

                        # Checa se o estado de destino da transicao ja foi adicionado ao array, se nao foi a adiciona
                        if estado_destino.startswith("halt") and estado_destino not in conjunto_estados_finais:
                            conjunto_estados_finais.append(estado_destino)

                # Imprime o array no terminal
                print("Conjunto de estados:")
                print(conjunto_estados)

                print("Conjunto de estados finais:")
                print(conjunto_estados_finais)

                print("transicoes:")
                print(transicoes)
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