
# PythonGeometryTools

Lightweight and simple methods for geometry comparison operations written using Python and ArcPy. Useful if you only want to compare a pair of points and don't want to mess with reading and writing to a geodatabase data table using ArcPy's native "Point Distance" tool. Also, serves as a pretty good example of my approach to neatly organized Python code.

Requires ESRI ArcPy libraries to run, but can be modified to use a custom point object if necessary. Will throw compilation errors if ArcPy is not installed.

## Installation

First, ensure Pyhon 2.7+ is installed. Optional: install ArcGIS for ArcPy libraries. You may then checkout and run example class straight from IDLE, or customize and inherit into existing Python project.

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
[atangeman20160308] - Construction of initial code

## Credits

Andrew Tangeman, 2016. Method and class creation.
	
Deduplicator, 2014. Reply to StackExchange "Calculate distance between two latitude-longitude points? (Haversine formula)." Edited Jul 31 '14 at 1:25. From http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula.  
