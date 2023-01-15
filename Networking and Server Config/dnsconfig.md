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

### cache only DNS server

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

DNS runs on port **53**

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

