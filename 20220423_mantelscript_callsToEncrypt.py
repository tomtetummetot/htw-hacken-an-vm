import os
import random

from Encryption_1 import call

path = '/Users/tschade/Library/Mobile Documents/com~apple~CloudDocs/Uni/5.Semester/Hacken an VMs/testData'
path2 = '/Users/tschade/Library/Mobile Documents/com~apple~CloudDocs/Uni/5.Semester/Hacken an VMs/encrypted_20201204_194840.jpg'
pw = 'Test1234'


def selectfile(pathToFolder):
    n = 1
    random.seed()
    for root, dir, files in os.walk(pathToFolder):
        for name in files:
            n += 1
            if random.uniform(0, n) < 1:
                selected = os.path.join(root, name)
                print(selected)
                return selected


def encryptChoosenFile(file, password):
    call(1, password, file)
    print('encryption done')


def main():
    # encryptChoosenFile(selectfile(path), pw)
    call(2, pw, path2)


if __name__ == '__main__':
    main()
