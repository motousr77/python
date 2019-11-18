#!/c/Programs/Python/Python38/python.exe
# executanle python  by ./renamer oin the bash only !
import sys, re, os
from os import listdir
from os.path import isfile, join

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
else:
    print(sys.stderr.write('Input path to folder. \nOr drop direcory to the current command shell\nerr: '))
    exit() # break this app.

f_lst = [f for f in listdir('.') if isfile(join('.', f))]
print('\n' + str(os.getcwd()) + '/\n')
# print('\n')
print(os.listdir())
prompt = input("\nRemove digits at start Y/n ? ")
if re.search(r'[yY]', prompt):
    do_work = True
elif re.search(r'[a-zA-Z0-9][^ yY][\t\n]', prompt):
    do_work = False
    print('Rejected. Exit!')
    exit()
else:
    print('Rejected. Exit (0)')
    exit()

sub_str = ""
for f_name in f_lst:
    if re.search(r'^[a-zA-Z]', f_name):
        print('\n')
        print('****************************')
        print('**  No numbers on begin!  **')
        print('****************************')
        do_work = False
        break
    if re.search(r'[0-9]', f_name):
        if re.search(r'Cover', f_name):
            print('\n\nCover : find\n\n')
            continue
        if re.search(r'^\d\d\. ', f_name):
            sub_str = re.search(r'^\d\d\.\ ', f_name).group()
            # os.rename(f_name, re.sub(sub_str, '', f_name))
            print(re.sub(sub_str, '', f_name))
        else:
            sub_str = re.search(r'^\d\d\ ', f_name).group()
            # os.rename(f_name, re.sub(sub_str, '', f_name))
            print(re.sub(sub_str, '', f_name))
print('\n')
print(os.listdir())

if do_work:
    print('\n')
    print('****************************')
    print('**  Yeah!  All Complete!  **')
    print('****************************')
else:
    print('\n')
    print('********************************')
    print('** Try Another or Do Nothing. **')
    print('********************************')
# print(str(os.getcwd()))