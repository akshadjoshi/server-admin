
# awk 

```bash

ps -aux | awk '$1=="root"{print $1,"--",$11}'   **(to see the processes run by root)**

```

# tail
```bash
tail -n3 /etc/passwd /etc/shadow /etc/group

**-n** switch helps us print sepcific number of lines
```
# grep
```bash
grep '$_' * | grep -v '_SERVER\|_SESSION'
```
`the \| is basically OR and * is for show all`


# find

```bash
find /dir/to/search -name "file-pattern" -print | xargs grep "word-to-search"
```
