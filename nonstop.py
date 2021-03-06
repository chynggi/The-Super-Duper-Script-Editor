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

from bitstring import ConstBitStream, BitStream
import logging
import os

from enum import Enum

import common
from script_pack import ScriptPack
from sprite import SpriteId, SPRITE_TYPE
from voice import VoiceId

_LOGGER_NAME = common.LOGGER_NAME + "." + __name__
_LOGGER = logging.getLogger(_LOGGER_NAME)

NONSTOP_LINE_TYPE = Enum("normal", "chatter")
LINE_TYPE_MAP = {
  ConstBitStream(hex = "0x00000000"): NONSTOP_LINE_TYPE.normal,
  ConstBitStream(hex = "0x01000100"): NONSTOP_LINE_TYPE.chatter,
  # ConstBitStream(hex = "0x01000000"): NONSTOP_LINE_TYPE.unknown1,
  # ConstBitStream(hex = "0x02000000"): NONSTOP_LINE_TYPE.unknown2,
  # ConstBitStream(hex = "0x03000000"): NONSTOP_LINE_TYPE.unknown3,
  # ConstBitStream(hex = "0x04000000"): NONSTOP_LINE_TYPE.unknown4,
}

NONSTOP_DIR = {
  "nonstop_01_001.dat": "e01_102_001.lin",
  "nonstop_01_002.dat": "e01_104_001.lin",
  "nonstop_01_003.dat": "e01_106_001.lin",
  "nonstop_01_004.dat": "e01_110_001.lin",
  "nonstop_01_005.dat": "e01_112_001.lin",
  "nonstop_01_006.dat": "e01_114_001.lin",
  "nonstop_01_007.dat": "e01_116_001.lin",
  "nonstop_01_008.dat": "e01_118_001.lin",

  "nonstop_02_001.dat": "e02_102_001.lin",
  "nonstop_02_002.dat": "e02_104_001.lin",
  "nonstop_02_003.dat": "e02_108_001.lin",
  "nonstop_02_004.dat": "e02_110_001.lin",
  "nonstop_02_005.dat": "e02_112_001.lin",
  "nonstop_02_006.dat": "e02_114_001.lin",
  "nonstop_02_007.dat": "e02_118_001.lin",
  "nonstop_02_008.dat": "e02_120_001.lin",
  "nonstop_02_009.dat": "e02_122_001.lin",

  "nonstop_03_001.dat": "e03_102_001.lin",
  "nonstop_03_002.dat": "e03_106_001.lin",
  "nonstop_03_003.dat": "e03_108_001.lin",
  "nonstop_03_004.dat": "e03_112_001.lin",
  "nonstop_03_005.dat": "e03_114_001.lin",
  "nonstop_03_006.dat": "e03_116_001.lin",
  "nonstop_03_007.dat": "e03_118_001.lin",
  "nonstop_03_008.dat": "e03_120_001.lin",
  "nonstop_03_009.dat": "e03_122_001.lin",
  "nonstop_03_010.dat": "e03_124_001.lin",
  "nonstop_03_011.dat": "e03_126_001.lin",

  "nonstop_04_001.dat": "e04_102_001.lin",
  "nonstop_04_002.dat": "e04_104_001.lin",
  "nonstop_04_003.dat": "e04_106_001.lin",
  "nonstop_04_004.dat": "e04_110_001.lin",
  "nonstop_04_005.dat": "e04_116_001.lin",
  "nonstop_04_006.dat": "e04_118_001.lin",
  "nonstop_04_007.dat": "e04_122_001.lin",
  "nonstop_04_008.dat": "e04_124_001.lin",

  "nonstop_05_001.dat": "e05_102_001.lin",
  "nonstop_05_002.dat": "e05_104_001.lin",
  "nonstop_05_003.dat": "e05_110_001.lin",
  "nonstop_05_004.dat": "e05_114_001.lin",
  "nonstop_05_005.dat": "e05_116_001.lin",
  "nonstop_05_006.dat": "e05_118_001.lin",
  "nonstop_05_007.dat": "e05_120_001.lin",
  "nonstop_05_008.dat": "e05_122_001.lin",
  "nonstop_05_009.dat": "e05_151_001.lin",

  "nonstop_06_001.dat": "e06_102_001.lin",
  "nonstop_06_002.dat": "e06_106_001.lin",
  "nonstop_06_003.dat": "e06_108_001.lin",
  "nonstop_06_004.dat": "e06_110_001.lin",
  "nonstop_06_005.dat": "e06_112_001.lin",
  "nonstop_06_006.dat": "e06_118_001.lin",
  "nonstop_06_007.dat": "e06_120_001.lin",
  "nonstop_06_008.dat": "e06_134_001.lin",
  "nonstop_06_009.dat": "e06_137_001.lin",
  
  # All variations on the same set of text.
  "nonstop_06_010.dat": "e06_143_001.lin",
  "nonstop_06_011.dat": "e06_143_001.lin",
  "nonstop_06_012.dat": "e06_143_001.lin",
  "nonstop_06_013.dat": "e06_143_001.lin",
  "nonstop_06_014.dat": "e06_143_001.lin",
  "nonstop_06_015.dat": "e06_143_001.lin",
  "nonstop_06_016.dat": "e06_143_001.lin",
  "nonstop_06_017.dat": "e06_143_001.lin",
  "nonstop_06_018.dat": "e06_143_001.lin",
  "nonstop_06_019.dat": "e06_143_001.lin",
  "nonstop_06_020.dat": "e06_143_001.lin",
  "nonstop_06_021.dat": "e06_143_001.lin",
  "nonstop_06_022.dat": "e06_143_001.lin",
  "nonstop_06_023.dat": "e06_143_001.lin",
  "nonstop_06_024.dat": "e06_143_001.lin",
  "nonstop_06_025.dat": "e06_143_001.lin",
}

