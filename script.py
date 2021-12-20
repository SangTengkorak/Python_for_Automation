# executing terminal commands

import subprocess as sp

for i in range(0, 5):
    # run command in check_call array sequentially
    sp.check_call(['python3', 'example.py'])
