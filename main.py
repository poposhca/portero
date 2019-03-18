import readConfig as config
import QRreader
import keyBoardReader
import socket

conf = config.readFile('./config.json')
host = conf['HOST']
port = int(conf['PORT'])
s = socket.socket()
print "Attempting to connect to %s on port %s" % (host, port)
try:
    s.connect((host, port))
    while True:
        print("Selecciona una opcion:\t1)Codigo QR\n\t2)Teclear codigo")
        keyReader = keyBoardReader.KeyBoardReader()
        key = 0
        while(key != 1 and key != 2):
            key = keyReader.raedInput()
            print(key)
        print "Seleccionaste : " + str(key)
        print("Esperando entrada: ")
        data = QRreader.readInput()
        respond = s.sendall(data)
        try:
            isValid = respond.split('|')[0].replace("'", "")
            if (isValid == "SI"):
                print("Valid")
            elif (isValid == "NO"):
                print("No valid")
        except:
            print "Data input invalid"
except socket.error, e:
    print "Connection to %s on port %s failed: %s" % (host, port, e)
finally:
    s.close()
