import re

#Return a list containing every occurrence of "ai":

procVariaveis = r"(([ ]*[\w+]*[ ]*[,][ ]*)*[\w+]+[ ]*[:][ ]*)"
#txt = "i , j , n , lin , col , linhas ,  colunas : integer ;"
txt = "var i , j : integer ;"

x = re.findall(procVariaveis, txt)
k=re.search(procVariaveis, txt)
if re.search(procVariaveis, txt)!= None:
    res=k.group().split()

#print(res)
for item in res:
    #if item!=','and item!=':':
    print(item)