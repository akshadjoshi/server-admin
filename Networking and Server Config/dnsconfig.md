**step 1:** look for the package in the machine/server

```bash
rpm -qa | grep bind
bind-utils-9.11.4-26.P2.el7_9.10.x86_64   # has all dns client tools
```
```bash
yum install bind-utils          # cmd to install dns client tool

# it brings command like nslookup,dig
 ``` 
 ```bash
 rpm -ql bind-utils-9.11.4-26.P2.el7_9.10.x86_64
 
rpm -ql <packagename>       # will give you the details of all the files that came along with the package.

# it is a client tool so it does not have configuration file
 ```
 #### dig
 
```sh
dig   # this will give you the details of rooting servers

# there are 13 rooting servers accross the world (a-m)
```
```bash
dig google.com @64.6.64.6

dig <domain name> @<server which you want to resolv query from>
```
```bash
dig www.google.com +short   # will give short answer (by default it gives A record)
```
```bash
dig google.com +short       # will give A record 
```
```bash
dig google.com ns +noall +answer  # will give NS record and answer field of query

# you can use it but 'short' is better;
```
```bash
dig -f <file that contain domain names> +short
```
```bash
dig -x 8.8.8.8   # will bring PTR record
# PTR record is basically when you have IP and want to know its Domain
```
**step 2: Find the configuration file and configure it**
### cache only DNS server	(comes under non-authoritive server)

```bash
vim /etc/hostname
```
```bash
cat /etc/resolv.conf     # DNS infomation   
```

to configure DNS you see **bind** package 

```bash
rpm -qc bind-9.11.4-26.P2.el7_9.10.x86_64

# the config files that you will see after running the -qc are not the only configuration files that come with the package 
# they are just the main ones
```
**`/etc/named*`** all the files that start with **named** are main files

ALL the *files* that are in under the name **`/var/named/`** are also configuration files

```bash
cat /etc/named.conf
```



vim **/etc/named.conf**

```bash
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//
// See the BIND Administrator's Reference Manual (ARM) for details about the
// configuration located in /usr/share/doc/bind-{version}/Bv9ARM.html

options {
	listen-on port 53 { 127.0.0.1; 192.168.1.200; };                   # this is where you mention your server IP so that network client can listen/access
	listen-on-v6 port 53 { ::1; };
	directory 	"/var/named";                                             # this is where in holds the zone file
	dump-file 	"/var/named/data/cache_dump.db";                          # WILL build cache here coz it's a cache only dns server
	statistics-file "/var/named/data/named_stats.txt";
	memstatistics-file "/var/named/data/named_mem_stats.txt";
	recursing-file  "/var/named/data/named.recursing";
	secroots-file   "/var/named/data/named.secroots";
	allow-query     { localhost; 192.168.1.0/24; };      # who can query (default is localhost) but we want our network to query so mention network here  

	/* 
	 - If you are building an AUTHORITATIVE DNS server, do NOT enable recursion. 
	 - If you are building a RECURSIVE (caching) DNS server, you need to enable 
	   recursion. 
	 - If your recursive DNS server has a public IP address, you MUST enable access 
	   control to limit queries to your legitimate users. Failing to do so will
	   cause your server to become part of large scale DNS amplification 
	   attacks. Implementing BCP38 within your network would greatly
	   reduce such attack surface 
	*/
	recursion yes;

	dnssec-enable yes;
	dnssec-validation yes;

	/* Path to ISC DLV key */
	bindkeys-file "/etc/named.root.key";

	managed-keys-directory "/var/named/dynamic";

	pid-file "/run/named/named.pid";
	session-keyfile "/run/named/session.key";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {                         # internet records
	type hint;
	file "named.ca";                     # 13 routing server is maintain here
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";

```

**step 3 : start the service**


```bash
systemctl status named.service		# named is the service name for DNS server and bind is the package
```
```bash 
systemctl restart named.service		# start the service
```

```bash
netstat -nltup				# check if the service is running on the port be it default or defined

# if you see dnsmasq don't get confused because its a internal used service has nothing to do with your DNS server conf
# look for your IP and localhost 
```
to check if DNS is configured properly resolve a domain via localhost


```bash
dig googl.com @127.0.0.1		# resolving query via localhost after DNS config
```
when you conf DNS nslookup and dig cmd don't use your PC cache it used server cache
but when you seach something on browser it uses PC cache

**step 4: Allow the port in firewall**
DNS runs on port **53** of udp
```bash
vim /etc/sysconfig/iptables

```

`if you will not allow the port you can't resolve the query from any other PC in the LAN because the service is running internally` 
THIS IS THE **ERROR** YOU WILL SEE ON OTHER PC
```sh
└─$ nslookup facebook.com 192.168.1.200                                                                                                                  10 ⨯
;; communications error to 192.168.1.200#53: timed out
Server:		192.168.1.200
Address:	192.168.1.200#53

** server can't find facebook.com: SERVFAIL
```

```bash

iptables -I INPUT 4 -p udp --dport 53 -j ACCEPT			# this will allow the port in firewall temporarily

# INPUT 4 WILL ADD IT ON NO. 4 AND THE EXISTING 4TH NO. LINE WILL ON 5TH 
```



> THIS ENDS CACHE ONLY DNS SERVER CONFIG


## Master/Primart Nameserver (Forward zone)
`when you have the domain name and you need IP you use FORWARD zone`

```bash
hostname		# the zone you are going to make should get resolved here

# it is NOT necessary that you need to set FQDN to resovle 
```

```bash
vim /etc/hosts		# bind the hostname with IP
```
```bash

vim /etc/named.rfc1912.zones	# this is where you make and maintain zones
/var/named			# this is where zone data or zone files will be here 
# this is the file whose inclusion you will see in the main file
```

```bash
zone "cipher.local" IN {			# in "you need to define zones"
        type master;				# what is the zone master or salve is to be defined here (primary or secondary)
        file "forward.cipher.local";	# zone file (the record of this zone) location /var/named make the file here under the name specified by you 
        allow-update { none; };
};
  
```



```bash
cp -v named.localhost forward.cipher.local

```
now give the access of this file to **named group**

```bash
chgrp named forward.cipher.local
```
```bash
vim forward.cipher.local
# wherever you see @ this denotes FQDN of you local PC
# where there is @ your nameserver will come on that place if FQDN is no set
# basically @ holds the value of your nameserver, remove @ and type nameserver/hostname/FQDN 
```
```bash
$TTL 1D
@	IN SOA	ns1.cipher.local. rname.invalid. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	127.0.0.1
	AAAA	::1

# rname is responsible name server/or person name
```
**ERROR detection**

```bash
named-checkconf		# to check for errors in /etc/named.config
```
```bash
named-checkzone cipher.local /var/named/forward.cipher.local
		 (zonename)
# to check for error in zone file 
```








