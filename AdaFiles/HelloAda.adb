with Ada.Text_IO; use Ada.Text_IO;

procedure Hello_World is
begin
    Put_Line ("Hello Ada!");
    for i in 1..10 loop
        Put_Line (Integer'Image (i));
        if i mod 2 and i > 3 = 0 then
            Put_Line ("Even!");
        elsif i = 10 then
            Put_Line ("End Loop");
        else
            null;
        end if;
    end loop;
end Hello_World;