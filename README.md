# noc-config

nova noc-config

## Development guidelines

### pull plugins

```sh
opnsense-code plugins
```

### pull noc source code

```sh
cd /usr/plugins/devel
git clone https://github.com/nova-opnsense/noc-config-demo.git
git checkout develop
```

### build

```sh
make install clean
```

using `upgrade` for reinstalling

```sh
make upgrade clean
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
    -a nocconfig/ezmesh/set \
    -d '{
            "nocconfig": {
                "ezmesh": {
                    "Enabled": "1",
                    "SSID": "NovaIntechs",
                    "Password": "123"
                }
            }
        }'


api.py \
    -a nocconfig/ezmesh/get
```

Segment API

```sh
# get all segments
api.py \
    -a nocconfig/segment/searchItem

# search segment
api.py \
    -m post \
    -a nocconfig/segment/searchItem \
    -d 'current=1&rowCount=1&searchPhrase=<search phrase>' \
    -t 'application/x-www-form-urlencoded'

api.py \
    -a nocconfig/segment/getItem/<uuid>


api.py \
    -m post \
    -a nocconfig/segment/addItem \
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
