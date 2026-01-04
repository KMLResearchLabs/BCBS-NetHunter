def geo_IP(colors):
    import requests

    def geoip(ip):
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url).json()

        if r['status'] == 'success':
            answer = (
                "\n"
                f"=== <GEO IP> ===\n"
                + "-" * 40 + "\n"  
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Consulted IP: {r["query"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Country: {r["country"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Region: {r["regionName"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] City: {r["city"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Latitude: {r["lat"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Longitude: {r["lon"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Provider: {r["isp"]}\n"
                f"[{colors["%>+<%"]}+{colors["%---%"]}] Google link: https://www.google.com/maps/@{r["lat"]},{r["lon"]},20z\n"
                + "-" * 40
            )
            return answer
        else:
            return print(f"[{colors["%>-<%"]}ERROR{colors["%---%"]}] Check if the IP is right, if it is, something goed wrong")

    target_ip = str(input("\n>>> Type the IP: ")).strip()
    request = geoip(target_ip)
    print(request)

def get_domain_ip(colors):
    import dns.resolver

    def get_ip_dns(domain):
        try:
            result = dns.resolver.resolve(domain, "A")
            print("\n=== <GET IP> ===")
            print("-" * 40)
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Consulted domain: {domain}")
            for ip in result:
                print(f"[{colors["%>+<%"]}+{colors["%---%"]}] {ip.to_text()}")
            print("-" * 40)
        except Exception as e:
            print(f"[{colors["%>-<%"]}ERROR{colors["%---%"]}] {e}")

    target_domain = str(input("\n>>> Type the domain: ")).strip()
    get_ip_dns(target_domain)

def get_domain_whois(colors):
    import whois

    def consultar_whois(dominio):
        try:
            info = whois.whois(dominio)

            print("\n=== <DOMAIN WHOIS> ===")
            print("-" * 40)
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Consulted domain: {info.domain_name}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Register: {info.registrar}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Organization: {info.organization}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Adress: {info.address}, {info.city}, {info.state}, {info.zipcode}, {info.country}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Emails: {info.emails}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] WHOIS Provider: {info.whois_server}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Creation date: {info.creation_date}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Expiration date: {info.expiration_date}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Last update: {info.updated_date}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] DNS Servers {info.name_servers}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Status: {info.status}")
            print(f"[{colors["%>+<%"]}+{colors["%---%"]}] DNS Sec: {info.dnssec}")
            print("-" * 40)

        except Exception as e:
            print(f"[{colors["%>-<%"]}ERROR{colors["%---%"]}] {e}")

    target_domain = str(input("\n>>> Type the domain: ")).strip()
    consultar_whois(target_domain)
