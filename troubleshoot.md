**command to fix install (if repositaries are missing)**
```bash

 sudo apt --fix-broken install 

```


```bash
apt --fix-missing install
```

```bash
sudo apt satisfy 
```

```bash
apt list --manual-installed=true  # (to see the packages installed)
```


**if your GUI fails to load in Ubuntu** 

```bash
sudo apt purge gdm gdm3
```
```bash
sudo apt install gdm3 ubuntu-desktop
```
**to upgrade a single package**
```bash
--apt list upgradable  # will give you list of packages that can upgraded aka has new version
sudo apt --only-upgrade install <packagename/applicationname/toolname>

# this commands comes to play because sudo apt upgrade is not considered as ideal to use all the time on your pc 
```
