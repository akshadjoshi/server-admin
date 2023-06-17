# php 7.4 installation in debain-12

```bash
apt update
```

```bash
apt -y install apt-transport-https lsb-release ca-certificates curl wget gnupg2
```

```bash
wget -qO- https://packages.sury.org/php/apt.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/sury-php-x.x.gpg
```

```bash
sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" \
> /etc/apt/sources.list.d/php.list'
```

```bash
apt update
```

```bash
apt-cache policy php7.4
```

```bash
apt install php7.4
```

```bash
apt install php7.4 php7.4-common php7.4-mbstring php7.4-xmlrpc php7.4-soap php7.4-gd php7.4-xml php7.4-intl php7.4-mysql php7.4-cli php7.4-ldap php7.4-zip php7.4-curl

```


```bash
vim /etc/php/7.4/apache2/php.ini
```



