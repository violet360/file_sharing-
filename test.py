import os
import sys
print(int(os.path.getsize("Capture1.png"))+1)
print(os.path.isfile('hello.txt'))
z = 1
with open("voice.MP3", "rb") as f:
    byte = f.read(1024)
    while byte:
        # Do stuff with byte.
        byte = f.read(1024)
        z+=1
        print((sys.getsizeof(byte)), f".............{z}...........")

