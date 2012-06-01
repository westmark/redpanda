# -*- coding: UTF-8 -*-


class Buttons(object):

  ESCAPE = 'escape'
  RETURN = 'enter'
  ENTER = 'enter'
  SPACE = 'space'
  CTRL = 'control'
  RIGHT_CTRL = 'rcontrol'
  LEFT_CTRL = 'lcontrol'
  SHIFT = 'shift'
  LEFT_SHIFT = 'lshift'
  RIGHT_SHIFT = 'rshift'
  ALT = 'alt'
  LEFT_ALT = 'lalt'
  RIGHT_ALT = 'ralt'
  ARROW_UP = 'arrow_up'
  ARROW_DOWN = 'arrow_down'
  ARROW_LEFT = 'arrow_left'
  ARROW_RIGHT = 'arrow-right'

  MOUSE_1 = 'mouse1'
  MOUSE_2 = 'mouse2'
  MOUSE_3 = 'mouse3'
  MOUSE_4 = 'mouse4'
  MOUSE_5 = 'mouse5'
  MOUSE_6 = 'mouse6'

  WHEEL_UP = 'wheel_up'
  WHEEL_DOWN = 'wheel_down'

  LOOKUP = {}

  MODIFIERS = [CTRL, LEFT_CTRL, RIGHT_CTRL,
               SHIFT, LEFT_SHIFT, RIGHT_SHIFT,
               ALT, LEFT_ALT, RIGHT_ALT,
              ]

  @staticmethod
  def up(tag):
    return '%s-up' % tag

for prop in dir(Buttons):
  if not prop.startswith('__'):
    attr = getattr(Buttons, prop)
    if type(attr) == str:
      Buttons.LOOKUP.update({attr: attr})


class Axis(object):
  POS_X = 0
  POS_Y = 1
  POS_Z = 2
  NEG_X = 3
  NEG_Y = 4
  NEG_Z = 5

  ALL = [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]
