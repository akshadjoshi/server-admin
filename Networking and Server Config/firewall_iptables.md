## iptables

#### concept

OUTPUT - source me IP output chain

INPUT  - hum pe attack lag raha hain (destination me humhara IP)

FORWARD CHAIN  it replaces IP eg IP changed to port 80

check for iptables in the system 

```bash
rpm -qa | grep iptables
yum install iptables-services
```

check for iptables command and it's corresponding package 

```bash
which iptables
```
```bash
rpm -qf /usr/sbin/iptables        # will show which package brought this command
```

`you need to disable firewalld so that you can configure firewall via iptables`
```bash
systemctl status firewalld.service    
```
```bash
systemctl stop firewalld.service    
```
```bash 
systemctl disable firewalld.service     # completely disable firewalld
```
```bash 
systemctl mask <servicename>            # mask will send the service to /dev/null
```



```sh
iptables -L
```
```bash
iptables -n --line-numbers -L INPUT
```






