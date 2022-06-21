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
make install
```

using `upgrade` for reinstalling

```sh
make upgrade
```
