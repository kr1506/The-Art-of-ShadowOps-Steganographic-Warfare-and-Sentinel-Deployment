def encipher(message, r):
    a = 'a'
    z = 'z'
    message.lower()
    message.strip()
    message.replace(" ","")
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
    emessage.lower()
    emessage.strip()
    emessage.replace(" ","")
    list_emessage=list(emessage)
    for i in range(len(emessage)):
        ch=list_emessage[i]
        if ch>='a' and ch<='z' :
            ch=chr(ord(ch)-r)
            if ch<'a' :
                ch=chr(ord(ch)+ord(z)-ord(a)+1)
            list_emessage[i]=ch
    return ''.join(list_emessage)

user_input=input("what do you want to do: Encryption=type e,Decryption=type d")
if user_input=='e':
    with open('/mnt/c/Users/KALP/OneDrive/Desktop/input.txt','r') as f:
        f_contents=f.read()
        r=int(input("key:"))
        enciphered_message=encipher(f_contents,r)
        with open('/mnt/c/Users/KALP/OneDrive/Desktop/output.txt','w') as f:
            f.write(enciphered_message)
if user_input=='d':
     with open('/mnt/c/Users/KALP/OneDrive/Desktop/input.txt','r') as f:
        f_contents=f.read()
        r=int(input("key:"))
        deciphered_message=decipher(f_contents,r)
        with open('/mnt/c/Users/KALP/OneDrive/Desktop/output.txt','w') as f:
            f.write(deciphered_message)



