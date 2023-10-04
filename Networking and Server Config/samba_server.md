```bash
rpm -qa | grep samba
```
```bash
yum install samba-client

# samba is a client tool we use to access smb service
```
```bash
rpm -qi samba-client-4.10.16-20.el7_9.x86_64
```

```sh
smbtree

# finds smb server in the network (will work on kali)
```
```bash
smbtree -D workgroup -U emp1
```
```bash
smbtree -D <workgroup/domain> -U <username>
```
**smbtree** is for detection but use **nmap** if for scan

### smbclient

```bash
smbclient -L <IP> -U <username>
```

```bash
# Example : 

smbclient -L //192.168.1.100 -U emp1

# -L shows list 
# to access the listed data remove -L
```
**NULL session**
```bash

 smbclient -L //192.168.1.100 -U "" -N
```
`works if smb service is misconfigured`

```bash
smbclient -L <ip> -U "" -N
```


    

**data fetch**

```bash

smbclient  //192.168.1.100/data -U emp1
````
```
lcd <dirlocation>

# to change the dir you want to download the file on your local PC
```
`see this code in raw mode`

<!-- https://subba-lakshmi.medium.com/create-a-network-share-in-linux-using-samba-via-cli-and-access-using-samba-client-46ae16a012c3 -->




