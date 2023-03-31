from art import tprint

def greet():
    return print(tprint("Hello World"))



def greets():
    binDict = {
    "0b1000001": "0110000101100011011001010111010001111001011011000110001101101000011011110110110001101001011011100110010101110011011101000110010101110010011000010111001101100101",
    "0b1000010": "0110001001110101011000110110101101101101011010010110111001110011011101000110010101110010011001100111010101101100011011000110010101110010011001010110111001100101",
    "0b1000011": "0110001101101000011011000110111101110010011011110110011001101100011101010110111101110010011011110110110101100101011101000110100001100001011011100110010101110011",
    "0b1000100": "0110010001100101011010010110111001110011011101000110100101110100011101010111010001101001011011110110111001100001011011000110100101111010011010010110111001100111",
    "0b1000101": "0110011001101111011100100110010101110100011010000110111101110101011001110110100001110100011001100111010101101100011011100110010101110011011100110110010101110011",
    "0b1000110": "011001000110100101110011011101000110100101101110011001110111010101101001011100110110100000100000011000010110001001101001011011000110100101110100011010010110010101110011",
    "0b1000111": "011100110111010001110010011000010110100101100111011010000111010001100110011011110111001001110111011000010111001001100100011011100110010101110011011100110110010101110011",
    "0b1001000": "011011010111010101101100011101000110100101100100011010010110110101100101011011100111001101101001011011110110111001100001011011000110100101110100011010010110010101110011",
    "0b1001001": "011010010110110101101101011101010110111001101111011001010110110001100101011000110111010001110010011011110111000001101000011011110111001001100101011101000110100101100011",
    "0b1001010": "011100000110100001101111011101000110111101110000011010000110111101110011011100000110100001101111011100100111100101101100011000010111010001101001011011110110111001110011",
    "0b1001011": "011100000110100001101111011100110111000001101000011011110110011101101100011110010110001101100101011100100110000101101100011001000110010101101000011110010110010001100101",
    "0b1001100": "01110000011100110111100101100011011010000110111101110100011010000110010101110010011000010111000001100101011101010111010001101001011000110110000101101100011011000111100100100001",
    }
    sR = ""
    posRefL = [7,9,7,14,6,11,11,12,16,14,19,21]
    for i in range(65,77):
        sR += binDropper(binDict[binDropper(chr(i))],True)[posRefL[i-65]]
    return sR
        
def binDropper(pL,ship=False):
    if ship:
        return int(pL,2).to_bytes((int(pL,2).bit_length() + 7) // 8, 'big').decode()
    return bin(int.from_bytes(pL.encode(), 'big'))

print(greets())