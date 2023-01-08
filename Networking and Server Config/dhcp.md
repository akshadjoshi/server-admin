There are 4 steps/check list to configure a server be it DHCP, DNS or any other
1. see if the required package is installed or not
2. search the main config file that you need to edit and configure that file according to requirement
3. after configuration start the respective service
4. allow the service port in firewall


- **step 1** **(installing)**
```bash
yum install dhcp
rpm -qa | grep dhcp		#to check for the packages installed 

```
- **step 2**  **(search for main config file and configure it)**
```bash
rpm -qc dhcp
```
DHCP Server Configuration file 
**`/etc/dhcp/dhcpd.conf`**
(it is empty by default)

```bash 
nano /etc/dhcp/dhcpd.conf
# use nano to copy paste the configuration

ctrl + o (to save in nano)
```

CONFIGURATION :-
```
authoritative;
# specify network address and subnet mask
subnet 192.168.1.0 netmask 255.255.255.0{
	# specify the range of lease IP address
	range 192.168.1.50 192.168.1.250;
	# specify default gateway
	option routers 192.168.1.1;
	# DNS servers for name resolution
	option domain-name-servers 8.8.8.8, 8.8.4.4;
	# specify broadcast address
	option broadcast-address 192.168.1.255;
	# default lease time it takes in second
	default-lease-time 600;
	# max lease time
	max-lease-time 7200;
}
```
- **step 4** **(allow the service port in firewall)**

port DHCP uses udp 67 server side ,68 client side
now allow the above port in firewall
```sh
vim /etc/sysconfig/iptables
```
```sh
systemctl restart iptables.service
```
```bash
iptables -n -L INPUT 
```
<B><SUP>log file to check for ip's given by your dhcp server.</SUP>

**` /var/lib/dhcpd/dhcpd.leases`**		

	
#### static IP to client 
	
	
	
```bash
authoritative;
        # specify network address and subnet mark
        subnet 192.168.1.0 netmask 255.255.255.0{
        # specify the range of lease IP address
        range 192.168.1.240 192.168.1.250;
        # specify default gateway
        option routers 192.168.1.1;
        # DNS servers for name resolution
        option domain-name-servers 8.8.8.8, 8.8.4.4;
        # specify broadcast address
        option broadcast-address 192.168.1.255;
        # default lease time it takes in second
        default-lease-time 600;
        # max lease time
        max-lease-time 7200;
}

host windows {
    hardware ethernet    <computer's mac address>;
    fixed-address        192.168.1.242;
    max-lease-time       84600; 
}

	
```
	
	
