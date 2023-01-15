# ServerOS 
`red hat (.rpm)` `centOS, Fedora` 

`linux structure`
| user    | shell | kernel | hardware      
| ------- | ---   | -----  | --------
         
```bash
# shell is where user interation happens
# kernel: It is responsible for interacting with the hardware of a computer basically it acts as a bridge between the hardware and software.

# DIFF B/W kernel and shell
# WHERE AS A  Shell and Applications are built on top of the kernel, providing a way for the user to interact with the operating system
```
| Distribution | Package Format | Package Manager | OS      
| -------------| ---------------| --------------- | --------
| Debian       |  .deb          |    dpkg, apt    | kali, ubuntu   
| Red hat      |  .rpm          | rpm, yum        | fedora, centOS

```sh
nmtui   # a command line tool that is used for network configuration 
```
### rpm

**Architecture**   
|              |                |        
| -------------| ---------------| 
|    i386      |   32 bit       
| X86_64       |  64 bit        | 
| noarch       |  platform independent       |   

`A package contains`
Name | Version | Release | Architecture

package is a single file but when you install it, it places the file in various location or DIR

http://rpmfind.net/  **site to search for rpm packages**

https://yum-info.contradodigital.com/     **searchable resource to find awesome packages to install via yum**

### TYPE of rpm file

1. RPM - contains the compiled code
2. SRPM - contains the source code for a particular application

#### Dir
```sh
/var/lib/rpm  # (database files)
/etc/yum.repos.d/   # (Repo database)
```
### PACKAGES
 **core utils**  package has all the basic commands
 
 **net-tools** package has networking tools `like ifconfig`
 
 **psmisc** package will bring all the process management related commands
 
 ## RPM database queries
```bash
rpm -qa <packagename>   # Show all packages installed on the system
```
```bash
rpm -qi <packagename>   # to know details about installed package
rpm -qpi <packagename>  # to know about any package even not installed ones but you need the .rpm file of that tool

EXAMPLE:

[root@localhost tool]# ls
opera-uget-integrator-1.0.0-2.12.x86_64.rpm
[root@localhost tool]# rpm -qpi opera-uget-integrator-1.0.0-2.12.x86_64.rpm 
warning: opera-uget-integrator-1.0.0-2.12.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID 3dbdc284: NOKEY
Name        : opera-uget-integrator
Version     : 1.0.0
Release     : 2.12
Architecture: x86_64
Install Date: (not installed)
Group       : Productivity/Networking/Web/Utilities
Size        : 340
License     : GPL-3.0-or-later
Signature   : RSA/SHA256, Wed 31 Aug 2022 06:03:55 PM IST, Key ID b88b2fd43dbdc284
Source RPM  : uget-integrator-1.0.0-2.12.src.rpm
Build Date  : Wed 31 Aug 2022 06:03:41 PM IST
Build Host  : cloud102
Relocations : (not relocatable)
Packager    : https://bugs.opensuse.org
Vendor      : openSUSE
URL         : https://github.com/ugetdm/uget-integrator
Summary     : Integration of uGet with Opera
Description :
Integration of the uGet Download Manager with Opera.

```

```bash
rpm -ql <packagename>   # to know about the package placement in various dir

# List the files controlled by a package
```
```sh
rpm -qf <file/tool/cmd name> 
# to know which package is related to which (command) ----> package owning detail of Binary (executable file)

EXAMPLE:

[root@localhost ~]# rpm -qf /bin/nmtui
NetworkManager-tui-1.18.8-2.el7_9.x86_64
[root@localhost ~]# rpm -qf /bin/ssh
openssh-clients-7.4p1-22.el7_9.x86_64

# which package brought which command
[root@localhost tool]# rpm -qf /sbin/ifconfig 
net-tools-2.0-0.25.20131004git.el7.x86_64

```

`dependency`
```sh
rpm -qR <packagename>   # dependency needed to install a package or tool

ERROR to remember
root@localhost tool]# rpm -qR opera-uget-integrator-1.0.0-2.12.x86_64.rpm
package opera-uget-integrator-1.0.0-2.12.x86_64.rpm is not installed

EXAMPLE:

[root@localhost tool]# rpm -qR net-tools 
/bin/sh
libc.so.6()(64bit)
libc.so.6(GLIBC_2.14)(64bit)
libc.so.6(GLIBC_2.2.5)(64bit)
libc.so.6(GLIBC_2.3)(64bit)
libc.so.6(GLIBC_2.3.4)(64bit)
libc.so.6(GLIBC_2.4)(64bit)
libselinux.so.1()(64bit)
rpmlib(CompressedFileNames) <= 3.0.4-1
rpmlib(FileDigests) <= 4.6.0-1
rpmlib(PayloadFilesHavePrefix) <= 4.0-1
rtld(GNU_HASH)
systemd-units
rpmlib(PayloadIsXz) <= 5.2-1

```
```bash

rpm -qcf {/path/to/file}   # Display list of configuration files for a command

EXAMPLE:

[root@localhost tool]# rpm -qfc /bin/wget 
/etc/wgetrc

```
## RPM instal­lation commands

```bash
rpm -i { filena­me.rpm }   # Install the filename RPM package

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
```bash
rpm -U --test {filena­me.rpm}     # Test run of instal­lation without actually installing anything

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
yum groups install "Server with GUI"
OR
yum groups install "Graphical Administration Tools" "GNOME Desktop"
cat /etc/systemd/system/default.target
        
systemctl set-default graphical

systemctl isolate graphical.target

init 6

# By default after installing these packages, the default target should have automatically updated
# reboot the GUI will automatically be loaded.
systemctl get-default      # current default target 
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

# Debian

```bash
dpkg -l   # list of all the packeages installed 

dpkg -l | grep "ps"   
```

```bash
dpkg -s <packagename>   # give the package details/status 
dpkg -s psmisc

```













