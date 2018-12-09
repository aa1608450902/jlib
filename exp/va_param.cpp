#include <stdarg.h>

void va_param(int arg_1, int arg_2, int arg_3, ...) {
	va_list va_p;
	va_start(va_p, arg_3);  // The second arg must be the last arg before ... .
	// type arg = va_arg(va_p, type); e.g.:
	int lenght = 5; // Here, assume the length of variable length parameter is 5.
	for (int i = 0; i < length; i++) {
		int arg = va_arg(va_p, int);
		printf("arg %d = %d", i, arg);
	}
	// Finally, release the space of va_p.
	va_end(va_p);
}