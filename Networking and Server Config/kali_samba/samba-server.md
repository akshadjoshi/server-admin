```bash
apt update 
```


```bash
apt install samba
```


```bash
cd /etc/samba
ls -l
```


```bash
cp smb.conf smb.conf.backup
```


```bash
vim smb.conf
```

```bash
[nobody]   # id 
	path = /opt/transfer
	writeable = yes
	guest ok = yes
 	guest only = yes 
 	read only = no
 	create mode = 0777
 	directory mode = 0777
 	force user = nobody  # keep it nobody coz you have user on you pc with this name 
```



```bash
systemctl status smbd.service
```

```bash
systemctl restart smbd.service
```

```bash
netstat -nltup 

# check for port 139 and 445
```
