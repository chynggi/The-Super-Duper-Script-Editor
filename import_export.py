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

# from PyQt4 import QtGui, QtCore
# from PyQt4.QtCore import QProcess, QString

import glob
import logging
import os
import re
import shutil
import tempfile

from bitstring import ConstBitStream

import common

from backup import backup_files
from dupe_db import DupesDB
from enum import Enum
from list_files import list_all_files
from gim_converter import GimConverter, QuantizeType
from model_pak import ModelPak

_CONV     = GimConverter()
_DUPE_DB  = DupesDB()

DIR_TYPE  = Enum("umdimage", "umdimage2")

SKIP_CONV = ["save_icon0.png", "save_icon0_t.png", "save_new_icon0.png", "save_pic1.png"]

FORCE_QUANTIZE = [
  (re.compile(ur"art_chip_002_\d\d\d.*", re.UNICODE),                         QuantizeType.index8),
  (re.compile(ur"bgd_\d\d\d.*", re.UNICODE),                                  QuantizeType.index8),
  (re.compile(ur"bustup_\d\d_\d\d.*", re.UNICODE),                            QuantizeType.index8),
  (re.compile(ur"(cutin|gallery|kotodama|present)_icn_\d\d\d.*", re.UNICODE), QuantizeType.index8),
]

# MODEL_PAK = re.compile(ur"bg_\d\d\d")

_LOGGER_NAME = common.LOGGER_NAME + "." + __name__
_LOGGER = logging.getLogger(_LOGGER_NAME)

################################################################################
### FUNCTIONS
################################################################################

######################################################################
### Importing
######################################################################
def import_dir(src, dst, dir_type, convert_png = True, unique = False):
  if dir_type == DIR_TYPE.umdimage:
    import_umdimage(src, dst, convert_png, unique)
  elif dir_type == DIR_TYPE.umdimage2:
    import_umdimage2(src, dst, convert_png, unique)
  else:
    _LOGGER.error("Unable to import %s. Unknown dirtype %s provided." % (src, dir_type))

def import_umdimage(src, dst, convert_png = True, unique = False):
  pass

def import_umdimage2(src, dst, convert_png = True, unique = False):
  pass

######################################################################
### Exporting
######################################################################
def export_dir(src, dst, dir_type, convert_gim = True, unique = False):
  if dir_type == DIR_TYPE.umdimage:
    export_umdimage(src, dst, convert_gim, unique)
  elif dir_type == DIR_TYPE.umdimage2:
    export_umdimage2(src, dst, convert_gim, unique)
  else:
    _LOGGER.error("Unable to export %s. Unknown dirtype %s provided." % (src, dir_type))

def export_umdimage(src, dst, convert_gim = True, unique = False):
  pass

def export_umdimage2(src, dst, convert_gim = True, unique = False):
  if unique:
    tmp_dst = tempfile.mkdtemp(prefix = "sdse-")
  else:
    tmp_dst = dst
  
  for pak in glob.iglob(os.path.join(src, "bg_*.pak")):
    extract_model_pak(pak, tmp_dst, convert_gim)
    _LOGGER.info("Exported %s to %s" % (pak, tmp_dst))
  
  if unique:
    seen_groups = []
    
    _LOGGER.info("Copying unique files to %s" % (dst))
    for img in list_all_files(tmp_dst):
      img_base  = img[len(tmp_dst) + 1:]
      dupe_name = os.path.splitext(img_base)[0] + ".gim"
      dupe_name = os.path.join("umdimage2", dupe_name)
      dupe_name = os.path.normpath(os.path.normcase(dupe_name))
      # print dupe_name
      
      group = _DUPE_DB.group_from_file(dupe_name)
      
      if group in seen_groups:
        continue
      
      if not group == None:
        seen_groups.append(group)
      
      dst_file = os.path.join(dst, img_base)
      dst_dir  = os.path.dirname(dst_file)
      
      try:
        os.makedirs(dst_dir)
      except:
        pass
      
      shutil.copy(img, dst_file)
    
    shutil.rmtree(tmp_dst)

######################################################################
### Models/textures
######################################################################
def extract_model_pak(filename, dst_dir, to_png = True):
  # out_dir = os.path.splitext(os.path.basename(filename))[0]
  out_dir = os.path.basename(filename)
  out_dir = os.path.join(dst_dir, out_dir)
  
  pak = ModelPak(filename = filename)
  pak.extract(out_dir, to_png)
  
  return out_dir

def insert_textures(pak_dir, filename):
  
  pak = ModelPak(filename = filename)
  
  for gmo_name in os.listdir(pak_dir):
    full_path = os.path.join(pak_dir, gmo_name)
    if not os.path.isdir(full_path):
      _LOGGER.warning("Not a directory of textures. Skipped importing %s to %s" % (full_path, filename))
      continue
  
    gmo_id = pak.id_from_name(gmo_name)
    if gmo_id == None:
      _LOGGER.warning("GMO %s does not exist in %s" % (gmo_name, filename))
      continue
    
    gmo = pak.get_gmo(gmo_id)
    if gmo == None:
      _LOGGER.warning("Failed to retrieve GMO %s from %s" % (gmo_name, filename))
      continue
    
    for img in os.listdir(os.path.join(pak_dir, gmo_name)):
      name, ext = os.path.splitext(img)
      
      if ext.lower() == ".gim":
        is_png = False
      elif ext.lower() == ".png":
        is_png = True
      else:
        continue
      
      gim_id = int(name)
      if is_png:
        gmo.replace_png_file(gim_id, os.path.join(pak_dir, gmo_name, img))
      else:
        gmo.replace_gim_file(gim_id, os.path.join(pak_dir, gmo_name, img))
      
      _LOGGER.info("Inserted %s into %s" % (img, gmo_name))
    
    pak.replace_gmo(gmo_id, gmo)
    _LOGGER.info("Inserted %s into %s" % (gmo_name, filename))
  
  pak.save(filename)
  _LOGGER.info("Saved %s" % filename)

if __name__ == "__main__":
  import sys
  handler = logging.StreamHandler(sys.stdout)
  logging.getLogger(common.LOGGER_NAME).addHandler(handler)
  
  export_umdimage2("X:/Danganronpa/Danganronpa_BEST/umdimage2", "wip/umdimage3", convert_gim = True, unique = True)
  
  # extract_model_pak("wip/test/bg_042.pak", "wip/test")
  # import_model_pak("wip/test/bg_042-eng", "wip/test/bg_042.pak")
  # extract_model_pak("wip/test/bg_042.pak", "wip/test")

### EOF ###