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
**`Install phpmyadmin`**

```bash

wget https://files.phpmyadmin.net/phpMyAdmin/5.2.0/phpMyAdmin-5.2.0-all-languages.zip

```
```bash
mv -v phpMyAdmin-5.2.0-all-languages /var/www/html/phpmyadmin
```

