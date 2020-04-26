"Tento program Vám zašifruje vložený text!"
k = int(input("Jaký je klíč?"))
text = input("Text k zašifrování?")
rozkouskovani = list(text)
i = len(text)
for opakovani in range(i):
    prevod = ord(rozkouskovani[opakovani]) + k
    novy = chr(prevod)
    print(novy, end="")

#pi =
ord("a")
chr(97)

#ci = (pi + k) % 26
