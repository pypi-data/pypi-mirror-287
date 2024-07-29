# Dockrich

![GitHub stars](https://img.shields.io/github/stars/prasaanth2k/dockrich?style=social)
![GitHub issues](https://img.shields.io/github/issues/prasaanth2k/dockrich)
![GitHub license](https://img.shields.io/github/license/prasaanth2k/dockrich)

A tool to pretty print Docker command outputs.

## Installation

```bash
pip install dockrich
```

## CLI Mode 

```bash
$ dockrich -h
```

![helpimg](/images/helpmessage.png)

```bash
$ dockrich -r
```
![runningcontainers](/images/runncontainers.png)

```bash
$ dockrich -i 
```
![dockerimages](/images/images.png)

```bash
$ dockrich -p
```
![dockerports](/images/ports.png)


```bash

$ dockrich -n

```
![dockernetworks](/images/images.png)

```bash

$ dockrich -s 
```
![dockerstop](/images/stopcontainers.png)

```bash

$ dockrich -a 

```
![dockerich](/images/allcontainers.png)


## Api Mode 
```python3
from dockrich.dockerinspector import Dockerinspector
from dockrich.dockerhistory import Dockerhistory
from dockrich.dockerstats import Dockerstats
from dockrich.dockermanage import Dockermanage

inspect = Dockerinspector(containerid_or_name="debian_container")
images = Dockerhistory(image_name="prasaanthdjango")
status = Dockerstats(containerid_or_name="debian_container")

values = inspect.getvalues()
print(values.Id)

for image in images.getvalues():
    print(image.Size)

s = status.getstats()
print(s.BlockIO)

ps = Dockermanage(containerid_or_name="debian_container")

output = ps.ps()
print(output.LocalVolumes)


```