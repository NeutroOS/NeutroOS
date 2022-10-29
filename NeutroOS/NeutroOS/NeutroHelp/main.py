import os
import time

print("Welcome to NeutroHelp, type help for a list of commands. Please type commands in all lower text.")

commands = ["help", "what", "apps", "who", "credits", "quit", "neutrotext", "neutronet", "neutromath", "neutroterminal", "neutroart"]
apps = ["NeutroText", "NeutroMath", "NeutroTerminal", "NeutroNet", "NeutroArt"]
what = "NeutroOS is a package of great python based apps to help with daily activities or work."
who = "NeutroOS was created by Nathan Sietko."
credits1 = "Creator:Nathan Sietko, email:mypuzzle15@gmail.com, github:NeutroOS"
os.system('color 2')


thing = "n"



while thing == "n":
    time.sleep(1)
    choice = input("command: ")

    if choice=="help":
        print(commands)



    elif choice=="what":
        print(what)



    elif choice=="who":
        print(who)



    elif choice=="apps":
        print(apps)



    elif choice=="credits":
        print(credits1)



    elif choice=="quit":
        os.system('color 7')
        os.system("cmd /c cls")
        print("this window will stay open but the program has closed, return to the NeutroOS window and do NOT close this terminal.")
        exit()


    elif choice=="neutrotext":
        print("NeutroText is a python based text editor containing color changing text, all text editor functions and file managment.")

    elif choice=="neutronet":
        print("NeutroNet is a python based browser that has google intigrated.")

    elif choice=="neutroart":
        print("NeutroArt is a python based paint program that has multiple brush sizes and multiple colors with exportable as PNG.")

    elif choice=="neutroterminal":
        print("The NeutroTerminal is a terminal that contains all the commands of a basic terminal and is an early view at the creator's future project.")

    elif choice=="neutromath":
        print("NeutroMath is a python based GUI calculator with basic math functions.")

