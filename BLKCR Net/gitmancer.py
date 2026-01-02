def gitmancer():
    import subprocess

    git_fetch = subprocess.run(['git', 'fetch'], cwd = 'BCBS-NetHunter', capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], cwd = 'BCBS-NetHunter', capture_output=True, text=True)
    print(git_status.stdout)

    git_pull = subprocess.run(['git', 'pull'], cwd = 'BCBS-NetHunter', capture_output=True, text=True)
    print(git_pull.stdout)
