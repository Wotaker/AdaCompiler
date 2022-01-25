function Sdbx return Boolean is
    bt: Boolean := TRUE;
    bf: Boolean := FALSE and not bt;
    b_res: Boolean := TRUE;
begin
    b_res := (not bf and bt) or bf;
    if 2.0 < 4.0 then
        return b_res;
    end if;
    return not b_res;
end Sdbx;