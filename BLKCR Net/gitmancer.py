def gitmancer():
    import subprocess

    #Sys

    git_fetch = subprocess.run(['git', 'fetch'], cwd = '..', capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], cwd = '..', capture_output=True, text=True)
    print(git_status.stdout)

    git_pull = subprocess.run(['git', 'pull'], cwd = '..', capture_output=True, text=True)
    print(git_pull.stdout)

    #Python lib

    pip_requests = subprocess.run(['pip', 'install', 'requests'], cwd = '..', capture_output=True, text=True)
    print(pip_requests.stdout)

    pip_dnspython = subprocess.run(['pip', 'install', 'dnspython'], cwd = '..', capture_output=True, text=True)
    print(pip_dnspython.stdout)

    pip_pythonwhois = subprocess.run(['pip', 'install', 'python-whois'], cwd = '..', capture_output=True, text=True)
    print(pip_pythonwhois.stdout)

    pip_phonenumbers = subprocess.run(['pip', 'install', 'phonenumbers'], cwd = '..', capture_output=True, text=True)
    print(pip_phonenumbers.stdout)