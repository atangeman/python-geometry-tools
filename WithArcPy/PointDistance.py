#!/usr/bin/env python3

# Class to return closest point based on a static base point and a list of
# candidate points.
# [atangeman20160308] - Construction of initial code

import arcpy, math

class FindClosestPoint:
    def __init__(self, PointArray, BasePoint, MinDist=1000): #minDist is optional
        self.minDist = MinDist
        self.closestPt = None # closest point (should only return 1)
        self.closestPtIdx = None # index of closest point found in array
        self.getDistances(PointArray, BasePoint)

    def dist(self, point1, point2):
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

    def getDistances(self, pointArray, basePoint):
            closestPt = None
            self.closestPtIdx = 0
            for testPoint in pointArray:
                try:
                    if self.dist(testPoint, basePoint) < self.minDist:
                        self.minDist = self.dist(testPoint, basePoint)
                        self.closestPt = testPoint
                    self.closestPtIdx += 1
                except ValueError as e:
                    self.closestPtIdx += 1
                    raise

#----------------APPLICATION-----------------------------------------------------

resultPointArray = [arcpy.Point(32.71899999, -117.16106011),  # Sample for Test - Assume result array returned from QueryService
                    arcpy.Point(32.72850201, -117.16110222),  # You may have to wrap objects returned from ArcGIS Rest
                    arcpy.Point(32.72854171, -117.16119991),
                    arcpy.Point(32.71899999, -117.16106011)]  # into separate point objects using the constructor result1 = arcpy.Point(result1.lat, result1.long)

UserLat = 32.7187620495576 # Sample for Test - Assume input point from user
UserLong = -117.159968435585 # Sample for Test - Assume input point from user
SampleUserPoint = arcpy.Point(UserLat, UserLong)

try:
    f = FindClosestPoint(resultPointArray, SampleUserPoint) # Initialize class function
except Exception as e:
    print "Unknown Exception encountered" + e

if (f.closestPt != None):
    print "[Debugging Message]: Closest point found with a distance of " + str(f.minDist) +" and an index of "+ str(f.closestPtIdx)
    print "[Debugging Message]: Point(" + str(f.closestPt.X) + ", " + str(f.closestPt.Y) + ")"



