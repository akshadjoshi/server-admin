There are 4 steps/check list to configure a server be it DHCP, DNS or any other
1. see if the required package is installed or not
2. search the main config file that you need to edit and configure that file according to requirement
3. after configuration start the respective service
4. allow the service port in firewall

```
authoritative;
# specify network address and subnet mark
subnet 192.168.1.0 netmark 255.255.255.0{
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
port DHCP uses **udp 67 server side** ,**68 client side**
now allow the above port in firewall
```bash
vim /etc/sysconfig/iptables
```
```bash
systemctl restart iptables.service
```
```bash
iptables -n -L INPUT 
```
> dir
**/var/lib/dhcpd/dhcpd.leases**   # log file to check for ip's given by your dhcp server.
