#container for common functions

import yaml

def userData():
    try:
        with open(r'user.yml') as file:
            return(yaml.full_load(file))
    except FileNotFoundError :
        return False

def certificate():
    try :
        with open(r'certificate.yml') as file:
            return(yaml.full_load(file))
    except FileNotFoundError :
        return False
