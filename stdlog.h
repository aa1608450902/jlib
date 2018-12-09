#ifndef __STDLOG_H__
#define __STDLOG_H__

#ifdef __cplusplus
extern "C" {
#endif
#include <stdio.h>
#ifdef __cplusplus
};
#endif

#define O_NONE      "\e[0m"
#define O_GREEN     "\e[0;32m"
#define O_BGREEN    "\e[1;32m"
#define O_RED       "\e[0;31m"
#define O_BRED      "\e[1;31m"
#define O_YELLOW    "\e[0;33m"
#define O_BYELLOW   "\e[1;33m"
#define O_BLUE      "\e[0;34m"
#define O_BBLUE     "\e[1;34m"
#define O_END       O_NONE
#define O_ENTER     "\n"

#define LOG(format, ...) \
	printf("[ INFO] "); \
	printf(format, __VA_ARGS__); \
	printf(O_ENTER)

#define DEBUG(format, ...) \
	printf(O_GREEN "[DEBUG] "); \
	printf(format, __VA_ARGS__); \
	printf(O_END O_ENTER)

#define ERROR(format, ...) \
	printf(O_BRED "[ERROR] "); \
	printf(format, __VA_ARGS__); \
	printf(O_END O_ENTER)

#define WARN(format, ...) \
	printf(O_BYELLOW "[ WARN] "); \
	printf(format, __VA_ARGS__); \
	printf(O_END O_ENTER)

#define INFO(format, ...) LOG(format, __VA_ARGS__)

#endif /* __STDLOG_H__ */