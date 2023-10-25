
- **master scan**

```bash
nmap -v -Pn -n -sT -sV -sC  -p- 192.168.1.3 --webxml -oA allportscan
```
`change the target IP`
****
- **the go to command**
```bash
nmap -v -Pn -n -sT -sV -sC  <IP>
```
```bash
nmap -v -Pn -n -sC -sV 192.168.56.103 --open
```
```bash
nmap -vv -Pn -n 192.168.56.103
```


- **scan a specific/particular port**

```bash
nmap -v -Pn -sT -sV -p <specific port -sV=<default> <ip>
```
- **specific script scan**

```bash
nmap -v -Pn -sT -sV -p 445 --script=smb* <ip>
```
- **might help in port knocking situation**
```bash
nmap -vv -Pn -sS -p 80,22 192.168.56.103
```

### Internal Network Scan

```bash
nmap -v -sn 192.168.1.100
```
```bash
nmap -v -p- 
```
```bash
 nmap -v -p- -sV 192.168.1.4
```



## pivot network scan
`ping sweep` 

```bash
for i in $(seq 254); do ping 192.168.56.${i} -c -W1 & done | grep from
```

### UDP

```bash
nmap -v -Pn -n 192.168.1.194 -sU --top-ports=20 -v
```

`best for UDP`

```bash
nmap -vv -Pn -n -sU --top-ports=20 -A 192.168.1.38
```

### arp-scan for virtual box host-only adapter

```bash
sudo arp-scan --interface=vboxnet0 --localnet
```
