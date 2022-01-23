procedure Factorial10loop is
    b_res: Boolean := TRUE;
    acc: Integer := 1;
    i: Integer := 1;
begin

loop
    acc := acc * i;
    i := i + 1;
end loop;

-- Put_Line(Integer'Image(acc));
    
end Factorial10loop;