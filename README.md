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
mqtt.py
```

Test ezmesh api

```sh
api.py \
    -m set \
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
    -m get \
    -a nocconfig/ezmesh/get
```

Test segment api

```sh
api.py \
    -m get \
    -a nocconfig/segment/searchItem


api.py \
    -m get \
    -a nocconfig/segment/getItem/<uuid>


api.py \
    -m set \
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
