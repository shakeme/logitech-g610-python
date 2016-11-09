# logitech-g610-python
Simple python script to control logitech g610 keyboard (e.g. backlit)

Based on https://github.com/MatMoul/g810-led-python

## Install requirements
This script need the PyUSB library.

`pip install -r requirements.txt`

## Usage
To change the backlit intensity, use the backlit argument:
```
python g610.py backlit {0,1,2,3,4}
```
where 0 is backlit off and 4 is brightest.

## Example
To turn the backlit off:
```
sudo python g610.py backlit 0
```

