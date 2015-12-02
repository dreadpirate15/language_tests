#include <stdio.h>

int main() {
  int a;
  int b;
  int c;

  for (a = 1; a < 1000; a++) {
    for (b = a; b < 1000; b++) {
      c = 1000 - (a + b);
      if ( a*a + b*b == c*c) {
	printf("Triplets - a: %d b: %d c: %d\n", a, b, c);
	return 0;
      }
    }
  }
}
