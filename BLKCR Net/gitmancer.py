def gitmancer(colors):
    import subprocess

    #Sys

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Looking for updates...\n")

    git_fetch = subprocess.run(['git', 'fetch'], cwd = '..', capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], cwd = '..', capture_output=True, text=True)
    print(git_status.stdout)

    git_pull = subprocess.run(['git', 'pull'], cwd = '..', capture_output=True, text=True)
    print(git_pull.stdout)

    #Python lib

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Updating libraries...")

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing requests...")
    pip_requests = subprocess.run(['pip', 'install', 'requests'], cwd = '..', capture_output=True, text=True)
    print(pip_requests.stdout)

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing dnspython...")
    pip_dnspython = subprocess.run(['pip', 'install', 'dnspython'], cwd = '..', capture_output=True, text=True)
    print(pip_dnspython.stdout)

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing python-whois...")
    pip_pythonwhois = subprocess.run(['pip', 'install', 'python-whois'], cwd = '..', capture_output=True, text=True)
    print(pip_pythonwhois.stdout)

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing phonenumbers...")
    pip_phonenumbers = subprocess.run(['pip', 'install', 'phonenumbers'], cwd = '..', capture_output=True, text=True)
    print(pip_phonenumbers.stdout)

    print(f"\n[{colors["%>K<%"]} OK {colors["%---%"]}] All packages checked.")