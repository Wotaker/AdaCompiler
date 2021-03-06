
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'progABS AMPERSAND AND APOSTROPHE ARRAY ASSIGN BEGIN BOOL BOOL_VAL BOOL_VAL COLON COMMA COMMENT DECLARE DIV DOT DUB_DOT ELSE ELSIF END EQUALS FOR FUNC GREATER GTEQ IDENT IF IMAGE IN IS LEFT_CUR_PAR LEFT_PAR LEFT_SQ_PAR LESS LOOP LSEQ MINUS MOD MUL NOT NOT_EQUALS NULL NUMBER OF OR PLUS POW PROC PUT_LINE RETURN REVERSE RIGHT_CUR_PAR RIGHT_PAR RIGHT_SQ_PAR SEMICOLON STRING THEN TYPE_BOOL TYPE_FLOAT TYPE_INT USE WHILE WITH XORempty :prog : subprogram\n            | headers subprogramheaders : headers header\n               | headerheader : WITH pkg SEMICOLON\n              | WITH pkg SEMICOLON USE pkg SEMICOLONpkg : pkg DOT IDENT\n           | IDENTsubprogram : procedure\n                  | functionfunction : FUNC IDENT args_opt RETURN type IS declarations BEGIN ret_statements END IDENT SEMICOLONfunction_call : IDENT LEFT_PAR value RIGHT_PARprocedure : PROC IDENT args_opt IS declarations BEGIN statements END IDENT SEMICOLONargs_opt : LEFT_PAR args RIGHT_PAR\n                | emptyargs : args COMMA arg\n            | argarg : IDENT COLON typetype : TYPE_INT\n            | TYPE_FLOAT\n            | TYPE_BOOLdeclarations : declarations declaration\n                    | declarationdeclaration : empty\n                   | function\n                   | procedure\n                   | IDENT COLON type ASSIGN value SEMICOLONvalue : expr\n             | bool_exprexpr : expr PLUS term\n            | expr MINUS term\n            | termterm : term MUL factor\n            | term DIV factor\n            | factorfactor : LEFT_PAR expr RIGHT_PAR\n              | function_call\n              | IDENT\n              | NUMBERbool_expr : bool_term AND bool_term\n                 | bool_term OR bool_term\n                 | bool_termbool_term : NOT bool\n                 | boolbool : LEFT_PAR bool_expr RIGHT_PAR\n            | BOOL_VAL\n            | IDENT\n            | rel_operand rel_operator rel_operandrel_operand : NUMBER\n                   | IDENTrel_operator : EQUALS\n                    | NOT_EQUALS\n                    | GREATER\n                    | LESS\n                    | GTEQ\n                    | LSEQstatements : statements statement\n                  | statementstatement : assign\n                 | if\n                 | loop\n                 | put_line\n                 | function_call SEMICOLONret_statements : ret_statements ret_statement\n                      | ret_statementret_statement : statement\n                     | RETURN value SEMICOLONassign : IDENT ASSIGN value SEMICOLONif : IF bool_expr THEN ret_statements elsifs else END IF SEMICOLONelsifs : elsifs elsif\n              | emptyelsif : ELSIF bool_expr THEN ret_statementselse : ELSE ret_statements\n            | emptyloop : loop_body\n            | for_range loop_body\n            | while loop_bodyloop_body : LOOP statements END LOOP SEMICOLONfor_range : FOR IDENT IN expr DUB_DOT exprwhile : WHILE bool_exprput_line : PUT_LINE LEFT_PAR str_expr RIGHT_PAR SEMICOLONstr_expr : str_expr AMPERSAND str_term\n                | str_termstr_term : STRING\n                | type APOSTROPHE IMAGE LEFT_PAR value RIGHT_PAR'
    
