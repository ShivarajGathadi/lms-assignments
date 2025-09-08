a = input()
spl = a.split()
freq = {}
for word in spl:
    freq[word] = freq.get(word,0)+1 
sor = sorted(freq.keys())
for word in sor:
    print(f"{word} :{freq[word]}")