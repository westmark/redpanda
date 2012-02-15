# -*- coding: UTF-8 -*-

from panda3d.core import NodePath

class SkyBox(object):
  
  def __init__(self, modelPath, scale=1.0):
    self._nodePath = NodePath('skybox')
    self._nodePath.setPos((0,0,0))
    self._scale = scale
    
    m = base.assetManager.loadModel(modelPath)
    m.reparentTo(self._nodePath)
    self._nodePath.setScale(self._scale)
      
    self._nodePath.flattenStrong()
    self._nodePath.setLightOff(True)
    self._nodePath.setShaderOff()
    self._nodePath.setDepthWrite(False)
      
  @property
  def nodePath(self):
    return self._nodePath
