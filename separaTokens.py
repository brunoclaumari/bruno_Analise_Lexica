import re

pascal_code = ""
pascal_keys = ""
pascal_datatype = ""
pascal_operators = ""
pascal_separators = ""


with open('p6.pas', "r") as pkeys2:
    pascal_code = pkeys2.read().lower().splitlines()

with open('pascal_keys.txt', "r") as pkeys:
    pascal_keys = pkeys.read().lower().split()

with open('pascal_datatype.txt', "r") as pkeys:
    pascal_datatype = pkeys.read().lower().split()

with open('pascal_operators.txt', "r") as pkeys:
    pascal_operators = pkeys.read().lower().split()

with open('pascal_separators.txt', "r") as pkeys:
    pascal_separators = pkeys.read().lower().split()

lexemas = []

# expressões regulares
integerPattern = r"^([ ]?[+/-]?[0-9]+[;]?)$"
realPattern = r"^([ ]?[+/-]?[0-9]+[.][0-9]*[[E/e]?[+/-]?[0-9]+]?[ ]*[;]?)|([ ]?[+/-]?[0-9]*[.][0-9]+[ ]*[;]?)$"


testandoPascal = []


for linhas in pascal_code:
    testandoPascal.append(linhas.lstrip().splitlines())

pascalCortado = []

#coloca espaços entre os caracteres para facilitar 
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


testandoPascal.clear()

listaTestandoPegaVariavel=[]

#passa pelo vetor, quebra os espaços e depois elimina as strings vazias
for item in pascalCortado:
    teste = item.casefold().strip().split(' ')
    aux = []
    for indiv in teste:      
        if indiv != '':
            aux.append(indiv)
    testandoPascal.append(aux)
 
decVariavel = False
abrestring = False
listaVariaveis = []
listaProcedures = []
listaFunctions = []
#abreFechaParenteses = ['(', ')']
abreFechaComents = ['{', '}']
#abreFechaPosVetor = ['[', ']']

#identificação dos tokens
for itens in testandoPascal:
    lAux = []
    lAux = itens
    
    if abreFechaComents[0] in lAux:  # tira os comentários
        inic = lAux.index(abreFechaComents[0])
        finn = lAux.index(abreFechaComents[1])
        while inic <= finn:
            lAux[inic] = ''
            inic += 1

    #identifica o que é variável de function e adiciona na lista de variáveis
    if lAux[0] == 'function':
        listaFunctions.append(lAux[1])
        inicioDec = lAux.index('(')
        fimDec = lAux.index(')')

        aux = inicioDec
        while aux < fimDec:            
            if lAux[aux] == ':':  
                refIndex=aux              
                listaVariaveis.append(lAux[aux-1])
                while lAux[refIndex-2]==',':
                    listaVariaveis.append(lAux[refIndex-3]) 
                    refIndex-=2
            aux += 1

    #identifica o que é variável de procedure e adiciona na lista de variáveis
    elif lAux[0] == 'procedure':
        listaProcedures.append(lAux[1])
        inicioDec = lAux.index('(')
        fimDec = lAux.index(')')

        aux = inicioDec
        while aux < fimDec:            
            if lAux[aux] == ':':
                refIndex=aux
                listaVariaveis.append(lAux[aux-1])
                while lAux[refIndex-2]==',':
                    listaVariaveis.append(lAux[refIndex-3]) 
                    refIndex-=2
            aux += 1

    #separa o que é variável e adiciona na lista de variáveis    
    elif ':' in lAux or lAux[0] == 'var':
        
        if len(lAux) > 1:
            indice = lAux.index(':')
            aux = 1
            while aux < indice:
                listaVariaveis.append(lAux[aux])
                aux += 2
        else:
            aux = 0
        while aux < len(lAux):
            if lAux[aux] == ':' and lAux[aux+1] in pascal_datatype and not lAux[aux-1] in listaVariaveis:
                listaVariaveis.append(lAux[aux-1])
            aux += 1
           
    #
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
        elif token in listaVariaveis:
            lexemas.append([token, "variable"])
        elif token in listaFunctions:
            lexemas.append([token, "function name"])
        elif token in listaProcedures:
            lexemas.append([token, "procedure name"])
        elif token == '':
            continue
        else:
            lexemas.append([token, "unknow"])

#mostra na tela o que vai para o arquivo tokens
for woou in lexemas:
    print(woou)

#escreve os tokens no arquivo
with open("tokens.txt", "w") as lexemas_text:
    lexemas_text.write(str(lexemas)+"\n")

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
