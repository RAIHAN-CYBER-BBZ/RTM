import os,time,platform
os.system('clear')
bit = platform.architecture()[0]
if bit=='64bit':
    import RR
else:
    print('\033[1;31m[×] Sorry Device Not Support')
 
 
