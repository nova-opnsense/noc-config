
```
# https://clockworkbird9.wordpress.com/2017/11/20/dissecting-openwrt-4-lib-functions-network-sh/
# test.sh


------------------------------------------

#!/bin/sh

. /lib/functions/network.sh

if [ "$#" -ne 1 ];then
    echo "Syntax:$0 interface"
    exit 1
fi

network_get_ipaddr ip $1
network_get_gateway gw $1 true
echo ip: $ip
echo gw: $gw

------------------------------------------


```