# -*- coding: UTF-8 -*-

from panda3d.core import * #@UnresolvedImport
import inspect
import libpanda #@UnresolvedImport
import pandac.PandaModules as pac #@UnresolvedImport

indent = '  '
importptrn = 'from %s import %s'
coreimpptrn = 'from panda3d.core import %s'
skip = [
        'DtoolGetSupperBase',
        'DtoolClassDict'
       ]

def record(t, name, f, noclasses=False, baseIndent=''):
  if name.startswith('__'): return
  if isinstance(t, int):
    f.write('%s%s = int\n\n' % (baseIndent, name))
    return True
  elif isinstance(t, float):
    f.write('%s%s = float\n\n' % (baseIndent, name))
    return True
  elif isinstance(t, str):
    f.write('%s%s = str\n\n' % (baseIndent, name))
    return True
  elif inspect.isclass(t):
    if noclasses: return
    f.write('%sclass %s:\n%s  def __init__(self):\n%s    pass\n' % (baseIndent, t.__name__, baseIndent, baseIndent))
    for _name in dir(t):
      if _name in skip:
        continue
      _t = eval('%s.%s' %(name, _name))
      record(_t, _name, f, noclasses=True, baseIndent=('%s  ' % baseIndent))
        
    return True
      
  elif callable(t):
    if hasattr(t, '__objclass__'):
      f.write('%sdef %s(self):\n%s  pass\n' % (baseIndent, t.__name__, baseIndent))
    else:
      f.write('%sdef %s():\n%s  pass\n' % (baseIndent, t.__name__, baseIndent))
      return True
  return False

def generateCore():
  
  f = open('panda3d.core.pypredef', 'w')
  libpanda_names = dir(libpanda)
  
  for name in libpanda_names:
    try:
      exec(coreimpptrn % name)
      t = eval(name)
      
      print "Building %s..." % name
      record(t, name, f)
      
    except Exception, e:
      print e
      continue
    
  pac_names = [name for name in dir(pac) if not name in libpanda_names]
  for name in pac_names:
    try:
      exec(coreimpptrn % name)
      t = eval(name)
      
      print "Building %s..." % name
      record(t, name, f)
      
    except Exception, e:
      print e
      continue
    
  f.close()
    
if __name__ == '__main__':
  generateCore()