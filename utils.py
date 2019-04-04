# Utilities to support an Azure MLHub package
#
# These will migrate to MLHUB itself over time.

# Import the required libraries.

import os
import sys
import readline  # Don't remove !! For prompt of input() to take effect
import termios
import tty

# Load subscription key and endpoint from file.

def load_key(path):
    key = None
    endpoint = None
    markchar = "'\" \t"
    with open(path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            pair = line.split('=')
            if len(pair) == 2:
                k = pair[0].strip(markchar).lower()
                v = pair[1].strip(markchar)
                if k == 'key':
                    key = v
                elif k == 'endpoint':
                    endpoint = v
            elif not line.startswith('#'):
                line = line.strip(markchar)
                if line.startswith('http'):
                    endpoint = line
                else:
                    key = line
    return key, endpoint

# Either load key/endpoint from file or ask user and save to file.

def get_key_endpoint(key_file, service="Cognitive Services"):
    """The user is asked for an Azure subscription key and endpoint. The
    provided information is saved into a file for future use. The
    contents of that file is the key and endpoint with the endpoint
    identified as starting with http:

    a14d1234abcda4f2f6e9f565df34ef24
    https://westus2.api.cognitive.microsoft.com

    """

    key = None

    # Set up messages.
    
    prompt_key = "Please paste your {} subscription key: ".format(service)
    prompt_endpoint = "Please paste your endpoint: "

    msg_request = """\
An Azure resource is required to access this service (and to run this command).
See the README for details of a free subscription. If you have a subscription
then please paste the key and the endpoint here.
"""
    msg_found = """\
The following file has been found and is assumed to contain an Azure 
subscription key and endpoint for {}. We will load 
the file and use this information.

    {}
""".format(service, key_file)

    msg_saved = """
I've saved that information into the file:

    {}
""".format(key_file)

    # Obtain the key/endpoint.
    
    if os.path.isfile(key_file) and os.path.getsize(key_file) > 0:
        print(msg_found)
        key, endpoint = load_key(key_file)
    else:
        print(msg_request)
        
        key      = ask_password(prompt_key)
        endpoint = input(prompt_endpoint)

        if len(key) > 0 and len(endpoint) > 0:
            ofname = open(key_file, "w")
            ofname.write("{}\n{}\n".format(key, endpoint))
            ofname.close()
            print(msg_saved)

    return key, endpoint

# Simple input of password.

def ask_password(prompt=None):
    """Echo '*' for every input character. Only implements the basic I/O
    functionality and so only Backspace is supported.  No support for
    Delete, Left key, Right key and any other line editing.

    Reference: https://mail.python.org/pipermail/python-list/2011-December/615955.html
    """

    symbol = "`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    if prompt:
        sys.stdout.write(prompt)
        sys.stdout.flush()

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    chars = []
    try:
        tty.setraw(sys.stdin.fileno())
        while True:
            c = sys.stdin.read(1)
            if c in '\n\r':  # Enter.
                break
            if c == '\003':
                raise KeyboardInterrupt
            if c == '\x7f':  # Backspace.
                if chars:
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                    del chars[-1]
                continue
            if c.isalnum() or c in symbol:
                sys.stdout.write('*')
                sys.stdout.flush()
                chars.append(c)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        sys.stdout.write('\n')

    return ''.join(chars)
