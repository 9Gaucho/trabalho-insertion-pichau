from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import time
import os


def insertion_sort(produtos):
    for i in range(1, len(produtos)):
        key = produtos[i]
        j = i - 1
        while j >= 0 and key < produtos[j]:
            produtos[j + 1] = produtos[j]
            j -= 1
        produtos[j + 1] = key
    return produtos


def insertion_sort_desc(produtos):
    for i in range(1, len(produtos)):
        key = produtos[i]
        j = i - 1
        while j >= 0 and key > produtos[j]:
            produtos[j + 1] = produtos[j]
            j -= 1
        produtos[j + 1] = key
    return produtos


def manipularPichau():
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)

    driver.get("https://www.pichau.com.br/promocao/bgs")
    time.sleep(3)

    div = driver.find_element(By.CLASS_NAME, "infinite-scroll-component__outerdiv")
    texto = div.text
    valores = re.findall(r"R\$[\s\d.,]+", texto)

    arrayTexto = [valor.strip() for valor in valores]
    valores_sem_reais = [
        float(
            valor.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
        )
        for valor in arrayTexto
    ]
    driver.quit()
    return valores_sem_reais


def menu():
    print("-=" * 20)
    print("1 - Crescente")
    print("2 - Decrescente")
    print("3 - Sair")
    print("-=" * 20)
    opc = int(input("Selecione sua opção: "))
    return opc


def main():
    valores_sem_reais = manipularPichau()
    while True:
        opc = menu()
        if opc == 1:
            time.sleep(3)
            os.system("cls")
            produtos_ordenados = insertion_sort(valores_sem_reais.copy())
            print("Produtos ordenados em ordem crescente:")
            print(produtos_ordenados)
        elif opc == 2:
            time.sleep(3)
            os.system("cls")
            produtos_ordenados_desc = insertion_sort_desc(valores_sem_reais.copy())
            print("Produtos ordenados em ordem decrescente:")
            print(produtos_ordenados_desc)
        elif opc == 3:
            time.sleep(3)
            os.system("cls")
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


main()




======================================================================================================================================================================================================
======================================================================================================================================================================================================
======================================================================================================================================================================================================
======================================================================================================================================================================================================
======================================================================================================================================================================================================





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import time
import os
import tempfile
import heapq


def merge_sort_externo(precos, chunk_size=10):
    temp_files = []

    # Passo 1: Dividir e ordenar os preços
    for i in range(0, len(precos), chunk_size):
        chunk = precos[i:i + chunk_size]
        chunk.sort()  # Ordena a parte
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
        temp_file.writelines(f"{valor}\n" for valor in chunk)
        temp_file.flush()
        temp_files.append(temp_file.name)

    # Passo 2: Mesclar os arquivos temporários
    sorted_file = 'saida_ordenada.txt'
    with open(sorted_file, 'w') as out_file:
        min_heap = []

        for temp_file in temp_files:
            f = open(temp_file, 'r')
            line = f.readline()
            if line:
                heapq.heappush(min_heap, (float(line.strip()), f))

        while min_heap:
            smallest_value, f = heapq.heappop(min_heap)
            out_file.write(f"{smallest_value}\n")
            next_line = f.readline()
            if next_line:
                heapq.heappush(min_heap, (float(next_line.strip()), f))

    # Limpar arquivos temporários
    for temp_file in temp_files:
        os.remove(temp_file)

    return sorted_file


def manipularPichau():
    try:
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.get("https://www.pichau.com.br/promocao/bgs")
        time.sleep(3)

        div = driver.find_element(By.CLASS_NAME, "infinite-scroll-component__outerdiv")
        texto = div.text
        valores = re.findall(r"R\$[\s\d.,]+", texto)

        arrayTexto = [valor.strip() for valor in valores]
        valores_sem_reais = [
            float(valor.replace("R$", "").replace(" ", "").replace(".", "").replace(",", "."))
            for valor in arrayTexto
        ]
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        valores_sem_reais = []
    finally:
        driver.quit()

    return valores_sem_reais


def menu():
    print("-=" * 20)
    print("1 - Ordenar em ordem crescente")
    print("2 - Ordenar em ordem decrescente")
    print("3 - Exibir produtos originais")
    print("4 - Sair")
    print("-=" * 20)
    opc = int(input("Selecione sua opção: "))
    return opc

def main():
    valores_sem_reais = manipularPichau()
    while True:
        opc = menu()
        if opc == 1:
            time.sleep(3)
            os.system("cls")
            produtos_ordenados = insertion_sort(valores_sem_reais.copy())
            print("Produtos ordenados em ordem crescente:")
            print(produtos_ordenados)
        elif opc == 2:
            time.sleep(3)
            os.system("cls")
            produtos_ordenados_desc = insertion_sort_desc(valores_sem_reais.copy())
            print("Produtos ordenados em ordem decrescente:")
            print(produtos_ordenados_desc)
        elif opc == 3:
            time.sleep(3)
            os.system("cls")
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

