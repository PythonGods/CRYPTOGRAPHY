import sys 
while(1):
    print("What do you want to do?")
    x=input()

    if x=="encrypt":
    
        def encrypter(string, shift):   
            ciper=""
            for char in string:
                if char=='':
                    ciper=ciper+ciper
                elif char.isupper():
                    ciper=ciper+chr((ord(char)+shift-65)%26+65)
                else:
                    ciper=ciper+chr((ord(char)+shift-97)%26+97)
            return ciper   
        text=input("Enter text ")
        print("Enter a key")
        sec_key=int(input())
        print("The encrypted message is:",encrypter(text, sec_key))

    if x=="decrypt":
    
        def decrypter(string, shift):   
            ciper=""
            for char in string:
                if char=='':
                    ciper=ciper+ciper
                elif char.isupper():
                    ciper=ciper+chr((ord(char)+shift-65)%26+65)
                else:
                    ciper=ciper+chr((ord(char)+shift-97)%26+97)
            return ciper   
        text=input("Enter text ")
        print("Enter a key")
        sec_key=int(input())
        sec_key= -sec_key
        print("The decrypted message is:",decrypter(text, sec_key))
    if x=="exit":
        sys.exit()
    