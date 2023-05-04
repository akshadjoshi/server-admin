
```bash
yum install squid*
```

#### SSL cert generation

```bash
mkdir /etc/squid/ssl_cert
```

`change the ownership of dir /etc/squid/ssl_cert from root to squid`

```bash
chown squid:squid /etc/squid/ssl_cert/
# can use the bellow dir
/etc/pki/tls/certs/ssl_certs
```

`change the permission`

```bash
chmod 700 /etc/squid/ssl_cert/
```

`key generation`

```bash
openssl req -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout myCA.pem -out myCA.pem
```

`extracting CA cert out of the key generated`
`the cert extracted will be encrypted and will be placed in browser`

```bash
openssl x509 -in myCA.pem -outform DER -out myCA.der
```

create a strong Diffie-Hellman group
`initialize key` do it right outside the folder /etc/squid

```bash
openssl dhparam -outform PEM -out dhparam.pem 2048
```

`db creation`

```bash
/usr/lib64/squid/ssl_crtd -c -s /var/lib/ssl_db
```

`change the owner of the db created`
```bash
chown -R squid:squid /var/lib/ssl_db/
```

`check SELinux status:` should be disabled

```bash
sestatus
```

bind
```sh
<VirtualHost 192.168.1.200>
    SSLEngine on

    SSLCertificateFile /etc/pki/tls/certs/localhost.crt
    SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
        DocumentRoot /var/www/html/phpmyadmin/
        DirectoryIndex index.php
</VirtualHost>

```
#### squid configuration
 
```bash
shutdown_lifetime 0 seconds
http_port  3126 intercept
https_port 3127 intercept ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=16MB cert=/etc/squid/ssl_cert/myCA.pem
http_port  3128 ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=16MB cert=/etc/squid/ssl_cert/myCA.pem
ssl_bump server-first all
# And finally deny all other access to this proxy
http_access deny all

# Squid normally listens to port 3128
#http_port 3128
```

```bash
systemctl restart squid
```

`check if the service is running on defined ports (internally) `

```bash
netstat -nltup
```

`enable IP forwarding`

```bash
vim /etc/sysctl.d/ipv4_forward.conf
```

`add this line to` ipv4_forward.conf 
`this basically transerfers the traffic of one interface to another`

```bash
net.ipv4.ip_forward = 1
```

`allow the ports in iptables firewall`

```bash
vim /etc/sysconfig/iptables
```

```bash
-A INPUT -p tcp --dport 3126 -j ACCEPT
-A INPUT -p tcp --dport 3127 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 3128 -j ACCEPT
```

```bash
systemctl restart iptables.service 
```

```bash
iptables -L INPUT --line-numbers -n
```

