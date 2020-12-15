import sys
import subprocess
import requests
import json

def process():
    # if not os.path.exists('foo'):
    #subprocess.call(["gcc", "cournot.c", "-ocournot", "-lm"]) # lm to compile include math library. Or the math operations fails
    # also include -mcmodel=medium as argument to subprocess call if needed ,"-mcmodel=medium"]
    subprocess.call(["gcc", "cournot.c", "-ocournot", "-lm","-mcmodel=medium"])

def cournotModel(*args):
    print("arguments are:\n" + str(args[0]))
    process()

    subprocess.call(["./cournot", str(args[0])], stdin=sys.stdin)

    subprocess.run(["python3", "moveToS3.py"]) # this shuld be uncommented
    print("printing result")
    return 'cournot_form.html'
