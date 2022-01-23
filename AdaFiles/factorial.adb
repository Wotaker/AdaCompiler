with Ada.Text_IO;           
with Ada.Integer_Text_IO;
use Ada.Integer_Text_IO;
use Ada.Text_IO;

procedure Factorial is
    function Factorial (x: Integer) return Integer
    is
    begin  
        if x > 1 then
            return x * Factorial(x - 1);
        else
            return x;
        end if;
    end Factorial;
begin

for i in 1..6 loop
    Put_Line(Integer'Image(Factorial(i)));
end loop;
    
end Factorial;