
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND ASSIGNMENT CLOSEBRACE COLON COMMENT DECI DEN DIVIDE DOUBLE_GREATER DOUBLE_LESS EF EFNOT END_LINE EQUAL GREATER_EQUAL GREATER_THAN IDENTIFIER LESS_EQUAL LESS_THAN LETTA MINUS MODULUS NOT NOT_EQUAL NUMBA OPENBRACE OR OREF PLUS SHOW TIMES WHICHEVA WUD deci letta numba wudprogram : statementstatement : expression\n                 | if_statement\n                 | assign\n                 | print arith_stmt : expression arithm_symbol expression\n                   | expression error term expression : symbol expression : compar_stmt\n                   | arith_stmt symbol : arithm_symbol \n               | compar_symbol arithm_symbol : PLUS\n                      | MINUS\n                      | DIVIDE\n                      | TIMES\n                      | MODULUS  compar_symbol : GREATER_THAN\n                      | LESS_THAN\n                      | EQUAL\n                      | NOT_EQUAL\n                      | GREATER_EQUAL\n                      | LESS_EQUAL arith_stmt : IDENTIFIER arithm_symbol term\n                  | IDENTIFIER error term\n    compar_stmt : factor compar_symbol factor\n                | factor error factor\n    compar_stmt : IDENTIFIER compar_symbol IDENTIFIER\n                | IDENTIFIER compar_symbol factor\n                | IDENTIFIER error factor\n                | IDENTIFIER error IDENTIFIERexpression : termterm : factorarith_symbol : factor arithm_symbol factor \n    factor : NUMBA\n            | DECI\n    term : IDENTIFIERfactor : OPENBRACE expression CLOSEBRACE\n    if_statement : DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement DOUBLE_GREATER\n                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER\n                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement OREF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER\n                 | DOUBLE_LESS EF OPENBRACE error CLOSEBRACE DEN statement DOUBLE_GREATER\n    \n    assign : IDENTIFIER ASSIGNMENT expression\n            | IDENTIFIER ASSIGNMENT WUD\n            | IDENTIFIER ASSIGNMENT LETTA\n            | IDENTIFIER ASSIGNMENT WHICHEVA\n    \n    print : SHOW OPENBRACE IDENTIFIER CLOSEBRACE\n    \n    print : SHOW OPENBRACE factor CLOSEBRACE\n          | SHOW OPENBRACE WUD CLOSEBRACE\n          | SHOW OPENBRACE LETTA CLOSEBRACE\n          | SHOW OPENBRACE error CLOSEBRACE\n    '
    
