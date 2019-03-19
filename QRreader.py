import base64

def readInput():
    line = raw_input()
    line_64 = base64.b64encode(line) + '\n'
    return line_64
