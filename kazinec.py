# -*- coding: utf-8 -*-
import math, sys, random

class Kazinec:
    def __init__(self, W):
        self.W = W
        self.L = self.initL()
        self.oldL = [0 for i in self.L]
        self.E = 0.0001
        self.theta = 0

    def initL(self):
        minVal = self.normVector(self.W[0])
        minEl = self.W[0]

        for w in self.W:
            curMin = self.normVector(w)
            if curMin < minVal:
                minVal = curMin
                minEl = w

        return minEl

    def nextValueL(self, lambdaValue, w):
        self.oldL = self.L

        v1 = [l * lambdaValue for l in self.L]
        v2 = [((1 - lambdaValue) * i) for i in w]
        self.L = [v1[i] + v2[i] for i in xrange(len(self.L))]

    def learn(self, verbose = False):
        while True:
            lChanched = False

            print self.normVector(self.L)

            if self.normVector(self.L) < self.E:
                return self.L

            for w in self.W:
                lambdaValue = self.calculateLambda(w)

                #if lambdaValue > 0 and lambdaValue < 1:
                if lambdaValue < 1:
                    self.nextValueL(lambdaValue, w)

                    # Проверка (хз зачем, но вроде так пашет :))
                    if self.normVector([self.L[i] - self.oldL[i] for i in xrange(len(self.L))]) < self.E:
                        if verbose:
                            print "Super if else statement !"
                        return self.L

                    lChanched = True
                    break

            if not lChanched:
                return self.L

    def calculateLambda(self, w):
        if (len(w) != len(self.L)):
            raise ValueError('CalculateLambda error: len(w) != len(L)')

        numerator = self.scalar([(w[i] - self.L[i]) for i in xrange(len(w))], w)
        denumerator = self.normVector([(self.L[i] - w[i]) for i in xrange(len(w))]) ** 2

        if denumerator == 0:
            #raise ValueError('denumerator = 0')
            return 0

        return float(numerator) / denumerator

    def scalar(self, vector1, vector2):
        if (len(vector1) != len(vector2)):
            raise ValueError('Len vector1 != len vector2')

        """
        result = 0
        for i in xrange(len(vector1)):
            result += vector1[i] * vector2[i]
        
        return result
        """

        return sum([vector1[i] * vector2[i] for i in xrange(len(vector1))])

    def normVector(self, vector):
        """
        result = 0
        for el in vector:
            result += el ** 2
        return math.sqrt(result)
        """

        return math.sqrt(sum([el ** 2 for el in vector]))

    def recognize(self, vectorToRecognize):
        scalarMul = self.scalar(self.L, vectorToRecognize)

        if scalarMul > self.theta:
            return 1
        else:
            return 2

    def addNoise(self, sourceVector, count):
        for i in xrange(count):
            randIndex = random.randint(0, len(sourceVector) - 1)
            sourceVector[randIndex] = sourceVector[randIndex] ^ 1

        return sourceVector