#-------------------------------------------------------------------------------
# Name:        PointUtilsClass
# Purpose:     Provides point distance operations for basic point objects
#
# Author:      ATangeman
#
# Created:     08/03/2016
# Copyright:   (c) ATangeman 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import radians, cos, sin, asin, sqrt

# ----------Class Objects-----------------------------------------------------

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def X(self):
        return self.X

    def Y(self):
        return self.X

    def isValidPoint(self, x=None, y=None):
        default = False
        try:
            if (isinstance(self.X or x, (int, long, float)) and ((self.X or x) != 0)):
                default = True
            if (isinstance(self.Y or y, (int, long, float)) and ((self.Y or y) != 0)):
                default = True
        except TypeError:
            raise
        return default

# ----------Type Objects-----------------------------------------------------
# Type enums are similar to a dictionary, just simpler footprint. They are used in most languages (C, C#, Java...)
# They make it easier to clearly define correct values because intellisense (aka autocomplete)
# will automatically provide a list of possible parameters

class CalcTypes(object):
    GreatCircle = 0
    Euclidian = 1

class UnitTypes(object):
    Meters = 0
    Kilometers = 1
    Feet = 2
    Miles = 3

class CustomType(object):
    @classmethod
    def enum(cls, **enums):
        return type('Enum', (), enums)

# ----------Class Constructor-----------------------------------------------------

class FindNearestPoint:
    def __init__(self, PointArray, BasePoint, MinDist=100, Units = 0, DistMethod = 0): #minDist, Units, and DistMethod are optional
        self.minDist = MinDist
        self.nearestPt = None # closest point (should only return 1)
        self.nearestPtIdx = -1 # index of closest point found in array
        if (Units == 0):
            self.radius = 6371000 # radius of earth in meters
        elif (Units == 1):
            self.radius = 6371 # radius of earth in kilometers
        elif (Units == 2):
            self.radius = 20887733 # radius of earth in feet
        elif (Units == 3):
            self.radius = 3956 # radius of earth in miles
        self.method = DistMethod
        self.getDistances(PointArray, BasePoint)

    # Code and formula adapted from http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    # distanceMethod Option 0
    def GreatCircleDist(self, point1, point2):
        #if((type(point1) is not arcpy.Point) or (type(point1) is not arcpy.Point)):
        if(point1.isValidPoint() == False or point2.isValidPoint() == False):
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
        if(point1.isValidPoint() == False or point2.isValidPoint() == False):
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
                self.nearestPtIdx += 1
                try:
                    if(self.method == 0):
                        distance = self.GreatCircleDist(testPoint, basePoint)
                    elif(self.method == 1):
                        distance = self.EuclidianDist(testPoint, basePoint)
                    if distance < self.minDist:
                        self.minDist = distance
                        self.nearestPt = testPoint
                except ValueError as e:
                    raise


