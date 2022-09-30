# noc-config

A plugin for OPNsense

---

## Development guidelines

### pull plugins

```sh
opnsense-code plugins

```

### pull noc source code

```sh
cd /usr/plugins/devel
git clone https://thanhhai135@bitbucket.org/novaintechs/noc-demo.git

cd noc-demo
git checkout develop

```

### build

install

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make install clean

```

using `upgrade` for reinstalling

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make upgrade clean

```

build the package `/usr/plugins/devel/noc-demo/work/pkg/os-noc-demo-1.0_1.txz`

```sh
# root@nova:/usr/plugins/devel/noc-demo #
make package
ls work/pkg/

```

### running

restart config daemon

```sh
service configd restart

```

run command

```sh
configctl noc init

configctl noc ezmesh

configctl noc startmosquitto
configctl noc stopmosquitto

configctl noc startclient
configctl noc stopclient

```

### testing

Test ezmesh config

```sh
ezmesh.py

```

Test mqtt connection

```sh
mqtt-test.py

```

Test API

`usage: api.py [-h] [-m METHOD] -a API [-d DATA] [-t CONTENTTYPE]`

Ezmesh API

```sh
api.py \
    -m post \
    -a noc/ezmesh/set \
    -d '{
            "noc": {
                "ezmesh": {
                    "Enabled": "1",
                    "SSID": "NovaIntechs",
                    "Password": "123"
                }
            }
        }'


api.py \
    -a noc/ezmesh/get
```

Segment API

```sh
# get all segments
api.py \
    -a noc/segment/searchItem


# search segment
api.py \
    -m post \
    -a noc/segment/searchItem \
    -d 'current=1&rowCount=1&searchPhrase=<search phrase>' \
    -t 'application/x-www-form-urlencoded'


api.py \
    -a noc/segment/getItem/<uuid>


api.py \
    -m post \
    -a noc/segment/addItem \
    -d '{
            "segment":{
                "enabled":"1",
                "hubId":"123",
                "name":"123",
                "lastUpdate":"123",
                "status":"123"
            }
        }'

```

## python develop environment

Check version

```sh
python3 --version
# Python 3.9.13

opnsense-version
# NOC 22.7.4_2 (amd64/OpenSSL)

```

Build/Install pip

```sh
opnsense-code ports

cd /usr/ports/devel/py-pip
make install clean

pip --version
# pip 22.2.2 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)

```

Generates requirements

```sh
pip install pipreqs
pipreqs --force src/opnsense/scripts/OPNsense/Noc

```

Install dependencies from requirements.txt

```sh
pip install -r src/opnsense/scripts/OPNsense/Noc/requirements.txt

```

---

## About

hai.nt <hai.nt@novaintechs.com>

---
