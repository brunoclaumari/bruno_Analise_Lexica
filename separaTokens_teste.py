import re

pascal_code = ""
pascal_keys = ""
pascal_datatype = ""
pascal_operators = ""
pascal_separators = ""

#aqui vc lê o programa pascal que quer tratar
with open('p3.pas', "r") as pkeys2:
    pascal_code = pkeys2.read().lower().splitlines()

#adiciona as palavras reservadas do pascal em uma variável
with open('pascal_keys.txt', "r") as pkeys:
    pascal_keys = pkeys.read().lower().split()

#adiciona os tipos do pascal em uma variável
with open('pascal_datatype.txt', "r") as pkeys:
    pascal_datatype = pkeys.read().lower().split()

#adiciona os operadores do pascal em uma variável
with open('pascal_operators.txt', "r") as pkeys:
    pascal_operators = pkeys.read().lower().split()

#adiciona os separadores do pascal em uma variável
with open('pascal_separators.txt', "r") as pkeys:
    pascal_separators = pkeys.read().lower().split()

lexemas = []

# expressões regulares
integerPattern = r"^([ ]?[+/-]?[0-9]+[;]?)$"
realPattern = r"^([ ]?[+/-]?[0-9]+[.][0-9]*[[E/e]?[+/-]?[0-9]+]?[ ]*[;]?)|([ ]?[+/-]?[0-9]*[.][0-9]+[ ]*[;]?)$"
procVariaveis = r"(([\w+]*[ ]*[,][ ]*)*[\w+]+[ ]*[:][ ]*)"

testandoPascal = []

for linhas in pascal_code:
    testandoPascal.append(linhas.lstrip().splitlines())

pascalCortado = []

# coloca espaços entre os caracteres para facilitar
for linhas in testandoPascal:
    aux = ""
    for lt in linhas:
        if ':=' in lt:
            pascalCortado.append(lt.casefold()
                                 .replace('(', ' ( ')
                                 .replace(')', ' ) ')
                                 .replace('{', ' { ')
                                 .replace('}', ' } ')
                                 .replace('[', ' [ ')
                                 .replace(']', ' ] ')
                                 .replace("'", " ' ")
                                 .replace(',', ' , ')
                                 .replace(':=', ' := ')
                                 .replace('*', ' * ')
                                 .replace('+', ' + ')
                                 .replace('/', ' / ')
                                 .replace('-', ' - ')
                                 .replace(';', ' ;'))
        else:
            pascalCortado.append(lt.casefold()
                                 .replace('(', ' ( ')
                                 .replace(')', ' ) ')
                                 .replace('{', ' { ')
                                 .replace('}', ' } ')
                                 .replace('[', ' [ ')
                                 .replace(']', ' ] ')
                                 .replace("'", " ' ")
                                 .replace(',', ' , ')
                                 .replace(':', ' : ')
                                 .replace('.', ' . ')
                                 .replace('*', ' * ')
                                 .replace('+', ' + ')
                                 .replace('/', ' / ')
                                 .replace('-', ' - ')
                                 .replace(';', ' ;'))

decVariavel = False
abrestring = False
listaVariaveis = []
listaProcedures = []
listaFunctions = []
abreFechaParenteses = ['(', ')']
abreFechaComents = ['{', '}']
#abreFechaPosVetor = ['[', ']']
abreComentario = False
fechaComentario = False


testandoPascal.clear()

listaTestandoPegaVariavel = []

# passa pelo vetor, quebra os espaços, procura variaveis para adicionar
# na lista de variaveis e depois elimina as strings vazias
for item in pascalCortado:
    
    if re.search(procVariaveis, item)!= None and ':=' not in item and '(' not in item:
        k=re.search(procVariaveis, item).group()
        res=k.split()
        
        for palav in res:
            if palav!=','and palav!=':':                
                listaVariaveis.append(palav)
                

    teste = item.casefold().strip().split(' ')
    aux = []
    for indiv in teste:
        if indiv != '':
            aux.append(indiv)
    testandoPascal.append(aux)


inic = 0
finn = 0
# identificação dos tokens
for itens in testandoPascal:
    lAux = []
    lAux = itens
    # print(itens)

    # tira os comentários
    if abreFechaComents[0] in lAux:
        abreComentario = True
    else:
        abreComentario = False
    if abreFechaComents[1] in lAux:
        fechaComentario = True
    else:
        fechaComentario = False
    if abreComentario and fechaComentario:
        inic = lAux.index(abreFechaComents[0])
        finn = lAux.index(abreFechaComents[1])
        while inic <= finn:

            lAux[inic] = ''
            inic += 1
    elif abreComentario and not fechaComentario:
        inic = lAux.index(abreFechaComents[0])
        finn = len(lAux)-1-inic
        while inic <= finn:
            lAux[inic] = ''
            inic += 1
    elif not abreComentario and fechaComentario:
        inic = 0
        finn = lAux.index(abreFechaComents[1])
        while inic <= finn:
            lAux[inic] = ''
            inic += 1

   

    # identifica o que é variável de function e adiciona na lista de variáveis
    if lAux[0] == 'function':
        listaFunctions.append(lAux[1])
        if '(' in lAux and ')' in lAux:
            inicioDec = lAux.index('(')
            fimDec = lAux.index(')')

            aux = inicioDec
            while aux < fimDec:
                if lAux[aux] == ':':
                    refIndex = aux
                    listaVariaveis.append(lAux[aux-1])
                    while lAux[refIndex-2] == ',':
                        listaVariaveis.append(lAux[refIndex-3])
                        refIndex -= 2
                aux += 1

    # identifica o que é variável de procedure e adiciona na lista de variáveis
    elif lAux[0] == 'procedure':
        listaProcedures.append(lAux[1])
        if '(' in lAux and ')' in lAux:
            inicioDec = lAux.index('(')
            fimDec = lAux.index(')')

            aux = inicioDec
            while aux < fimDec:
                if lAux[aux] == ':':
                    refIndex = aux
                    listaVariaveis.append(lAux[aux-1])
                    while lAux[refIndex-2] == ',':
                        listaVariaveis.append(lAux[refIndex-3])
                        refIndex -= 2
                aux += 1


    #passa por cada item separando os tokens
    for token in itens:
        if token in pascal_keys:
            lexemas.append([token, "key word"])
        elif token in pascal_datatype:
            lexemas.append([token, "datatype"])
        elif token in pascal_operators:
            lexemas.append([token, "operator"])
        elif token in pascal_separators:
            lexemas.append([token, "separator"])
        elif re.match(integerPattern, token):
            lexemas.append([token, "integer"])
        elif re.match(realPattern, token):
            lexemas.append([token, "real"])        
        elif token in listaFunctions:
            lexemas.append([token, "function name"])
        elif token in listaProcedures:
            lexemas.append([token, "procedure name"])
        elif token in listaVariaveis:
            lexemas.append([token, "variable"])    
        elif token == '':
            continue
        else:
            lexemas.append([token, "unknow"])

# mostra na tela o que vai para o arquivo tokens
for woou in lexemas:
    print(woou)

# escreve os tokens no arquivo
with open("tokens.txt", "w") as lexemas_text:
    for woou in lexemas:
        lexemas_text.write(str(woou))
        lexemas_text.write('\n')
        






#DICAS DO PROFESSOR
# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping

# TODO: Terminar...
