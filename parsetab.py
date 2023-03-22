
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGNMENT CLOSEBRACE COLON COMMENT DECI DEN DIVIDE DOUBLE_GREATER DOUBLE_LESS Deci EF EFNOT END_LINE EQUAL GREATER_EQUAL GREATER_THAN IDENTIFIER LESS_EQUAL LESS_THAN LETTA Letta MINUS NOT NOT_EQUAL NUMBA Numba OPENBRACE OR OREF PLUS SHOW TIMES WHICHEVA WUD Wudprogram : statementstatement : expression\n                 | if_statement\n                 | assign\n                 | print  expression : expression PLUS term expression : expression MINUS term expression : symbol symbol : arithm_symbol \n               | compar_symbol arithm_symbol : PLUS\n                      | MINUS\n                      | DIVIDE\n                      | TIMES  compar_symbol : GREATER_THAN\n                      | LESS_THAN\n                      | EQUAL\n                      | NOT_EQUAL\n                      | GREATER_EQUAL\n                      | LESS_EQUAL expression : IDENTIFIER arithm_symbol term \n    expression : factor compar_symbol factor \n    expression : IDENTIFIER compar_symbol IDENTIFIER\n               | IDENTIFIER compar_symbol factor expression : termterm : factorterm : factor arithm_symbol factor \n    factor : NUMBA\n            | DECI\n    factor : OPENBRACE expression CLOSEBRACE\n    if_statement : EF OPENBRACE expression CLOSEBRACE DEN statement\n                 | EF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement\n                 | EF OPENBRACE expression CLOSEBRACE DEN statement OREF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement\n\n    \n    assign : IDENTIFIER ASSIGNMENT NUMBA\n            | IDENTIFIER ASSIGNMENT DECI\n            | IDENTIFIER ASSIGNMENT WUD\n            | IDENTIFIER ASSIGNMENT LETTA\n            | IDENTIFIER ASSIGNMENT WHICHEVA\n            | IDENTIFIER ASSIGNMENT expression\n    \n    print : SHOW OPENBRACE WUD CLOSEBRACE\n          | SHOW OPENBRACE LETTA CLOSEBRACE\n          | SHOW OPENBRACE IDENTIFIER CLOSEBRACE\n    \n    print : SHOW OPENBRACE factor CLOSEBRACE\n          \n    '
    
