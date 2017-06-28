# randmandel

Generate the Mandelbrot pattern and randomly colour it with 256 colours.

Uses some code from [Julia](https://github.com/wolfmankurd/Julia/).

## Usage

```
python mandelbrot.py
```

## Dependencies

#### To run

* python 2.7
* numpy
* scipy

#### To build

* SWIG
* build-essentials (gcc)
* python-dev

## Building

```
cd src/
./build_module.sh
cp mandel.py _mandel.so ../
```
