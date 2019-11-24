l1='     O'
l2='    /|\\\n'
l3='   / | \\\n'
l4='     |\n'
l5='     /\\\n'
l6=' \\__/__\\__/\n'
l7='   0    0'

import time
while True:
    for i in range(35):
        print(' '*i+l1)
        print(' '*i+l2)
        print(' '*i+l3)
        print(' '*i+l4)
        print(' '*i+l5)
        print(' '*i+l6)
        print(' '*i+l7)
        time.sleep(0.1)
        print('\n'*50)
