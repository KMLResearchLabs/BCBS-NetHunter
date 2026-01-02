def gitmancer():
    import subprocess

    df = subprocess.run(['cd', 'BCBS-NetHunter'], capture_output=True, text=True)
    print(df.stdout)

    git_fetch = subprocess.run(['git', 'fetch'], capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], capture_output=True, text=True)
    print(git_status.stdout)

    git_pull = subprocess.run(['git', 'pull'], capture_output=True, text=True)
    print(git_pull.stdout)
