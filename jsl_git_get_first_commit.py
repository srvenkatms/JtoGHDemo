#### jsl_git_get_first_commit.py

import subprocess

def jsl_git_get_first_commit():
    result = subprocess.run(
        'git log --reverse | head -1 | awk \'{print $2}\'', 
        shell=True, 
        stdout=subprocess.PIPE
    )
    return result.stdout.decode().strip()

