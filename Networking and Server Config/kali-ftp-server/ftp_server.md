```bash
apt install vsftpd
```

```bash
vim /etc/vsftpd.conf
```
```bash
# Allow anonymous FTP? (Disabled by default).
anonymous_enable=YES
anon_root=/opt/transfer/

chroot_local_user=YES    # uncomment this line 
#chroot_list_enable=YES
# (default follows)
```
`add the below lines at the very end of the config file`

```bash
allow_writeable_chroot=YES
pasv_min_port=50000
pasv_max_port=59999
pasv_enable=YES
```
```bash
systemctl status vsftpd.service
```
```bash
systemctl restart  vsftpd.service
```

```bash
netstat -nltup
# look for port 21 
```
