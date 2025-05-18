import json

def abrirJSON():
    dicFinal=[]
    with open("./db/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./db/datos.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs():
    dicFinal=[]
    with open("./db/logs.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def logsJSON(dic):
    dicTemporal = []
    #print("Diccionario Importado LOGS")
    
    dicTemporal=cargarLogs()
    #print(dicTemporal)
    dicTemporal.append(dic)
    with open("./db/logs.json",'w') as outFile:
        json.dump(dicTemporal,outFile)