# -*- coding: UTF-8 -*-

from panda3d.core import Quat, Vec3


def find_rotation_quat(*args):
  v1 = Vec3(args[0])
  q = Quat(1, 0, 0, 0)
  vectors = args[1:]

  for v2 in vectors:
    v2 = Vec3(v2)
    if v1.almost_equal(v2):
      continue
    elif (v1 * -1).almost_equal(v2):
      v, smallest = Vec3(1, 0, 0), abs(v1[0])
      if abs(v[1]) < smallest:
        v = Vec3(0, 1, 0)
        smallest = abs(v[1])
      if abs(v[2]) < smallest:
        v = Vec3(0, 0, 1)

      q = Quat(0, v1.cross(v)) * q
    else:
      v = v1 + v2
      v.normalize()
      angle = v.dot(v2)
      axis = v.cross(v2)
      q = Quat(angle, axis) * q

    v1 = v2

  return q
