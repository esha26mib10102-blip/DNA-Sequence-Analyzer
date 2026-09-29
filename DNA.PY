print("=================================")
print("      DNA SEQUENCE ANALYZER")
print("=================================")

#Input DNA sequence
sequence = input("Enter DNA sequence: ").upper()

#Set for DNA validation
valid_bases = set("ATGC")

if set(sequence).issubset(valid_bases):
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence")
print("DNA sequence:", sequence)
print("Length:", len(sequence))

print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))

#List: store individual DNA bases
dna_list = list(sequence)
print("DNA as a list:", dna_list)

#Dictionary:count each DNA base
base_count = {
    "A": sequence.count("A"),
    "T": sequence.count("T"),
    "G": sequence.count("G"),
    "C": sequence.count("C")
}
print("Base count:", base_count)

#Set: find unique DNA bases
unique_bases= set(sequence)
print("unique DNA bases:",unique_bases)

#kth element: position analysis
k = int(input("Enter the position (K) of the DNA base you want to find: "))

if 1 <= k <= len(dna_list):
    print("K-th DNA base:", dna_list[k - 1])
else:
    print("Invalid position")

#array partitioning: divide DNA sequence into two parts
mid = len(dna_list) // 2

first_part = dna_list[:mid]
second_part = dna_list[mid:]

print("First part of DNA:", first_part)
print("Second part of DNA:", second_part)

#GC content
gc_count = sequence.count("G") + sequence.count("C")
gc_content = (gc_count / len(sequence)) * 100

print("GC Content:", gc_content, "%")

#complentary DNA sequence
complement = ""

for base in sequence:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

print("Complementary DNA:", complement)

#Reverse DNA sequence
reverse_sequence = sequence[::-1]
print("Reverse DNA:", reverse_sequence)

print("\n======================================")
print("       ANALYSIS COMPLETED")
print("======================================")


    

