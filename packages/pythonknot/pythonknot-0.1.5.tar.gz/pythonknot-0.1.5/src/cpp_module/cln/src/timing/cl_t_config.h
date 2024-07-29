/* src/timing/cl_t_config.h.  Generated from cl_t_config.h.in by configure.  */
// Defines OS dependent macros

#ifndef _CL_T_CONFIG_H
#define _CL_T_CONFIG_H

/* These definitions are adjusted by `configure' automatically. */


/* functions and declarations */

/* CL_GETTIMEOFDAY */
/* Define if you have the gettimeofday() function. */
#define HAVE_GETTIMEOFDAY 1
/* Define if the declaration of gettimeofday() needs dots. */
/* #undef GETTIMEOFDAY_DOTS */
/* Define as the type of `tzp' in gettimeofday() declaration. */
#define GETTIMEOFDAY_TZP_T void *

/* CL_RUSAGE */
/* Define if you have <sys/resource.h>. */
#define HAVE_SYS_RESOURCE_H 1
/* Define if you also have <sys/time.h>, the getrusage() function,
   the struct rusage type, and <sys/resource.h> defines RUSAGE_SELF. */
#define HAVE_GETRUSAGE /**/
/* Define as the type of `who' in getrusage() declaration. */
#define RUSAGE_WHO_T int
/* Define if you have <sys/times.h>. */
#define HAVE_SYS_TIMES_H 1

/* CL_PERROR */
/* Define if <errno.h> or <stdio.h> contains a declaration for perror(). */
#define HAVE_PERROR_DECL /**/


#endif /* _CL_T_CONFIG_H */

