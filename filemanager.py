import os

def create(filename,content=""):
    try:
        with open(filename, 'x') as file: 
            file.write(content)
        print(f"File '{filename}' created.")
        print("Successful")
 
    except Exception:
        print("File already exists")

def delete(filename):
    try:
        os.remove(filename)
    except Exception:
        print("file doresnt exist")


def read(filename):
    try: 
        with open(filename,'r') as file:
            content = file.read()
    except Exception:
        print("File doesnt exist")

flag = True

while flag:
    args = input(f"Operation you want to perform : (touch / ls / cd / exit) : {os.getcwd()} $ ").strip().split()

    if args[0] == 'touch':
        if len(args) == 2:
            create(args[1].strip('"'))
        elif len(args) >= 3:
            content = ' '.join(args[2:]).strip('"')
            create(args[1].strip('"'),content)


    def format(cwd):
        formatted = []  
        for item in cwd:
            if os.path.isdir(item):
                    formatted.append(item + "/")
            else:
                formatted.append(item)
        return formatted

    if args[0] == 'ls':
        cwd = os.listdir()
        cwd = format(cwd)
        print(*cwd)

    if args[0] == 'cd':
        try:
            if(args[1] == ".."):
                os.chdir("./")
            os.chdir(args[1])
        except Exception:
            print("No such directory exists")

    if args[0] == 'exit':
        flag = False

