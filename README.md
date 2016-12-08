# logitech-g610-python
Simple python script to control logitech g610 keyboard (e.g. backlit)

Based on https://github.com/MatMoul/g810-led-python

## Install requirements
This script need the PyUSB library.

`pip install -r requirements.txt`

## Usage
To change the backlit intensity, use a pre defined level or a direct value:
```
python3 g610.py {off,l1-6,max}
```
You can also set the backlit intensity for specific groups:
```
python3 g610.py -g <group> {off,l1-6,max}
```
The following groups are available:
```
logo, multimedia, fkeys, modifiers, arrows, numeric, gaming
```

## Example
To turn the backlit off:
```
sudo python3 g610.py off
```


