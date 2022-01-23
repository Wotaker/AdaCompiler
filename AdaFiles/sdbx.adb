-- with Ada.Text_IO;           
-- with Ada.Integer_Text_IO;
-- use Ada.Integer_Text_IO;
-- use Ada.Text_IO;


procedure Sdbx is
    bt: Boolean := TRUE;
    bf: Boolean := FALSE and not bt;
    b_res: Boolean := TRUE;
begin
    b_res := (not bf and bt) or bf;
    -- b_res := TRUE;
end Sdbx;