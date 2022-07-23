
def addPeso(qtdAnimais):
    """ Função para adicionar o peso separadamente para cada animal. """
    global listaAnimais
    listaAnimais = []
    for animal in range(qtdAnimais):
        peso: float = float(input("Digite o peso do animal: "))
        listaAnimais.append({"cod_animal":animal, "peso":peso})



def areaegmd(areas):
    """ Função para adicionar o gmd para uma área e também adicionar a quantidade animais que a área. """
    global ListaAreas
    ListaAreas = []

    for tamanho in range(areas):
        gmd: float = float(input("Digite o GMD da área: "))
        qtdarea: int = int(input("Digite a quantidade de animais que a área suporta: "))
        ListaAreas.append({"Área":tamanho, "GMD da área":gmd, "Quantidade de animais da área":qtdarea})


def separa_animais(qtdanimais):
    """ Função que separa os animais para uma área e a quantidade de dias que ele vai ficar nessa área . """
    for x in range(qtdanimais):
        animalArea: int = input("Digite o numero do animal e o número da área separados por virgula para separar os animais por área: ")
        qtd_dias: int = int(input("Digite a quantidade de dias que cada animal vai ficar em uma área: "))
        codAnimal, codArea = animalArea.split(",")
        codAnimal, codArea = int(codAnimal), int(codArea)
        listaAnimais[codAnimal-1]["peso"] = listaAnimais[codAnimal-1]["peso"] + ListaAreas[codArea-1]["GMD da área"] * qtd_dias


def getTodosPesos() -> float:
    """ Função para pegar todos os pesos dos animais digitados. """
    pesoTotal = 0

    for animal in listaAnimais:
        pesoTotal = pesoTotal + animal["peso"]

    return pesoTotal


def getPesoEspecifico(codAnimais: int) -> float:
    """ Função para pegar o peso de cada animal espeficadamente. """
    lista_de_pesos = []

    for cod in codAnimais:
        lista_de_pesos.append(listaAnimais[cod-1]["peso"])
    return lista_de_pesos


if __name__ == "__main__":

    # Sessão para os inputs do usuário
    gado: int =  int(input("Digite quantos animais tem: "))
    addPeso(gado)
    areas: int = int(input("Digite quantas áreas tem: "))
    areaegmd(areas)
    separa_animais(gado)
    codigosParaPesagem = input("Digite os códigos dos animais para a pesagem, separados por espaço: ").split()
    codigosParaPesagem = [int(cod) for cod in codigosParaPesagem]

    # Print com as informações pedidas, o peso específico de cada animal e o peso total do peso deles
    print(getPesoEspecifico(codigosParaPesagem))
    print (f"O peso de todos os animais é: {getTodosPesos()}")

