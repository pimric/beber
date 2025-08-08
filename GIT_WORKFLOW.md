# Git Workflow

To ensure your changes are correctly tracked and pushed to the remote repository, follow these steps:

1.  **Stage changes:** Add all modified or new files to the staging area.
    ```bash
    git add .
    ```
    (Or `git add <file_name>` for specific files)

2.  **Commit changes:** Record the staged changes to the repository with a descriptive message.
    ```bash
    git commit -m "Your descriptive commit message here"
    ```

3.  **Push changes:** Upload your local commits to the remote repository.
    ```bash
    git push origin main
    ```
    (Assuming your branch is `main` and remote is `origin`)
