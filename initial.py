## Author: Victor Rezende
## This code prepares a ubuntu based OS to be a development
## ambient to java, python, c, rust, installing awesome vim and some
## plugins to make the experience better

import os

command = open('commands.txt',"r")
for com in command:
    os.system(com)

command.close

print("--The Following languages are supported now:\n *Rust\n *C\n *Java\n *Python\n
        IDES installed in the System: \n *Atom\n *Awesome-Vim\n *NetBeans-Apache\n \n")
