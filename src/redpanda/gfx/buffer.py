# -*- coding: UTF-8 -*-

from redpanda.util import get_closest_power_of_2, is_point_in_rect
from panda3d.core import NodePath, OrthographicLens
import uuid


class BufferRegion(object):

  def __init__(self, b, region):
    self._buffer = b
    self._region = region

  @property
  def buffer(self):
    return self._buffer

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    self._region = region

  @property
  def texcoords(self):
    (x, y), (w, h) = self._region
    return (x, y, x + w - 1, y + h - 1)

  @property
  def render2d(self):
    return self._buffer.render2d

  @property
  def texture(self):
    return self._buffer.texture


class Buffer(object):

  def __init__(self, size, bg_color=(0, 0, 0, 1), overflow=False, name='Off screen buffer', film_size=(2, 2), near=-1000, far=1000):
    self._size = size
    self._bg_color = bg_color
    self._film_size = film_size
    self._near = near
    self._far = far
    self._name = name
    self._texture = None
    self._render2d = None
    self._used_regions = []
    self._overflow = overflow

  def create(self):
    g_buffer = base.win.makeTextureBuffer(self._name, self._size, self._size)
    g_buffer.setClearColor(self._bg_color)
    self._texture = g_buffer.getTexture()
    g_buffer.setSort(-100)

    camera2d = NodePath(base.makeCamera(g_buffer))
    lens = OrthographicLens()
    lens.setFilmSize(2, 2)
    lens.setNearFar(-1000, 1000)
    camera2d.node().setLens(lens)

    self._render2d = NodePath('{0}-my-render2d'.format(self._name))
    self._render2d.setDepthTest(False)
    self._render2d.setDepthWrite(False)
    camera2d.reparentTo(self._render2d)

    return self._render2d, self._texture

  def _can_fit_specific_region(self, region):
    (x1, y1), (w, h) = region
    x2, y2 = x1 + w, y1 + h

    for br in self._used_regions:
      r = br.region
      if is_point_in_rect((x1, y1), r) or is_point_in_rect((x2, y2), r):
        return False

    return True

  def _find_fit_for_region(self, region_size):
    w, h = region_size
    x, y = 0, 0

    if not self._used_regions:
      return ((x, y), (w, h))

    sox, soy = self._overflow, self._overflow

    if type(self._overflow) in (tuple, list):
      sox, soy = self._overflow

    for br in self._used_regions:
      (rx, ry), (rw, rh) = br.region

      if not sox:
        x, y = rx + rw + 1, ry
        if x + w < self._size and y + h < self._size:
          if self._can_fit_specific_region(((x, y), (w, h))):
            return ((x, y), (w, h))

      if not soy:
        x, y = rx, ry + rh + 1
        if x + w < self._size and y + h < self._size:
          if self._can_fit_specific_region(((x, y), (w, h))):
            return ((x, y), (w, h))

    return None

  def reserve(self, region_size, overflow, bg_color):

    if tuple(bg_color) != tuple(self._bg_color):
      return False

    ox, oy, sox, soy = overflow, overflow, self._overflow, self._overflow
    if type(overflow) in (tuple, list):
      ox, oy = overflow

    if type(self._overflow) in (tuple, list):
      sox, soy = self._overflow

    if ox and sox is False or oy and soy is False:
      return False

    region = self._find_fit_for_region(region_size)
    if region is None:
      return False

    buffer_region = BufferRegion(self, region)
    self._used_regions.append(buffer_region)
    return buffer_region

  def release(self, buffer_region):
    if buffer_region in self._used_regions:
      self._used_regions.remove(buffer_region)

  @property
  def size(self):
    return self._size

  @property
  def render2d(self):
    return self._render2d

  @property
  def texture(self):
    return self._texture


class BufferManager(object):

  def __init__(self):
    self._buffers = {}

  def create_buffer(self, size, bg_color=(0, 0, 0, 1), overflow=False):
    buffer_size = get_closest_power_of_2(max(size[0], size[1]))
    buffer_region = self._find_available_buffer(buffer_size, size, overflow, bg_color)

    if not buffer_region:
      b = Buffer(buffer_size, bg_color=bg_color, overflow=overflow, name='buffer-' + str(uuid.uuid4()), film_size=(2, 2), near=-1000, far=1000)
      b.create()
      self._buffers.setdefault(buffer_size, []).append(b)
      buffer_region = b.reserve(size, overflow, bg_color)

    return buffer_region

  def _find_available_buffer(self, buffer_size, region_size, overflow, bg_color):
    for size in self._buffers.keys():
      if buffer_size > size:
        continue

      buffers = self._buffers[size]
      for b in buffers:
        buffer_region = b.reserve(region_size, overflow, bg_color)
        if buffer_region:
          return buffer_region

    return None


if __name__ == '__main__':
  bm = BufferManager()

  br = bm.create_buffer((120, 60))
  print br, br.buffer.size, br.buffer.render2d, br.buffer.texture
