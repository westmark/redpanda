# -*- coding: UTF-8 -*-
from redpanda.util import getIntersection, getUnitNormalVector
import math


class Bezier(object):

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def p(self, t):
    x0 = self.a[0] * t + (1 - t) * self.b[0]
    x1 = self.b[0] * t + (1 - t) * self.c[0]
    x = x0 * t + (1 - t) * x1

    y0 = self.a[1] * t + (1 - t) * self.b[1]
    y1 = self.b[1] * t + (1 - t) * self.c[1]
    y = y0 * t + (1 - t) * y1

    return (x, y)

  def points(self, gran):
    granFrac = (1.0 / float(gran))
    for t in range(gran):
      p = self.p(granFrac * float(t))
      yield (p[0], p[1])
    p = self.p(1)
    yield (p[0], p[1])

  def generate(self, gran):
    return [p for p in self.points(gran)]


class PolyLine(object):
  def __init__(self, points, thickness=1, color=(255, 255, 255)):
    self.points = points
    self.genPoints = []
    self.thickness = thickness
    self.color = color

  def generate(self):
    pointsNormalsSlopes, i = [], 0

    for p2 in self.points[1:]:
      p1 = self.points[i]
      i += 1
      normal = getUnitNormalVector(p1, p2)
      pointsNormalsSlopes.append((p1, p2, normal))
    lines = []

    for p1, p2, n in pointsNormalsSlopes:
      if p1 and p2:
        e1, e2 = self.getEndpoints(p1, p2, self.thickness, n)
        e3, e4 = self.getEndpoints(p1, p2, self.thickness, n * -1)
        lines.append(((e1, e2), (e3, e4)))

    self.genPoints = [(lines[0][0][0], lines[0][1][0])]

    i = 1
    for (e1, e2), (e3, e4) in lines:
      if i >= len(lines):
        break
      (e11, e22), (e33, e44) = lines[i]

      i1 = getIntersection(e1, e2, e11, e22)
      i2 = getIntersection(e3, e4, e33, e44)

      self.genPoints.append((i1, i2))

      i += 1

    self.genPoints.append((lines[-1][0][1], lines[-1][1][1]))

    return self.genPoints

  def getEndpoints(self, p1, p2, thickness, normalVec):
    offset = normalVec * (float(thickness) / 2.0)
    return ((p1[0] + offset.getX(), p1[1] + offset.getY()), (p2[0] + offset.getX(), p2[1] + offset.getY()))


class Circle(object):
  def __init__(self, radius=0.1, hollowRadius=0, quality=16):
    self._radius = radius
    self._hollowRadius = hollowRadius
    self._quality = quality

  def points(self):
    pid = math.pi / float(self._quality / 2)
    yield (math.sin(0) * self._radius, math.cos(0) * self._radius)
    for i in range(self._quality):
      yield (math.sin(pid * i) * self._hollowRadius, math.cos(pid * i) * self._hollowRadius)
      yield (math.sin(pid * (i + 1)) * self._radius, math.cos(pid * (i + 1)) * self._radius)

    yield (math.sin(0) * self._hollowRadius, math.cos(0) * self._hollowRadius)

  def generate(self):
    return [p for p in self.points()]
