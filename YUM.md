### YUM
`advance package managing tool for CentOS and RHEL`

```bash
yum deplist <toolname>     # to list the tool dependency & provide | Display dependencies for a package

EXAMPLE
# yum deplist nmap
#Loaded plugins: fastestmirror, langpacks
#Loading mirror speeds from cached hostfile
# * base: centos.excellmedia.net
# * epel: repo.extreme-ix.org
# * extras: centos.excellmedia.net
# * updates: centos.excellmedia.net
#package: nmap.x86_64 2:6.40-19.el7
#  dependency: /usr/bin/python
#   provider: python.x86_64 2.7.5-92.el7_9
#  dependency: libc.so.6(GLIBC_2.15)(64bit)
#   provider: glibc.x86_64 2.17-326.el7_9
#  dependency: libcrypto.so.10()(64bit)
#   provider: openssl-libs.x86_64 1:1.0.2k-25.el7_9
#  dependency: libcrypto.so.10(libcrypto.so.10)(64bit)
#  provider: openssl-libs.x86_64 1:1.0.2k-25.el7_9

```
```bash   
yum upgrade <toolname>        to upgrade a specific tool
```
```bash
yum distro-sync
# distribution-synchronization Synchronize installed packages to the latest available versions
```

```bash
yum provides nmap     # Find packages that provide the queried file (packages due to which you have that particular command)
#Loaded plugins: fastestmirror, langpacks
#Loading mirror speeds from cached hostfile
# * base: centos.excellmedia.net
# * epel: repo.extreme-ix.org
# * extras: centos.excellmedia.net
# * updates: centos.excellmedia.net
#2:nmap-6.40-19.el7.x86_64 : Network exploration tool and security scanner
#Repo        : base



#2:nmap-6.40-19.el7.x86_64 : Network exploration tool and security scanner
#Repo        : @base

```
```bash
yum groupinfo <PRESS TAB TWICE> # a group of packages which you need for a specific work

yum group info Development\ Tools  # will install various development languages in PC 
````
Links : https://access.redhat.com/sites/default/files/attachments/rh_yum_cheatsheet_1214_jcs_print-1.pdf
 
**. Configuring Yum and Yum Repositories** `below links`

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-configuring_yum_and_yum_repositories

https://www.redhat.com/sysadmin/add-yum-repository

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-setting_repository_options 

