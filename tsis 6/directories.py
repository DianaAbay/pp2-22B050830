import os


path = "C:\pp2_22B\pp2-22B050830-1"
print("Only directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files")
print([f for f in os.listdir(path) if
       
print("All files and directories:")
print([fd for fd in os.listdir(path)])


filepath = "C:\pp2_22B\pp2-22B050830-1\tsis 6\\builtin func.py"
print(f'Exist:{os.access(filepath,os.F_OK)}')
print(f'Readable:{os.access(filepath,os.R_OK)}')
print(f'Writable:{os.access(filepath,os.W_OK)}')
print(f'Executable:{os.access(filepath,os.X_OK)}')

if os.access(filepath, os.F_OK):
    print(f'{os.path.basename(filepath)}')
    print(f'{os.path.dirname(filepath)}')

with open("lol.txt", "r") as read:
    for i, j in enumerate(read, 1):
        pass
    print(f'Number of lines in text:{i}')

l = ["I", "am", "doing", "TSIS6"]
with open("lol.txt", "w") as file:
    for i in l:
        file.write("%s " % i)
text = open("lol.txt", "r")
print(text.read())

def generate():
    if not os.path.exists("Letters"):
        os.makedirs("Letters")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in letters:
        with open(i+".txt", "w") as lettertxt:
            lettertxt.writelines(i)

with open("first.txt", "r") as first, open("second.txt", "a") as second:
    for line in first:
        second.write(line)

rpath="C:\pp2_22B\pp2-22B050830-1\tsis 6\\removed.txt"
if os.path.exists(rpath):
    os.remove(rpath)
        
