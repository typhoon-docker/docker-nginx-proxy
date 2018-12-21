#!/usr/bin/env python3

# import argparse

# parser = argparse.ArgumentParser(description='Make the right configuration for nginx')
# parser.add_argument("-a", "--append", help="Append to the conf file instead of making a new one", action="store_true")
# parser.add_argument("-d", "--domain", help="Host domain name")
# parser.add_argument("-n", "--name", help="Missile name", action="append")
# parser.add_argument("-p", "--port", help="Missile internal port", action="append")

# args = parser.parse_args()

with open("proxy.template.conf", "r") as f:
    template = f.read().strip()

hostname = None
loopback = None

with open("hostname.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("hostname"):
            hostname = line.split("=")[1].strip()

        elif line.startswith("loopback"):
            loopback = line.split("=")[1].strip()

names_ports = []

with open("database.txt", "r") as f:
    for line in f.readlines():
        try:
            name, port, include = line.strip().split(" ")
            if include.lower() == "true":
                names_ports.append((name, port))
        except Exception as e:
            print("Warning: Exception in parsing: {}".format(e))

conf = ""

for name, port in names_ports:
    mn_hn = hostname if name == "_" else name + "." + hostname
    conf += template.replace("MISSILE_NAME.HOSTNAME", mn_hn).replace("LOOPBACK", loopback) \
                    .replace("MISSILE_PORT", port) + "\n"

with open("proxy.conf", "w") as f:
    f.write(conf)
