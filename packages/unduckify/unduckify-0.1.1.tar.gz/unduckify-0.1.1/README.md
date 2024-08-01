# Unduckify

Recover the payloads of a *Duckify* BadUSB from a memory dump.

Reverse the process of [duckify](https://github.com/SpacehuhnTech/duckify).

Whole process explained [here](https://0xlibris.net/posts/reversing_badusb_3/).

# Install

Install from PyPI:

`pip install unduckify`

Or clone the repo and install with pip:

`pip install .`

# Usage

```bash
usage: unduckify [-h] (-f FILE | -t TEST) [-l {hu,be,ca-cms,ru,se,cz,in,pl,ro,us,ch-fr,ch-de,fi,is,pt,pt-br,no,hr,dk,lv,lt,si,ee,gr,fr,de,ua,bg,ie,tr,gb,sk,it,es-la,es,ca-fr,nl}]
                 [-s {win,mac}] [-v]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -t TEST, --test TEST  Provide a value list to test. Example: "0,6, 0,16, 0,7, 0,44, 2,36, 0,14"
  -l {hu,be,ca-cms,ru,se,cz,in,pl,ro,us,ch-fr,ch-de,fi,is,pt,pt-br,no,hr,dk,lv,lt,si,ee,gr,fr,de,ua,bg,ie,tr,gb,sk,it,es-la,es,ca-fr,nl}, --layout {hu,be,ca-cms,ru,se,cz,in,pl,ro,us,ch-fr,ch-de,fi,is,pt,pt-br,no,hr,dk,lv,lt,si,ee,gr,fr,de,ua,bg,ie,tr,gb,sk,it,es-la,es,ca-fr,nl}
  -s {win,mac}, --system {win,mac}
  -v, --verbose

```
