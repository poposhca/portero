import base64

def readInput():
    line = raw_input()
    line_64 = base64.b64encode(line)
    return line_64
