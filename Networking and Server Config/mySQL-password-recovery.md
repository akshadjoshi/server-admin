## password reset ``(if root privilege is flushed by mistake)``


Refer to this : https://dba.stackexchange.com/questions/16397/cannot-grant-privileges-as-root
for centos 7

```bash
sudo systemctl stop mysqld
```


```bash
mysqld --skip-grant-tables &
```

`the above command will go in background`

```bash
mysql_upgrade
```

use this if above doesn't work

```bash
mysql_upgrade=FORCE
```

`if error occurs` read this:


The mysql_upgrade client is now deprecated. The actions executed by the upgrade client are now done by the server.
To upgrade, please start the new MySQL binary with the older data directory. Repairing user tables is done automatically. Restart is not required after upgrade.
The upgrade process automatically starts on running a new MySQL binary with an older data directory. To avoid accidental upgrades, please use the --upgrade=NONE option with the MySQL binary. **The option --upgrade=FORCE** is also provided to run the server upgrade sequence on demand.
It may be possible that the server upgrade fails due to a number of reasons. In that case, the upgrade sequence will run again during the next MySQL server start. If the server upgrade fails repeatedly, the server can be started with the --upgrade=MINIMAL option to start the server without executing the upgrade sequence, thus allowing users to manually rectify the problem.
`
> this works like charm : look below 


```bash
[root@localhost ~]# mysqld --skip-grant-tables &
[1] 1720
[root@localhost ~]# 2023-06-03T20:10:58.611494Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.33) starting as process 1720
2023-06-03T20:10:58.612656Z 0 [ERROR] [MY-010123] [Server] Fatal error: Please read "Security" section of the manual to find out how to run mysqld as root!
2023-06-03T20:10:58.612689Z 0 [ERROR] [MY-010119] [Server] Aborting
2023-06-03T20:10:58.612964Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.33)  MySQL Community Server - GPL.
mysql_upgrade=FORCE
```


```bash
sudo systemctl start mysqld
```

```bash
sudo systemctl start mysqld
```

- NOW the `mysql` installation will begin from scratch 

- grep the temp password (centos 7)

```bash
sudo grep 'temporary password' /var/log/mysqld.log
```

```bash
sudo mysql_secure_installation
```
