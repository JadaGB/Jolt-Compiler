
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND ASSIGNMENT CLOSEBRACE COLON COMMENT DECI DEN DIVIDE DOUBLE_GREATER DOUBLE_LESS Deci EF EFNOT END_LINE EQUAL FUNCTION GREATER_EQUAL GREATER_THAN IDENTIFIER LESS_EQUAL LESS_THAN LETTA Letta MINUS NOT NOT_EQUAL NUMBA Numba OPENBRACE OR OREF PLUS SHOW TIMES WHICHEVA WUD Wudprogram : statementstatement : expression\n                 | if_statement\n                 | assign\n                 | print  expression : expression arithm_symbol term\n                  | expression error term expression : symbol symbol : arithm_symbol \n               | compar_symbol arithm_symbol : PLUS\n                      | MINUS\n                      | DIVIDE\n                      | TIMES  compar_symbol : GREATER_THAN\n                      | LESS_THAN\n                      | EQUAL\n                      | NOT_EQUAL\n                      | GREATER_EQUAL\n                      | LESS_EQUAL expression : IDENTIFIER arithm_symbol term\n                  | IDENTIFIER error term\n    expression : factor compar_symbol factor\n               | factor error factor\n    expression : IDENTIFIER compar_symbol IDENTIFIER\n               | IDENTIFIER compar_symbol factor\n               | IDENTIFIER error factor\n               | IDENTIFIER error IDENTIFIERexpression : termterm : factorterm : factor arithm_symbol factor \n    factor : NUMBA\n            | DECI\n    term : IDENTIFIERfactor : OPENBRACE expression CLOSEBRACE\n    if_statement : EF OPENBRACE expression CLOSEBRACE DEN statement\n                 | EF error expression CLOSEBRACE DEN statement\n                 | EF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement\n                 | EF OPENBRACE expression CLOSEBRACE DEN statement OREF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement\n    \n    assign : IDENTIFIER ASSIGNMENT NUMBA\n            | IDENTIFIER ASSIGNMENT DECI\n            | IDENTIFIER ASSIGNMENT WUD\n            | IDENTIFIER ASSIGNMENT LETTA\n            | IDENTIFIER ASSIGNMENT WHICHEVA\n            | IDENTIFIER ASSIGNMENT expression\n    \n    print : SHOW OPENBRACE WUD CLOSEBRACE\n          | SHOW error WUD CLOSEBRACE\n          | SHOW OPENBRACE LETTA CLOSEBRACE\n          | SHOW OPENBRACE IDENTIFIER CLOSEBRACE\n    \n    print : SHOW OPENBRACE factor CLOSEBRACE\n    '
    
