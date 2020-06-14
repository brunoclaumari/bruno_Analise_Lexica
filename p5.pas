program ex6_7;
uses crt;
var a,b,c: integer;
    nome: string;
procedure altera_variavel(var x:integer; n:integer);
 {a e' parametro de referencia, n e' parametro de valor}
 begin
  x:= x+n;
 end;
procedure reduz_string (var frase:string; n:integer);
 {esse procedimento elimina os n primeiros caracteres da frase}
 var i:integer;
     s:string;
 begin
  s:=''; {s e'  inicializada com uma string vazia, ou nula}
  for i:= n+1 to length(frase) do s:=s+frase[i]; {operador + de concatenacao}
  frase:=s; {o conteudo de frase no programa sera’ alterado}
 end; 

begin  {aqui inicia a execucao do programa}
clrscr;
 a:=10;
 b:=20;
 c:=30;
 writeln(a:4,b:4,c:4);
 altera_variavel(a, 5); {a variavel a tera' seu valor alterado para a+5}
 altera_variavel(b, 7); {a variavel b tera' seu valor alterado para b+7}
 altera_variavel(c, 15); {a variavel c tera' seu valor alterado para c+15}
 writeln(a:4,b:4,c:4);
 nome:= 'Antonio Claudio da Sliva';
 writeln('nome antes : ', nome);
 reduz_string(nome,8); {deve eliminar os 8 caracteres antes de Claudio}
 writeln('nome depois: ', nome);
 readln;
end.