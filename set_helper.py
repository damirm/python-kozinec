# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageColor

class SetHelper:
    def getSets(self, mask = [], n = 10, m = 10):
        sets = []
        startX = 0
        startY = 0
        
        while (startY <= m - len(mask)):
            startX = 0
            while (startX <= n - len(mask[0])):
                
                result = [[0 for i in xrange(n)] for i in xrange(m)]
                
                curI = startY
                for maskLine in mask:
                    curJ = startX
                    for maskBit in maskLine:
                        result[curI][curJ] = maskBit
                        curJ += 1
                    curI += 1
                    
                sets.append(result)
                startX += 1
            startY += 1

        return sets

    def setsToLinearSets(self, sets, addedEl = 1, inverseSet = False):
        return map(lambda el: [-i if inverseSet else i for j in el for i in j] + [addedEl], sets)

    def saveSetsImage(self, set, dir = "i", name = "test_set", format = "jpg", scale = 1):
        sizeY = scale * len(set)
        sizeX = scale * len(set[0])
        
        img = Image.new("RGB", (sizeX, sizeY), "white")
        
        i = j = 0
        
        for line in set:
            j = 0
            
            for bit in line:
                k = i * scale
                color = ImageColor.getrgb("white") if (bit == 0) else ImageColor.getrgb("black")
                
                while (k < i * scale + scale):
                    l = j * scale
                    
                    while (l < j * scale + scale):
                        img.putpixel((l, k), color)
                        l += 1
                    k += 1
                    
                j += 1
            i += 1
        
        resultFile = dir + "/" + name + "." + format
        img.save(resultFile)
        
    def saveSetsImages(self, sets, dir = 'i', scale = 10, format = 'png'):
        i = 0
        
        if not os.path.exists(dir):
            os.makedirs(dir) 
            
        for set in sets:
            self.saveSetsImage(set, dir, str(i), format, scale)
            i += 1

    def initW(self, G1, G2):
        return [[G1[i][j] - G2[i][j] for j in xrange(len(G1[i]))] for i in xrange(len(G1))]