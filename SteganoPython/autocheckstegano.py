import magic
import binwalk
import string
import sys


## useful functions

def strings(filename, min=4):
    with open(filename, errors="ignore") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min:  # catch result at EOF
            yield result

## main part

# TODO parse args
if len(sys.argv) < 2:
    print("Things are missing. Usage: "+str(sys.argv[0])+" <file>")
    exit(-1)

file = sys.argv[1]

file_type = magic.from_file(file, mime=True) # equivalent to the 'file' command on Linux
embedded = binwalk.scan(file) # binwalk scan
#TODO extract files ?
file_strings = list(strings(file))

# TODO print the results of basic scans

# TODO si image :
    # TODO lancer exiftool
    # TODO lancer PIT
    # TODO lancer un LSB
    # TODO lancer PVD
    # TODO lancer Stegsolve
    
# TODO si wav :
    # TODO ouvrir analyseur de spectre

# TODO si pdf :
    # TODO lancer pdfparser
    # TODO checker Angecryption

# TODO traduire automatiquement la b64