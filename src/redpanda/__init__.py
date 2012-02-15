# -*- coding: UTF-8 -*-

from redpanda.camera import SateliteCamera, FPSCamera
from redpanda.keyboard import KeyboardMgr
from redpanda.picker import MousePicker
from redpanda.util import ScreenUtils
import sys

def getKeyboardMgr():
  module = sys.modules[__name__]
  if not hasattr(module, '_keyboardMgr'):
    setattr(module, '_keyboardMgr', KeyboardMgr())
  return getattr(module, '_keyboardMgr')
    
def getScreenUtils():
  module = sys.modules[__name__]
  if not hasattr(module, '_screenUtils'):
    setattr(module, '_screenUtils', ScreenUtils())
  return getattr(module, '_screenUtils')