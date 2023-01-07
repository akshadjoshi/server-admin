## iptables

<!-- #### concept

OUTPUT - source me IP output chain

INPUT  - hum pe attack lag raha hain (destination me humhara IP)

**INPUT** - data jab humhare server pe aaraha ho. Jab hum par attack lagega toh data hum par aae ga
(jo bhi packets humhare pass aaegay usme destination me humhara IP hoga. aur jab bhi **destination** me humhara IP hoga hum INPUT chain ko dhekhegay)**


FORWARD CHAIN  it replaces IP eg IP changed to port 80

**FORWARD** - WHEN destination me router ka IP (i.e aap ka ip)toh inbound traffic. But when router ne packet liya aur internal PC pe forward kardiya or another kisi server par send kardiya

ROUTER packet ka source and destination modify karega aur usse aage forward kardega rather than consuming it 

eg : router ki port  80 pe jo traffic aaraha hain hum chahate hain ki vo 8080 par chala ja e toh iss senario ke liye FORWARD rule lagaegay

it can forward the packet/traffic internally, external, in the lan. packet ko utilize nahi kar ta modify and forward --> 


**check for iptables in the system** 

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


iptables main configuration file **`/etc/sysconfig/iptables`**


```sh
iptables -L
```
```bash
iptables -n --line-numbers -L INPUT
```

```bash
iptables -A INPUT -p tcp --dport 2222 -j ACCEPT       
# it won't work because the sequence is important. You need to specify the port above the REJCET line
# -A this switch will by default add the port to the end of the list bellow the REJECT 
```
`switches` `-A append or add and chain` `-p protocol` `--dport port to allow` `-j ACCEPT OR REJECT `

```bash
iptables -I INPUT -p tcp --dport 2222 -j ACCEPT        # cmd to allow or inser a port in firewall 

> this command will by default insert the port at the top of the list (among the 5 rules) 
```


```bash
iptables -D INPUT <chain number>						# to delete a chain from the table 	
           <chain>
```
### ERRORS
1. when the **port is allowed in firewall via iptables** but **service is not running on the server**

```bash
$ nc -v 192.168.1.200 9001                                                                                                                              1 
192.168.1.200: inverse host lookup failed: Unknown host
(UNKNOWN) [192.168.1.200] 9001 (?) : Connection refused
 
```
2. when the **port is not allowed in firewall via iptables** but **service is running on the server**

```bash
$ nc -v 192.168.1.200 9001                                                                                                                              1 
192.168.1.200: inverse host lookup failed: Unknown host
(UNKNOWN) [192.168.1.200] 9001 (?) : No route to host

```

#### Note : the concept of iptables is comment out by me because of linguistic reasons see this page in raw form to reveal the concept 

