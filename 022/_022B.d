import std.stdio;
import std.algorithm;
import std.string;
import std.array;
import std.conv;

void main(){
  //  auto f = File("input.txt");
  int N = to!int(chomp(readln()));
  int[int] list;
  int p = 0;
  for(int i = 0; i < N; i++){
    int Ai = to!int(chomp(readln()));
    if(Ai in list) p += 1;
    list[Ai] = Ai;
  }
  writeln(p);
}
