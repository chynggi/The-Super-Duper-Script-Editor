﻿################################################################################
### Copyright © 2012-2013 BlackDragonHunt
### 
### This file is part of the Super Duper Script Editor.
### 
### The Super Duper Script Editor is free software: you can redistribute it
### and/or modify it under the terms of the GNU General Public License as
### published by the Free Software Foundation, either version 3 of the License,
### or (at your option) any later version.
### 
### The Super Duper Script Editor is distributed in the hope that it will be
### useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
### 
### You should have received a copy of the GNU General Public License
### along with the Super Duper Script Editor.
### If not, see <http://www.gnu.org/licenses/>.
################################################################################

import logging
import os
import re
import traceback

# from common import SCENE_MODES, SCENE_SPECIAL, BOX_COLORS, LOGGER_NAME
# from common import get_dir_info
import common
import dir_tools
from list_files import list_all_files
from script_file import ScriptFile
from wrd.wrd_file import WrdFile

_LOGGER_NAME = common.LOGGER_NAME + "." + __name__
_LOGGER = logging.getLogger(_LOGGER_NAME)

class ScriptPack():
  def __init__(self, directory = None, umdimage = "umdimage"):
    self.script_files = []
    self.directory    = directory
    self.wrd          = None
    self.wrd_file     = None
    
    if not directory == None:
      self.load_dir(directory, umdimage)
      
  def __getitem__(self, index):
    return self.script_files[index]
  
  def __len__(self):
    return len(self.script_files)
  
  def get_index(self, filename):
    for index, file in enumerate(self.script_files):
      if os.path.split(file.filename)[1] == filename:
        return index
    
    return None
  
  def get_script(self, filename):
    index = self.get_index(filename)
    
    if not index == None:
      return self.__getitem__(index)
    
    else:
      return None
  
  def get_real_dir(self):
    # Rather than the easy to look at directory name we usually store,
    # get the actual, untampered directory name where you can find the files.
    return dir_tools.expand_dir(self.directory)
  
  def load_dir(self, directory, umdimage = "umdimage"):
    
    self.script_files = []
    self.directory    = directory
    self.wrd          = None
    self.wrd_file     = None
    self.py_file      = None
    
    base_name = directory
    directory, wrd_file = dir_tools.parse_dir(directory, umdimage)
    
    if directory == None:
      self.directory = ""
      raise Exception("Directory \"" + base_name + "\" not found.")
    
    full_dir = os.path.join(umdimage, directory)
    
    scene_info = []
    
    if not wrd_file == None and os.path.isfile(wrd_file):
      
      # Even of the first directory existed and we have a .wrd file,
      # it's possible there aren't actually any text files here.
      if not os.path.isdir(full_dir):
        raise Exception("There are no text files in \"" + directory + "\".")
      
      self.wrd  = WrdFile()
      
      py_file   = os.path.splitext(wrd_file)[0] + ".py"
      
      if os.path.isfile(py_file):
        try:
          self.wrd.load_python(py_file)
        except:
          _LOGGER.warning("%s failed to load. Parsing wrd file instead. Exception info:\n%s" % (py_file, traceback.format_exc()))
          self.wrd.load_bin(wrd_file)
        else:
          # If we succeeded in loading the python file, compile it to binary.
          # _LOGGER.info("%s loaded successfully. Compiling to binary." % py_file)
          # self.wrd.save_bin(wrd_file)
          _LOGGER.info("%s loaded successfully." % py_file)
      
      else:
        _LOGGER.info("Decompiled wrd file not found. Generating %s" % py_file)
        self.wrd.load_bin(wrd_file)
        self.wrd.save_python(py_file)
      
      scene_info    = self.wrd.to_scene_info()
      self.wrd_file = wrd_file
      self.py_file  = py_file
    
    else:
      scene_info    = None
      self.wrd      = None
      self.wrd_file = None
    
    self.script_files = []
    if scene_info == None:
      text_files = list_all_files(full_dir)
      for file in text_files:
        self.script_files.append(ScriptFile(file))
        
    else:
      # Get our files in the order listed by the wrd.
      for info in scene_info:
        filename = os.path.join(full_dir, "%04d.txt" % info.file_id)
        script_file = ScriptFile(filename, info)
        
        if script_file.filename == None:
          _LOGGER.warning("File %s referenced by %s does not exist." % (filename, wrd_file))
          continue
        
        self.script_files.append(script_file)
    
    chapter, scene, room, mode = common.get_dir_info(base_name)
    
    for file in self.script_files:
      if file.scene_info.chapter == -1: file.scene_info.chapter = chapter
      if file.scene_info.scene == -1:   file.scene_info.scene   = scene
      if file.scene_info.room == -1:    file.scene_info.room    = room
      if file.scene_info.mode == None:  file.scene_info.mode    = mode

if __name__ == "__main__":
  pack = ScriptPack("e00_001_000.lin", umdimage = "X:/Danganronpa/Danganronpa_BEST/umdimage")
  
  for index, file in enumerate(pack.script_files):
    print "File:      ", file.scene_info.file_id
    print " * Speaker:", file.scene_info.speaker
    if not file.scene_info.sprite == (-1, -1):
      print " * Sprite: ", file.scene_info.sprite
    # if not file.scene_info.sfx == (-1, -1):
      # print " * SFX:    ", file.scene_info.sfx
    
    # if file.scene_info.special == SCENE_SPECIAL.option1:
      # print " * Special: Option 1"
    # elif file.scene_info.special == SCENE_SPECIAL.option2:
      # print " * Special: Option 2"
    # elif file.scene_info.special == SCENE_SPECIAL.option3:
      # print " * Special: Option 3"
    # elif file.scene_info.special == SCENE_SPECIAL.optionX:
      # print " * Special: Option ???"
    # elif file.scene_info.special == SCENE_SPECIAL.showopt:
      # print " * Special: Show Options"
    # print ""

### EOF ###