class NonstopLine():
  def __init__(self):
    self.file_num     = -1
    self.line_type    = -1
    self.ammo_id      = -1
    self.converted_id = -1
    self.unknown1     = -1
    self.weak_point   = -1
    
    self.delay        = -1
    self.unknown2     = -1
    self.in_effect    = -1
    self.out_effect   = -1
    self.time_visible = -1
    self.x_start      = -1
    self.y_start      = -1
    self.velocity     = -1
    self.angle        = -1
    self.zoom_start   = -1
    self.zoom_change  = -1
    self.shake        = -1
    self.rot_angle    = -1
    self.spin_vel     = -1
    
    self.speaker      = -1
    
    self.char_id      = -1
    self.sprite_id    = -1
    
    self.unknown3     = -1
    self.voice_id     = -1
    self.unknown4     = -1
    self.chapter      = -1
    self.unknown5     = -1
  
  def to_data(self):
    data = \
      ConstBitStream(uintle = self.file_num, length = 16) + \
      [key for key, value in LINE_TYPE_MAP.iteritems() if value == self.line_type][0] + \
      ConstBitStream(uintle = self.ammo_id, length = 16) + \
      ConstBitStream(uintle = self.converted_id, length = 16) + \
      self.unknown1 + \
      ConstBitStream(uintle = self.weak_point, length = 16) + \
      ConstBitStream(intle = self.delay, length = 16) + \
      ConstBitStream(intle = self.unknown2, length = 16) + \
      ConstBitStream(intle = self.in_effect, length = 16) + \
      ConstBitStream(intle = self.out_effect, length = 16) + \
      ConstBitStream(intle = self.time_visible, length = 16) + \
      ConstBitStream(intle = self.x_start, length = 16) + \
      ConstBitStream(intle = self.y_start, length = 16) + \
      ConstBitStream(intle = self.velocity, length = 16) + \
      ConstBitStream(intle = self.angle, length = 16) + \
      ConstBitStream(intle = self.zoom_start, length = 16) + \
      ConstBitStream(intle = self.zoom_change, length = 16) + \
      ConstBitStream(intle = self.shake, length = 16) + \
      ConstBitStream(intle = self.rot_angle, length = 16) + \
      ConstBitStream(intle = self.spin_vel, length = 16) + \
      ConstBitStream(uintle = self.char_id, length = 16) + \
      ConstBitStream(uintle = self.sprite_id, length = 16) + \
      self.unknown3 + \
      ConstBitStream(uintle = self.voice_id, length = 16) + \
      self.unknown4 + \
      ConstBitStream(uintle = self.chapter, length = 16) + \
      self.unknown5
    
    return data

