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
## iptables

#### concept

OUTPUT - source me IP output chain

INPUT  - hum pe attack lag raha hain (destination me humhara IP)

FORWARD CHAIN  it replaces IP eg IP changed to port 80



```sh
iptables -L
```
