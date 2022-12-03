# ServerOS 
`red hat (.rpm)` `centOS, Fedora` 

`linux structure`
| user    | shell | kernal | hardware      
| ------- | ---   | -----  | --------
         
```bash
# shell is where user interation happens
```
| Distribution | Package Format | Package Manager | OS      
| -------------| ---------------| --------------- | --------
| Debian       |  .deb          |    dpkg, apt    | kali, ubuntu   
| Red hat      |  .rpm          | rpm, yum        | fedora, centOS

```sh
nmtui   # a command line tool that is used for network configuration 
```
#### rpm

**Architecture**   
|              |                |        
| -------------| ---------------| 
|    i386      |   32 bit       
| X86_64       |  64 bit        | 
| noarch       |  platform independent       |   

`A package contains`
Name | Version | Release | Architecture

http://rpmfind.net/  **site to search for rpm packages**

https://yum-info.contradodigital.com/     **searchable resource to find awesome packages to install via yum**

#### Dir
```sh
/var/lib/rpm  # (database files)
/etc/yum.repos.d/   # (Repo database)
```
### PACKAGES
 **core utils**  package has all the basic commands
 
 **net-tools** package has networking tools `like ifconfig`
 
 ### Commands
```bash
rpm -qa <packagename>   # to know installed app package
```
```bash
rpm -qi <packagename>   # to know about package
rpm -qpi <packagename>  # to know about any package even not installed ones
```

```bash
rpm -ql <packagename>   # to know about the package placement in various dir
```
```sh
rpm -qR <packagename>   # dependency needed to install a package or tool
```
```bash

rpm -qcf {/path/to/file}   # Display list of configuration files for a command

EXAMPLE
[root@localhost ~]# rpm -qcf /usr/bin/bash
/etc/skel/.bash_logout
/etc/skel/.bash_profile
/etc/skel/.bashrc

```
```sh
rpm -qf <file/tool name> # to know which package is related
# to which (command) ----> package owning detail of Binary (executable file)

EXAMPLE
[root@localhost ~]# rpm -qf /bin/nmtui
NetworkManager-tui-1.18.8-2.el7_9.x86_64
[root@localhost ~]# rpm -qf /bin/ssh
openssh-clients-7.4p1-22.el7_9.x86_64

# which package brought which command
```
```sh
rpm -Vv <packagename>   # details about whether a package was modified or not
```
```sh
rpm -e <packagename>    # to remove package
```
```sh
rpm --nodeps -ivF <packagename>    to  *install* and **resolve dependency error**
```

```sh
rpm -Uvh <packagename>      # to upgrade
```

```sh
yum repolist all          # to show all the avaliable repo on system you can also check the status of the repo via this cmd
```

> note : environment group gives graphic 


#### minimal to GUI (centOS)

```sh 
nmtui   
```
`give a static IP to your centOS via above cmd & take SSH connection`

```sh
yum -y update
yum search epel   # eltra package for enterprise linux epel is repolist
yum install epel-release.noarch
yum install net-tools   # Basic networking tools
yum install bash* # press TAB
yum install vim
```
```bash
yum update 
yum groups list
yum groups install "Graphical Administration Tools" "GNOME Desktop"
cat /etc/systemd/system/default.target
systemctl set-default graphical
init 6
```

### YUM
`advance package managing tool for CentOS and RHEL`

```bash
yum deplist <toolname>     # to list the tool dependency & it's provider | Display dependencies for a package

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











