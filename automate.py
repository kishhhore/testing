import time
import os
import subprocess

# Define constants
file_name = "contribution.txt"
repo_path = r"C:\Backend\del in few mins\testing"  # Your repository path
file_path = os.path.join(repo_path, file_name)
create_commit_message = "add new text file"
delete_commit_message = "delete text file"

def automate_commit_and_delete():
    # Step 1: Create a text file
    with open(file_path, "w") as file:
        file.write("This is an automated contribution.")

    # Change to the repository directory
    os.chdir(repo_path)

    # Step 2: Run commands in the integrated terminal of VS Code
    commands = [
        f'git add {file_name}',
        f'git commit -m "{create_commit_message}"',
        'git push',
        f'git rm {file_name}',  # Remove the file from Git
        f'git commit -m "{delete_commit_message}"',
        'git push'
    ]

    for command in commands:
        subprocess.run(command, shell=True)

# Loop to continuously commit and delete until manually stopped
try:
    while True:
        automate_commit_and_delete()
        time.sleep(10)  # Interval between each commit, adjust as needed
except KeyboardInterrupt:
    print("Script stopped by user.")




