# -*- coding: UTF-8 -*-

from redpanda.camera import SateliteCamera, FPSCamera, Camera
from redpanda import getKeyboardMgr
from redpanda.constants import Buttons


def setupBasicCameraControls(camera=None):

  if not camera:
    if hasattr(base, '_camera'):
      camera = base._camera
    elif hasattr(base, 'camera'):
      camera = base.camera

  if isinstance(camera, SateliteCamera):

    def onControlLeftMouseDown(*args, **kwargs):
      camera.resume()

    def onLeftMouseUp(*args, **kwargs):
      camera.pause()

    def onMouseWheelUp(*args, **kwargs):
      camera.zoom(delta=-1.5)

    def onMouseWheelDown(*args, **kwargs):
      camera.zoom(delta=1.5)

    base.accept('control-mouse1', onControlLeftMouseDown)
    base.accept('mouse1-up', onLeftMouseUp)
    base.accept('wheel_up', onMouseWheelUp)
    base.accept('wheel_down', onMouseWheelDown)

  elif isinstance(camera, FPSCamera):

    def task(task):
      km, dir = getKeyboardMgr(), []
      if km.status('w'):
        dir.append(Camera.DIRECTION_FORWARD)
      elif km.status('s'):
        dir.append(Camera.DIRECTION_BACKWARD)
      if km.status('a'):
        dir.append(Camera.DIRECTION_LEFT)
      elif km.status('d'):
        dir.append(Camera.DIRECTION_RIGHT)
      if km.status(Buttons.SPACE):
        if km.status(Buttons.SHIFT):
          dir.append(Camera.DIRECTION_DOWN)
        else:
          dir.append(Camera.DIRECTION_UP)
      elif km.status('shift-space') and km.status(Buttons.SHIFT):
        dir.append(Camera.DIRECTION_DOWN)
      else:
        km.status('shift-space', False)
        if Camera.DIRECTION_DOWN in dir:
          dir.remove(Camera.DIRECTION_DOWN)
        if Camera.DIRECTION_UP in dir:
          dir.remove(Camera.DIRECTION_UP)

      camera.move(dir)

      return task.cont

    taskMgr.add(task, 'KeyboardCheckTask')
