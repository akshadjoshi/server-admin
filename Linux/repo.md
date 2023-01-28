```

epel           (Extra Packages for Enterprise Linux)
REMI repo      (Used to install and configure PHP) sudo rpm -ivh http://rpms.remirepo.net/enterprise/remi-release-7.rpm

RPM fusion     (Used to install Multimedia Packages)

EL repo        (has around 135 packages) > adding it might resolve dependency errors 
yum install https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm

NUX repo       (GUI tools for CentOS) > also helps in Desktop creation 
IUS repo       (provides newer versions of select software for RHEL and CentOS.)
Webtatic repo  (repository generally deals with the web hosting related packages)


yum repolist        # (will show enable list) 
yum list            # (avaliable package list)
yum repolist all    # (will update the repo)

To enable a repository, set enabled=1 in the corresponding repository configuration section in /etc/yum.repos.d/remi.repo.

```
DEBIAN 

debgen.simplylinux.ch   # (repo generator for debian distro)


NOTE :  *REMEMBER MORE PACKAGES MEANS LESS DEPENDENCY ERROR*

links : https://tecadmin.net/top-5-yum-repositories-for-centos-rhel-systems/
Links : https://access.redhat.com/sites/default/files/attachments/rh_yum_cheatsheet_1214_jcs_print-1.pdf

. Configuring Yum and Yum Repositories below links

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-configuring_yum_and_yum_repositories

https://www.redhat.com/sysadmin/add-yum-repository

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-setting_repository_options




REPO link

NUX repo
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
