program ex6_4;
var
 frase:string;
 i: integer;
function maiusc_str(s:string):string;
{essa funcao retorna uma string com todas as letras maiusculas}
 var i: integer;
 begin
 for i:= 1 to length(s) do
 case s[i] of
   'a'..'z': s[i]:= chr(ord('A') + ord(s[i])-ord('a'));
 end;
 maiusc_str:= s;
end;
begin
 writeln('Digite uma frase. Ela sera'' re-escrita em letras maiusculas: ');
 readln (frase);
 writeln(maiusc_str(frase));
end.