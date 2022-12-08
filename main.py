import os
import signal


def file_hundeler():
    while True:
        file_path = input("Entre the absolute path or the name of the file :\n")
        if not file_path.endswith(".txt"):
            file_path +=".txt"
        if os.path.exists(file_path):
            ans = input("the file is alredy exist do you want to open it(y:yes/n:no):\n")
            if ans.lower() == 'y':
                ans = input("do you want to erase the contenat of the file or to add (e:erase/a:add):\n")
                print("press ctrl+C to exit and save\nwrite exit() to exit without saving")
                print("____________________*__________________")
                if ans== 'a':
                    handel = open(file_path,"r+")
                    print(handel.read())
                    return handel
                else:
                    handel = open(file_path, "w")
                    return handel
            else:
                continue
        else:
            try:
                handel = open(file_path,"w")
                print("press ctrl+C to exit and save\nwrite exit() to exit without saving")
                print("____________________*__________________")
                return handel
            except:
                print("the absolute path you passed is not exist")
                exit()
def catch_ctrl_C(signum, stack_frame):
    handel.write(text)
    handel.close()
    exit()

text = ""
handel = file_hundeler()
while True:
    signal.signal(signal.SIGINT, catch_ctrl_C)
    n = input()
    if n == "exit()":
        break
    else:
        pass
    text += n + "\n"

handel.close()
quit()