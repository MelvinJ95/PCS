
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEAPPEND BODY CLEAR COLUMN COMMA DIVIDE ELEMENT_GRID_ADD EQUALS EXIT FALSE FLOAT FOOTER HEAD LPAREN MINUS MULTIPLY NUMBER PATHNAME PERIOD PLUS RECEIPT RPAREN SET_CART_QUANTITY_ENABLE SET_CART_ROW_SIZE SET_DIMENSION SET_SHOP_NAME STRING TABLE_C TABLE_R TO TRUE VIEW item_enable item_type_enable\n    calc : expression\n         | tableExp\n         | pathexpr\n         | receiptexpr\n         | mainviewexpr\n         | reportexpr\n         | empty\n    \n    id : FLOAT\n        | STRING\n    \n    boolean : TRUE\n            | FALSE\n    \n    expression : expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression PLUS expression\n               | expression MINUS expression\n    \n    expression : NUMBER\n               | FLOAT\n    \n    pathexpr : PERIOD PERIOD DIVIDE pathexpr\n           | PERIOD DIVIDE pathexpr\n           | STRING DIVIDE pathexpr\n           | STRING DIVIDE filename\n    filename : STRING PERIOD STRING\n           | STRING\n    \n    receiptexpr : RECEIPT CLEAR HEAD\n            | RECEIPT CLEAR BODY\n            | RECEIPT CLEAR FOOTER\n    \n    receiptexpr : RECEIPT APPEND STRING TO HEAD\n            | RECEIPT APPEND STRING TO BODY\n            | RECEIPT APPEND STRING TO FOOTER\n    \n    mainviewexpr : VIEW STRING\n                | VIEW SET_SHOP_NAME STRING\n                | VIEW SET_DIMENSION NUMBER COMMA NUMBER\n                | VIEW SET_CART_ROW_SIZE NUMBER\n                | VIEW SET_CART_QUANTITY_ENABLE boolean\n                | VIEW ELEMENT_GRID_ADD path_series\n    \n    path_series : STRING\n                | STRING DIVIDE STRING\n    \n    tableExp : TABLE_C STRING column\n    \n    tableExp : TABLE_R STRING column\n    \n    tableExp : TABLE_C STRING\n    \n    column : id\n            | id COMMA column\n    \n    reportexpr : item_type_enable boolean\n                | item_enable boolean\n    \n    expression : EXIT\n    \n    empty :\n    '
    
