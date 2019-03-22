import sys
import codecs

with open(r'input.csv', 'r', encoding="utf-8", errors="ignore") as infile, \
    open(r'output.csv', 'w', encoding="utf-8", errors="ignore") as outfile:
        l=0
        c=0
        d=0
        data = infile.read()
        for line in data:
            l =l+ 1
            for letter in line:
                if ord(letter) > 255:
                    d=d+1
                    print("deleting atrocity")
                    data = data.replace(letter, "")
                    print(l,c,d)

                c=c+ 1
        print("general ! we have killed ",c," atrocity !")
        outfile.write(data)
