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
