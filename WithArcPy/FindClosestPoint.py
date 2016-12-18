#!/usr/bin/env python3

# Class to return closest point based on a static base point and a list of
# candidate points.
# [atangeman20160308] - Construction of initial code

import arcpy
from math import radians, cos, sin, asin, sqrt

# ======== CLASS CONSTRUCTORS - NOT MEANT TO BE MODIFIED =======================

class FindClosestPoint:
    def __init__(self, PointArray, BasePoint, MinDist=100, Units = 0, DistMethod = 0): #minDist, Units, and DistMethod are optional
        self.minDist = MinDist
        self.closestPt = None # closest point (should only return 1)
        self.closestPtIdx = -1 # index of closest point found in array
        if (Units == 0):
            self.radius = 6371 # radius of earth in km
        elif (Units == 1):
            self.radius = 3956 # radius of earth in miles
        self.method = DistMethod
        self.getDistances(PointArray, BasePoint)

    # Code and formula adapted from http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    # distanceMethod Option 0
    def GreatCircleDist(self, point1, point2):
        if((type(point1) is not arcpy.Point) or (type(point1) is not arcpy.Point)):
            raise ValueError("Invalid point object") # Raise exception up stack
        R = self.radius
        lon1 = point1.Y
        lon2 = point2.Y
        lat1 = self.deg2rad(point1.X)
        lat2 = self.deg2rad(point2.X)
        dLon = self.deg2rad((point2.Y - point1.Y))
        dLat = self.deg2rad((point2.X - point1.X))
        a = sin(dLat/2)**2 + cos(lat1) * cos(lat2) * sin(dLon/2)**2
        c = 2 * asin(sqrt(a))
        d = R * c
        return d

    # distanceMethod Option 1
    def EuclidianDist(self, point1, point2):
        if((type(point1) is not arcpy.Point) or (type(point1) is not arcpy.Point)):
            raise ValueError("Invalid point object") # Raise exception up stack
        x1 = point1.X
        x2 = point2.X
        y1 = point1.Y
        y2 = point2.Y
        d1 = math.pow((x2 - x1), 2)
        d2 = math.pow((y2 - y1), 2)
        d = math.sqrt((d1 + d2))
        return d

    def deg2rad(self, deg):
        return deg * 0.017453292519943295

    def getDistances(self, pointArray, basePoint):
            for testPoint in pointArray:
                self.closestPtIdx += 1
                try:
                    if(self.method == 0):
                        distance = self.GreatCircleDist(testPoint, basePoint)
                    elif(self.method == 1):
                        distance = self.EuclidianDist(testPoint, basePoint)
                    if distance < self.minDist:
                        self.minDist = distance
                        self.closestPt = testPoint
                except ValueError as e:
                    raise

def enum(**enums):
    return type('Enum', (), enums)

# Type enums are similar to a dictionary, just simpler footprint.
# They make it easier to clearly define correct values without using strings
DistMethod = enum(GreatCircle = 0, Euclidian = 1) # No modification required
Units = enum(Meters = 0, Feet = 1) # No modification required

#---------APPLICATION CODE - Modifyable ----------- ----------------------------


resultPointArray = [arcpy.Point(32.777056, -117.056189),  # Sample for Test - Assume result array returned from QueryService
                    arcpy.Point(32.750558, -117.125333),  # You may have to wrap objects returned from ArcGIS Rest
                    arcpy.Point(32.72854171, -117.16119991),  # into separate point objects using the constructor result1 = arcpy.Point(result1.lat, result1.long)
                    arcpy.Point(32.688662, -117.022458)]

UserLat = 32.689174 # Sample for Test - Assume input point from user
UserLong = -117.022401	 # Sample for Test - Assume input point from user
SampleUserPoint = arcpy.Point(UserLat, UserLong)
MinDist=10

try:
    f = FindClosestPoint(resultPointArray, SampleUserPoint, MinDist, Units.Meters, DistMethod.GreatCircle) # Initialize class function
    if (f.closestPt != None):
        print "[Debugging Message]: Closest point found with a distance of " + str(f.minDist) +" and an index of "+ str(f.closestPtIdx)
        print "[Debugging Message]: Point(" + str(f.closestPt.X) + ", " + str(f.closestPt.Y) + ")"
except Exception as e:
    print "Unknown Exception encountered" + str(e)



