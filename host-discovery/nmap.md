
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
nmap -Pn -n -sCV 
```

- **scan a specific/particular port**

```bash
nmap -v -Pn -sT -sV -p <specific port -sV=<default> <ip>
```
- **specific script scan**

```bash
nmap -v -Pn -sT -sV -p 445 --script=smb* <ip>
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

### UDP

```bash
nmap -v -Pn -n 192.168.1.194 -sU --top-ports=20 -v
```
