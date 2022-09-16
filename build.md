## install virtualBox

## install FreeBSD 13.1 on virtualBox

download: https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.1/

### NAT port for ssh

| name | protocol | host ip | host port | guest ip | guest port |
| ---- | -------- | ------- | --------- | -------- | ---------- |
| SSH  |          |         | 2022      |          | 22         |


## build opnsense

```
pkg lock pkg
pkg install git nano

cd /usr
git clone https://github.com/opnsense/tools

cd tools
make update


```
