with Ada.Text_IO;           
with Ada.Integer_Text_IO;
use Ada.Integer_Text_IO;
use Ada.Text_IO;

procedure DeclareAda is
    Beta : Float := 2.0;
    function AddAB (A: Integer; B : Integer) return Integer
    is
    begin
        return A + B;
    end AddAB;

    procedure Foo is   
    begin
        Put_Line ("Now in Foo Procedure");
    end Foo;

begin
    Put_Line ("Before the inner block");
    Put_Line (Float'Image (Beta));
    declare
        Alpha : Integer := 0;
        Sum: Integer;
    begin
        Alpha := 1;
        Put_Line ("Now inside the inner block");
        Put_Line ("Alpha" & Integer'Image (Alpha));
        -- Put("Alpha: "); Put(Alpha); Put(", Beta: "); Put(Beta); New_Line(1);
        Put_Line ("Alpha" & "Beta" & Integer'Image (Alpha) & Float'Image (Beta));
        Sum := AddAB (2, 3);
        Put_Line ("Sum" & Integer'Image (Sum));
        Foo;
    end;

    Put_Line ("After the inner block");
end DeclareAda;