_lr_action_items = {'PROC':([0,3,6,11,20,22,30,31,32,33,34,45,48,49,67,124,132,171,],[7,7,-5,-4,-6,7,7,-24,-25,-26,-27,-23,7,-7,7,-28,-14,-12,]),'FUNC':([0,3,6,11,20,22,30,31,32,33,34,45,48,49,67,124,132,171,],[8,8,-5,-4,-6,8,8,-24,-25,-26,-27,-23,8,-7,8,-28,-14,-12,]),'WITH':([0,3,6,11,20,49,],[9,9,-5,-4,-6,-7,]),'$end':([1,2,4,5,10,132,171,],[0,-2,-10,-11,-3,-14,-12,]),'IDENT':([7,8,9,17,21,22,27,30,31,32,33,34,36,44,45,48,52,53,54,55,56,57,59,60,64,65,66,67,68,69,70,71,72,73,76,78,83,84,86,89,96,102,103,104,107,108,109,110,111,112,113,119,120,121,122,123,124,125,126,127,128,130,132,133,145,148,149,157,160,161,162,166,168,169,171,173,177,179,180,],[12,13,15,25,28,29,15,29,-24,-25,-26,-27,25,51,-23,29,51,-59,-60,-61,-62,-63,80,-76,51,87,80,29,90,90,90,101,-58,-64,80,80,-77,-78,51,51,90,51,80,80,138,-52,-53,-54,-55,-56,-57,143,90,51,-66,-67,-28,143,143,143,143,-69,-14,51,143,163,-65,-82,-79,143,-68,51,80,90,-12,51,51,-70,51,]),'LEFT_PAR':([12,13,51,59,63,66,68,69,70,76,78,90,96,103,104,119,120,125,126,127,128,143,145,159,161,168,169,],[17,17,70,78,85,78,96,96,96,78,78,70,96,78,78,145,96,145,145,145,145,70,145,169,145,78,96,]),'IS':([12,16,18,35,38,39,40,41,],[-1,22,-16,-15,48,-20,-21,-22,]),'RETURN':([13,18,19,35,54,55,56,57,60,73,83,84,89,102,121,122,123,130,133,149,157,160,162,166,173,177,179,180,],[-1,-16,26,-15,-60,-61,-62,-63,-76,-64,-77,-78,120,120,120,-66,-67,-69,120,-65,-82,-79,-68,120,120,120,-70,120,]),'SEMICOLON':([14,15,28,42,58,75,77,79,80,82,90,91,92,93,94,95,97,98,99,101,105,131,134,135,136,137,138,139,142,143,146,147,150,151,152,153,154,163,176,],[20,-9,-8,49,73,-43,-45,-47,-48,-50,-39,124,-29,-30,-33,-36,-38,-40,130,132,-44,-13,-41,-42,-46,-49,-51,157,160,-39,-40,162,-31,-32,-34,-35,-37,171,179,]),'DOT':([14,15,28,42,],[21,-9,-8,21,]),'USE':([20,],[27,]),'BEGIN':([22,30,31,32,33,34,45,48,67,124,132,171,],[-1,44,-24,-25,-26,-27,-23,-1,89,-28,-14,-12,]),'RIGHT_PAR':([23,24,39,40,41,46,47,75,77,79,80,82,90,92,93,94,95,97,98,100,105,106,114,115,116,129,131,134,135,136,137,138,143,146,150,151,152,153,154,158,175,178,],[35,-18,-20,-21,-22,-17,-19,-43,-45,-47,-48,-50,-39,-29,-30,-33,-36,-38,-40,131,-44,136,139,-84,-85,154,-13,-41,-42,-46,-49,-51,-39,-40,-31,-32,-34,-35,-37,-83,178,-86,]),'COMMA':([23,24,39,40,41,46,47,],[36,-18,-20,-21,-22,-17,-19,]),'COLON':([25,29,],[37,43,]),'TYPE_INT':([26,37,43,85,140,],[39,39,39,39,39,]),'TYPE_FLOAT':([26,37,43,85,140,],[40,40,40,40,40,]),'TYPE_BOOL':([26,37,43,85,140,],[41,41,41,41,41,]),'ASSIGN':([39,40,41,50,51,],[-20,-21,-22,68,69,]),'APOSTROPHE':([39,40,41,117,],[-20,-21,-22,141,]),'IF':([44,52,53,54,55,56,57,60,64,72,73,83,84,86,89,102,121,122,123,130,133,149,157,160,162,166,172,173,177,179,180,],[59,59,-59,-60,-61,-62,-63,-76,59,-58,-64,-77,-78,59,59,59,59,-66,-67,-69,59,-65,-82,-79,-68,59,176,59,59,-70,59,]),'PUT_LINE':([44,52,53,54,55,56,57,60,64,72,73,83,84,86,89,102,121,122,123,130,133,149,157,160,162,166,173,177,179,180,],[63,63,-59,-60,-61,-62,-63,-76,63,-58,-64,-77,-78,63,63,63,63,-66,-67,-69,63,-65,-82,-79,-68,63,63,63,-70,63,]),'LOOP':([44,52,53,54,55,56,57,60,61,62,64,72,73,75,77,79,80,82,83,84,86,88,89,94,95,97,102,105,118,121,122,123,130,131,133,134,135,136,137,138,143,146,149,150,151,152,153,154,157,160,162,166,170,173,177,179,180,],[64,64,-59,-60,-61,-62,-63,-76,64,64,64,-58,-64,-43,-45,-47,-48,-50,-77,-78,64,-81,64,-33,-36,-38,64,-44,142,64,-66,-67,-69,-13,64,-41,-42,-46,-49,-51,-39,-40,-65,-31,-32,-34,-35,-37,-82,-79,-68,64,-80,64,64,-70,64,]),'FOR':([44,52,53,54,55,56,57,60,64,72,73,83,84,86,89,102,121,122,123,130,133,149,157,160,162,166,173,177,179,180,],[65,65,-59,-60,-61,-62,-63,-76,65,-58,-64,-77,-78,65,65,65,65,-66,-67,-69,65,-65,-82,-79,-68,65,65,65,-70,65,]),'WHILE':([44,52,53,54,55,56,57,60,64,72,73,83,84,86,89,102,121,122,123,130,133,149,157,160,162,166,173,177,179,180,],[66,66,-59,-60,-61,-62,-63,-76,66,-58,-64,-77,-78,66,66,66,66,-66,-67,-69,66,-65,-82,-79,-68,66,66,66,-70,66,]),'END':([52,53,54,55,56,57,60,72,73,83,84,86,121,122,123,130,133,149,155,156,157,160,162,164,165,167,173,179,180,],[71,-59,-60,-61,-62,-63,-76,-58,-64,-77,-78,118,148,-66,-67,-69,-1,-65,-1,-72,-82,-79,-68,172,-71,-75,-74,-70,-73,]),'ELSE':([54,55,56,57,60,73,83,84,122,123,130,133,149,155,156,157,160,162,165,179,180,],[-60,-61,-62,-63,-76,-64,-77,-78,-66,-67,-69,-1,-65,166,-72,-82,-79,-68,-71,-70,-73,]),'ELSIF':([54,55,56,57,60,73,83,84,122,123,130,133,149,155,156,157,160,162,165,179,180,],[-60,-61,-62,-63,-76,-64,-77,-78,-66,-67,-69,-1,-65,168,-72,-82,-79,-68,-71,-70,-73,]),'NOT':([59,66,68,69,70,78,96,103,104,120,168,169,],[76,76,76,76,76,76,76,76,76,76,76,76,]),'BOOL_VAL':([59,66,68,69,70,76,78,96,103,104,120,168,169,],[79,79,79,79,79,79,79,79,79,79,79,79,79,]),'NUMBER':([59,66,68,69,70,76,78,96,103,104,107,108,109,110,111,112,113,119,120,125,126,127,128,145,161,168,169,],[82,82,98,98,98,82,82,98,82,82,82,-52,-53,-54,-55,-56,-57,146,98,146,146,146,146,146,146,82,98,]),'THEN':([74,75,77,79,80,82,105,134,135,136,137,138,174,],[102,-43,-45,-47,-48,-50,-44,-41,-42,-46,-49,-51,177,]),'AND':([75,77,79,80,82,90,105,136,137,138,],[103,-45,-47,-48,-50,-48,-44,-46,-49,-51,]),'OR':([75,77,79,80,82,90,105,136,137,138,],[104,-45,-47,-48,-50,-48,-44,-46,-49,-51,]),'EQUALS':([80,81,82,90,98,],[-51,108,-50,-51,-50,]),'NOT_EQUALS':([80,81,82,90,98,],[-51,109,-50,-51,-50,]),'GREATER':([80,81,82,90,98,],[-51,110,-50,-51,-50,]),'LESS':([80,81,82,90,98,],[-51,111,-50,-51,-50,]),'GTEQ':([80,81,82,90,98,],[-51,112,-50,-51,-50,]),'LSEQ':([80,81,82,90,98,],[-51,113,-50,-51,-50,]),'STRING':([85,140,],[116,116,]),'IN':([87,],[119,]),'MUL':([90,94,95,97,98,131,143,146,150,151,152,153,154,],[-39,127,-36,-38,-40,-13,-39,-40,127,127,-34,-35,-37,]),'DIV':([90,94,95,97,98,131,143,146,150,151,152,153,154,],[-39,128,-36,-38,-40,-13,-39,-40,128,128,-34,-35,-37,]),'PLUS':([90,92,94,95,97,98,129,131,143,144,146,150,151,152,153,154,170,],[-39,125,-33,-36,-38,-40,125,-13,-39,125,-40,-31,-32,-34,-35,-37,125,]),'MINUS':([90,92,94,95,97,98,129,131,143,144,146,150,151,152,153,154,170,],[-39,126,-33,-36,-38,-40,126,-13,-39,126,-40,-31,-32,-34,-35,-37,126,]),'DUB_DOT':([94,95,97,131,143,144,146,150,151,152,153,154,],[-33,-36,-38,-13,-39,161,-40,-31,-32,-34,-35,-37,]),'AMPERSAND':([114,115,116,158,178,],[140,-84,-85,-83,-86,]),'IMAGE':([141,],[159,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'subprogram':([0,3,],[2,10,]),'headers':([0,],[3,]),'procedure':([0,3,22,30,48,67,],[4,4,34,34,34,34,]),'function':([0,3,22,30,48,67,],[5,5,33,33,33,33,]),'header':([0,3,],[6,11,]),'pkg':([9,27,],[14,42,]),'args_opt':([12,13,],[16,19,]),'empty':([12,13,22,30,48,67,133,155,],[18,18,32,32,32,32,156,167,]),'args':([17,],[23,]),'arg':([17,36,],[24,46,]),'declarations':([22,48,],[30,67,]),'declaration':([22,30,48,67,],[31,45,31,45,]),'type':([26,37,43,85,140,],[38,47,50,117,117,]),'statements':([44,64,],[52,86,]),'statement':([44,52,64,86,89,102,121,133,166,173,177,180,],[53,72,53,72,123,123,123,123,123,123,123,123,]),'assign':([44,52,64,86,89,102,121,133,166,173,177,180,],[54,54,54,54,54,54,54,54,54,54,54,54,]),'if':([44,52,64,86,89,102,121,133,166,173,177,180,],[55,55,55,55,55,55,55,55,55,55,55,55,]),'loop':([44,52,64,86,89,102,121,133,166,173,177,180,],[56,56,56,56,56,56,56,56,56,56,56,56,]),'put_line':([44,52,64,86,89,102,121,133,166,173,177,180,],[57,57,57,57,57,57,57,57,57,57,57,57,]),'function_call':([44,52,64,68,69,70,86,89,96,102,119,120,121,125,126,127,128,133,145,161,166,169,173,177,180,],[58,58,58,97,97,97,58,58,97,58,97,97,58,97,97,97,97,58,97,97,58,97,58,58,58,]),'loop_body':([44,52,61,62,64,86,89,102,121,133,166,173,177,180,],[60,60,83,84,60,60,60,60,60,60,60,60,60,60,]),'for_range':([44,52,64,86,89,102,121,133,166,173,177,180,],[61,61,61,61,61,61,61,61,61,61,61,61,]),'while':([44,52,64,86,89,102,121,133,166,173,177,180,],[62,62,62,62,62,62,62,62,62,62,62,62,]),'bool_expr':([59,66,68,69,70,78,96,120,168,169,],[74,88,93,93,93,106,106,93,174,93,]),'bool_term':([59,66,68,69,70,78,96,103,104,120,168,169,],[75,75,75,75,75,75,75,134,135,75,75,75,]),'bool':([59,66,68,69,70,76,78,96,103,104,120,168,169,],[77,77,77,77,77,105,77,77,77,77,77,77,77,]),'rel_operand':([59,66,68,69,70,76,78,96,103,104,107,120,168,169,],[81,81,81,81,81,81,81,81,81,81,137,81,81,81,]),'value':([68,69,70,120,169,],[91,99,100,147,175,]),'expr':([68,69,70,96,119,120,145,161,169,],[92,92,92,129,144,92,129,170,92,]),'term':([68,69,70,96,119,120,125,126,145,161,169,],[94,94,94,94,94,94,150,151,94,94,94,]),'factor':([68,69,70,96,119,120,125,126,127,128,145,161,169,],[95,95,95,95,95,95,95,95,152,153,95,95,95,]),'rel_operator':([81,],[107,]),'str_expr':([85,],[114,]),'str_term':([85,140,],[115,158,]),'ret_statements':([89,102,166,177,],[121,133,173,180,]),'ret_statement':([89,102,121,133,166,173,177,180,],[122,122,149,149,122,149,122,149,]),'elsifs':([133,],[155,]),'else':([155,],[164,]),'elsif':([155,],[165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',12),
  ('prog -> subprogram','prog',1,'p_prog','parser.py',17),
  ('prog -> headers subprogram','prog',2,'p_prog','parser.py',18),
  ('headers -> headers header','headers',2,'p_headers','parser.py',25),
  ('headers -> header','headers',1,'p_headers','parser.py',26),
  ('header -> WITH pkg SEMICOLON','header',3,'p_header','parser.py',33),
  ('header -> WITH pkg SEMICOLON USE pkg SEMICOLON','header',6,'p_header','parser.py',34),
  ('pkg -> pkg DOT IDENT','pkg',3,'p_pkg','parser.py',48),
  ('pkg -> IDENT','pkg',1,'p_pkg','parser.py',49),
  ('subprogram -> procedure','subprogram',1,'p_subprogram','parser.py',61),
  ('subprogram -> function','subprogram',1,'p_subprogram','parser.py',62),
  ('function -> FUNC IDENT args_opt RETURN type IS declarations BEGIN ret_statements END IDENT SEMICOLON','function',12,'p_function','parser.py',66),
  ('function_call -> IDENT LEFT_PAR value RIGHT_PAR','function_call',4,'p_function_call','parser.py',80),
  ('procedure -> PROC IDENT args_opt IS declarations BEGIN statements END IDENT SEMICOLON','procedure',10,'p_procedure','parser.py',87),
  ('args_opt -> LEFT_PAR args RIGHT_PAR','args_opt',3,'p_args_opt','parser.py',99),
  ('args_opt -> empty','args_opt',1,'p_args_opt','parser.py',100),
  ('args -> args COMMA arg','args',3,'p_args','parser.py',108),
  ('args -> arg','args',1,'p_args','parser.py',109),
  ('arg -> IDENT COLON type','arg',3,'p_arg','parser.py',116),
  ('type -> TYPE_INT','type',1,'p_type','parser.py',120),
  ('type -> TYPE_FLOAT','type',1,'p_type','parser.py',121),
  ('type -> TYPE_BOOL','type',1,'p_type','parser.py',122),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',131),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',132),
  ('declaration -> empty','declaration',1,'p_declaration','parser.py',139),
  ('declaration -> function','declaration',1,'p_declaration','parser.py',140),
  ('declaration -> procedure','declaration',1,'p_declaration','parser.py',141),
  ('declaration -> IDENT COLON type ASSIGN value SEMICOLON','declaration',6,'p_declaration','parser.py',142),
  ('value -> expr','value',1,'p_value','parser.py',152),
  ('value -> bool_expr','value',1,'p_value','parser.py',153),
  ('expr -> expr PLUS term','expr',3,'p_expr','parser.py',157),
  ('expr -> expr MINUS term','expr',3,'p_expr','parser.py',158),
  ('expr -> term','expr',1,'p_expr','parser.py',159),
  ('term -> term MUL factor','term',3,'p_term','parser.py',168),
  ('term -> term DIV factor','term',3,'p_term','parser.py',169),
  ('term -> factor','term',1,'p_term','parser.py',170),
  ('factor -> LEFT_PAR expr RIGHT_PAR','factor',3,'p_factor','parser.py',179),
  ('factor -> function_call','factor',1,'p_factor','parser.py',180),
  ('factor -> IDENT','factor',1,'p_factor','parser.py',181),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',182),
  ('bool_expr -> bool_term AND bool_term','bool_expr',3,'p_bool_expr','parser.py',199),
  ('bool_expr -> bool_term OR bool_term','bool_expr',3,'p_bool_expr','parser.py',200),
  ('bool_expr -> bool_term','bool_expr',1,'p_bool_expr','parser.py',201),
  ('bool_term -> NOT bool','bool_term',2,'p_bool_term','parser.py',208),
  ('bool_term -> bool','bool_term',1,'p_bool_term','parser.py',209),
  ('bool -> LEFT_PAR bool_expr RIGHT_PAR','bool',3,'p_bool','parser.py',216),
  ('bool -> BOOL_VAL','bool',1,'p_bool','parser.py',217),
  ('bool -> IDENT','bool',1,'p_bool','parser.py',218),
  ('bool -> rel_operand rel_operator rel_operand','bool',3,'p_bool','parser.py',219),
  ('rel_operand -> NUMBER','rel_operand',1,'p_rel_operand','parser.py',231),
  ('rel_operand -> IDENT','rel_operand',1,'p_rel_operand','parser.py',232),
  ('rel_operator -> EQUALS','rel_operator',1,'p_rel_operator','parser.py',239),
  ('rel_operator -> NOT_EQUALS','rel_operator',1,'p_rel_operator','parser.py',240),
  ('rel_operator -> GREATER','rel_operator',1,'p_rel_operator','parser.py',241),
  ('rel_operator -> LESS','rel_operator',1,'p_rel_operator','parser.py',242),
  ('rel_operator -> GTEQ','rel_operator',1,'p_rel_operator','parser.py',243),
  ('rel_operator -> LSEQ','rel_operator',1,'p_rel_operator','parser.py',244),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',249),
  ('statements -> statement','statements',1,'p_statements','parser.py',250),
  ('statement -> assign','statement',1,'p_statement','parser.py',258),
  ('statement -> if','statement',1,'p_statement','parser.py',259),
  ('statement -> loop','statement',1,'p_statement','parser.py',260),
  ('statement -> put_line','statement',1,'p_statement','parser.py',261),
  ('statement -> function_call SEMICOLON','statement',2,'p_statement','parser.py',262),
  ('ret_statements -> ret_statements ret_statement','ret_statements',2,'p_ret_statements','parser.py',269),
  ('ret_statements -> ret_statement','ret_statements',1,'p_ret_statements','parser.py',270),
  ('ret_statement -> statement','ret_statement',1,'p_ret_statement','parser.py',278),
  ('ret_statement -> RETURN value SEMICOLON','ret_statement',3,'p_ret_statement','parser.py',279),
  ('assign -> IDENT ASSIGN value SEMICOLON','assign',4,'p_assign','parser.py',287),
  ('if -> IF bool_expr THEN ret_statements elsifs else END IF SEMICOLON','if',9,'p_if','parser.py',293),
  ('elsifs -> elsifs elsif','elsifs',2,'p_elsifs','parser.py',301),
  ('elsifs -> empty','elsifs',1,'p_elsifs','parser.py',302),
  ('elsif -> ELSIF bool_expr THEN ret_statements','elsif',4,'p_elsif','parser.py',309),
  ('else -> ELSE ret_statements','else',2,'p_else','parser.py',315),
  ('else -> empty','else',1,'p_else','parser.py',316),
  ('loop -> loop_body','loop',1,'p_loop','parser.py',323),
  ('loop -> for_range loop_body','loop',2,'p_loop','parser.py',324),
  ('loop -> while loop_body','loop',2,'p_loop','parser.py',325),
  ('loop_body -> LOOP statements END LOOP SEMICOLON','loop_body',5,'p_loop_body','parser.py',332),
  ('for_range -> FOR IDENT IN expr DUB_DOT expr','for_range',6,'p_for_range','parser.py',339),
  ('while -> WHILE bool_expr','while',2,'p_while','parser.py',346),
  ('put_line -> PUT_LINE LEFT_PAR str_expr RIGHT_PAR SEMICOLON','put_line',5,'p_put_line','parser.py',350),
  ('str_expr -> str_expr AMPERSAND str_term','str_expr',3,'p_str_expr','parser.py',357),
  ('str_expr -> str_term','str_expr',1,'p_str_expr','parser.py',358),
  ('str_term -> STRING','str_term',1,'p_str_term','parser.py',365),
  ('str_term -> type APOSTROPHE IMAGE LEFT_PAR value RIGHT_PAR','str_term',6,'p_str_term','parser.py',366),
]
