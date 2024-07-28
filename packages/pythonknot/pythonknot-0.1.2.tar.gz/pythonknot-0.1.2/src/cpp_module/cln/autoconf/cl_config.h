/* autoconf/cl_config.h.  Generated from cl_config.h.in by configure.  */
/* autoconf/cl_config.h.in.  Generated from configure.ac by autoheader.  */

#ifndef _CL_CONFIG_H

#define _CL_CONFIG_H

#include "cln/host_cpu.h"

/* prevents cln/config.h from being included, so no macro gets redefined */

#define _CL_CONFIG_PUBLIC_H

/* prevents cln/version.h from being included, so no macro gets redefined */

#define _CL_VERSION_H

/* Define if building universal (internal helper macro) */
/* #undef AC_APPLE_UNIVERSAL_BUILD */

/* symbols are prefixed by an underscore in assembly language */
/* #undef ASM_UNDERSCORE */

/* Define if compiler supports __attribute__((flatten)) */
#define CL_HAVE_ATTRIBUTE_FLATTEN /**/

/* Define if GNU MP library is available */
#define CL_USE_GMP 1

/* CLN release number */
#define CL_VERSION 1.3.6

/* Major version number of CLN */
#define CL_VERSION_MAJOR 1

/* Minor version number of CLN */
#define CL_VERSION_MINOR 3

/* Patchlevel version number of CLN */
#define CL_VERSION_PATCHLEVEL 6

/* declaration of gettimeofday() needs dots */
/* #undef GETTIMEOFDAY_DOTS */

/* type of `tzp' in gettimeofday() declaration */
#define GETTIMEOFDAY_TZP_T void *

/* have <alloca.h> and it should be used (not Ultrix) */
#define HAVE_ALLOCA_H /**/

/* define if the compiler supports basic C++11 syntax */
#define HAVE_CXX11 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* have <sys/time.h>, the getrusage() function, the struct rusage type, and
   <sys/resource.h> defines RUSAGE_SELF */
#define HAVE_GETRUSAGE /**/

/* Define to 1 if you have the `gettimeofday' function. */
#define HAVE_GETTIMEOFDAY 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Define if compiler supports long double type */
#define HAVE_LONGDOUBLE /**/

/* compiler supports the `long long' type */
#define HAVE_LONGLONG /**/

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* <errno.h> or <stdio.h> contains a declaration for perror() */
#define HAVE_PERROR_DECL /**/

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the <sys/resource.h> header file. */
#define HAVE_SYS_RESOURCE_H 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/times.h> header file. */
#define HAVE_SYS_TIMES_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* need to link with an external alloca.o when using alloca() */
/* #undef NO_ALLOCA */

/* Name of package */
#define PACKAGE "cln"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT ""

/* Define to the full name of this package. */
#define PACKAGE_NAME "cln"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "cln 1.3.6"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "cln"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "1.3.6"

/* type of `who' in getrusage() declaration */
#define RUSAGE_WHO_T int

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* Version number of package */
#define VERSION "1.3.6"

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
/* #  undef WORDS_BIGENDIAN */
# endif
#endif

/* Define to 1 if type `char' is unsigned and you are not using gcc.  */
#ifndef __CHAR_UNSIGNED__
/* # undef __CHAR_UNSIGNED__ */
#endif

#endif /* _CL_CONFIG_H */
