```bash
sudo yum --enablerepo=remi-php74 install php php-bz2 php-mysql php-curl php-gd php-intl php-common php-mbstring php-xml

# need this to install packages regarding phpmyadmin
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

## phpmyadmin

```bash

yum install php php-common.x86_64 php-mcrypt.x86_64 php-cli.x86_64 php-opcache.x86_64 php-gd.x86_64 php-curl php-mysqlnd.x86_64 php-xml.x86_64 php-mbstring.x86_64 mysql-devel php-pear php-mbstring php-pecl-http php-pecl-curl php-session
```

```bash
wget https://files.phpmyadmin.net/phpMyAdmin/5.2.0/phpMyAdmin-5.2.0-all-languages.zip

unzip phpMyAdmin-5.2.0-all-languages.zip
```
```bash
mv phpMyAdmin-5.2.0-all-languages /var/www/html/phpmyadmin
```
```bash
vim /etc/httpd/conf/httpd.conf

```
**start [virtualhosting](https://github.com/akshadjoshi/OSCP/blob/main/Networking%20and%20Server%20Config/apache_webserver%20CentOS.md#virtual-host-binding) for phpmyadmin (via IP)**

```bash
<VirtualHost 192.168.1.201:80>
	DocumentRoot /var/www/html/phpmyadmin/
	DirectoryIndex index.php
</VirtualHost>
```
```bash
systemctl restart httpd.service
```
### disable selinux

```bash
vim /etc/sysconfig/selinux

SELINUX=enforcing

# change it to 

SELINUX=disabled
```

restart the PC

```
# Even if you don't change the ownership to apache user you can still call it on browser
# Remember to install relevant dependency package for phpmyadmin 
# if the service is configured properly check it via netstat
# dont forget to allow the port in firewall
```
```sh
 iptables -L INPUT --line-numbers -n
```
```bash
iptables -I INPUT 4 -p tcp --dport 80 -j ACCEPT
```

### Virtual Host BINDING

**by PORT**

```bash
Listen 6969
<VirtualHost 192.168.1.150:6969>
	DirectoryIndex index.html
	DocumentRoot /var/www/html/site1
</VirtualHost>


<VirtualHost 192.168.1.150>				# default port 80
	DirectoryIndex index.html
	DocumentRoot /var/www/html/site2
</VirtualHost>

```


# command to check syntax error

```bash
httpd -t
```
**by NAME**

```bash
#Listen 8080
<VirtualHost 192.168.1.150>
Servername ritesh.local
	DirectoryIndex index.html
	DocumentRoot /var/www/html/mouintain
ServerAlias www.ritesh.local
</VirtualHost>

Listen 6969
<VirtualHost 192.168.1.150:6969>
	DirectoryIndex index.html
	DocumentRoot /var/www/html/bitcoin
</VirtualHost>

`Give the dns server of your centOS in windows machine and browse the by the name specified in you centos.`
```
![on client](https://github.com/akshadjoshi/OSCP/blob/main/image/dns%20practical.png?raw=true)

**You all need to make changes in server's host file /etc/hosts**
![hostfile](https://github.com/akshadjoshi/OSCP/blob/main/image/on%20you%20centos%20os.png?raw=true)


**by TYPE**

```bash
<VirtualHost 192.168.1.200>
    SSLEngine on

    SSLCertificateFile /etc/pki/tls/certs/localhost.crt
    SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
        DocumentRoot /var/www/html/phpmyadmin/
        DirectoryIndex index.php
</VirtualHost>

```
<!-- https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-with-apache-on-a-centos-7-server -->
<!-- https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-centos-7 -->
z
