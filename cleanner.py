import os
import shutil

def organizar_arquivos():
    print("--- ORGANIZADOR DE ARQUIVOS v1.1 ---")

    # 1. ENTRADA DE DADOS
    caminho_origem = input("Digite o caminho da pasta origem: ").strip('"')
    caminho_destino_base = input("Digite o caminho da pasta destino: ").strip('"')

    if not os.path.exists(caminho_origem):
        print("Erro: A pasta de origem não existe.")
        return

    # 2. MAPA DE REGRAS
    regras = {
        ".jpg": "Imagens",
        ".jpeg": "Imagens",
        ".png": "Imagens",
        ".gif": "Imagens",
        ".pdf": "Documentos_PDF",
        ".doc": "Documentos_Word", 
        ".docx": "Documentos_Word",
        ".txt": "Notas_Texto",
        ".csv": "Planilhas_Excel",
        ".xlsx": "Planilhas_Excel",
        ".zip": "Arquivos_Zip",
        ".rar": "Arquivos_Zip",
        ".exe": "Instaladores"
    }

    # Dicionário para guardar o relatório (NOVO)
    # A chave será o nome da pasta e o valor será uma lista de arquivos
    relatorio = {} 

    arquivos_encontrados = os.listdir(caminho_origem)
    contador_movidos = 0

    print(f"\nIniciando organização...\n")

    for arquivo in arquivos_encontrados:
        caminho_completo_origem = os.path.join(caminho_origem, arquivo)

        if os.path.isfile(caminho_completo_origem):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            if extensao in regras:
                nome_pasta_destino = regras[extensao]
                caminho_pasta_final = os.path.join(caminho_destino_base, nome_pasta_destino)

                os.makedirs(caminho_pasta_final, exist_ok=True)
                caminho_final_arquivo = os.path.join(caminho_pasta_final, arquivo)
                
                try:
                    shutil.move(caminho_completo_origem, caminho_final_arquivo)
                    
                    # --- ATUALIZAÇÃO DO RELATÓRIO (NOVO) ---
                    # Se a pasta ainda não está no relatório, cria uma lista vazia para ela
                    if nome_pasta_destino not in relatorio:
                        relatorio[nome_pasta_destino] = []
                    
                    # Adiciona o nome do arquivo na lista dessa pasta
                    relatorio[nome_pasta_destino].append(arquivo)
                    
                    contador_movidos += 1
                    print(f"[OK] Movido: {arquivo}")

                except Exception as e:
                    print(f"[ERRO] Falha ao mover {arquivo}: {e}")

    # 4. EXIBINDO O RELATÓRIO FINAL (NOVO)
    print("\n" + "="*40)
    print("RESUMO DA ORGANIZAÇÃO")
    print("="*40)

    if contador_movidos == 0:
        print("Nenhum arquivo precisou ser movido.")
    else:
        # Loop para mostrar Pasta -> Arquivos que foram para ela
        for pasta, lista_arquivos in relatorio.items():
            print(f"\n📂 Pasta criada/usada: '{pasta}'")
            print(f"   Arquivos movidos ({len(lista_arquivos)}):")
            for item in lista_arquivos:
                print(f"   - {item}")

    print("\n" + "="*40)
    print(f"Total geral: {contador_movidos} arquivos organizados.")

if __name__ == "__main__":
    organizar_arquivos()