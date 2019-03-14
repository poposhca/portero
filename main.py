import readConfig as config
import QRreader
import keyBoardReader
import socketClient as client

conf = config.readFile('./config.json')
host = conf['HOST']
port = int(conf['PORT'])
print("Selecciona una opcion:\t1)Codigo QR\n\t2)Teclear codigo")
keyReader = keyBoardReader.KeyBoardReader()
key = 0
while(key != 1 and key != 2):
    key = keyReader.raedInput()
    print(key)
print "Seleccionaste : " + str(key)
while True:
    print("Esperando entrada: ")
    data = QRreader.readInput()
    respond = client.sendMessage(host, port, data)
    isValid = respond.split('|')[0].replace("'", "")
    if (isValid == "SI"):
        print("Valid")
    elif (isValid == "NO"):
        print("No valid")
