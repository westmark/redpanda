# -*- coding: UTF-8 -*-

from direct.showbase.DirectObject import DirectObject #@UnresolvedImport
from math import pi, sqrt
from panda3d.core import Vec3, Point3 #@UnresolvedImport
from panda3d.core import WindowProperties #@UnresolvedImport
from redpanda.util import g2scoord, s2gcoord
from redpanda import events

pi2 = pi * 2


class Camera(DirectObject):

  DIRECTION_FORWARD = 1
  DIRECTION_BACKWARD = 2
  DIRECTION_LEFT = 3
  DIRECTION_RIGHT = 4
  DIRECTION_UP = 5
  DIRECTION_DOWN = 6

  def __init__(self,
               invert=False,
               sensitivity=0.05,
               pitch=0,
               heading=0,
               roll=0,
               pos=(0, 0, 0),
               name='DefaultCamera',
               lookAt=None,
               speedY=40,
               speedX=20,
               speedZ=20,
               hideCursor=True,
               **kwargs
               ):
    from redpanda import getScreenUtils
    u = getScreenUtils()

    self._invert = invert
    self._sensitivity = sensitivity
    self._heading = heading
    self._pitch = pitch
    self._roll = roll
    self._running = False
    self._name = name
    self._taskName = self._name + 'Task'
    self._pos = Point3(pos)
    self._lookAt = lookAt
    self._dir = Vec3(0, 0, 0)
    self._middle = (int(u.winXmaxHalf), int(u.winYmaxHalf))
    self._lastPos = self._middle
    self._revealMouseAt = None
    self._cameraMoved = False
    self._speedX = speedX
    self._speedY = speedY
    self._speedZ = speedZ
    self._hideCursor = hideCursor

  def start(self, paused=False):
    base.disableMouse()
    if not paused:
      if self._hideCursor:
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)
      base.win.movePointer(0, self._middle[0], self._middle[1])

    base.camera.setPos(self._pos)
    if self._lookAt:
      base.camera.lookAt(self._lookAt)
      self._heading, self._pitch, self._roll = base.camera.getHpr()
    else:
      base.camera.setHpr(self._heading, self._pitch, self._roll)
    self._running = not paused
    self._cameraTask = taskMgr.add(self.task, self._taskName, uponDeath=self.cleanup)

  def stop(self):
    self.pause()
    taskMgr.remove(self._cameraTask)
    self._cameraTask = None

  def resume(self):
    md = base.win.getPointer(0)
    if self._hideCursor:
      props = WindowProperties()
      props.setCursorHidden(True)
      base.win.requestProperties(props)
      self._revealMouseAt = (md.getX(), md.getY())
      base.win.movePointer(0, self._middle[0], self._middle[1])
    else:
      self._revealMouseAt = None
      self._lastPos = (md.getX(), md.getY())
    self._running = True

  def pause(self):
    self._running = False
    props = WindowProperties()
    props.setCursorHidden(False)
    base.win.requestProperties(props)
    if self._revealMouseAt:
      base.win.movePointer(0, self._revealMouseAt[0], self._revealMouseAt[1])
      self._revealMouseAt = None

  def destroy(self):
    taskMgr.remove(self._taskName)
    self.cleanup()
    self._running = False

  def cleanup(self, task):
    base.enableMouse()
    props = WindowProperties()
    props.setCursorHidden(False)
    base.win.requestProperties(props)

  def task(self, task):
    md = base.win.getPointer(0)

    x, y = md.getX(), md.getY()
    if self._hideCursor:
      dx, dy = x - self._middle[0], y - self._middle[1]
    else:
      dx, dy = x - self._lastPos[0], y - self._lastPos[1]

    if self._running:
      if self._hideCursor:
        base.win.movePointer(0, self._middle[0], self._middle[1])
      if dx == 0 and dy == 0:
        return task.cont

      self.mouseDelta(dx, dy)
      if self._cameraMoved:
        base.messenger.send(events.CAMERA_MOVED)
    else:
      if not (x, y) == self._lastPos:
        base.messenger.send('mousemove', [(x, y), self._lastPos])

    self._lastPos = (x, y)

    return task.cont

  def mouseDelta(self, dx, dy):
    pass

  def move(self, direction, distance=None):

    if not isinstance(direction, tuple):
      direction = (direction)

    dirVector = None
    if Camera.DIRECTION_FORWARD in direction:
      dirVector, speed = base.camera.getMat().getRow3(1), self._speedY

    elif Camera.DIRECTION_BACKWARD in direction:
      dirVector, speed = base.camera.getMat().getRow3(1), -self._speedY

    if Camera.DIRECTION_LEFT in direction:
      dirVector, speed = base.camera.getMat().getRow3(0), -self._speedX

    elif Camera.DIRECTION_RIGHT in direction:
      dirVector, speed = base.camera.getMat().getRow3(0), self._speedX

    if Camera.DIRECTION_UP in direction:
      dirVector, speed = base.camera.getMat().getRow3(2), self._speedZ

    elif Camera.DIRECTION_DOWN in direction:
      dirVector, speed = base.camera.getMat().getRow3(2), -self._speedZ

    if dirVector:
      self._dir = base.camera.getPos() + (dirVector * 5)
      if distance:
        self._dir = self._dir + dirVector * (distance)
      else:
        self._dir = self._dir + dirVector * globalClock.getDt() * speed

      base.camera.setPos(self._dir - (dirVector * 5))
      self._cameraMoved = True


