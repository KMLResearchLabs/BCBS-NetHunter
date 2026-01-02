def gitmancer():
    import subprocess

    #Sys

    print("[<>] Looking for updates...\n")

    git_fetch = subprocess.run(['git', 'fetch'], cwd = '..', capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], cwd = '..', capture_output=True, text=True)
    print(git_status.stdout)

    git_pull = subprocess.run(['git', 'pull'], cwd = '..', capture_output=True, text=True)
    print(git_pull.stdout)

    #Python lib

    print("[<>] Updating libraries...")

    print("[<>] Checking/installing requests...")
    pip_requests = subprocess.run(['pip', 'install', 'requests'], cwd = '..', capture_output=True, text=True)
    print(pip_requests.stdout)

    print("[<>] Checking/installing dnspython...")
    pip_dnspython = subprocess.run(['pip', 'install', 'dnspython'], cwd = '..', capture_output=True, text=True)
    print(pip_dnspython.stdout)

    print("[<>] Checking/installing python-whois...")
    pip_pythonwhois = subprocess.run(['pip', 'install', 'python-whois'], cwd = '..', capture_output=True, text=True)
    print(pip_pythonwhois.stdout)

    print("[<>] Checking/installing phonenumbers...")
    pip_phonenumbers = subprocess.run(['pip', 'install', 'phonenumbers'], cwd = '..', capture_output=True, text=True)
    print(pip_phonenumbers.stdout)

    print("\n[ OK ] All packages checked.")