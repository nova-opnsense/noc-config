```bash

ssh-keygen
eval `ssh-agent -c`
ssh-add ~/.ssh/id_rsa

```

~/.ssh/config

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa

```
