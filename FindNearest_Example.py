#-------------------------------------------------------------------------------
# Name:        Find Nearest Point Example
# Purpose:     Sample code to show how to import and implement the FindClosestPoint
#
# Author:      ATangeman
#
# Created:     08/03/2016
# Copyright:   (c) ATangeman 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PointUtils import FindNearestPoint, Point, UnitTypes, CalcTypes

#-----------Parameters---------------

ptList = [Point(32.777056, -117.056189),  # Sample for Test - Assume result array returned from QueryService
          Point(32.750558, -117.125333),  # You may have to wrap objects returned from ArcGIS Rest
          Point(32.72854171, -117.16119991),  # into separate point objects using the constructor result1 = arcpy.Point(result1.lat, result1.long)
          Point(32.688662, -117.022458)]

userLat = 32.689174 # Sample for Test - Assume input point from user
userLong = -117.022401	 # Sample for Test - Assume input point from user
userPt = Point(userLat, userLong) # User Defined Pointsdfsdfsdfwsefa
minDist=10sf

# I have included two custom enums (UnitTypes and CalcTypes)
# when they are assigned to a variable, reading the value results to an integer (Meters = 0, Feet = 1)
# Intelisense will show you the options when you create a new variable of UnitTypes or CalcTypes
# Uncomment code to print Example:
##unitType = UnitTypes.Meters
##print("Unit type: Meters (" + str(unitType)) + ")" # = 0
##
##calcType = CalcTypes.GreatCircle
##print("Calculation type: GreatCircle (" + str(calcType)) + ")" # = 0
##print("")

#--------------Main---------------

try:
    f = FindNearestPoint(ptList, userPt, minDist, UnitTypes.Feet, CalcTypes.GreatCircle) # Initialize class function
    if (f.nearestPt != None):
        print("Distance: " + str(f.minDist)) # distance
        print("Index: " + str(f.nearestPtIdx)) # index of point in ptList
        print("Point Lat: " + str(f.nearestPt.Y)) # latitude
        print("Point Long: " + str(f.nearestPt.X)) #longitude

except Exception as e:
    print "Unknown Exception encountered" + str(e)