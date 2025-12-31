def blackport():
    import socket
    from concurrent.futures import ThreadPoolExecutor


    open_ports = []  # [(80, "TCP"), (53, "UDP")]


    def scan_tcp(ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            if s.connect_ex((ip, port)) == 0:
                open_ports.append((port, "TCP"))

            s.close()
        except:
            pass


    def scan_port(ip, port):
        scan_tcp(ip, port)


    def get_service(port, proto):
        try:
            return socket.getservbyport(port, proto.lower())
        except:
            return "Unknown"
        

    def scan_target(target, start=1, end=65535, threads=10000):
        ip = socket.gethostbyname(target)

        with ThreadPoolExecutor(max_workers=threads) as executor:
            for port in range(start, end + 1):
                executor.submit(scan_port, ip, port)


        print("\n=== <BlackPort Report> ===")
        print("-" * 40)
        print(f"[+] Open doors of {target}:")

        # remove duplicates
        unique_ports = list(set(open_ports))
        unique_ports.sort(key=lambda x: x[0])

        for port, proto in unique_ports:
            service = get_service(port, proto if "TCP" in proto else "TCP")
            print(f"[+] Port: {port} (Protocol: {proto}/Service: {service})")

        print("-" * 40)

    target = str(input("\n>>> Type the domain: "))
    scan_target(target)
