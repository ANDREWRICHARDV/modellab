def ceaser_cipher(text,shift):
    return''.join(chr((ord (c)-(offset,ord("A"))if c.isupper()else ord("a")+shift)%26+offset)if c.isalpha() else c for c in text)
text=input("text:")
shift=int(input("shift:"))
print("answer:",ceaser_cipher(text,shift))