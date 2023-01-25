```bash
sudo yum --enablerepo=remi-php74 install php php-bz2 php-mysql php-curl php-gd php-intl php-common php-mbstring php-xml
```
## mysql installation in centOS 7

```bash

wget https://dev.mysql.com/get/mysql80-community-release-el7-7.noarch.rpm

yum install ./mysql80-community-release-el7-7.noarch.rpm


yum install mysql-server
```
```bash
sudo systemctl start mysqld

sudo systemctl start mysqld
```
#### NOTE : During the installation process, a temporary password is generated for the MySQL root user. Locate it in the `mysqld.log` with this command

```bash
sudo grep 'temporary password' /var/log/mysqld.log
```

## mysql configuration in centOS 7

```bash
sudo mysql_secure_installation

# you have to give the temprary pasword here so as to be promoted to make a new one
```
```bash
mysql -u root -p 

# try to login and run qurey
```


<!-- https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-with-apache-on-a-centos-7-server -->
<!-- https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-centos-7 -->
z
