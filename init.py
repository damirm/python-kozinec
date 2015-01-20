# -*- coding: utf-8 -*-

from kazinec import Kazinec
from set_helper import SetHelper
from linear_separate import LinearSeparate

import letters, helper, sys

setHelper = SetHelper()

# Получим все смещения
classA = setHelper.getSets(letters.A, 10, 10)
# Сохраним изображения смещений
setHelper.saveSetsImages(classA, dir = "i/A")

# Транспонируем каждый элемент класса в один массив, добавив к нему элемент -1
classA = setHelper.setsToLinearSets(classA, addedEl = -1)

classB = setHelper.getSets(letters.B, 10, 10)
setHelper.saveSetsImages(classB, dir = "i/B")

# Транспонируем каждый элемент класса в один массив, добавив к нему элемент 1.
# Так же нужно изменить знак у всех элементов множества
classB = setHelper.setsToLinearSets(classB, addedEl = 1, inverseSet = True)

"""
classC= setHelper.getSets(letters.C)
setHelper.saveSetsImages(classC, dir = "i/C")
"""

G = classA + classB

analyzer = LinearSeparate(G)

if not analyzer.analyze():
    print "Inseparable !"
    sys.exit(1)
else:
    print "Separable"

# Далее избавимся от n+1 го элемента в множествах, и от знака минус во втором можестве
for el in classA:
    el.pop()

for el in classB:
    for i in xrange(len(el) - 1):
        el[i] *= -1
    el.pop()

# Инициализируем множество W
W = setHelper.initW(classA, classB)

kazinec = Kazinec(W)
kazinec.learn()

#print kazinec.recognize([j for i in letters.toRecognize for j in i])
toRecognize = kazinec.addNoise([j for i in letters.toRecognize for j in i], 10)
#toRecognize = kazinec.addNoise([i for i in classB[0]], 5)
print kazinec.recognize(toRecognize)
