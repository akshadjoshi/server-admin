- **step 1: (installing)**

*see for the package* 

```bash
dpkg -l | grep "apache"
```
```bash
apt install apache2
```

- **step 2: (configure)**
**disable directory listing**

```bash

sed -i "s/Options Indexes FollowSymLinks/Options FollowSymLinks/" /etc/apache2/apache2.conf

# directory listing is enabled by default in apache webserver so the above cmd will disable it.
```

`now restart the service`

```bash
systemctl restart apache2.service

```
```bash
apt install php7.4

# or 

apt install php7.4 php7.4-common php7.4-mbstring php7.4-xmlrpc php7.4-soap php7.4-gd php7.4-xml php7.4-intl php7.4-mysql php7.4-cli php7.4-ldap php7.4-zip php7.4-curl
```

## configuring PHP on the webserver
```bash
vim /etc/php/7.4/apache2/php.ini

<things to edit>

/memory_limit         # set it to 512M

/max_execution        # set to 500 (takes value in seconds)
/max_input_vars
uncomment ;max_input_vars and set it to 10000 

/upload_max_filesize   # set it to 2048M

/post_max_size         # set it to 2048M
# post size defines the post request that is made/recieve


/allow_url_fopen      # must be On
```
`now restart the service`

```bash

systemctl restart apache2.service
```
```bash
vim /var/www/html/phpinfo.php
```

```php
<?php

// Show all information, defaults to INFO_ALL
phpinfo();

// Show just the module information.
// phpinfo(8) yields identical results.
phpinfo(INFO_MODULES);

?>

```
to check if php is configured properly call the page on web-browser
```php
<IP>/phpinfo.php
```
## mysql deployment

```bash
apt install gnupg
```

```bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb      

# mysql community server for debain 

# we are downloading the repo
```
```bash
apt install ./mysql-apt-config_0.8.24-1_all.deb

adding the repo to out repolist
```
**if the above command gives error install via bellow command**

```bash
sudo dpkg -i mysql-apt-config*
```
```bash
apt update
```

```bash
apt install mysql-community-server
```

```bash
systemctl restart mysql.service
```
```bash
systemctl enable mysql.service
```
```bash
systemctl restart apache2@.service
```

```bash
systemctl enable apache2@.service
```

**`login in into mysql to see if it is configured properly`**

```bash
mysql -u root -p 
```

## mysql remote login (root)

```mysql
edit the root privileges via phpmyadmin
# this is the qurey that runs in the background
CREATE USER 'root'@'%' IDENTIFIED WITH caching_sha2_password BY '***'; GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION; 


# you need to change password of the new root user which is created by query
```

## enable remote login internally
```mysql
vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
add this line at the bottom

```txt
bind-address	= 0.0.0.0
```

**`Install phpmyadmin`**

```bash

wget https://files.phpmyadmin.net/phpMyAdmin/5.2.0/phpMyAdmin-5.2.0-all-languages.zip

```
```bash
mv -v phpMyAdmin-5.2.0-all-languages /var/www/html/phpmyadmin
```
```bash
chown -Rv www-data:www-data phpmyadmin/

# the web user in debian is 'www-data' (for apache webserver)
# the web user in centos is 'apache' 

# the ownership on the webcontent should be of apache user
```


### wordpress installation and configuration

```bash
wget https://wordpress.org/latest.zip
```
```bash
mv -v wordpress /var/www/html/wordpress
```

```bash
chown -Rv www-data:www-data wordpress
```

### make wordpress database

```bash
make a new data base user in phpmyadmin and configure the wordpress with it


# this is the qurey that runs behind when you create a new user

CREATE USER 'wordpress'@'localhost' IDENTIFIED WITH caching_sha2_password BY '***';GRANT USAGE ON *.* TO 'wordpress'@'localhost';ALTER USER 'wordpress'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `wordpress`;GRANT ALL PRIVILEGES ON `wordpress`.* TO 'wordpress'@'localhost';GRANT ALL PRIVILEGES ON `wordpress\_%`.* TO 'wordpress'@'localhost'; 
```
**`name binding`**

```bash
 vim /etc/hosts
192.168.1.250	web-server mywordpress.local www.mywordpress.local
```

```bash
vim /etc/apache2/sites-available/mywordpress.conf



<VirtualHost *:80>
    DocumentRoot /var/www/html/wordpress/
	<Directory /var/www/html/wordpress/>
		Options FollowSymLinks
		AllowOverride All
		Order allow,deny
		allow from all
	</Directory>
	ErrorLog /var/log/apache2/wordpress-error_log
	CustomLog /var/log/apache2/wordpress-access_log common
</VirtualHost>
```
```sh

<VirtualHost *:80>
	ServerName wordpress.local
    DocumentRoot /var/www/html/wordpress/
	<Directory /var/www/html/wordpress/>
		Options FollowSymLinks
		AllowOverride All
		Order allow,deny
		allow from all
	</Directory>
	ErrorLog /var/log/apache2/wordpress-error_log
	CustomLog /var/log/apache2/wordpress-access_log common
	ServerAlias www.wordpress.local
</VirtualHost>
```
```bash
<VirtualHost *:80>
	ServerName mywordpress.local
    DocumentRoot /var/www/html/wordpress/
	<Directory /var/www/html/wordpress/>
		Options FollowSymLinks
		AllowOverride All
		Order allow,deny
		allow from all
	</Directory>
	ErrorLog /var/log/apache2/wordpress-error_log
	CustomLog /var/log/apache2/wordpress-access_log common
	ServerAlias www.mywordpress.local
</VirtualHost>
```

```bash
a2ensite mywordpress.conf 

# enable site

look in 

/etc/apache2/sites-sites-enabled

ls

# should show the site you made

```
```bash
systemctl restart apache2.service

```

```bash
sudo a2enmod rewrite
# or 
a2enmod rewrite
```

```bash
systemctl restart apache2.service

```


### now define the ip and domain on you pc to access it 

```bash
sudo vim /etc/hosts

#practical ip
192.168.1.250	www.mywordpress.local mywordpress.local
                                                        
```
**Note** - everything under `/var/www/html/*` should be owned by the **web server user** which is in this case **'www-data'**
