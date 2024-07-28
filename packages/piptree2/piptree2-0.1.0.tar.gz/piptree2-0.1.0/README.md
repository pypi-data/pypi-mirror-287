# piptree
piptree is a tool for visualizing the dependency tree of a pip installation. It is a wrapper around pip freeze, so it will only work with packages that are installed with pip.

# Usage
### install piptree
```bash
pip install piptree2
```

### list dependencies and children
```bash
piptree -l

piptree -l requests
```

### list dependencies and children to piptree.txt (requirements.txt)
```bash
piptree -l > piptree.txt

piptree -l > requirements.txt
```

### uninstall dependencies and children
```bash
piptree -r requests

piptree -r requests -y
```

### more options
```bash
piptree -h

usage: piptree [-h] [-v] [-f] [-t] [-l [LIST [LIST ...]]] [-r [REMOVE [REMOVE ...]]]

piptree is a tool for visualizing the dependency tree of a pip installation. It is a wrapper around pip freeze, so it will only work with packages that are installed with pip.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show this version number and exit
  -l [LIST [LIST ...]], --list [LIST [LIST ...]]
                        list dependencies and children
  -r [REMOVE [REMOVE ...]], --remove [REMOVE [REMOVE ...]]
                        remove dependencies and children
  -y, --yes             do not ask for confirmation of uninstall deletions
```
