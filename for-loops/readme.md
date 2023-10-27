#### port knocking 
```bash
for x in 159 27391 4; do nmap -Pn --host-timeout 100 --max-retries 0 -p 80 192.168.56.103; done
```

### user enum via smb
```bash
for i in $(seq 500 1100);do rpcclient -N -U "" 192.168.56.103 -c "queryuser 0x$(printf '%x\n' $i)" | grep "User Name\|user_rid\|group_rid" && echo "";done
```
