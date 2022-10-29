import os
import shutil
import sys
import time
from distutils.dir_util import copy_tree

commands = ["cd", "help", "ls", "launch", "quit", "exit", "cmd", "cls","del", "rmdir", "rmfile", "rmall", "mkdir", "mkfile", "wfile", "wfile notepad", "cfile", "cdir", "rename"]
thing = "n"
os.system("cmd /c cls")

while thing == "n":

    os.system('color 37')
    cpath = os.getcwd()

    cmd = input(cpath + "_$: ")

    if cmd=="cd":
        try:
            chpath = input("cd: ")
            os.chdir(chpath)
        except:
            pass


    if cmd=="help":
        try:
            print(commands)
            time.sleep(1)
        except:
            pass



    if cmd=="ls":
        try:
            print(os.listdir(os.getcwd()))
            time.sleep(1)
        except:
            pass

    if cmd=="exit":
            os.system('color 7')
            os.system("cmd /c cls")
            exit()

    if cmd=="quit":
            os.system('color 7')
            os.system("cmd /c cls")
            exit()

    if cmd=="launch":
        try:
            launch = input("launch: ")
            os.system("cmd /c " + launch)
        except:
            pass

    if cmd == "cls":
            try:
                os.system("cmd /c cls")
            except:
                pass

    if cmd=="cmd":
        try:
            os.system('color 7')
            prompt = input("command prompt: ")
            os.system("cmd /c " + prompt)
        except:
            pass

    if cmd=="mkdir":
        try:
            dir1 = input("mkdir: ")
            os.mkdir(dir1)

        except:
            pass

    if cmd=="del":
        try:
            print("commands for deletion: rmdir: remove empty directory, rmfile: remove a single file, rmall: remove entire directory.")
        except:
            pass

    if cmd=="rmdir":
        try:
            rmdir = input("rmdir: ")
            os.rmdir(rmdir)
        except:
            pass

    if cmd=="rmfile":
        try:
            rmfile = input("rmfile: ")
            os.remove(rmfile)
        except:
            pass


    if cmd=="rmall":
        try:
            rmall = input("rmall: ")
            shutil.rmtree(rmall)
        except:
            pass

    if cmd=="mkfile":
        try:
            mkfile = input("mkfile: ")
            file = open(mkfile, "a")
            file.close()
        except:
            pass

    if cmd=="wfile":
        try:
            wfile = input("wfile: ")
            os.system("cmd /c " + wfile)
        except:
            pass

    if cmd=="wfile notepad":
        try:
            wfilenotepad = input("wfile notepad: ")
            os.system("cmd /c notepad " + wfilenotepad)
        except:
            pass

    if cmd=="cfile":
        try:
            file1 = input("file: ")
            file2 = input("destination: ")

            shutil.copy2(file1, file2)
        except:
            pass

    if cmd=="cdir":
        try:
            src = input("directory: ")
            dest = input("destination: ")

            copy_tree(src, dest)
        except:
            pass

    if cmd=="rename":
        try:
            source = input("source: ")
            newname = input("newname: ")

            os.rename(source, newname)
        except:
            pass

    if cmd=="mfile":
        try:

            print("To move a file, copy it to a new destination (cfile) them delete the old file (rmfile)")
        except:
            pass
