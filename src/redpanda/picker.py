# -*- coding: UTF-8 -*-

'''
Originally by tolleybot, october 3, 2010
http://tolleybot.wordpress.com / 2010 / 10 / 03 / panda3d - simple - mouse - picking/

Slightly modified by astrogee
'''

from panda3d.core import Vec3, BitMask32
from panda3d.core import CollisionRay, CollisionNode, CollisionTraverser
from panda3d.core import CollisionHandlerQueue


class MousePicker(object):

  def __init__(self, pickTag='MyPickingTag', nodeName='pickRay', showCollisions=False):
    self.pickTag = pickTag
    self.nodeName = nodeName
    self.showCollisions = showCollisions

  def create(self):
    self.mPickerTraverser = CollisionTraverser()
    self.mCollisionQue = CollisionHandlerQueue()

    self.mPickRay = CollisionRay()
    self.mPickRay.setOrigin(base.camera.getPos(base.render))
    self.mPickRay.setDirection(base.render.getRelativeVector(base.camera, Vec3(0, 1, 0)))

    #create our collison Node to hold the ray
    self.mPickNode = CollisionNode(self.nodeName)
    self.mPickNode.addSolid(self.mPickRay)

    #Attach that node to the camera since the ray will need to be positioned
    #relative to it, returns a new nodepath
    #well use the default geometry mask
    #this is inefficent but its for mouse picking only

    self.mPickNP = base.camera.attachNewNode(self.mPickNode)

    #we'll use what panda calls the "from" node.  This is reall a silly convention
    #but from nodes are nodes that are active, while into nodes are usually passive environments
    #this isnt a hard rule, but following it usually reduces processing

    #Everything to be picked will use bit 1. This way if we were doing other
    #collision we could seperate it, we use bitmasks to determine what we check other objects against
    #if they dont have a bitmask for bit 1 well skip them!
    self.mPickNode.setFromCollideMask(BitMask32(1))

    #Register the ray as something that can cause collisions
    self.mPickerTraverser.addCollider(self.mPickNP, self.mCollisionQue)

    #Setup 2D picker
    self.mPickerTraverser2D = CollisionTraverser()
    self.mCollisionQue2D = CollisionHandlerQueue()

    self.mPickNode2D = CollisionNode('2D PickNode')
    self.mPickNode2D.setFromCollideMask(BitMask32(1))
    self.mPickNode2D.setIntoCollideMask(BitMask32.allOff())

    self.mPick2DNP = base.camera2d.attachNewNode(self.mPickNode2D)

    self.mPickRay2D = CollisionRay()
    self.mPickNode2D.addSolid(self.mPickRay2D)

    self.mPickerTraverser2D.addCollider(self.mPick2DNP, self.mCollisionQue2D)

    if self.showCollisions:
      self.mPickerTraverser.showCollisions(base.render)
      self.mPickerTraverser2D.showCollisions(base.aspect2d)

  def mousePick(self, traverse=None, tag=None):
    #do we have a mouse
    if (base.mouseWatcherNode.hasMouse() == False):
      return None, None

    traverse = traverse or base.render
    tag = tag or self.pickTag

    mpos = base.mouseWatcherNode.getMouse()

    #Set the position of the ray based on the mouse position
    self.mPickRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
    self.mPickerTraverser.traverse(traverse)

    if (self.mCollisionQue.getNumEntries() > 0):
      self.mCollisionQue.sortEntries()

      for entry in self.mCollisionQue.getEntries():
        pickedObj = entry.getIntoNodePath()
        pickedObj = pickedObj.findNetTag(tag)

        if not pickedObj.isEmpty():
          pos = entry.getSurfacePoint(base.render)
          return pickedObj, pos

    return None, None

  def mousePick2D(self, traverse=None, tag=None, all=False):
    #do we have a mouse
    if (base.mouseWatcherNode.hasMouse() == False):
      return None, None

    traverse = traverse or base.render
    tag = tag or self.pickTag

    mpos = base.mouseWatcherNode.getMouse()

    self.mPickRay2D.setFromLens(base.cam2d.node(), mpos.getX(), mpos.getY())

    self.mPickerTraverser2D.traverse(base.aspect2d)

    if self.mCollisionQue2D.getNumEntries() > 0:
      self.mCollisionQue2D.sortEntries()

      if all:
        return [(entry.getIntoNodePath().findNetTag(tag), entry.getSurfacePoint(base.aspect2d)) for entry in self.mCollisionQue2D.getEntries()], None
      else:
        entry = self.mCollisionQue2D.getEntry(0)
        pickedObj = entry.getIntoNodePath()

        pickedObj = pickedObj.findNetTag(tag)
        if not pickedObj.isEmpty():
          pos = entry.getSurfacePoint(base.aspect2d)
          return pickedObj, pos

    return None, None