class FPSCamera(Camera):
  def __init__(self, *args, **kwargs):
    kwargs.update({'name': 'FPSCamera'})
    Camera.__init__(self, *args, **kwargs)

  def mouseDelta(self, dx, dy):
    if self._invert:
      dy *= -1

    self._heading -= dx * self._sensitivity
    self._pitch -= dy * self._sensitivity

    if self._pitch < -89.9:
      self._pitch = -89.9
    if self._pitch > 89.9:
      self._pitch = 89.9

    base.camera.setHpr(self._heading, self._pitch, self._roll)
    self._cameraMoved = True


class SateliteCamera(Camera):
  def __init__(self, *args, **kwargs):
    kwargs.update({'name': 'SateliteCamera',
                   'hideCursor': True})
    Camera.__init__(self, *args, **kwargs)
    self._distance = kwargs.get('distance', 10.0)
    self._zoomSpeed = kwargs.get('zoom_speed', 1.0)
    self._minDistance = kwargs.get('min_distance', 5.0)
    self._maxDistance = kwargs.get('max_distance', 100.0)

  def start(self, *args, **kwargs):
    Camera.start(self, *args, **kwargs)
    self.setPos(self._pos, reset=True)

  def setPos(self, pos=None, reset=False, withoutMoving=False):
    if pos:
      if isinstance(pos, tuple):
        pos = Point3(pos)
      if reset:
        theta, phi = pi / 4, pi * 1.25
      else:
        _, theta, phi = g2scoord(base.camera.getPos() - self._pos)
        if withoutMoving:
          x, y, z = (base.camera.getPos() - pos)
          self._distance = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

      newPos = s2gcoord(self._distance, theta, phi)
      base.camera.setPos(Point3(newPos) + pos)
      base.camera.lookAt(pos)
      self._pos = pos
      self._cameraMoved = True

  def zoom(self, delta=None, distance=None):
    if delta:
      self._distance += delta * self._zoomSpeed
    elif distance:
      self._distance = distance
    else:
      return

    if self._distance <= self._minDistance:
      self._distance = self._minDistance

    if self._distance > self._maxDistance:
      self._distance = self._maxDistance

    self.recalculatePosition()

  def recalculatePosition(self):
    camPos = base.camera.getPos() - self._pos
    _, theta, phi = g2scoord(camPos)
    x, y, z = s2gcoord(self._distance, theta, phi)

    base.camera.setPos(Point3(x, y, z) + self._pos)
    base.camera.lookAt(self._pos)
    self._cameraMoved = True

  def mouseDelta(self, dx, dy):
    camPos = base.camera.getPos() - self._pos
    r, theta, phi = g2scoord(camPos)

    if self._invert:
      dy = -dy
    dx = -dx

    theta += dy * self._sensitivity
    phi += dx * self._sensitivity

    while theta > pi:
      theta = pi - 0.0001
    while theta < 0:
      theta = 0.0001

    while phi > pi2:
      phi -= pi2

    while phi < 0:
      phi += pi2

    x, y, z = s2gcoord(r, theta, phi)

    base.camera.setPos(Point3(x, y, z) + self._pos)
    base.camera.lookAt(self._pos)

    self._cameraMoved = True
