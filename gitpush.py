from git import Repo
import socket
from datetime import datetime
import logging

branch_name = "develop"

# Configure logger for file output
file_log = logging.getLogger("file_log")
file_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("app.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_log.addHandler(file_handler)


def git_push(branch_name):
    print('\n*********** Initializing Repo ***********')
    file_log.debug(f'Initializing Repo and Branch {branch_name}')
    # Initialize the repository object
    repo = Repo()

    # Check if there are changes to commit
    if repo.is_dirty():
        try:
            # Get the PC name
            pc_name = socket.gethostname()

            # Get the current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Commit message
            commit_message = f'Commit and push from Pythomat {pc_name} at {current_datetime}'

            # Run git commands

            print('\n*********** Committing and pushing to git ***********')
            file_log.debug(f'Committing and pushing to git')
            repo.git.add("--all")
            repo.git.commit("-m", commit_message)
            repo.git.push("origin")
            print(f'\n*********** {commit_message} ***********')
            file_log.debug(commit_message)
        except Exception as e:
            print("An error occurred while pushing to git:", e)
            file_log.exception('An error occurred while pushing to git')

    else:
        print("No changes to commit.")
        file_log.warning('No changes to commit.')


# The following block will only be executed if the script is run directly,
# and not imported as a module by another script.

if __name__ == "__main__":
    branch_name = "develop"

    git_push(branch_name)
