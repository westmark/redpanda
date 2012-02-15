# -*- coding: UTF-8 -*-

from PIL import Image
import sys, os, os.path
import math
import re

def create_base(size):
  base = Image.new('RGB', (size, size))
  return base

def analyze_input(path):
  input_size = 0
  images = {}
  ext_p, file_p = re.compile(r'\..*$'), re.compile(r'^(neg|pos)[XYZ]\..*$', re.IGNORECASE)
  entries = os.listdir(path)
  for entry in entries:
    if os.path.isfile(os.path.join(path, entry)) and file_p.match(entry):
      try:
        i = Image.open(os.path.join(path, entry))
        input_size = max(input_size, i.size[0])
        images[ext_p.sub('', entry).upper()] = i
      except:
        continue
      
  return int(input_size), images

if __name__ == '__main__':
  print 'Analyzing files in %s' % sys.argv[1]
  input_size, src_images = analyze_input(sys.argv[1])
  input_size *= 3
  size, j = math.pow(2, 2), 2
  while size < input_size:
    j += 1
    size = int(math.pow(2, j))
    
  print 'Size is %dx%d' % (size, size)
    
  base = create_base(size)
  order = [
           ('POSZ', 90), 
           ('POSX', 90), 
           ('POSY', 90), 
           ('NEGX', 90), 
           ('NEGZ', 90),
           ('NEGY', 270), 
           ]
  positions = [(0, size/2), (size/4, size/4), (size/4, size/2),
               (size/4, (size/4)*3), (size/2, size/2), ((size/4)*3, size/2)]
  
  for side_rot, pos in list(zip(order, positions)):
    side, rotation = side_rot
    print 'Patch-Pasting side %s' % side
    src = src_images.get(side)
    if rotation:
      print 'Rotating by %d degrees' % rotation 
      src = src.rotate(rotation)
      src_images[side] = src
    i = 1
    base.paste(src, (max(0, pos[0]-i), pos[1]))
    base.paste(src, (pos[0], max(0, pos[1]-i)))
    
    base.paste(src, (min(size, pos[0]+i), pos[1]))
    base.paste(src, (pos[0], min(size, pos[1]+i)))
    
  for side_rot, pos in list(zip(order, positions)):
    side, rotation = side_rot
    print 'Pasting side %s' % side
    src = src_images.get(side)
    base.paste(src, pos)
    
  if size > 4096:
    print 'Resizing'
    base = base.resize((4096, 4096), Image.ANTIALIAS)  
    
  print 'Saving output'
  base.save(os.path.join(sys.argv[1], 'skybox_texture.png'), 'PNG', optimize=True)
  print 'Done'
    