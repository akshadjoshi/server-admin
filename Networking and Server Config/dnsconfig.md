step 1: look for the package in the machine/server

```bash
rpm -qa | grep bind
bind-utils-9.11.4-26.P2.el7_9.10.x86_64   # has all dns client tools
```
```bash
yum install bind-utils    # cmd to install dns client tool

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

