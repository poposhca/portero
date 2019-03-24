import readConfig as config
import QRreader
import keyBoardReader
import socket

conf = config.readFile('./config.json')
host = conf['HOST']
port = int(conf['PORT'])

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
    try:
        s = socket.socket()
        s.settimeout(3)
        print "Attempting to connect to host, please wait some seconds"
        s.connect((host, port))
        s.send(data)
        respond = s.recv(1024)
        try:
            messages = respond.split('|')
            isValid = messages[0].replace("'", "")
            print messages[1]
            if (isValid == "SI"):
                print("Valid")
            elif (isValid == "NO"):
                print("No valid")
        except:
            print "Data input invalid: %s" % (respond)
    except socket.error, e:
        print "Connection to %s on port %s failed: %s" % (host, port, e)
    finally:
        s.close()
