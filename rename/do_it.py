import sys, re, os
from os import listdir
from os.path import isfile, join

my_path = ""
if len(sys.argv) > 1:
    my_path = sys.argv[1]
else:
    print(sys.argv[0])
    print(sys.stderr.write('Input argument / path to folder'))

f_lst = [f for f in listdir(my_path) if isfile(join(my_path, f))]
sub_str = ""
for f_name in f_lst:
    sub_str = re.search(r'^\d\d\. ', f_name).group()
    os.rename(my_path + f_name, my_path + str(re.sub(sub_str, '', f_name)))

print('Done.')


# import os
# os.rename('a.txt', 'b.kml')

# import os
# os.path.abspath("mydir/myfile.txt")
#  'C:/example/cwd/mydir/myfile.txt'
#  Also works if it is already an absolute path:
#  import os
#  os.path.abspath("C:/example/cwd/mydir/myfile.txt")
#  'C:/example/cwd/mydir/myfile.txt'