_lr_action_items = {'IDENTIFIER':([0,16,22,23,24,25,26,27,31,32,35,38,64,66,69,72,74,],[11,37,-15,-16,-17,-18,-19,-20,43,37,37,57,11,11,37,11,11,]),'EF':([0,64,66,72,74,],[15,15,15,15,15,]),'SHOW':([0,64,66,72,74,],[19,19,19,19,19,]),'NUMBA':([0,7,9,16,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,64,66,69,72,74,],[17,-11,-12,17,-13,-14,-15,-16,-17,-18,-19,-20,17,17,17,17,45,17,17,17,17,17,17,17,17,17,]),'DECI':([0,7,9,16,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,64,66,69,72,74,],[18,-11,-12,18,-13,-14,-15,-16,-17,-18,-19,-20,18,18,18,18,46,18,18,18,18,18,18,18,18,18,]),'OPENBRACE':([0,7,9,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,64,66,67,69,72,74,],[16,-11,-12,35,16,38,-13,-14,-15,-16,-17,-18,-19,-20,16,16,16,16,16,16,16,16,16,16,16,69,16,16,16,]),'PLUS':([0,3,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,32,35,36,37,39,40,41,42,43,44,45,46,50,51,52,53,54,64,66,69,70,72,74,],[7,28,-11,-25,-12,-8,7,-9,7,-10,7,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,7,7,28,7,-6,7,-7,-21,-23,-24,-28,-29,28,-22,-27,28,-30,7,7,7,28,7,7,]),'MINUS':([0,3,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,32,35,36,37,39,40,41,42,43,44,45,46,50,51,52,53,54,64,66,69,70,72,74,],[9,29,-11,-25,-12,-8,9,-9,9,-10,9,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,9,9,29,9,-6,9,-7,-21,-23,-24,-28,-29,29,-22,-27,29,-30,9,9,9,29,9,9,]),'DIVIDE':([0,11,13,16,17,18,32,35,37,40,45,46,54,64,66,69,72,74,],[20,20,20,20,-28,-29,20,20,20,20,-28,-29,-30,20,20,20,20,20,]),'TIMES':([0,11,13,16,17,18,32,35,37,40,45,46,54,64,66,69,72,74,],[21,21,21,21,-28,-29,21,21,21,21,-28,-29,-30,21,21,21,21,21,]),'GREATER_THAN':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[22,22,22,22,-28,-29,22,22,22,-28,-29,-30,22,22,22,22,22,]),'LESS_THAN':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[23,23,23,23,-28,-29,23,23,23,-28,-29,-30,23,23,23,23,23,]),'EQUAL':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[24,24,24,24,-28,-29,24,24,24,-28,-29,-30,24,24,24,24,24,]),'NOT_EQUAL':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[25,25,25,25,-28,-29,25,25,25,-28,-29,-30,25,25,25,25,25,]),'GREATER_EQUAL':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[26,26,26,26,-28,-29,26,26,26,-28,-29,-30,26,26,26,26,26,]),'LESS_EQUAL':([0,11,13,16,17,18,32,35,37,45,46,54,64,66,69,72,74,],[27,27,27,27,-28,-29,27,27,27,-28,-29,-30,27,27,27,27,27,]),'$end':([1,2,3,4,5,6,7,8,9,10,12,13,14,17,18,20,21,22,23,24,25,26,27,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,60,61,62,63,65,68,75,],[0,-1,-2,-3,-4,-5,-11,-25,-12,-8,-9,-26,-10,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,-6,-26,-7,-21,-23,-24,-28,-29,-36,-37,-38,-39,-22,-27,-30,-40,-41,-42,-43,-31,-32,-33,]),'EFNOT':([3,4,5,6,7,8,9,10,12,13,14,17,18,20,21,22,23,24,25,26,27,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,60,61,62,63,65,68,73,75,],[-2,-3,-4,-5,-11,-25,-12,-8,-9,-26,-10,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,-6,-26,-7,-21,-23,-24,-28,-29,-36,-37,-38,-39,-22,-27,-30,-40,-41,-42,-43,66,-32,74,-33,]),'OREF':([3,4,5,6,7,8,9,10,12,13,14,17,18,20,21,22,23,24,25,26,27,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,60,61,62,63,65,68,75,],[-2,-3,-4,-5,-11,-25,-12,-8,-9,-26,-10,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,-6,-26,-7,-21,-23,-24,-28,-29,-36,-37,-38,-39,-22,-27,-30,-40,-41,-42,-43,67,-32,-33,]),'CLOSEBRACE':([7,8,9,10,12,13,14,17,18,20,21,22,23,24,25,26,27,36,39,40,41,42,43,44,51,52,53,54,55,56,57,58,70,],[-11,-25,-12,-8,-9,-26,-10,-28,-29,-13,-14,-15,-16,-17,-18,-19,-20,54,-6,-26,-7,-21,-23,-24,-22,-27,59,-30,60,61,62,63,71,]),'ASSIGNMENT':([11,],[32,]),'WUD':([32,38,],[47,55,]),'LETTA':([32,38,],[48,56,]),'WHICHEVA':([32,],[49,]),'DEN':([59,71,],[64,72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,64,66,72,74,],[2,65,68,73,75,]),'expression':([0,16,32,35,64,66,69,72,74,],[3,36,50,53,3,3,70,3,3,]),'if_statement':([0,64,66,72,74,],[4,4,4,4,4,]),'assign':([0,64,66,72,74,],[5,5,5,5,5,]),'print':([0,64,66,72,74,],[6,6,6,6,6,]),'term':([0,16,28,29,30,32,35,64,66,69,72,74,],[8,8,39,41,42,8,8,8,8,8,8,8,]),'symbol':([0,16,32,35,64,66,69,72,74,],[10,10,10,10,10,10,10,10,10,]),'arithm_symbol':([0,11,13,16,32,35,37,40,64,66,69,72,74,],[12,30,34,12,12,12,30,34,12,12,12,12,12,]),'factor':([0,16,28,29,30,31,32,33,34,35,38,64,66,69,72,74,],[13,13,40,40,40,44,13,51,52,13,58,13,13,13,13,13,]),'compar_symbol':([0,11,13,16,32,35,37,64,66,69,72,74,],[14,31,33,14,14,14,31,14,14,14,14,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','jolt_yacc.py',10),
  ('statement -> expression','statement',1,'p_statement','jolt_yacc.py',15),
  ('statement -> if_statement','statement',1,'p_statement','jolt_yacc.py',16),
  ('statement -> assign','statement',1,'p_statement','jolt_yacc.py',17),
  ('statement -> print','statement',1,'p_statement','jolt_yacc.py',18),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','jolt_yacc.py',27),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','jolt_yacc.py',31),
  ('expression -> symbol','expression',1,'p_expression_symbol','jolt_yacc.py',35),
  ('symbol -> arithm_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',39),
  ('symbol -> compar_symbol','symbol',1,'p_expr_symbols','jolt_yacc.py',40),
  ('arithm_symbol -> PLUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',45),
  ('arithm_symbol -> MINUS','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',46),
  ('arithm_symbol -> DIVIDE','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',47),
  ('arithm_symbol -> TIMES','arithm_symbol',1,'p_symbol_arithm','jolt_yacc.py',48),
  ('compar_symbol -> GREATER_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',52),
  ('compar_symbol -> LESS_THAN','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',53),
  ('compar_symbol -> EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',54),
  ('compar_symbol -> NOT_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',55),
  ('compar_symbol -> GREATER_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',56),
  ('compar_symbol -> LESS_EQUAL','compar_symbol',1,'p_symbol_comparison','jolt_yacc.py',57),
  ('expression -> IDENTIFIER arithm_symbol term','expression',3,'p_expression_withidentifier','jolt_yacc.py',61),
  ('expression -> factor compar_symbol factor','expression',3,'p_expression_comparison','jolt_yacc.py',77),
  ('expression -> IDENTIFIER compar_symbol IDENTIFIER','expression',3,'p_expression_comparison2','jolt_yacc.py',94),
  ('expression -> IDENTIFIER compar_symbol factor','expression',3,'p_expression_comparison2','jolt_yacc.py',95),
  ('expression -> term','expression',1,'p_expression_term','jolt_yacc.py',125),
  ('term -> factor','term',1,'p_term_factor','jolt_yacc.py',129),
  ('term -> factor arithm_symbol factor','term',3,'p_term_times_div_factors','jolt_yacc.py',133),
  ('factor -> NUMBA','factor',1,'p_factor_digit','jolt_yacc.py',147),
  ('factor -> DECI','factor',1,'p_factor_digit','jolt_yacc.py',148),
  ('factor -> OPENBRACE expression CLOSEBRACE','factor',3,'p_factor_expr','jolt_yacc.py',153),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement','if_statement',6,'p_if_statement','jolt_yacc.py',159),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement','if_statement',8,'p_if_statement','jolt_yacc.py',160),
  ('if_statement -> EF OPENBRACE expression CLOSEBRACE DEN statement OREF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement','if_statement',14,'p_if_statement','jolt_yacc.py',161),
  ('assign -> IDENTIFIER ASSIGNMENT NUMBA','assign',3,'p_assign','jolt_yacc.py',183),
  ('assign -> IDENTIFIER ASSIGNMENT DECI','assign',3,'p_assign','jolt_yacc.py',184),
  ('assign -> IDENTIFIER ASSIGNMENT WUD','assign',3,'p_assign','jolt_yacc.py',185),
  ('assign -> IDENTIFIER ASSIGNMENT LETTA','assign',3,'p_assign','jolt_yacc.py',186),
  ('assign -> IDENTIFIER ASSIGNMENT WHICHEVA','assign',3,'p_assign','jolt_yacc.py',187),
  ('assign -> IDENTIFIER ASSIGNMENT expression','assign',3,'p_assign','jolt_yacc.py',188),
  ('print -> SHOW OPENBRACE WUD CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',197),
  ('print -> SHOW OPENBRACE LETTA CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',198),
  ('print -> SHOW OPENBRACE IDENTIFIER CLOSEBRACE','print',4,'p_print_show','jolt_yacc.py',199),
  ('print -> SHOW OPENBRACE factor CLOSEBRACE','print',4,'p_print_show2','jolt_yacc.py',210),
]
