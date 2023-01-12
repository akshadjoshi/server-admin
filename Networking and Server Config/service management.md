Service maintains our Appication
### Old Methord
<B><sub>service maintained via</sub> **`/etc/init.d/`**
  
```bash 
  ls /etc/init.d/<PRESS TAB TWICE> 
# to see the services maintained/run from this directory  
```
  
```bash
  /etc/init.d/cron status       # will tell you the status of that particular service or appication
  ```
  
  the remaining files go in `/usr/lib/systemd/system`   `` on this location you will get all the service files``
  
```bash
  
 ls /usr/lib/systemd/system
 # to see the service file
  
 Example:-
  
  Created symlink /etc/systemd/system/multi-user.target.wants/apache2.service → /lib/systemd/system/apache2.service.
 ```
  </B>
  
```
  you can not directly call a service if it does not have an execution permission
  example:
  
 ls -lha | grep httpd
-rw-r--r--.  1 root root  752 Jan 13  2022 httpd.service
  ```
```bash
  chkconfig --list # run level command
  ```
  
  ## NEW Methord
 
  in new methord service is maintained by **`/usr/lib/systemd/system`**
  
  ```bash
  systemctl --type=service        # will show all the services
  ```
  
  ```bash
  systemctl --type=service --state=running    # will show the services that are running 
  ```
  
  ```bash
   systemctl --type=service --state=exited      # will show the status of exited service
  ```
  ```bash
  systemctl list-units --type # PRESS TAB
  ```
  
  #### subcommand
  
  ```bash
  systemctl list-units --type=service
  ```
  ```bash
  systemctl list-units --type=service --state=running | grep ssh
  
  # cmd to grep a particular service
  ```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
