# -*- coding: utf-8 -*-
import math, sys

class LinearSeparate:
    def __init__(self, G):
        self.maxIteration = 10000
        self.E = 0.01
        self.h = 0.05
        self.theta = 0
        self.L = []
        self.G = G

        # Проинициализируем начальный вектор L
        self.initVectorL()

    def initVectorL(self):
        G = self.G
        resultSum = [0 for i in G[0]]
        
        for el in G:
            resultSum = map(lambda a, b: a + b, el, resultSum)
        
        self.L = map(lambda a: float(a) / len(G), resultSum)
        self.L[len(self.L) - 1] = self.theta

    def generateNewVectorL(self, g):
        i = 0
        for el in g:
            self.L[i] = self.L[i] + self.h * el
            i += 1

    def getFl(self):
        minVal, minEl = self.findGmin()
        self.generateNewVectorL(minEl)
        return minVal
        
    def scalarMultiplication(self, vector1, vector2):
        if (len(vector1) != len(vector2)):
            raise ValueError('Len vector1 != len vector2')

        result = 0
        for i in range(len(vector1)):
            result += vector1[i] * vector2[i]
        
        return result

    def findGmin(self):
        minVal = self.scalarMultiplication(self.L, self.G[0])
        minEl = self.G[0]

        for el in self.G:
            scalar = self.scalarMultiplication(self.L, el)

            if scalar < minVal:
                minVal = scalar
                minEl = el

        return (minVal, minEl)
    
    def normVectorL(self):
        result = 0

        for el in self.L:
            result += el**2
            
        return math.sqrt(result)

    def analyze(self, verbose = False):
        i = 0

        while (i < self.maxIteration):
            fl = self.getFl()
            
            if verbose == True:
                print "F(L) = %s; Norma L = %s" % (fl, self.normVectorL())

            if (fl > 0):
                return True
            elif (self.normVectorL() < self.E):
                return False

            i += 1

        return False