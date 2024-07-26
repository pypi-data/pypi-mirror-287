<h1 align="center">
  <b>colorframe</b>
</h1>

A simple package to add a colored frame on pictures.

## Install

This code is compatible with all currently supported Python versions.
Install it in your virtual enrivonment with:

```bash
pip install colorframe
```

## Usage

With this package is installed in the activated enrivonment, it can be called through `python -m colorframe` or through a newly created `colorframe` command.

Detailed usage goes as follows:

```bash
Usage: python -m colorframe [OPTIONS] [PATH]                                                 
                                                                                              
 Add a colored frame on pictures, easily.                                                     
                                                                                              
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────╮
│   path      [PATH]  Location, relative or absolute, to the file or directory of files to   │
│                     add a colored border to.                                               │
│                     [default: None]                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────╮
│ --vertical                  INTEGER  Size (width) of the whiteframe to add on the vertical │
│                                      image edges.                                          │
│                                      [default: 150]                                        │
│ --horizontal                INTEGER  Size (height) of the whiteframe to add on the         │
│                                      horizontal image edges.                               │
│                                      [default: 150]                                        │
│ --color                     TEXT     The desired color of the added border. Should be a    │
│                                      keyword recognized by Pillow.                         │
│                                      [default: white]                                      │
│ --log-level                 TEXT     The base console logging level. Can be 'debug',       │
│                                      'info', 'warning' and 'error'.                        │
│                                      [default: info]                                       │
│ --install-completion                 Install completion for the current shell.             │
│ --show-completion                    Show completion for the current shell, to copy it or  │
│                                      customize the installation.                           │
│ --help                               Show this message and exit.                           │
╰────────────────────────────────────────────────────────────────────────────────────────────╯
```

The script will crawl files, add borders and export the results in a newly created `outputs` folder.

You can otherwise import the high-level object from the package, and use at your convenience:

```python
from colorframe import BorderCreator

border_api = BorderCreator(
    commandline_pathp="path_to_your_images", vertical_border=150, horizontal_border=100, color="blue"
)
border_api.execute_target()
```

---

<div align="center">
  <sub><strong>Made with ♥︎ by fsoubelet</strong></sub>
  <br>
  <sub><strong>MIT &copy 2020 Felix Soubelet</strong></sub>
</div>
