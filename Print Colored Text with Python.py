#print coloured text with Python using the Colorama module

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is safeer "+ Fore.YELLOW+ Back.BLUE+"I am your friend")
print(Back.CYAN+"Hi My name is muhammad")
print(Fore.RED + Back.GREEN+ "Hi My name is safeer")
