with Ada.Text_IO; use Ada.Text_IO;

function arrayPass return Integer is

   type v2 is array (1..10) of integer;
   m, n: v2;

   function addthem(a,b: in v2) return v2 is c: v2;
   begin
      for i in 1..10 loop
         c(i) := a(i) + b(i);
      end loop;
      return c;
   end addthem;

begin
   m := (1,2,3,4,5,6,7,8,9,10);
   n := addthem(m,(1,1,2,3,5,8,13,21,34,55));

   for i in 1..10 loop
      Put_Line("next:" & Integer'Image(-n(i)) & " value");
   end loop;
   return 42;
end arrayPass;