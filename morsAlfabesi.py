Morsalfabe={'A': '.-', 'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'R': '.-.',    'S': '...',
        'T': '-',      'U': '..-',    'V': '...-',
        'Y': '-.--',   'Z': '--..',   '.': '.-.-.-'}

def TurkceKarakterCevir(metinB):
    metinB=metinB.replace("Ç","C")
    metinB=metinB.replace("Ş","S")
    metinB=metinB.replace("Ö","O")
    metinB=metinB.replace("Ü","U")
    metinB=metinB.replace("İ","I")
    metinB=metinB.replace("Ğ","G")
    #metinB=metinB.replace(" ",".")
    return  metinB


metin=input("Metin Giriniz:\n")
metinB=metin.upper()
liste=["Ç","ç","Ş","ş","Ö","ö","Ü","ü","ı","İ","Ğ,ğ"]
#morsliste=[i for i in metinB]
morsliste=list()

metinB=(TurkceKarakterCevir(metinB))
print(metinB)
for i in metinB:
    if i == " ":
        morsliste.append(" ")
    else:
        morsliste.append(Morsalfabe[i])

print(morsliste)

dmetin=""
for i in morsliste:
    if i == " ":
        donus= " "
    else:
        donus = list(Morsalfabe.keys())[list(Morsalfabe.values()).index(i)]
    dmetin += donus
#print(donus)
print(dmetin)