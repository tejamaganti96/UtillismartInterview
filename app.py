from input_handler import Readinput, sortInput

def main():
    Readinput()
    x = sortInput()

    for i in range(len(x)):
        print(x[i].SN, x[i].Manu_name)
main()