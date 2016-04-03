import std.stdio;
import std.algorithm;
import std.string;
import std.array;
import std.conv;

void main(){
  //  auto f = File("input.txt");
  string[] input = split(chomp(readln()));
  int N = to!int(input[0]);
  int S = to!int(input[1]);
  int T = to!int(input[2]);
  //  writeln(N, " ", S, " ",  T); // debug
  int W = to!int(chomp(readln()));
  //  writeln(W); // debug
  int bestBody;
  if(S <= W && W <= T) bestBody = 1;
  else bestBody = 0;
  //  writeln(bestBody); // debug
  for(int i = 0; i < N-1; i++){
    W += to!int(chomp(readln()));
    if(S <= W && W <= T) bestBody += 1;
  }
  writeln(bestBody);
}
