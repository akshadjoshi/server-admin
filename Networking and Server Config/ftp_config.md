```bash
rpm -qa | grep ftp
```

```bash
yum install vsftpd
```

```bash
rpm -ql vsftpd-3.0.2-29.el7_9.x86_64
```

```bash
rpm -qc vsftpd-3.0.2-29.el7_9.x86_64
```
You have to **activate passive ports** or else you won't be able to access the FTP service

```bash
vim /etc/vsftpd/vsftpd.conf
```

```bash
pasv_min_port=55000
pasv_max_port=55999
pasv_enable=YES

```

```bash
netstat -nltup | grep ftp

# checking for the service if running internally
```

```bash
systemctl restart vsftpd
```


```bash
vim /etc/sysconfig/iptables

# allowing the port in firewall 

# you need to allow the default port as well as passive ports (which can be in range form)
```

**The file in which you will place the content is:**

```bash
/var/ftp/pub/
```
### FTP client

```bash
ftp <IP>

login NAME : ftp 
password : rule says email
```
```bash
# The names you can use in FTP login (if you don't know username) are:

anonymous
ftp 

```

