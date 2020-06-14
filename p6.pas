program ex6_6;
uses crt;  {necessario para usar gotoxy e clrscr}
 var linhamedia,colunamedia: integer;
    m:string;
 procedure msg(frase:string; x,y,a,k: integer);
  begin
  gotoxy(x,y);
  write(frase);
 end;
begin
 clrscr;
 msg('esta frase na linha 1 coluna 1', 1, 1);
 msg('esta frase na linha 3 coluna 2', 2, 3);
 msg('esta frase na linha 5 coluna 3', 3, 5);
 m:= 'meio da tela';
 linhamedia:=12;
 colunamedia:=40;
 msg(m,colunamedia-length(m) div 2,linhamedia);
end.