_lr_action_items = {'DOUBLE_LESS':([0,78,79,85,93,95,],[11,11,11,11,11,11,]),'IDENTIFIER':([0,12,18,19,20,21,22,23,24,25,26,27,28,31,32,36,37,38,39,40,47,77,78,79,85,89,93,95,],[13,35,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,35,46,35,53,55,46,59,69,80,13,13,13,69,13,13,]),'SHOW':([0,78,79,85,93,95,],[14,14,14,14,14,14,]),'PLUS':([0,3,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,48,49,53,54,55,56,57,58,64,65,78,79,85,93,95,],[18,18,-8,-9,-10,-32,18,18,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,18,18,18,18,18,-7,-33,-37,-38,18,-28,-29,-31,-30,-25,-24,-26,-27,18,18,18,18,18,]),'MINUS':([0,3,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,48,49,53,54,55,56,57,58,64,65,78,79,85,93,95,],[19,19,-8,-9,-10,-32,19,19,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,19,19,19,19,19,-7,-33,-37,-38,19,-28,-29,-31,-30,-25,-24,-26,-27,19,19,19,19,19,]),'DIVIDE':([0,3,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,48,49,53,54,55,56,57,58,64,65,78,79,85,93,95,],[20,20,-8,-9,-10,-32,20,20,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,20,20,20,20,20,-7,-33,-37,-38,20,-28,-29,-31,-30,-25,-24,-26,-27,20,20,20,20,20,]),'TIMES':([0,3,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,48,49,53,54,55,56,57,58,64,65,78,79,85,93,95,],[21,21,-8,-9,-10,-32,21,21,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,21,21,21,21,21,-7,-33,-37,-38,21,-28,-29,-31,-30,-25,-24,-26,-27,21,21,21,21,21,]),'MODULUS':([0,3,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,48,49,53,54,55,56,57,58,64,65,78,79,85,93,95,],[22,22,-8,-9,-10,-32,22,22,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,22,22,22,22,22,-7,-33,-37,-38,22,-28,-29,-31,-30,-25,-24,-26,-27,22,22,22,22,22,]),'GREATER_THAN':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[23,23,23,23,-13,-14,-15,-16,-17,-35,-36,23,23,23,-38,23,23,23,23,23,23,23,]),'LESS_THAN':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[24,24,24,24,-13,-14,-15,-16,-17,-35,-36,24,24,24,-38,24,24,24,24,24,24,24,]),'EQUAL':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[25,25,25,25,-13,-14,-15,-16,-17,-35,-36,25,25,25,-38,25,25,25,25,25,25,25,]),'NOT_EQUAL':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[26,26,26,26,-13,-14,-15,-16,-17,-35,-36,26,26,26,-38,26,26,26,26,26,26,26,]),'GREATER_EQUAL':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[27,27,27,27,-13,-14,-15,-16,-17,-35,-36,27,27,27,-38,27,27,27,27,27,27,27,]),'LESS_EQUAL':([0,12,13,15,18,19,20,21,22,29,30,31,35,36,48,68,69,78,79,85,93,95,],[28,28,28,28,-13,-14,-15,-16,-17,-35,-36,28,28,28,-38,28,28,28,28,28,28,28,]),'NUMBA':([0,12,18,19,20,21,22,23,24,25,26,27,28,31,32,36,37,38,39,40,41,42,47,77,78,79,85,89,93,95,],[29,29,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DECI':([0,12,18,19,20,21,22,23,24,25,26,27,28,31,32,36,37,38,39,40,41,42,47,77,78,79,85,89,93,95,],[30,30,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'OPENBRACE':([0,12,14,18,19,20,21,22,23,24,25,26,27,28,31,32,33,36,37,38,39,40,41,42,47,77,78,79,85,86,89,93,95,],[12,12,40,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,12,12,47,12,12,12,12,12,12,12,12,12,12,12,12,89,12,12,12,]),'$end':([1,2,3,4,5,6,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,64,65,70,71,72,73,74,84,87,90,97,],[0,-1,-2,-3,-4,-5,-8,-9,-10,-32,-37,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,-37,-6,-7,-33,-37,-38,-43,-44,-45,-46,-28,-29,-31,-30,-25,-24,-26,-27,-47,-48,-49,-50,-51,-39,-42,-40,-41,]),'DOUBLE_GREATER':([3,4,5,6,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,64,65,70,71,72,73,74,82,83,84,87,88,90,96,97,],[-2,-3,-4,-5,-8,-9,-10,-32,-37,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,-37,-6,-7,-33,-37,-38,-43,-44,-45,-46,-28,-29,-31,-30,-25,-24,-26,-27,-47,-48,-49,-50,-51,84,87,-39,-42,90,-40,97,-41,]),'EFNOT':([3,4,5,6,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,64,65,70,71,72,73,74,82,84,87,90,94,97,],[-2,-3,-4,-5,-8,-9,-10,-32,-37,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,-37,-6,-7,-33,-37,-38,-43,-44,-45,-46,-28,-29,-31,-30,-25,-24,-26,-27,-47,-48,-49,-50,-51,85,-39,-42,-40,95,-41,]),'OREF':([3,4,5,6,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,64,65,70,71,72,73,74,82,84,87,90,97,],[-2,-3,-4,-5,-8,-9,-10,-32,-37,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,-37,-6,-7,-33,-37,-38,-43,-44,-45,-46,-28,-29,-31,-30,-25,-24,-26,-27,-47,-48,-49,-50,-51,86,-39,-42,-40,-41,]),'error':([3,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,35,40,43,44,45,46,47,48,49,53,54,55,56,57,58,64,65,68,69,],[32,-8,-9,-10,-32,38,42,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,32,38,63,32,-7,-33,-37,67,-38,32,-28,-29,-31,-30,-25,-24,-26,-27,42,77,]),'CLOSEBRACE':([7,8,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,35,43,44,45,46,48,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,80,81,91,],[-8,-9,-10,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-35,-36,48,-37,-6,-7,-33,-37,-38,-28,-29,-31,-30,-25,-24,70,71,72,73,74,-26,-27,75,76,-31,-30,92,]),'EF':([11,],[33,]),'ASSIGNMENT':([13,],[36,]),'WUD':([36,40,],[50,61,]),'LETTA':([36,40,],[51,62,]),'WHICHEVA':([36,],[52,]),'DEN':([75,76,92,],[78,79,93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,78,79,85,93,95,],[2,82,83,88,94,96,]),'expression':([0,12,31,36,78,79,85,93,95,],[3,34,43,49,3,3,3,3,3,]),'if_statement':([0,78,79,85,93,95,],[4,4,4,4,4,4,]),'assign':([0,78,79,85,93,95,],[5,5,5,5,5,5,]),'print':([0,78,79,85,93,95,],[6,6,6,6,6,6,]),'symbol':([0,12,31,36,78,79,85,93,95,],[7,7,7,7,7,7,7,7,7,]),'compar_stmt':([0,12,31,36,47,78,79,85,89,93,95,],[8,8,8,8,66,8,8,8,91,8,8,]),'arith_stmt':([0,12,31,36,78,79,85,93,95,],[9,9,9,9,9,9,9,9,9,]),'term':([0,12,31,32,36,38,39,78,79,85,93,95,],[10,10,10,44,10,57,58,10,10,10,10,10,]),'factor':([0,12,31,32,36,37,38,39,40,41,42,47,77,78,79,85,89,93,95,],[15,15,15,45,15,54,56,45,60,64,65,68,81,15,15,15,68,15,15,]),'arithm_symbol':([0,3,12,13,31,34,35,36,43,49,78,79,85,93,95,],[16,31,16,39,16,31,39,16,31,31,16,16,16,16,16,]),'compar_symbol':([0,12,13,15,31,35,36,68,69,78,79,85,93,95,],[17,17,37,41,17,37,17,41,37,17,17,17,17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','jolt_yacc.py',23),
  ('statement -> expression','statement',1,'p_statement','jolt_yacc.py',28),
  ('statement -> if_statement','statement',1,'p_statement','jolt_yacc.py',29),
  ('statement -> assign','statement',1,'p_statement','jolt_yacc.py',30),
  ('statement -> print','statement',1,'p_statement','jolt_yacc.py',31),
  ('arith_stmt -> expression arithm_symbol expression','arith_stmt',3,'p_expression_plus','jolt_yacc.py',36),
  ('arith_stmt -> expression error term','arith_stmt',3,'p_expression_plus','jolt_yacc.py',37),
  ('expression -> symbol','expression',1,'p_expression_symbol','jolt_yacc.py',62),
  ('expression -> compar_stmt','expression',1,'p_expression_stmt_types','jolt_yacc.py',66),
  ('expression -> arith_stmt','expression',1,'p_expression_stmt_types','jolt_yacc.py',67),
  ('symbol -> arithm_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',71),
  ('symbol -> compar_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',72),
  ('arithm_symbol -> PLUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',77),
  ('arithm_symbol -> MINUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',78),
  ('arithm_symbol -> DIVIDE','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',79),
  ('arithm_symbol -> TIMES','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',80),
  ('arithm_symbol -> MODULUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',81),
  ('compar_symbol -> GREATER_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',85),
  ('compar_symbol -> LESS_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',86),
  ('compar_symbol -> EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',87),
  ('compar_symbol -> NOT_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',88),
  ('compar_symbol -> GREATER_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',89),
  ('compar_symbol -> LESS_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',90),
  ('arith_stmt -> IDENTIFIER arithm_symbol term','arith_stmt',3,'p_expression_withidentifier','jolt_yacc.py',94),
  ('arith_stmt -> IDENTIFIER error term','arith_stmt',3,'p_expression_withidentifier','jolt_yacc.py',95),
  ('compar_stmt -> factor compar_symbol factor','compar_stmt',3,'p_expression_comparison','jolt_yacc.py',117),
  ('compar_stmt -> factor error factor','compar_stmt',3,'p_expression_comparison','jolt_yacc.py',118),
  ('compar_stmt -> IDENTIFIER compar_symbol IDENTIFIER','compar_stmt',3,'p_expression_comparison2','jolt_yacc.py',136),
  ('compar_stmt -> IDENTIFIER compar_symbol factor','compar_stmt',3,'p_expression_comparison2','jolt_yacc.py',137),
  ('compar_stmt -> IDENTIFIER error factor','compar_stmt',3,'p_expression_comparison2','jolt_yacc.py',138),
  ('compar_stmt -> IDENTIFIER error IDENTIFIER','compar_stmt',3,'p_expression_comparison2','jolt_yacc.py',139),
  ('expression -> term','expression',1,'p_expression_term','jolt_yacc.py',177),
  ('term -> factor','term',1,'p_term_factor','jolt_yacc.py',181),
  ('arith_symbol -> factor arithm_symbol factor','arith_symbol',3,'p_term_times_div_factors','jolt_yacc.py',185),
  ('factor -> NUMBA','factor',1,'p_factor_digit','jolt_yacc.py',198),
  ('factor -> DECI','factor',1,'p_factor_digit','jolt_yacc.py',199),
  ('term -> IDENTIFIER','term',1,'p_term_factor_iden','jolt_yacc.py',204),
  ('factor -> OPENBRACE expression CLOSEBRACE','factor',3,'p_factor_expr','jolt_yacc.py',208),
  ('if_statement -> DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement DOUBLE_GREATER','if_statement',8,'p_if_statement','jolt_yacc.py',214),
  ('if_statement -> DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER','if_statement',10,'p_if_statement','jolt_yacc.py',215),
  ('if_statement -> DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement OREF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER','if_statement',16,'p_if_statement','jolt_yacc.py',216),
  ('if_statement -> DOUBLE_LESS EF OPENBRACE error CLOSEBRACE DEN statement DOUBLE_GREATER','if_statement',8,'p_if_statement','jolt_yacc.py',217),
  ('assign -> IDENTIFIER ASSIGNMENT expression','assign',3,'p_assign','jolt_yacc.py',243),
  ('assign -> IDENTIFIER ASSIGNMENT WUD','assign',3,'p_assign','jolt_yacc.py',244),
  ('assign -> IDENTIFIER ASSIGNMENT LETTA','assign',3,'p_assign','jolt_yacc.py',245),
  ('assign -> IDENTIFIER ASSIGNMENT WHICHEVA','assign',3,'p_assign','jolt_yacc.py',246),
  ('print -> SHOW OPENBRACE IDENTIFIER CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',256),
  ('print -> SHOW OPENBRACE factor CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',265),
  ('print -> SHOW OPENBRACE WUD CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',266),
  ('print -> SHOW OPENBRACE LETTA CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',267),
  ('print -> SHOW OPENBRACE error CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',268),
]
