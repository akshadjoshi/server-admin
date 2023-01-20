

## NETWORK

**`/etc/sysconfig/network-scripts/`**  has dedicated files for network interface in centOS ets0 old linux         
**`/etc/network/interfaces`**   has dedicated files for network interface in Debian

**ifconfig**

```bash
ifconfig -a       # to see the hidden interface
```
### To make changes in the interface (multipal IP's)
```bash
vim /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none                    # set this to dhcp and remove the lines that define static IP to get dynamic IP
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME=enp0s3                                       # interface name
UUID=6a9978c9-49cb-4d5b-8154-3edd52cd85eb
DEVICE=enp0s3
ONBOOT=yes                                          # when device starts it will get connected to internet (if set to yes)
IPADDR=192.168.1.210
PREFIX=24                                   # subnet
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

### one interface multiple IP's  (need when you configure webserver)

```bash
cp -v /etc/sysconfig/network-scripts/ifcfg-enp0s3 /etc/sysconfig/network-scripts/ifcfg-enp0s3:1

# the new virtual interface name should be added with ':'  

# you have to change the device identity and IP to set multiple IP on a single interface

vim vim /etc/sysconfig/network-scripts/ifcfg-enp0s3:1
```

```

TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME=enp0s3
UUID=6a9978c9-49cb-4d5b-8154-3edd52cd85eb
DEVICE=enp0s3:2                                   # this is what you need to change
ONBOOT=yes
IPADDR=192.168.1.202                              # and this too
PREFIX=24
GATEWAY=192.168.1.1
DNS1=8.8.8.8

```
### temporary IP

```bash
ifconfig {interfacename} <ip you want to assign>

```

```bash
ifconfig enp0s3 192.168.1.31/20       # temp IP with different subnet
```
```bash

ifconfig enp0s3 down        # to disable/stop an interface on hardware level

ifconfig enp0s3 up          # to enable it
```


**netstat**

```bash
netstat -ntup      # shows ports that a in use or ports that have connection established
```
```bash
netstat -nltup     # shows listening ports
```

```bash 
netstat -t        # will tell active and connected ports TCP
```
```bash
lsof -i -n            # will show details of network activities
lsof -i -n TCP        # will show TCP traffic
lsof -u ^root -n      # will show the data excluding root

```
```bash 
lsof -n -i UDP:67    # to see trafic on specific port
```

```bash

```

## PROCESS


```bash
jobs     # shows running commands in background 

fg      # to bring that background command in front

PRESS ctrl + c to kill 
```

```bash
ps -aux    # shows all process be it foreground or background
```

```bash
ps -e     #  shows terminal type process ID and command
```

```bash
ps -ejH   # shows process/commands and sub process or command in a branch format
```
```bash
ps -axjf  # show process and in branched format (GOOD WAY use this)
```
```bash
kill <process ID>
```
```bash
killall <processname>
```
```bash 
killall -r <name>   # regex give any name relating to the process and it will match the regex
```
you can use **htop** for process management

```bash 
htop -t     # will give output in branch format 
```

```bash 
htop -t -u <username>
```

```bash
htop -t -u <username> -p <PID>
```
```bash

```
