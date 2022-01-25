with Ada.Text_IO;
use Ada.Text_IO;           
with Ada.Integer_Text_IO;
use Ada.Integer_Text_IO;

procedure main is
    function Foo (x: Integer) return Boolean
    is
    begin  
        if x > 3 then
            return TRUE;
        else
            return FALSE;
        end if;
    end Foo;

    x : Integer := 4;
begin

for i in 1..6 loop
    Put_Line("Foo of" & Integer'Image(i) & " is " & Boolean'Image(Foo(i)));
    x := i;
end loop;
x := 2;
    
end main;