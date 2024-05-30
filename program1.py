def encipher(message, r):
    a = 'a'  
    z = 'z'  
    list_message = list(message)
    for i in range(len(message)):
        ch = list_message[i]
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) + r)
            if ch > 'z':
                ch = chr(ord(ch) - ord(z) + ord(a) - 1)  
            list_message[i] = ch
    return ''.join(list_message)
def decipher(emessage,r):
    a = 'a'
    z = 'z'
    list_emessage=list(emessage)
    for i in range(len(emessage)):
        ch=list_emessage[i]
        if ch>='a' and ch<='z' :
            ch=chr(ord(ch)-r)
            if ch<='a' :
                ch=chr(ord(ch)+ord(z)-ord(a)+1)
            list_emessage[i]=ch
    return ''.join(list_emessage)

user_input=input("what do you want to do: Encryption=type e,Decryption=type d")
if user_input=='e':
    message=input("enter message :")
    r = 3
    enciphered_message = encipher(message, r)
    print(enciphered_message)
    print(len(enciphered_message))
if user_input=='d':
    emessage=input("enter emessage :")
    r = 3
    deciphered_message = decipher(emessage, r)
    print(deciphered_message)
    print(len(deciphered_message))