_lr_action_items = {'NUMBER':([0,20,21,22,23,33,34,69,],[9,9,9,9,9,60,61,76,]),'FLOAT':([0,20,21,22,23,24,26,65,],[10,10,10,10,10,48,48,48,]),'EXIT':([0,20,21,22,23,],[11,11,11,11,11,]),'TABLE_C':([0,],[12,]),'TABLE_R':([0,],[14,]),'PERIOD':([0,15,25,28,49,53,],[15,27,15,15,66,15,]),'STRING':([0,12,14,17,24,25,26,28,30,32,36,53,65,66,70,],[13,24,26,31,45,49,45,13,58,59,64,13,45,72,77,]),'RECEIPT':([0,],[16,]),'VIEW':([0,],[17,]),'item_type_enable':([0,],[18,]),'item_enable':([0,],[19,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,24,31,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,59,61,62,63,64,67,71,72,73,74,75,76,77,],[-46,0,-1,-2,-3,-4,-5,-6,-7,-16,-17,-45,-40,-30,-43,-10,-11,-44,-12,-13,-14,-15,-9,-38,-41,-8,-23,-20,-21,-39,-19,-24,-25,-26,-31,-33,-34,-35,-36,-18,-42,-22,-27,-28,-29,-32,-37,]),'MULTIPLY':([2,9,10,11,41,42,43,44,],[20,-16,-17,-45,-12,-13,20,20,]),'DIVIDE':([2,9,10,11,13,15,27,41,42,43,44,49,64,],[21,-16,-17,-45,25,28,53,-12,-13,21,21,25,70,]),'PLUS':([2,9,10,11,41,42,43,44,],[22,-16,-17,-45,-12,-13,-14,-15,]),'MINUS':([2,9,10,11,41,42,43,44,],[23,-16,-17,-45,-12,-13,-14,-15,]),'CLEAR':([16,],[29,]),'APPEND':([16,],[30,]),'SET_SHOP_NAME':([17,],[32,]),'SET_DIMENSION':([17,],[33,]),'SET_CART_ROW_SIZE':([17,],[34,]),'SET_CART_QUANTITY_ENABLE':([17,],[35,]),'ELEMENT_GRID_ADD':([17,],[36,]),'TRUE':([18,19,35,],[38,38,38,]),'FALSE':([18,19,35,],[39,39,39,]),'HEAD':([29,68,],[55,73,]),'BODY':([29,68,],[56,74,]),'FOOTER':([29,68,],[57,75,]),'COMMA':([45,47,48,60,],[-9,65,-8,69,]),'TO':([58,],[68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,20,21,22,23,],[2,41,42,43,44,]),'tableExp':([0,],[3,]),'pathexpr':([0,25,28,53,],[4,50,54,67,]),'receiptexpr':([0,],[5,]),'mainviewexpr':([0,],[6,]),'reportexpr':([0,],[7,]),'empty':([0,],[8,]),'boolean':([18,19,35,],[37,40,62,]),'column':([24,26,65,],[46,52,71,]),'id':([24,26,65,],[47,47,47,]),'filename':([25,],[51,]),'path_series':([36,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','pcs_lexer.py',233),
  ('calc -> tableExp','calc',1,'p_calc','pcs_lexer.py',234),
  ('calc -> pathexpr','calc',1,'p_calc','pcs_lexer.py',235),
  ('calc -> receiptexpr','calc',1,'p_calc','pcs_lexer.py',236),
  ('calc -> mainviewexpr','calc',1,'p_calc','pcs_lexer.py',237),
  ('calc -> reportexpr','calc',1,'p_calc','pcs_lexer.py',238),
  ('calc -> empty','calc',1,'p_calc','pcs_lexer.py',239),
  ('id -> FLOAT','id',1,'p_id','pcs_lexer.py',245),
  ('id -> STRING','id',1,'p_id','pcs_lexer.py',246),
  ('boolean -> TRUE','boolean',1,'p_boolean','pcs_lexer.py',252),
  ('boolean -> FALSE','boolean',1,'p_boolean','pcs_lexer.py',253),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','pcs_lexer.py',260),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','pcs_lexer.py',261),
  ('expression -> expression PLUS expression','expression',3,'p_expression','pcs_lexer.py',262),
  ('expression -> expression MINUS expression','expression',3,'p_expression','pcs_lexer.py',263),
  ('expression -> NUMBER','expression',1,'p_expression_int_float','pcs_lexer.py',270),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','pcs_lexer.py',271),
  ('pathexpr -> PERIOD PERIOD DIVIDE pathexpr','pathexpr',4,'p_pathexpr','pcs_lexer.py',278),
  ('pathexpr -> PERIOD DIVIDE pathexpr','pathexpr',3,'p_pathexpr','pcs_lexer.py',279),
  ('pathexpr -> STRING DIVIDE pathexpr','pathexpr',3,'p_pathexpr','pcs_lexer.py',280),
  ('pathexpr -> STRING DIVIDE filename','pathexpr',3,'p_pathexpr','pcs_lexer.py',281),
  ('filename -> STRING PERIOD STRING','filename',3,'p_pathexpr','pcs_lexer.py',282),
  ('filename -> STRING','filename',1,'p_pathexpr','pcs_lexer.py',283),
  ('receiptexpr -> RECEIPT CLEAR HEAD','receiptexpr',3,'p_receiptexpr_creat','pcs_lexer.py',290),
  ('receiptexpr -> RECEIPT CLEAR BODY','receiptexpr',3,'p_receiptexpr_creat','pcs_lexer.py',291),
  ('receiptexpr -> RECEIPT CLEAR FOOTER','receiptexpr',3,'p_receiptexpr_creat','pcs_lexer.py',292),
  ('receiptexpr -> RECEIPT APPEND STRING TO HEAD','receiptexpr',5,'p_receiptexpr_append','pcs_lexer.py',299),
  ('receiptexpr -> RECEIPT APPEND STRING TO BODY','receiptexpr',5,'p_receiptexpr_append','pcs_lexer.py',300),
  ('receiptexpr -> RECEIPT APPEND STRING TO FOOTER','receiptexpr',5,'p_receiptexpr_append','pcs_lexer.py',301),
  ('mainviewexpr -> VIEW STRING','mainviewexpr',2,'p_mainviewexp','pcs_lexer.py',311),
  ('mainviewexpr -> VIEW SET_SHOP_NAME STRING','mainviewexpr',3,'p_mainviewexp','pcs_lexer.py',312),
  ('mainviewexpr -> VIEW SET_DIMENSION NUMBER COMMA NUMBER','mainviewexpr',5,'p_mainviewexp','pcs_lexer.py',313),
  ('mainviewexpr -> VIEW SET_CART_ROW_SIZE NUMBER','mainviewexpr',3,'p_mainviewexp','pcs_lexer.py',314),
  ('mainviewexpr -> VIEW SET_CART_QUANTITY_ENABLE boolean','mainviewexpr',3,'p_mainviewexp','pcs_lexer.py',315),
  ('mainviewexpr -> VIEW ELEMENT_GRID_ADD path_series','mainviewexpr',3,'p_mainviewexp','pcs_lexer.py',316),
  ('path_series -> STRING','path_series',1,'p_path_series','pcs_lexer.py',336),
  ('path_series -> STRING DIVIDE STRING','path_series',3,'p_path_series','pcs_lexer.py',337),
  ('tableExp -> TABLE_C STRING column','tableExp',3,'p_createTable','pcs_lexer.py',351),
  ('tableExp -> TABLE_R STRING column','tableExp',3,'p_addRowToTable','pcs_lexer.py',360),
  ('tableExp -> TABLE_C STRING','tableExp',2,'p_showTable','pcs_lexer.py',368),
  ('column -> id','column',1,'p_Column','pcs_lexer.py',376),
  ('column -> id COMMA column','column',3,'p_Column','pcs_lexer.py',377),
  ('reportexpr -> item_type_enable boolean','reportexpr',2,'p_report_create_view','pcs_lexer.py',397),
  ('reportexpr -> item_enable boolean','reportexpr',2,'p_report_create_view','pcs_lexer.py',398),
  ('expression -> EXIT','expression',1,'p_exit','pcs_lexer.py',408),
  ('empty -> <empty>','empty',0,'p_empty','pcs_lexer.py',415),
]
