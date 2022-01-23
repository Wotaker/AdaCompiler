-- with Ada.Text_IO;
-- use Ada.Text_IO;           
-- with Ada.Integer_Text_IO;
-- use Ada.Integer_Text_IO;

procedure Factorial10 is
    b_res: Boolean := TRUE;
    acc: Integer := 1;
begin

for i in 1..6+5 loop
    acc := acc * i;
end loop;

-- Put_Line(Integer'Image(acc));
    
end Factorial10;