## Disk Management

```bash
cd /dev
```

```bash
ls -lha | grep br
```

```bash
blkid
```

```bash
lsblk
```

```bash
fdisk -l
```

```bash
 fdisk -l | grep sd
# hard drive partition and size
```

`if the partition is logical the value will start from 5`

`standarad is only 4 `

`after fomat UUID is assigen `




```bash
fdisk /dev/sdb
```

```bash
 fdisk /dev/sda 
# then follow the bellow command
# a cmd prompt will open 
m 
l # list known partition types with no.

```


to format in diff file system
```bash
mkfs
```


## Permanent Mount

- `list all the block devices and mount point`

```bash
lsblk
```

- `cmd to check the partition of hard-drive and their format type`
 
**If you see the partition diff to that of linux OS format it via**  disk tool

```bash
fdisk -l
```

**mount**

```bash
 mount /dev/nvme0n1p4 /mnt/newspace
```

**After successful format check the blkid to enter in fstab**

```bash
blkid
```

-  `now enter the partition in fstab `
- `also check for` the mouting point by lsblk

```bash
UUID=<UUID of new partition> /mnt/newspace ext4 defaults 0 0
```

