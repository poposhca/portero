import readConfig as config
import QRreader as reader

data = config.readFile('./config.json')
line = reader.readInput()
print(data)
print("--")
print(line)