_lr_action_items = {'IDENTIFIER':([0,14,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,37,38,41,77,78,81,84,87,89,],[10,40,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,45,45,45,48,51,40,40,40,67,10,10,10,40,10,10,]),'EF':([0,77,78,81,87,89,],[13,13,13,13,13,13,]),'SHOW':([0,77,78,81,87,89,],[17,17,17,17,17,17,]),'NUMBA':([0,14,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,77,78,81,84,87,89,],[15,15,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,15,15,15,15,15,53,15,15,15,15,15,15,15,15,15,15,15,15,]),'DECI':([0,14,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,77,78,81,84,87,89,],[16,16,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,16,16,16,16,16,54,16,16,16,16,16,16,16,16,16,16,16,16,]),'OPENBRACE':([0,13,14,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,77,78,81,82,84,87,89,],[14,37,14,41,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,84,14,14,14,]),'PLUS':([0,3,7,8,9,10,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,33,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,77,78,81,84,85,87,89,],[18,18,-9,-29,-8,18,18,-10,18,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,18,18,18,18,18,-6,18,-34,-7,-21,-28,-22,18,-25,-26,-32,-33,18,-23,-24,-31,18,18,-35,18,18,18,18,18,18,18,]),'MINUS':([0,3,7,8,9,10,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,33,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,77,78,81,84,85,87,89,],[19,19,-9,-29,-8,19,19,-10,19,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,19,19,19,19,19,-6,19,-34,-7,-21,-28,-22,19,-25,-26,-32,-33,19,-23,-24,-31,19,19,-35,19,19,19,19,19,19,19,]),'DIVIDE':([0,3,7,8,9,10,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,33,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,77,78,81,84,85,87,89,],[20,20,-9,-29,-8,20,20,-10,20,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,20,20,20,20,20,-6,20,-34,-7,-21,-28,-22,20,-25,-26,-32,-33,20,-23,-24,-31,20,20,-35,20,20,20,20,20,20,20,]),'TIMES':([0,3,7,8,9,10,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,33,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,77,78,81,84,85,87,89,],[21,21,-9,-29,-8,21,21,-10,21,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,21,21,21,21,21,-6,21,-34,-7,-21,-28,-22,21,-25,-26,-32,-33,21,-23,-24,-31,21,21,-35,21,21,21,21,21,21,21,]),'GREATER_THAN':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[22,22,22,22,-32,-33,22,22,22,22,-32,-33,-35,22,22,22,22,22,22,]),'LESS_THAN':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[23,23,23,23,-32,-33,23,23,23,23,-32,-33,-35,23,23,23,23,23,23,]),'EQUAL':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[24,24,24,24,-32,-33,24,24,24,24,-32,-33,-35,24,24,24,24,24,24,]),'NOT_EQUAL':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[25,25,25,25,-32,-33,25,25,25,25,-32,-33,-35,25,25,25,25,25,25,]),'GREATER_EQUAL':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[26,26,26,26,-32,-33,26,26,26,26,-32,-33,-35,26,26,26,26,26,26,]),'LESS_EQUAL':([0,10,11,14,15,16,33,37,38,40,53,54,64,77,78,81,84,87,89,],[27,27,27,27,-32,-33,27,27,27,27,-32,-33,-35,27,27,27,27,27,27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,15,16,18,19,20,21,22,23,24,25,26,27,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,72,73,74,75,76,79,80,83,90,],[0,-1,-2,-3,-4,-5,-9,-29,-8,-34,-30,-10,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-34,-6,-30,-34,-7,-21,-28,-22,-27,-25,-26,-32,-33,-42,-43,-44,-45,-23,-24,-31,-35,-46,-48,-49,-50,-47,-36,-37,-38,-39,]),'EFNOT':([3,4,5,6,7,8,9,10,11,12,15,16,18,19,20,21,22,23,24,25,26,27,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,72,73,74,75,76,79,80,83,88,90,],[-2,-3,-4,-5,-9,-29,-8,-34,-30,-10,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-34,-6,-30,-34,-7,-21,-28,-22,-27,-25,-26,-32,-33,-42,-43,-44,-45,-23,-24,-31,-35,-46,-48,-49,-50,-47,81,-37,-38,89,-39,]),'OREF':([3,4,5,6,7,8,9,10,11,12,15,16,18,19,20,21,22,23,24,25,26,27,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,72,73,74,75,76,79,80,83,90,],[-2,-3,-4,-5,-9,-29,-8,-34,-30,-10,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-34,-6,-30,-34,-7,-21,-28,-22,-27,-25,-26,-32,-33,-42,-43,-44,-45,-23,-24,-31,-35,-46,-48,-49,-50,-47,82,-37,-38,-39,]),'error':([3,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,39,40,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,85,],[29,-9,-29,-8,31,35,-10,38,-32,-33,42,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,29,31,-6,-30,-34,-7,-21,-28,-22,-27,-25,-26,-32,-33,29,-23,-24,-31,29,29,-35,29,]),'CLOSEBRACE':([7,8,9,11,12,15,16,18,19,20,21,22,23,24,25,26,27,39,40,43,44,45,46,47,48,49,50,51,52,59,60,61,62,63,64,65,66,67,68,69,85,],[-9,-29,-8,-30,-10,-32,-33,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,64,-34,-6,-30,-34,-7,-21,-28,-22,-27,-25,-26,-23,-24,-31,70,71,-35,72,73,74,75,76,86,]),'ASSIGNMENT':([10,],[33,]),'WUD':([33,41,42,],[55,65,69,]),'LETTA':([33,41,],[56,66,]),'WHICHEVA':([33,],[57,]),'DEN':([70,71,86,],[77,78,87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,77,78,81,87,89,],[2,79,80,83,88,90,]),'expression':([0,14,33,37,38,77,78,81,84,87,89,],[3,39,58,62,63,3,3,3,85,3,3,]),'if_statement':([0,77,78,81,87,89,],[4,4,4,4,4,4,]),'assign':([0,77,78,81,87,89,],[5,5,5,5,5,5,]),'print':([0,77,78,81,87,89,],[6,6,6,6,6,6,]),'arithm_symbol':([0,3,10,11,14,33,37,38,39,40,44,50,58,62,63,77,78,81,84,85,87,89,],[7,28,30,36,7,7,7,7,28,30,36,36,28,28,28,7,7,7,7,28,7,7,]),'term':([0,14,28,29,30,31,33,37,38,77,78,81,84,87,89,],[8,8,43,46,47,49,8,8,8,8,8,8,8,8,8,]),'symbol':([0,14,33,37,38,77,78,81,84,87,89,],[9,9,9,9,9,9,9,9,9,9,9,]),'factor':([0,14,28,29,30,31,32,33,34,35,36,37,38,41,77,78,81,84,87,89,],[11,11,44,44,44,50,52,11,59,60,61,11,11,68,11,11,11,11,11,11,]),'compar_symbol':([0,10,11,14,33,37,38,40,77,78,81,84,87,89,],[12,32,34,12,12,12,12,32,12,12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','jolt_yacc.py',22),
  ('statement -> expression','statement',1,'p_statement','jolt_yacc.py',27),
  ('statement -> if_statement','statement',1,'p_statement','jolt_yacc.py',28),
  ('statement -> assign','statement',1,'p_statement','jolt_yacc.py',29),
  ('statement -> print','statement',1,'p_statement','jolt_yacc.py',30),
  ('expression -> expression arithm_symbol term','expression',3,'p_expression_plus','jolt_yacc.py',35),
  ('expression -> expression error term','expression',3,'p_expression_plus','jolt_yacc.py',36),
  ('expression -> symbol','expression',1,'p_expression_symbol','jolt_yacc.py',66),
  ('symbol -> arithm_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',70),
  ('symbol -> compar_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',71),
  ('arithm_symbol -> PLUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',76),
  ('arithm_symbol -> MINUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',77),
  ('arithm_symbol -> DIVIDE','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',78),
  ('arithm_symbol -> TIMES','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',79),
  ('compar_symbol -> GREATER_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',83),
  ('compar_symbol -> LESS_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',84),
  ('compar_symbol -> EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',85),
  ('compar_symbol -> NOT_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',86),
  ('compar_symbol -> GREATER_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',87),
  ('compar_symbol -> LESS_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',88),
  ('expression -> IDENTIFIER arithm_symbol term','expression',3,'p_expression_withidentifier','jolt_yacc.py',92),
  ('expression -> IDENTIFIER error term','expression',3,'p_expression_withidentifier','jolt_yacc.py',93),
  ('expression -> factor compar_symbol factor','expression',3,'p_expression_comparison','jolt_yacc.py',115),
  ('expression -> factor error factor','expression',3,'p_expression_comparison','jolt_yacc.py',116),
  ('expression -> IDENTIFIER compar_symbol IDENTIFIER','expression',3,'p_expression_comparison2','jolt_yacc.py',134),
  ('expression -> IDENTIFIER compar_symbol factor','expression',3,'p_expression_comparison2','jolt_yacc.py',135),
  ('expression -> IDENTIFIER error factor','expression',3,'p_expression_comparison2','jolt_yacc.py',136),
  ('expression -> IDENTIFIER error IDENTIFIER','expression',3,'p_expression_comparison2','jolt_yacc.py',137),
  ('expression -> term','expression',1,'p_expression_term','jolt_yacc.py',171),
  ('term -> factor','term',1,'p_term_factor','jolt_yacc.py',175),
  ('term -> factor arithm_symbol factor','term',3,'p_term_times_div_factors','jolt_yacc.py',179),
  ('factor -> NUMBA','factor',1,'p_factor_digit','jolt_yacc.py',192),
  ('factor -> DECI','factor',1,'p_factor_digit','jolt_yacc.py',193),
  ('term -> IDENTIFIER','term',1,'p_term_factor_iden','jolt_yacc.py',198),
  ('factor -> OPENBRACE expression CLOSEBRACE','factor',3,'p_factor_expr','jolt_yacc.py',202),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement','if_statement',6,'p_if_statement','jolt_yacc.py',208),
  ('if_statement -> EF error expression CLOSEBRACE DEN statement','if_statement',6,'p_if_statement','jolt_yacc.py',209),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement','if_statement',8,'p_if_statement','jolt_yacc.py',210),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement OREF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement','if_statement',14,'p_if_statement','jolt_yacc.py',211),
  ('assign -> IDENTIFIER ASSIGNMENT NUMBA','assign',3,'p_assign','jolt_yacc.py',236),
  ('assign -> IDENTIFIER ASSIGNMENT DECI','assign',3,'p_assign','jolt_yacc.py',237),
  ('assign -> IDENTIFIER ASSIGNMENT WUD','assign',3,'p_assign','jolt_yacc.py',238),
  ('assign -> IDENTIFIER ASSIGNMENT LETTA','assign',3,'p_assign','jolt_yacc.py',239),
  ('assign -> IDENTIFIER ASSIGNMENT WHICHEVA','assign',3,'p_assign','jolt_yacc.py',240),
  ('assign -> IDENTIFIER ASSIGNMENT expression','assign',3,'p_assign','jolt_yacc.py',241),
  ('print -> SHOW OPENBRACE WUD CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',251),
  ('print -> SHOW error WUD CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',252),
  ('print -> SHOW OPENBRACE LETTA CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',253),
  ('print -> SHOW OPENBRACE IDENTIFIER CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',254),
  ('print -> SHOW OPENBRACE factor CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',266),
]
