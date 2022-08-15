# ubuntu-server

https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-live-server-amd64.iso
https://releases.ubuntu.com/18.04.6/ubuntu-18.04.6-live-server-amd64.iso

# ubuntu-desktop

https://releases.ubuntu.com/18.04.6/ubuntu-18.04.6-desktop-amd64.iso
https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso
https://releases.ubuntu.com/22.04/ubuntu-22.04-desktop-amd64.iso

# debian https://cdimage.debian.org/mirror/cdimage/archive/

https://cdimage.debian.org/mirror/cdimage/archive/8.11.1/amd64/iso-cd/debian-8.11.1-amd64-netinst.iso
https://cdimage.debian.org/mirror/cdimage/archive/9.13.0/amd64/iso-cd/debian-9.13.0-amd64-netinst.iso
https://cdimage.debian.org/mirror/cdimage/archive/10.12.0/amd64/iso-cd/debian-10.12.0-amd64-netinst.iso
https://cdimage.debian.org/mirror/cdimage/archive/11.2.0/amd64/iso-cd/debian-11.2.0-amd64-netinst.iso

# freebsd

https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.1/FreeBSD-13.1-RELEASE-amd64-bootonly.iso

# install bhyve

```sh

# lock pkg and install opnsense packages
pkg lock -y pkg
pkg install -y git nano
# tmux screen

# install freebsd packages
echo "FreeBSD: { enabled: yes }" > /usr/local/etc/pkg/repos/FreeBSD.conf
pkg install -y vm-bhyve grub2-bhyve bhyve-firmware
echo "FreeBSD: { enabled: no }" > /usr/local/etc/pkg/repos/FreeBSD.conf

# create vm directory, replace 'zroot' to match your system
zfs create zroot/vm
sysrc vm_enable="YES"
sysrc vm_dir="zfs:zroot/vm"

# show to double check
sysrc -A | grep vm_

/*--------------------
vm_dir: zfs:zroot/vm
vm_enable: YES
--------------------*/

vm init
cp /usr/local/share/examples/vm-bhyve/* /zroot/vm/.templates/

# create switch
vm switch create public

# show to double check
vm switch list

/*--------------------
NAME    TYPE      IFACE      ADDRESS          PRIVATE  MTU  VLAN  PORTS
public  standard  vm-public  192.168.80.1/24  no       -    -     -
--------------------*/

vm switch add public alc0 # igb1

### add address
vm switch address public 192.168.80.1/24

### for NAT
sysrc gateway_enable="YES"
sysrc pf_enable="YES"

### nat on alc0 from {192.168.80.0/24} to any -> (alc0)

vm iso https://releases.ubuntu.com/18.04.6/ubuntu-18.04.6-live-server-amd64.iso

# edit config file if necessary:
nano /zroot/vm/.templates/ubuntu.conf

/*--------------------
loader="grub"
cpu=4
memory=2048M
network0_type="virtio-net"
network0_switch="public"
disk0_type="virtio-blk"
disk0_name="disk0.img"
disk0_size="30G"
grub_run_dir="/grub"
grub_run_partition="2"
debug="yes"
--------------------*/

# create [-d datastore] [-t template] [-s size] [-m memory] [-c vCPUs] <name>
vm create -t ubuntu ub

vm install ub ubuntu-18.04.6-live-server-amd64.iso

vm console ub

# (to disconnect, send ~. to exit the console session)

# vm control
vm start <vm_name>
vm stop <vm_name>
vm poweroff <vm_name>
vm destroy <vm_name>

```

```
vm iso https://cdimage.debian.org/mirror/cdimage/archive/10.12.0/amd64/iso-cd/debian-10.12.0-amd64-netinst.iso
nano /zroot/vm/.templates/debian.conf
vm create -t debian debianguest
vm install debianguest debian-10.12.0-amd64-netinst.iso
vm console debianguest

```

# refs

- https://github.com/churchers/vm-bhyve/wiki/NAT-Configuration
- https://github.com/churchers/vm-bhyve/blob/master/sample-templates/config.sample

```sh
# guest - ubuntu
sudo tcpdump -i enp0s5

netstat -4rn
/*--------------------
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.80.1    0.0.0.0         UG        0 0          0 enp0s5
192.168.80.0    0.0.0.0         255.255.255.0   U         0 0          0 enp0s5
--------------------*/

ip route show
/*--------------------
default via 192.168.80.1 dev enp0s5 proto static
192.168.80.0/24 dev enp0s5 proto kernel scope link src 192.168.80.123
--------------------*/

route -n
/*--------------------
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.80.1    0.0.0.0         UG    0      0        0 enp0s5
192.168.80.0    0.0.0.0         255.255.255.0   U     0      0        0 enp0s5
--------------------*/


# host - opnsense
tcpdump -i igb1

traceroute 192.168.80.123
/*--------------------
traceroute to 192.168.80.123 (192.168.80.123), 64 hops max, 40 byte packets
 1  192.168.80.123 (192.168.80.123)  0.423 ms  0.202 ms  0.162 ms
--------------------*/

netstat -4rn
/*--------------------
Routing tables

Internet:
Destination        Gateway            Flags     Netif Expire
default            192.168.3.1        UGS        igb0
8.8.4.4            link#2             UHS        igb0
8.8.8.8            link#2             UHS        igb0
127.0.0.1          link#10            UH          lo0
192.168.1.0/24     link#1             U          alc0
192.168.1.1        link#1             UHS         lo0
192.168.3.0/24     link#2             U          igb0
192.168.3.143      link#2             UHS         lo0
192.168.80.0/24    link#3             U          igb1
192.168.80.1       link#3             UHS         lo0
--------------------*/

```
