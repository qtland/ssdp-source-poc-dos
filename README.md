# SRCDS SSDP Denial of Service Vulnerability - Proof of Concept
This vulnerability exists on every source game server that doesn't hide its actual IP address via anycast or by using Valve SDR. This script will bypass any iptables (and DDoS protection) filtering set for detecting SSDP flood and flood the server via UDP packets (oops accidental discovery). The other versions can be easily patched as they will be sent from port 1900 to the game server's game port (UDP 27015, for example). Read [here](https://blog.cloudflare.com/ssdp-100gbps/#the-amplification) for how this is possible and how vulnerable the SSDP protocol is.

# Legal Disclaimer
This Proof of Concept public repository and tool, created by qtland, **is for educational purposes only**. **We are not held responsible or liable for any damages that may happen next**.

# Special Thanks
[Castaway TF](https://castaway.tf) server owner [random](https://steamcommunity.com/profiles/76561198076403312) for their packet capture when their servers are hit with this targeted attack.

# How to Fix
There is currently no correct way to filter this packet out, but please let us know if you have a 100% solution that filters the packets.

## Filter packets from port 1900
```
sudo iptables -I INPUT -p udp --dport 27015 -m udp --sport 1900 -j DROP
```
