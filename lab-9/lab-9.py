
import math
import random
import zlib


# 1.1
txt = 'ABC abc'
b = bytearray(txt, 'ASCII')
print(len(txt))
print(len(b))
print(b[0], b[1], b[2], b[3], b[4], b[5], b[6])


# 1.2

txt_swedish = 'ÅÄÖ'
try:
    b_swedish = bytearray(txt_swedish, 'ASCII')
except UnicodeEncodeError as e:
    print(f"Error: {e}")
# 1.3
txt_latin1 = 'ÅÄÖ'
b_latin1 = bytearray(txt_latin1, 'latin-1')
print([b_latin1[i] for i in range(len(b_latin1))])

# 1.4
print(':::::::::!!!!::::::::11111')
txt_utf8 = 'ÅÄÖ'
b_utf8 = bytearray(txt_utf8, 'utf-8')
print([b_utf8[i] for i in range(len(b_utf8))])


# 1.a,b,c
# Läs innehållet i filen exempeltext.txt, skapa en byte-array med utf-8 encoding

try:
    with open('exempeltext.txt', 'r', encoding='utf-8') as file:
        txt = file.read()
except UnicodeDecodeError:
    # Om UTF-8 misslyckas, försök med 'latin-1'
    with open('exempeltext.txt', 'r', encoding='latin-1') as file:
        txt = file.read()

byteArr = bytearray(txt, "utf-8")

print(f"Antal symboler i texten: {len(txt)}")
print(f"Antal byte i byte-array: {len(byteArr)}")


# 2.a
def makeHisto(byteArr):
    # En lista med 256 platser för att räkna varje möjligt värde
    histo = [0] * 256
    for byte in byteArr:
        histo[byte] += 1
    return histo
# 2.b


def makeProb(histo):
    total_symbols = sum(histo)
    prob = [count / total_symbols for count in histo]
    return prob
# 2.c


def entropi(prob):
    entropy = -sum(p * math.log2(p) if p > 0 else 0 for p in prob)
    return entropy


# 2.d
histogram = makeHisto(byteArr)
probability_distribution = makeProb(histogram)
entropy_value = entropi(probability_distribution)
print(f"Entropi: {entropy_value}")
min_bytes = entropy_value / 8
min_bits = entropy_value * len(byteArr)
print(f"Minsta antal byte för komprimering: {min_bytes}")


# 3.b
# Kopiera byteArr
theCopy = byteArr.copy()

# Blanda kopien med random.shuffle
random.shuffle(theCopy)

# 3.c
# Kontrollera att byteArr inte har ändrats
assert byteArr == bytearray(
    txt, "utf-8"), "Fel! byteArr har ändrats felaktigt."

# 4.b
compressed_copy = zlib.compress(theCopy)

# 4.c
len_in_bytes_copy = len(compressed_copy)
len_in_bits_copy = len(compressed_copy) * 8  # Eftersom varje byte har 8 bitar

# Räkna antalet symboler i theCopy
num_symbols_copy = len(theCopy)
bits_per_symbol_copy = len_in_bits_copy / num_symbols_copy

print(f"Zip-kodens längd i byte för theCopy: {len_in_bytes_copy}")
print(f"Zip-kodens längd i bitar för theCopy: {len_in_bits_copy}")
print(f"Antal symboler i theCopy: {num_symbols_copy}")
print(f"Antal bitar per symbol för theCopy: {bits_per_symbol_copy}")


# 4.d

compressed_arr = zlib.compress(byteArr)

len_in_bytes_arr = len(compressed_arr)
len_in_bits_arr = len(compressed_arr) * 8

# Räkna antalet symboler i byteArr
num_symbols_arr = len(byteArr)
bits_per_symbol_arr = len_in_bits_arr / num_symbols_arr

print(f"Zip-kodens längd i byte för byteArr: {len_in_bytes_arr}")
print(f"Zip-kodens längd i bitar för byteArr: {len_in_bits_arr}")
print(f"Antal symboler i byteArr: {num_symbols_arr}")
print(f"Antal bitar per symbol för byteArr: {bits_per_symbol_arr}")

# 4.e
print(f"Antal bitar per symbol för entropi: {entropy_value}")
print(
    f"Antal bitar per symbol för zlib-kodning av theCopy: {bits_per_symbol_copy}")
print(
    f"Antal bitar per symbol för zlib-kodning av byteArr: {bits_per_symbol_arr}")


# 5.a
t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
t10 = 10 * t1

# 5.b
compressed_t1 = zlib.compress(bytearray(t1, "utf-8"))
compressed_t10 = zlib.compress(bytearray(t10, "utf-8"))

# Räkna antalet byte för varje komprimerad sträng
len_in_bytes_t1 = len(compressed_t1)
len_in_bytes_t10 = len(compressed_t10)

print(f"Antal byte för komprimering av t1: {len_in_bytes_t1}")
print(f"Antal byte för komprimering av t10: {len_in_bytes_t10}")


# 5.c
# (c)
print(f"Är zip-koden för t10 tio gånger längre än zip-koden för t1?")
if len_in_bytes_t10 == 10 * len_in_bytes_t1:
    print("Ja, zip-koden för t10 är tio gånger längre än zip-koden för t1.")
else:
    print("Nej, det stämmer inte. Varför?")


print(f"Zip-kod för t1: {compressed_t1}")
print(f"Zip-kod för t10: {compressed_t10}")
