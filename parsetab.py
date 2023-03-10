
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'F9B55A3B71E1CCBCE87F7D03F5278EAA'
    
_lr_action_items = {'$end':([0,1,2,3,7,9,11,12,14,],[-9,0,-1,-2,-3,-8,-7,-5,-6,]),'ID':([0,],[5,]),'EQUALS':([4,5,],[6,-4,]),'INT':([6,10,13,],[9,9,9,]),'MINUS':([8,9,],[10,-8,]),'PLUS':([9,11,12,14,],[-8,-7,13,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'print':([0,],[1,]),'E':([0,],[2,]),'empty':([0,],[3,]),'R':([0,],[4,]),'S':([6,],[7,]),'L':([6,10,13,],[8,11,14,]),'F':([10,],[12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> print","S'",1,None,None,None),
  ('print -> E','print',1,'p_print','blackjack.py',51),
  ('print -> empty','print',1,'p_print','blackjack.py',52),
  ('E -> R EQUALS S','E',3,'p_E','blackjack.py',58),
  ('R -> ID','R',1,'p_R','blackjack.py',68),
  ('S -> L MINUS F','S',3,'p_S','blackjack.py',74),
  ('F -> F PLUS L','F',3,'p_F','blackjack.py',88),
  ('F -> L','F',1,'p_F_L','blackjack.py',94),
  ('L -> INT','L',1,'p_L','blackjack.py',100),
  ('empty -> <empty>','empty',0,'p_empty','blackjack.py',110),
]
