def geo_IP():
    import requests

    def geoip(ip):
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url).json()

        if r['status'] == 'success':
            answer = (
                "\n"
                f"=== <GEO IP> ===\n"
                + "-" * 40 + "\n"  
                f"[+] Consulted IP: {r["query"]}\n"
                f"[+] Country: {r["country"]}\n"
                f"[+] Region: {r["regionName"]}\n"
                f"[+] City: {r["city"]}\n"
                f"[+] Latitude: {r["lat"]}\n"
                f"[+] Longitude: {r["lon"]}\n"
                f"[+] Provider: {r["isp"]}\n"
                f"[+] Google link: https://www.google.com/maps/@{r["lat"]},{r["lon"]},20z\n"
                + "-" * 40
            )
            return answer
        else:
            return print("[ERROR] Check if the IP is right, if it is, something goed wrong")

    target_ip = str(input("\n>>> Type the IP: ")).strip()
    request = geoip(target_ip)
    print(request)

def get_domain_ip():
    import dns.resolver

    def get_ip_dns(domain):
        try:
            result = dns.resolver.resolve(domain, "A")
            print("\n=== <GET IP> ===")
            print("-" * 40)
            print(f"[+] Consulted domain: {domain}")
            for ip in result:
                print(f"[+] {ip.to_text()}")
            print("-" * 40)
        except Exception as e:
            print(f"[ERROR] {e}")

    target_domain = str(input("\n>>> Type the domain: ")).strip()
    get_ip_dns(target_domain)

def get_domain_whois():
    import whois

    def consultar_whois(dominio):
        try:
            info = whois.whois(dominio)

            print("\n=== <DOMAIN WHOIS> ===")
            print("-" * 40)
            print(f"[+] Consulted domain: {info.domain_name}")
            print(f"[+] Register: {info.registrar}")
            print(f"[+] Organization: {info.organization}")
            print(f"[+] Adress: {info.address}, {info.city}, {info.state}, {info.zipcode}, {info.country}")
            print(f"[+] Emails: {info.emails}")
            print(f"[+] WHOIS Provider: {info.whois_server}")
            print(f"[+] Creation date: {info.creation_date}")
            print(f"[+] Expiration date: {info.expiration_date}")
            print(f"[+] Last update: {info.updated_date}")
            print(f"[+] DNS Servers {info.name_servers}")
            print(f"[+] Status: {info.status}")
            print(f"[+] DNS Sec: {info.dnssec}")
            print("-" * 40)

        except Exception as e:
            print(f"[ERROR] {e}")

    target_domain = str(input("\n>>> Type the domain: ")).strip()
    consultar_whois(target_domain)
