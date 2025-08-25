# SRCDS SSDP Denial of Service Vulnerability - Proof of Concept
This vulnerability exist on gameservers that doesn't use Valve SDR. By overwhelming the gameserver with SSDP requests, the gameserver loses connection with Steam, then dies out due to players being unable to play the game, and new players will not be able to see the server in the master server (server browser), and any attempts to directly connect to the server will fail with a timeout error.

# Legal Disclaimer
This Proof of Concept public repository and tool, created by qtland, **is for educational purposes only**. **We are not held responsible or liable for any damages that may happen next**.

# Special Thanks
[Castaway TF](https://castaway.tf) server owner [random](https://steamcommunity.com/profiles/76561198076403312) for their packet capture when their servers are hit with this targetted attack.

# Quick Fix
Replace **`27015`** with the port that your gameserver runs on (it's usually **`27015`**)
```
sudo iptables -I INPUT -p udp --dport 27015 -m string --to 75 --algo bm --string 'HTTP/1.1 200 OK' -j DROP
```
OR
```
sudo iptables -I INPUT -p udp --dport 27015 -m udp --sport 1900 -j DROP
```