class NonstopParser():
  def __init__(self):
    self.script_pack = ScriptPack()
    self.filename = ""
    self.magic = None
    self.lines = []
  
  def save(self, filename):
    
    data = BitStream(self.magic) + BitStream(uintle = len(self.lines), length = 16)
    
    for line in self.lines:
      data += line.to_data()
    
    with open(filename, "wb") as f:
      data.tofile(f)
  
  def load(self, filename):
    filename = filename.lower()
    
    if not filename in NONSTOP_DIR:
      _LOGGER.error("Invalid nonstop file: %s" % filename)
      return
    
    self.filename = filename
    
    script_dir = NONSTOP_DIR[filename]
    self.script_pack = ScriptPack(script_dir, common.editor_config.umdimage_dir)
    
    ordered_files = []
    seen_file_ids = []
    
    # --- NONSTOP FORMAT ---
    # XX XX -- ???
    # XX XX -- Number of lines (not necessarily files)
    # 
    # [60 bytes per line]
    # XX XX       -- File number
    # XX XX XX XX
    #  * 0x00000000 = normal line
    #  * 0x01000100 = chatter
    #  * 0x01000000 = ??? (Only appears in SDR2)
    #  * 0x02000000 = ??? (Only appears in SDR2)
    #  * 0x03000000 = ??? (Only appears in SDR2)
    #  * 0x04000000 = ??? (Only appears in SDR2)
    # XX XX       -- Ammo ID that reacts to this line.
    # XX XX       -- Converted line ID that reacts to this line.
    # XX XX       -- ???
    # XX XX       -- 1 = has a weak point, 0 = has no weak point
    # XX XX       -- The amount of time before the next line is shown (in sixtieths of seconds (frames?)).
    # XX XX       -- Unknown (Possibly line orientation? Only 0 in the first game, but sometimes 2 in the second.)
    # XX XX       -- Effect used when transitioning text in.
    # XX XX       -- Effect used when transitioning text out.
    #  * 0: fade
    #  * 1: spin in/out
    #  * 2: zoom out
    #  * 3: slide in/out
    # XX XX       -- The amount of the the line stays on-screen (in sixtieths of seconds (frames?)).
    # XX XX       -- Initial X position (text centered around this pos).
    # XX XX       -- Initial Y position (text centered around this pos).
    # XX XX       -- Text velocity.
    # XX XX       -- Angle of motion.
    # XX XX       -- Initial text zoom (in percent).
    # XX XX       -- Change in zoom over time (in percent).
    #  * 90% means it gradually shrinks.
    #  * 100% means it stays the same size the whole time.
    #  * 110% means it gradually grows.
    # XX XX       -- 0 = no shake, 1 = shake
    # XX XX       -- Rotate the text clockwise to this angle.
    # XX XX       -- Text spins clockwise at this rate.
    # XX XX       -- Speaker (00 00 if chatter)
    # XX XX       -- Sprite ID (00 00 if chatter)
    # XX XX XX XX -- ???
    # XX XX       -- Voice index (FF FF if chatter)
    # XX XX       -- ???
    # XX XX       -- Chapter
    # XX XX XX XX -- ??? (padding?)
    nonstop = ConstBitStream(filename = os.path.join(common.editor_config.umdimage_dir, self.filename))
    
    self.magic = nonstop.read(16)
    num_lines = nonstop.read('uintle:16')
    
    # Four byte header plus 60 bytes per line.
    if nonstop.len < (4 + (num_lines * 60)) * 8:
      raise Exception("Invalid nonstop file.")
    
    prev_non_chatter = -1
    self.lines = []
    
    for i in range(num_lines):
      line              = NonstopLine()
      
      line.file_num     = nonstop.read('uintle:16')
      
      line.line_type    = nonstop.read(32)
      if line.line_type in LINE_TYPE_MAP:
        line.line_type = LINE_TYPE_MAP[line.line_type]
      
      line.ammo_id      = nonstop.read('uintle:16')
      line.converted_id = nonstop.read('uintle:16')
      line.unknown1     = nonstop.read(16)
      line.weak_point   = nonstop.read('uintle:16')
      
      line.delay        = nonstop.read('intle:16')
      line.unknown2     = nonstop.read('intle:16')
      line.in_effect    = nonstop.read('intle:16')
      line.out_effect   = nonstop.read('intle:16')
      line.time_visible = nonstop.read('intle:16')
      line.x_start      = nonstop.read('intle:16')
      line.y_start      = nonstop.read('intle:16')
      line.velocity     = nonstop.read('intle:16')
      line.angle        = nonstop.read('intle:16')
      line.zoom_start   = nonstop.read('intle:16')
      line.zoom_change  = nonstop.read('intle:16')
      line.shake        = nonstop.read('intle:16')
      line.rot_angle    = nonstop.read('intle:16')
      line.spin_vel     = nonstop.read('intle:16')
      
      line.speaker      = nonstop.read('uintle:16')
      
      # Since we mess with speaker a little bit later, we want to keep the ID for the sprite.
      line.char_id      = line.speaker
      line.sprite_id    = nonstop.read('uintle:16')
      
      line.unknown3     = nonstop.read(32)
      line.voice_id     = nonstop.read('uintle:16')
      line.unknown4     = nonstop.read(16)
      line.chapter      = nonstop.read('uintle:16')
      line.unknown5     = nonstop.read(32)
      
      # The second game uses an additional 8 bytes per entry.
      #line.dr2 = nonstop.read(64)
      
      if line.line_type == NONSTOP_LINE_TYPE.normal:
        prev_non_chatter = line.file_num
        
        # Fixing some weirdness.
        if filename in ["nonstop_06_003.dat", "nonstop_06_005.dat", "nonstop_06_006.dat", "nonstop_06_007.dat"] and line.speaker == 16:
          line.speaker = 15
        if filename[:10] == "nonstop_06" and int(filename[11:14]) >= 10 and line.speaker == 10:
          line.speaker = 18
        if filename in ["nonstop_02_003.dat", "nonstop_02_005.dat", "nonstop_04_005.dat", "nonstop_04_006.dat"] and line.speaker == 10:
          line.speaker = 18
        
        self.script_pack[line.file_num].scene_info.speaker = line.speaker
        
        sprite = SpriteId(SPRITE_TYPE.stand, line.char_id, line.sprite_id)
        self.script_pack[line.file_num].scene_info.sprite = sprite
        
        voice = VoiceId(line.speaker, line.chapter, line.voice_id)
        self.script_pack[line.file_num].scene_info.voice = voice
        
        self.script_pack[line.file_num].scene_info.special   = common.SCENE_SPECIAL.debate
      
      elif line.line_type == NONSTOP_LINE_TYPE.chatter:
        self.script_pack[line.file_num].scene_info.speaker   = -1
        self.script_pack[line.file_num].scene_info.special   = common.SCENE_SPECIAL.chatter
        self.script_pack[line.file_num].scene_info.extra_val = prev_non_chatter
      
      else:
        _LOGGER.error("Invalid line type: %s" % line.line_type)
      
      ordered_files.append(self.script_pack[line.file_num])
      seen_file_ids.append(line.file_num)
      
      self.lines.append(line)
    
    for index, file in enumerate(self.script_pack):
      if not index in seen_file_ids:
        ordered_files.append(file)
    
    self.script_pack.script_files = ordered_files

