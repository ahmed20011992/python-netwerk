import math
import random
import zlib

txt1 = 'ABC abc'
byte_arr1 = bytearray(txt1, 'ASCII')
print(len(txt1))
print(len(byte_arr1))
print(byte_arr1[0], byte_arr1[1], byte_arr1[2], byte_arr1[3],
      byte_arr1[4], byte_arr1[5], byte_arr1[6])

txt2 = 'ÅÄÖ'
try:
    byte_arr2 = bytearray(txt2, 'ASCII')
except UnicodeEncodeError as e:
    print(f"Error: {e}")

txt3 = 'ÅÄÖ'
byte_arr3 = bytearray(txt3, 'latin-1')
print([byte_arr3[i] for i in range(len(byte_arr3))])

print(':::::::::!!!!::::::::11111')
txt4 = 'ÅÄÖ'
byte_arr4 = bytearray(txt4, 'utf-8')
print([byte_arr4[i] for i in range(len(byte_arr4))])

try:
    with open('exempeltext.txt', 'r', encoding='utf-8') as file:
        txt = file.read()
except UnicodeDecodeError:
    with open('exempeltext.txt', 'r', encoding='latin-1') as file:
        txt = file.read()

byte_arr_example = bytearray(txt, "utf-8")

print(f"Antal symboler i texten: {len(txt)}")
print(f"Antal byte i byte-array: {len(byte_arr_example)}")


def create_histogram(byte_arr):
    histo = [0] * 256
    for byte in byte_arr:
        histo[byte] += 1
    return histo


def create_probability(histogram):
    total_symbols = sum(histogram)
    prob = [count / total_symbols for count in histogram]
    return prob


def calculate_entropy(prob):
    entropy = -sum(p * math.log2(p) if p > 0 else 0 for p in prob)
    return entropy


histogram_example = create_histogram(byte_arr_example)
prob_distribution_example = create_probability(histogram_example)
entropy_value_example = calculate_entropy(prob_distribution_example)

print(f"Entropi: {entropy_value_example}")
min_bytes_example = entropy_value_example / 8
min_bits_example = entropy_value_example * len(byte_arr_example)
print(f"Minsta antal byte för komprimering: {min_bytes_example}")


shuffled_copy = byte_arr_example.copy()
random.shuffle(shuffled_copy)

assert byte_arr_example == bytearray(
    txt, "utf-8"), "Fel! byte_arr har ändrats felaktigt."

compressed_copy = zlib.compress(shuffled_copy)

len_bytes_copy = len(compressed_copy)
len_bits_copy = len(compressed_copy) * 8

num_symbols_copy = len(shuffled_copy)
bits_per_symbol_copy = len_bits_copy / num_symbols_copy

print(f"Zip-kodens längd i byte för shuffled_copy: {len_bytes_copy}")
print(f"Zip-kodens längd i bitar för shuffled_copy: {len_bits_copy}")
print(f"Antal symboler i shuffled_copy: {num_symbols_copy}")
print(f"Antal bitar per symbol för shuffled_copy: {bits_per_symbol_copy}")


compressed_example = zlib.compress(byte_arr_example)

len_bytes_example = len(compressed_example)
len_bits_example = len(compressed_example) * 8

num_symbols_example = len(byte_arr_example)
bits_per_symbol_example = len_bits_example / num_symbols_example

print(f"Zip-kodens längd i byte för byte_arr_example: {len_bytes_example}")
print(f"Zip-kodens längd i bitar för byte_arr_example: {len_bits_example}")
print(f"Antal symboler i byte_arr_example: {num_symbols_example}")
print(
    f"Antal bitar per symbol för byte_arr_example: {bits_per_symbol_example}")

print(f"Antal bitar per symbol för entropi: {entropy_value_example}")
print(
    f"Antal bitar per symbol för zlib-kodning av shuffled_copy: {bits_per_symbol_copy}")
print(
    f"Antal bitar per symbol för zlib-kodning av byte_arr_example: {bits_per_symbol_example}")


text_t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
text_t10 = 10 * text_t1

compressed_t1 = zlib.compress(bytearray(text_t1, "utf-8"))
compressed_t10 = zlib.compress(bytearray(text_t10, "utf-8"))

len_bytes_t1 = len(compressed_t1)
len_bytes_t10 = len(compressed_t10)

print(f"Antal byte för komprimering av t1: {len_bytes_t1}")
print(f"Antal byte för komprimering av t10: {len_bytes_t10}")

if len_bytes_t10 == 10 * len_bytes_t1:
    print("Ja, zip-koden för t10 är tio gånger längre än zip-koden för t1.")
else:
    print("Nej, det stämmer inte. Varför?")

print(f"Zip-kod för t1: {compressed_t1}")
print(f"Zip-kod för t10: {compressed_t10}")
