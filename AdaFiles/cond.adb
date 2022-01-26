-- Nie działa, problem z wyrażeniem if
with Ada.Text_IO; use Ada.Text_IO;

procedure main is
    bt: Boolean := TRUE;
    b_comp: Boolean := 3 = 2;
    result: Integer := 0;
begin
    if b_comp then
        result := 1;
    elsif (not bt) then
        result := 2;
    elsif bt or b_comp then
        result := 3;
        for iter in 0..10 loop
            Put_Line(Integer'Image(iter));
        end loop;
    else
        result := 4;
    end if;
    Put_Line("The result is" & Integer'Image(result));

    -- return 0;
end main;