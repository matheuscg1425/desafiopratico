# 1
def exercicio_1():
    lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

    somas = [sum(sublista) for sublista in lista_de_listas]
    print("Exercício 1 - Somatório de cada lista:", somas)


# 2
def exercicio_2():
    lista_de_tuplas = [
        ("Pedro", 1.74, 81),
        ("Júlia", 1.65, 67),
        ("Otávio", 1.81, 83),
    ]

    terceiros_elementos = [t[2] for t in lista_de_tuplas]
    print("Exercício 2 - Terceiro elemento de cada tupla:", terceiros_elementos)


# 3
def exercicio_3():
    lista = ["Pedro", "Júlia", "Otávio", "Eduardo"]

    lista_de_tuplas = [(i, nome) for i, nome in enumerate(lista)]
    print("Exercício 3 - Lista de tuplas (posição, nome):", lista_de_tuplas)


# 4
def exercicio_4():
    aluguel = [
        ("Apartamento", 1700),
        ("Apartamento", 1400),
        ("Casa", 2150),
        ("Apartamento", 1900),
        ("Casa", 1100),
    ]

    valores_apartamento = [
        valor for tipo, valor in aluguel if tipo == "Apartamento"
    ]
    print("Exercício 4 - Valores de aluguel apenas de Apartamento:", valores_apartamento)


# 5
def exercicio_5():
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
             "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    despesa = [860, 490, 1010, 780, 900, 630,
               590, 770, 620, 560, 840, 360]


    despesas_por_mes = {mes: valor for mes, valor in zip(meses, despesa)}
    print("Exercício 5 - Dicionário de despesas por mês:", despesas_por_mes)


# 6
def exercicio_6():
    vendas = [
        ("2023", 4093), ("2021", 4320), ("2021", 5959),
        ("2022", 8883), ("2023", 9859), ("2022", 5141),
        ("2022", 7688), ("2022", 9544), ("2023", 4794),
        ("2021", 7178), ("2022", 3030), ("2021", 7471),
        ("2022", 4226), ("2022", 8190), ("2021", 9680),
        ("2022", 5616),
    ]


    vendas_filtradas = [
        (ano, valor) for ano, valor in vendas
        if ano == "2022" and valor > 6000
    ]
    print("Exercício 6 - Vendas de 2022 com valor > 6000:", vendas_filtradas)


# 7
def rotulo_glicemia(valor: int) -> str:
    """
    Glicose:
    - <= 70: 'Hipoglicemia'
    - 70 < valor <= 99: 'Normal'
    - 100 a 125: 'Alterada'
    - > 125: 'Diabetes'
    """
    if valor <= 70:
        return "Hipoglicemia"
    elif valor <= 99:
        return "Normal"
    elif valor <= 125:
        return "Alterada"
    else:
        return "Diabetes"


def exercicio_7():
    glicemia = [
        129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92,
        66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73,
    ]


    rotulos = [(rotulo_glicemia(valor), valor) for valor in glicemia]
    print("Exercício 7 - Rótulos de glicemia (rótulo, valor):", rotulos)


# 8
def exercicio_8():
    ids = list(range(10))
    quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
    preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

    cabecalho = ("id", "quantidade", "preco", "total")


    corpo_tabela = [
        (i, q, p, q * p)
        for i, q, p in zip(ids, quantidade, preco)
    ]

    tabela = [cabecalho] + corpo_tabela

    print("Exercício 8 - Tabela de vendas (primeira linha é o cabeçalho):")
    for linha in tabela:
        print(linha)


# 9
def exercicio_9():
    estados = [
        "SP", "ES", "MG", "MG", "SP", "MG", "ES", "ES", "ES",
        "SP", "SP", "MG", "ES", "SP", "RJ", "MG", "RJ", "SP",
        "MG", "SP", "ES", "SP", "MG",
    ]


    listas_por_estado = [
        [e for e in estados if e == uf_unico]
        for uf_unico in set(estados)
    ]

    contagem_estados_exemplo = {
        uf_lista[0]: len(uf_lista)
        for uf_lista in listas_por_estado
    }


    contagem_estados = {
        uf: estados.count(uf) for uf in set(estados)
    }

    print("Exercício 9 - Contagem de filiais por Estado (forma direta):", contagem_estados)
    print("Exercício 9 - Contagem usando passo intermediário (exemplo):", contagem_estados_exemplo)


# 10
def exercicio_10():
    funcionarios = [
        ("SP", 16), ("ES", 8), ("MG", 9), ("MG", 6), ("SP", 10),
        ("MG", 4), ("ES", 9), ("ES", 7), ("ES", 12), ("SP", 7),
        ("SP", 11), ("MG", 8), ("ES", 8), ("SP", 9), ("RJ", 13),
        ("MG", 5), ("RJ", 9), ("SP", 12), ("MG", 10), ("SP", 7),
        ("ES", 14), ("SP", 10), ("MG", 12),
    ]

    estados_unicos = {uf for uf, _ in funcionarios}


    colaboradores_por_estado = {
        uf: [qtd for estado, qtd in funcionarios if estado == uf]
        for uf in estados_unicos
    }


    soma_colaboradores_por_estado = {
        uf: sum(qtds)
        for uf, qtds in colaboradores_por_estado.items()
    }

    print("Exercício 10 - Listas de colaboradores por Estado:", colaboradores_por_estado)
    print("Exercício 10 - Soma de colaboradores por Estado:", soma_colaboradores_por_estado)


if __name__ == "__main__":
    exercicio_1()
    print("-" * 80)
    exercicio_2()
    print("-" * 80)
    exercicio_3()
    print("-" * 80)
    exercicio_4()
    print("-" * 80)
    exercicio_5()
    print("-" * 80)
    exercicio_6()
    print("-" * 80)
    exercicio_7()
    print("-" * 80)
    exercicio_8()
    print("-" * 80)
    exercicio_9()
    print("-" * 80)
    exercicio_10()
