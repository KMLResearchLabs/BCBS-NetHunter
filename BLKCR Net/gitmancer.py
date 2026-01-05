def gitmancer(colors):
    import subprocess

    #Sys

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Looking for updates...\n")

    git_fetch = subprocess.run(['git', 'fetch'], cwd = '..', capture_output=True, text=True)
    print(git_fetch.stdout)

    git_status = subprocess.run(['git', 'status'], cwd = '..', capture_output=True, text=True)
    print(git_status.stdout)

    git_diff = subprocess.run(['git', 'diff'], cwd = '..', capture_output=True, text=True)
    print(git_diff.stdout)

    #Python lib

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking libraries...")

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

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing colorama...")
    pip = subprocess.run(['pip', 'install', 'colorama'], cwd = '..', capture_output=True, text=True)
    print(pip.stdout)

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing pywifi...")
    pip = subprocess.run(['pip', 'install', 'pywifi'], cwd = '..', capture_output=True, text=True)
    print(pip.stdout)

    print(f"[{colors["%>!<%"]}<>{colors["%---%"]}] Checking/installing comtypes...")
    pip = subprocess.run(['pip', 'install', 'comtypes'], cwd = '..', capture_output=True, text=True)
    print(pip.stdout)

    print(f"\n[{colors["%>K<%"]} OK {colors["%---%"]}] All packages checked.")