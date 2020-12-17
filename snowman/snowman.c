#include <stdio.h>
#include <stdlib.h>

void
snowman ()
{
  printf ("flag{0laf}\n");
}

int
main ()
{
  char ans[2];
  printf ("Do you want to build a snowman?");
  scanf ("%1s", ans);
  if (ans[0] == 'y')
    {
      snowman ();
    }
  else
    {
      ans[0] = 'y';
      snowman ();
    }
  return 0;
}
