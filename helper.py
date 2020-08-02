#container for common functions

import yaml

def userData():
    with open(r'user.yml') as file:
        return(yaml.full_load(file))

def certificate():
    with open(r'certificate.yml') as file:
        return(yaml.full_load(file))
