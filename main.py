import readConfig as config
import QRreader
import socketClient as client

conf = config.readFile('./config.json')
host = conf['HOST']
port = int(conf['PORT'])
while True:
    print("Esperando entrada: ")
    data = QRreader.readInput()
    respond = client.sendMessage(host, port, data)
    isValid = respond.split('|')[0].replace("'", "")
    if (isValid == "SI"):
        print("Valid")
    elif (isValid == "NO"):
        print("No valid")
