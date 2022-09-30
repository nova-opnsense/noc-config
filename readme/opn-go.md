```sh

cd /usr

pkg install --yes wget

wget https://go.dev/dl/go1.19.1.freebsd-amd64.tar.gz

tar xvf go1.19.1.freebsd-amd64.tar.gz

mv go /usr/local/

mkdir /root/go

nano ~/.profile
-----------------------
GOROOT=/usr/local/go
export GOROOT
GOPATH=$HOME/go
export GOPATH
PATH=$GOPATH/bin:$GOROOT/bin:$PATH
export PATH
-----------------------

reboot

```
