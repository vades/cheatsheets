from git import Repo

def upload_directory_to_git(branch_name):
    # Clone the repository
    # repo = Repo.clone_from(repository_url, "temp_repo")
    
    # Initialize the repository object
    repo = Repo()
    
    # Check if there are changes to commit
    #if repo.is_dirty():
    repo.git.add("--all")
    repo.git.commit("-m", "Upload directory")
    repo.git.push("origin", branch_name)
   #else:
        #print("No changes to commit.")

# Example usage
directory_path = "./_input/docs"
repository_url = "https://github.com/vades/cheatsheets"
branch_name = "develop"

upload_directory_to_git(branch_name)
