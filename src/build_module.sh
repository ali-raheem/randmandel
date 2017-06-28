swig -python mandel.i
gcc -O2 -fpic -c mandelmodule.c
gcc -O2 -fpic -c mandel_wrap.c -I/usr/include/python2.7/ -lm
gcc -shared mandelmodule.o mandel_wrap.o -o _mandel.so -lpython2.7 -lm
