# Intern Project
This is a repository of Pisanu Boonyaanan about the intern project for KMUTT and KBTG.

## About this project
This project is a script generator for use in the Virtual User Generator (VUGen) program of Load Runner Enterprise (LRE) that is used to do a performance test. By the way, this project is just to create a text file in this folder, it will not create a C file that can run in the VUGen program. You will have to copy it to your VUGen script later.

## Noted
1. This is a WIP. Please don't expect too much. 🙏
2. This program doesn't have the option to rename the action file or transaction name, you have to change it after you copy it to your VUGen.

## Requirements
1. Python (3.x.x ++)
If you already have Python, you can use this script instantly because this script does not use a custom library.
2. Git
to use `git clone` and clone my project.

## How to use these script
1. Clone my project with `git clone`
2. After the clone is done. Run with `python genscript.py`
3. The program will request a JSON request file path, you can copy the file path by simply right-clicking from your file and selecting the "Copy file path" option, or you can type it if you can.
4. If the program shows an output that is saved to "Output/ActionXX.txt" successfully that means it's successfully created a script that is ready to use in the Virtual User Generator program.
