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
