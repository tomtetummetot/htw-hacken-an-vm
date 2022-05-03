import os
import random
import logging
import datetime

from Encryption_1 import call

path = '/Users/tschade/Library/Mobile Documents/com~apple~CloudDocs/Uni/5.Semester/Hacken an VMs/testData'
path2 = '/Users/tschade/Library/Mobile Documents/com~apple~CloudDocs/Uni/5.Semester/Hacken an VMs/encrypted_20201204_194840.jpg'


def selectfile(pathToFolder):
    n = 1
    random.seed()
    for root, dir, files in os.walk(pathToFolder):
        for name in files:
            n += 1
            if random.uniform(0, n) < 1:
                selected = os.path.join(root, name)
                logging.info('Enrypted: ' + str(selected))
                return selected


def encryptSelectedFile(file):
    enctime = datetime.datetime.now().replace(microsecond=0).isoformat()
    logging.warning('logging done at: ' + enctime)
    call(1, enctime, file)


def main():
    logging.basicConfig(filename="logging.log")
    encryptSelectedFile(selectfile(path))


if __name__ == '__main__':
    main()
