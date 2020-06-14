program ex6_2;
var
  x:integer;
function fat(n:integer): longint;
 var
   i: integer;
   f: longint;
 begin
   f:=1;
   for i:= 2 to n do f:= f*i;
   fat:= f;
 end; {fim da declaracao da funcao}
begin {inicio do programa}
 writeln('Digite varios numeros para saber o fatorial');
 writeln('Termine com -1');
 read(x);
 while x > 0 do begin
  writeln ('fatorial de ', x, ' = ', fat(x) );
  read(x);
 end;
end.