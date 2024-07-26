from list.strutils.to_list import multi_str_to_list
from os import system
def install(*args):
    system("sudo apt install " + " ".join(multi_str_to_list(" ", *args)))
def autoremove(*args):
    system("sudo apt autoremove " + " ".join(multi_str_to_list(" ", *args)))
def show(*args):
    system("apt show " + " ".join(multi_str_to_list(" ", *args)))
