#Subprocess module
#It helps in communicating through script to shell and
#bring data from shell

'''Open your command prompt, go to a directory, say
desktop using cd and then open python.
import subprocess
After this type in subprocess.call('dir',shell=True)
this will print all teh file in desktop with their dates
in the command prompt.
This wn't work if you do this in a python script in an ide,
the script won't print anything.

To get the output, we need to use in the shell
utput = subprocess.check_output('dir',shell=True)
print(output)'''
