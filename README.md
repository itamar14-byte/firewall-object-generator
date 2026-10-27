# firewall-object-generator

Adding many address objects to a Palo Alto firewall by hand means clicking **Add** and typing each one. This script creates them from a text file instead, optionally bundles them into an address group, and commits.

## Requirements

- Python 3
- A PAN-OS firewall reachable over HTTPS, and an admin account allowed to use the XML API

Install the two packages it uses:

```
pip install -r requirements.txt
```

## The input file

A plain text file with each object on two lines, its name and then its address. The address is an IP address or a subnet in CIDR form. Ranges and FQDNs aren't supported.

```
web-01
10.20.1.11/32
web-02
10.20.1.12/32
dmz-net
172.16.50.0/24
```

## Running it

```
python panos_objects.py
```

It asks for the file's path, the username and password (the password isn't shown as you type), and the firewall's address or hostname. It creates each address object, then asks whether to put them all into a new address group, and commits.

## Limitations

- The objects are created in the `shared` location.
- **The commit includes every pending change on the firewall**, not only this script's, so run it when no other admin has uncommitted work.
- Existing objects aren't checked first, and the file isn't validated before the firewall is changed.

## License

MIT, see [LICENSE](LICENSE).
