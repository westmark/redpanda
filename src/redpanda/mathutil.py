# -*- coding: UTF-8 -*-


from panda3d.core import Quat, Vec3


def find_rotation_quat(v1, v2):
  if v1.almost_equal(v2):
    return Quat(1, 0, 0, 0)
  elif (v1 * -1).almost_equal(v2):
    v, smallest = Vec3(1, 0, 0), abs(v1[0])
    if abs(v[1]) < smallest:
      v = Vec3(0, 1, 0)
      smallest = abs(v[1])
    if abs(v[2]) < smallest:
      v = Vec3(0, 0, 1)

    return Quat(0, v1.cross(v))

  v = v1 + v2
  v.normalize()
  angle = v.dot(v2)
  axis = v.cross(v2)
  return Quat(angle, axis)
