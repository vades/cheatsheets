# Git Cheat Sheet

This cheat sheet provides a list of 30 commonly used Git commands along with their short descriptions and examples.

| Command | Description | Example |
|---------|-------------|---------|
| `git init` | Initializes a new Git repository | `git init` |
| `git clone` | Creates a local copy of a remote repository | `git clone https://github.com/user/repo.git` |
| `git add` | Adds changes to the staging area | `git add file.txt` |
| `git commit` | Records changes to the repository | `git commit -m "Added new feature"` |
| `git status` | Shows the status of files in the repository | `git status` |
| `git push` | Pushes local changes to a remote repository | `git push origin master` |
| `git pull` | Fetches and merges changes from a remote repository | `git pull origin master` |
| `git branch` | Lists all branches in the repository | `git branch` |
| `git checkout` | Switches to a different branch | `git checkout new-feature` |
| `git merge` | Merges changes from one branch into another | `git merge feature-branch` |
| `git remote` | Manages remote repositories | `git remote add origin https://github.com/user/repo.git` |
| `git log` | Displays the commit history | `git log` |
| `git diff` | Shows the differences between commits, branches, etc. | `git diff HEAD~1 HEAD` |
| `git reset` | Resets the repository to a previous commit | `git reset HEAD~1` |
| `git stash` | Temporarily saves changes that are not ready to be committed | `git stash` |
| `git tag` | Creates, lists, or deletes tags | `git tag v1.0.0` |
| `git fetch` | Downloads objects and references from a remote repository | `git fetch origin` |
| `git remote -v` | Shows the URLs of remote repositories | `git remote -v` |
| `git revert` | Creates a new commit that undoes a previous commit | `git revert HEAD` |
| `git rm` | Removes files from the working directory and the repository | `git rm file.txt` |
| `git show` | Displays information about a commit | `git show abcdef123` |
| `git blame` | Shows who last modified each line of a file | `git blame file.txt` |
| `git cherry-pick` | Applies the changes of a specific commit to the current branch | `git cherry-pick abcdef123` |
| `git config` | Sets or displays Git configuration variables | `git config --global user.name "John Doe"` |
| `git remote rm` | Removes a remote repository from the list of remotes | `git remote rm origin` |
| `git rebase` | Applies commits from one branch onto another | `git rebase main` |
| `git show-branch` | Displays the branches and their commits | `git show-branch` |
| `git grep` | Searches for a pattern in files and commits | `git grep "hello"` |
| `git checkout -b` | Creates a new branch and switches to it | `git checkout -b feature` |
| `git clean` | Removes untracked files from the working directory | `git clean -n` |
| `git bisect` | Finds the commit that introduced a bug using binary search | `git bisect start` |
