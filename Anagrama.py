while True:
    text1= input("Introduce la 1ª palabra: ").upper()
    if not text1.isalpha():
        print("Error: '"+text1+"' no es una cadena alfabetica.")
        break
    else:
        text2 = input("Introduce la 2ª palabra: ").upper()
        if not text2.isalpha():
            print("Error: '"+text2+"' no es una cadena alfabetica.")
            break
for text1 in string1:
   i = find(text1, text2) 
   print (i)
   