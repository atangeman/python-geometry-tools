
# PythonGeometryTools

Lightweight and simple methods for geometry comparison operations written using Python and ArcPy. Useful if you only want to compare a pair of points and don't want to mess with reading and writing to a geodatabase data table using ArcPy's native "Point Distance" tool. Also, serves as a pretty good example of my approach to neatly organized Python code.
 

## Installation

First, ensure Pyhon 2.7+ is installed. Optional: install ArcGIS for ArcPy libraries. You may then checkout and run example class straight from IDLE, or customize and inherit into existing Python project. There are two Python classes to choose from, depending on requirements.

#### WithArcpy: 

Requires ESRI ArcPy libraries to run. Will throw compilation errors if ArcPy is not installed. Meant to interface with existing ArcPy operations using ArcPy FeaturePoint object.

#### WithoutArcpy: 

Uses custom Point object to perform comparison operations. Includes example operation in the FindNearest_Example.py. 

## Installation

## Usage

Classes are build for extensibility and incorporation into other projects as needed. Some coding or modification required to use.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

[atangeman20161217] - First commit of previously completed code.
[atangeman20160308] - Construction of initial code.

## Credits

Andrew Tangeman, 2016. Method and class creation.
	
