# -*- coding: UTF-8 -*-

from direct.showbase.DirectObject import DirectObject
from redpanda.constants import Buttons
from datetime import datetime


class KeyboardMgr(DirectObject):

  def __init__(self):
    self._callbacks = []
    self._key_map = {}
    self._repeatInterval = 0.1 * 1000000
    self._ignore = set()

  def start(self):
    self.setup_accepts()

  def cleanup(self, task):
    self.discard_accepts()

  def discard_accepts(self):
    for key in self._key_map.keys():
      self.ignore(str(key))

  def listen(self, callback):
    self._callbacks.append(callback)

  def ignoreKey(self, tag):
    self._ignore.add(tag)

  def setup_accepts(self):
    base.buttonThrowers[0].node().setButtonDownEvent('bdown')
    base.buttonThrowers[0].node().setButtonUpEvent('bup')
    base.buttonThrowers[0].node().setButtonRepeatEvent('brepeat')

    self.accept('bdown', self.buttons, [True])
    self.accept('bup', self.buttons, [False])
    self.accept('brepeat', self.buttonRepeat)

  def buttons(self, status, tag):
    if tag not in self._ignore:
      self._key_map.update({Buttons.LOOKUP.get(tag, tag): (status, datetime.now())})
      for callback in self._callbacks:
        callback(tag=tag, status=status)

  def buttonRepeat(self, tag):
    if tag not in self._ignore:
      status, dt = self._key_map.get(tag, (False, datetime.now()))
      if status:
        last = datetime.now() - dt
        if last.microseconds > self._repeatInterval:
          self._key_map.update({Buttons.LOOKUP.get(tag, tag): (status, datetime.now())})
          for callback in self._callbacks:
            callback(tag=tag, status=True)

  def status(self, tag, status=None):
    if not status == None:
      self._key_map.update({Buttons.LOOKUP.get(tag, tag): (status, datetime.now())})
      return self
    s, _ = self._key_map.get(Buttons.LOOKUP.get(tag, tag), (False, None))
    return s
