## NETWORK


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


**/etc/sysconfig/network-scripts/**       
> has dedicated files for network interface in centOS ets0 old linux 

 **/etc/network/interfaces**
 > has dedicated files for network interface in Debian 


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