if __name__ == "__main__":
  pass
  # parser = NonstopParser()
  # file = "nonstop_06_006.dat"
  # parser.load(file)
  # parser.lines[2].x_start += 42
  # parser.lines[2].y_start += 1
  # parser.lines[4].x_start += 24
  # parser.lines[6].x_start += 24
  # parser.lines[8].x_start += 24
  # parser.lines[10].x_start += 24
  # parser.lines[12].x_start += 24
  # parser.lines[14].x_start += 24
  # parser.lines[18].x_start += 24
  # parser.lines[21].x_start += 5
  # parser.save(os.path.join("debug", file))
  
  # file = "nonstop_06_005.dat"
  # parser.load(file)
  # parser.lines[10].x_start    += 52
  # parser.lines[10].y_start    += 28
  # parser.lines[12].x_start    += 49
  # parser.lines[12].y_start    -= 28
  # parser.lines[14].x_start    += 52
  # parser.lines[14].y_start    -= 28
  # parser.lines[16].x_start    += 49
  # parser.lines[16].y_start    += 28
  # parser.lines[18].x_start    += 85
  # parser.lines[18].y_start    -= 1
  # parser.lines[18].zoom_start += 5
  # parser.lines[18].angle       = 90
  # parser.lines[18].velocity    = 2
  # parser.save(os.path.join("debug", file))
    
  #for file in sorted(NONSTOP_DIR.keys()):
    # print file
    # for line in parser.lines:
      # print line.file_num, line.x_start, line.y_start, line.in_effect, line.shake
    # print ""

### EOF ###