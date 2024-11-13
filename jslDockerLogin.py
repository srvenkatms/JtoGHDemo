import os
import subprocess

def docker_login():
    docker_username = os.environ['DOCKER_USERNAME']
    docker_password = os.environ['DOCKER_PASSWORD']
    
    login_command = f'echo {docker_password} | docker login -u {docker_username} --password-stdin'
    subprocess.run(login_command, shell=True, check=True)

docker_login()
