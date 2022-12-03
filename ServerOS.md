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
```sh
rpm -qF <file/tool name> # to know which package is related
# to which (command) ----> package owning detail of Binary (executable file)
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









