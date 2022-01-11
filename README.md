# i3-show-desktop
Show desktop in i3. Works by switching to empty workspace on each monitor. These empty workspaces have to be mapped to monitors in advance.

## Build requirements
- Python 3.9
- [Poetry](https://python-poetry.org/)
- Make

## Installation
Clone repository and install the package:
```bash
git clone https://github.com/justpwned/i3-show-desktop
cd i3-show-desktop
make package-install
```
Add workspace-output mappings to i3 config:
```
i3-show-desktop --config >> ~/.config/i3/config
```
Create a keyboard binding:
```
echo "bindsym $mod+d exec --no-startup-id i3-show-desktop" >> ~/.config/i3/config
```

## Usage
```
usage: i3-show-desktop [-h] [-c] [-s START] [-d]

Show desktop/Minimize all windows like functionality present on any major DE of any OS.

optional arguments:
  -h, --help            show this help message and exit
  -c, --config          generate config file additions, specify --start argument to change frist unused workspace
  -s START, --start START
                        first free workspace
  -d, --debug           print debug messages
```
