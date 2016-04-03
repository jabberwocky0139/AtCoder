import std.stdio;
import std.algorithm;
import std.string;
import std.array;
import std.conv;

void main(){
  int input = to!int(chomp(readln()));
  writeln(input/10 + input%10);
}
