#include <math.h>
#include <complex.h>

int isMandelbrot(const int xx, const int yy, const int width, const int height, const int thresh) {
  float x, y;
  float hwidth = width/2;
  float hheight = height/2;
  x = (1.25 * ((hwidth - xx) / hwidth)) - 0.5;
  y = ((hheight - yy) / hheight);
  float complex z = 0;
  float complex c = x + y * I;
  
  unsigned int i;
  for(i = 0; 255 > i; ++i) {
    z = cpowf(z, 2) + c;
    if (thresh < cabsf(z))
      return i;
  }
  return i;
}
