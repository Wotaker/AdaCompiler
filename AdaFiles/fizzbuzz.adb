with Ada.Text_IO; use Ada.Text_IO;

procedure main is
    counter : Integer := 1;
    i3 : Integer := 1;
    i5 : Integer := 1;
begin
    while counter < 22 loop
        if i3 = 3 and i5 = 5 then
            Put_Line ("FizzBuzz!");
            i3 := 0;
            i5 := 0;
        elsif i3 = 3 then
            Put_Line ("Fizz!");
            i3 := 0;
        elsif i5 = 5 then
            Put_Line ("Buzz!");
            i5 := 0;
        else
            Put_Line (Integer'Image(counter));
        end if;
        counter := counter + 1;
        i3 := i3 + 1;
        i5 := i5 + 1;
        -- Put_Line ("i3, i5 =" & Integer'Image(i3) & Integer'Image(i5));
    end loop;
end main;