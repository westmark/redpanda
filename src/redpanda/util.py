# -*- coding: UTF-8 -*-

from direct.showbase.DirectObject import DirectObject
from panda3d.core import Point3, Vec3, Vec2D
from pandac.PandaModules import VBase4
from math import cos, atan2, acos, sin, sqrt, pow
import math


class ScreenUtils(DirectObject):
  def __init__(self):
    from redpanda import events
    self.setup()
    self.accept(events.WIN_RESIZE, self.setup)

  def setup(self):
    winProps = base.winList[0].getProperties()
    self.winXsize = winProps.getXSize()
    self.winYsize = winProps.getYSize()
    self.winXmaxHalf = (self.winXsize - 1) * .5
    self.winYmaxHalf = (self.winYsize - 1) * .5
    self.aspRatio = float(self.winXsize) / self.winYsize
    self.screenRect = ((-self.aspRatio, -1.0), (self.aspRatio, 1.0))

  def screenPixel(self, posR2D, y=None):
    if not y == None:
      posR2D = (posR2D, y)
    posSPx = 1 + (posR2D[0] + self.aspRatio) * self.winXmaxHalf
    posSPy = 1 + (-posR2D[1] + 1) * self.winYmaxHalf
    return (int(posSPx), int(posSPy))

  def unitToPixelSize(self, unitSize):
    return (int(round(self.winXsize * unitSize[0] / (self.aspRatio * 2))),
            int(round(self.winYsize * (unitSize[1] / 2.0))))

  def pandaPos(self, posSP, y=None):
    if not y == None:
      posSP = (posSP, y)
    pandaX = (posSP[0] - 1) / self.winXmaxHalf - self.aspRatio
    pandaY = ((posSP[1] - 1) / self.winYmaxHalf - 1) * -1
    return (pandaX, 0, pandaY)

  @property
  def left(self):
    return self.screenRect[0][0]

  @property
  def top(self):
    return self.screenRect[1][1]

  @property
  def right(self):
    return self.screenRect[1][0]

  @property
  def bottom(self):
    return self.screenRect[0][1]

  @property
  def width(self):
    return self.right - self.left

  @property
  def height(self):
    return self.top - self.bottom

  @property
  def topleft(self):
    return (self.left, self.top)

  @property
  def size(self):
    return (self.width, self.height)


def frange(start, stop=None, step=None):
  if stop is None:
    stop = float(start)
    start = 0.0
  if step is None:
    step = 1.0
  cur = float(start)
  while cur < stop:
    yield cur
    cur += step


def g2scoord(*args):
  if not args:
    return (0, 0, 0)

  if len(args) == 3:
    x, y, z = args

  elif len(args) == 1:
    o = args[0]
    if isinstance(o, Point3) or isinstance(o, Vec3):
      x, y, z = o.getX(), o.getY(), o.getZ()
    elif isinstance(o, tuple):
      x, y, z = o

  r = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
  theta = acos(z / r)
  phi = atan2(y, x)

  return (r, theta, phi)


def s2gcoord(*args):
  if not args:
    return (0, 0, 0)

  if len(args) == 3:
    r, theta, phi = args
  elif len(args) == 1:
    o = args[0]
    if isinstance(o, tuple):
      r, theta, phi = o

  x = r * sin(theta) * cos(phi)
  y = r * sin(theta) * sin(phi)
  z = r * cos(theta)

  return (x, y, z)


def getInheritedColorScale(np):
  while np and not np.hasColorScale():
    np = np.getParent()
  if np:
    return np.getColorScale()
  return VBase4(1, 1, 1, 1)


def projectCarelessly(point, lens=None):
  """
  Similar to Lens.project(), but never returns None.

  Source: http://www.panda3d.org / forums / viewtopic.php?t=2022 - by tarsierpi
  """

  lens = lens or base.camLens

  projection_mat = lens.getProjectionMat()
  print(projection_mat)
  full = projection_mat.xform(VBase4(point[0], point[1], point[2], 1.0))
  if full[3] == 0.0:
    # There is no meaningful projection for the nodal point of the lens.
    # So return a value that is Very Far Away.
    return (1000000.0, 1000000.0, -1000000.0)

  recip_full3 = 1.0 / full[3]
  return (full[0] * recip_full3,
          full[1] * recip_full3,
          full[2] * recip_full3)


def map3dToAspect2d(node, point):
  """
  Maps the indicated 3 - d point (a Point3), which is relative to
  the indicated NodePath, to the corresponding point in the aspect2d
  scene graph. Returns the corresponding Point3 in aspect2d.
  Returns None if the point is not onscreen.

  Source: http://www.panda3d.org / forums / viewtopic.php?t=2022 - by Redmond Urbino / tarsierpi
  """

  # Convert the point to the 3 - d space of the camera
  p3 = base.cam.getRelativePoint(node, point)

  # Convert from camera 3d space to camera 2d space.
  # Manual override.
  p2 = projectCarelessly(p3, base.camLens)

  r2d = Point3(p2[0], 0, p2[1])

  # And then convert it to aspect2d coordinates
  a2d = base.aspect2d.getRelativePoint(base.render2d, r2d)

  return a2d


if __name__ == '__main__':
  x, y, z = 3.0, 5.0, 7.0
  r, theta, phi = g2scoord(x, y, z)
  print r, theta, phi
  x, y, z = s2gcoord(r, theta, phi)
  print x, y, z


def getUnitNormalVector(p1, p2):
  (x1, y1), (x2, y2) = p1, p2
  dx, dy = float(x2 - x1), float(y2 - y1)

  unitNormal = Vec2D(-dy, dx)
  unitNormal.normalize()
  return unitNormal


def getIntersection(p1s, p1e, p2s, p2e):
  (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1s, p1e, p2s, p2e
  div = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
  if div != 0:
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / div
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / div
  else:
    px = p1e[0]
    py = p1e[1]

  return px, py


def is_point_in_rect(point, rect):
  px, py = point
  (rx, ry), (rw, rh) = rect

  return px >= rx and py > ry and px <= rx + rw and py <= ry + rh


def get_closest_power_of_2(x):
  return int(pow(2, math.ceil(math.log(x) / math.log(2))))
