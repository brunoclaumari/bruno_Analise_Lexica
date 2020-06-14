program codifica_matr;
{Este programa codifica textos usando o metodo da matriz transposta}
var
    frase: string;
    chave:integer; 

procedure le_frase (var frase:string);
begin
 writeln('Digite a frase a ser codificada ate'' 100 caracteres:' );
 readln(frase);
end; 

procedure le_chave(var chave:integer);
 var i: integer;
begin
 writeln('Digite a chave de codificacao < 10: '); readln(chave);
end; 

function linhas_necessarias(f:string; k: integer):integer;
{retorna o menor numero de linhas necessarias para codificar a string f
 com a chave k}
 begin
 linhas_necessarias:= round(length(f)/k +0.4);
 end; 

function codifica (frase:string; k: integer):string;
 var
    m: array[1..10,1..10] of char;
    i,j,n,lin,col,linhas, colunas:integer;
    s: string;

 procedure limpa_matriz;
  var i,j:integer;
  begin
  for i:= 1 to 10 do

   for j:= 1 to 10 do m[i,j]:= ' ';

 end; {limpa_matriz}

 begin

  limpa_matriz;

  colunas:= k;

  linhas:= linhas_necessarias(frase,k);

  for i:= 1 to length(frase) do begin

   lin:= (i- 1) div colunas+1;

   col:= i mod colunas;  if col=0 then col:=colunas;

   m[lin,col]:= frase[i];

  end;

  s:='';

  for j:=1 to colunas do

   for i:= 1 to linhas do s:=s+m[i,j];

  codifica:=s;

end; {codifica}

begin

 le_frase(frase);

 le_chave(chave);

 frase:=codifica(frase,chave);

 writeln('Frase codificada com a chave ', chave,': ', frase);

 chave := linhas_necessarias(frase, chave);

 frase:= codifica(frase,chave);

 writeln('Decodificando com a chave ', chave, ': ', frase);

 readln;

end.