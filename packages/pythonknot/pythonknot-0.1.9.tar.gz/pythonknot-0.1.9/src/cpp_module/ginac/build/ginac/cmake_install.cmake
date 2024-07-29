# Install script for directory: /home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/libginac.a")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/lib" TYPE STATIC_LIBRARY FILES "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/build/ginac/libginac.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/include/ginac/ginac.h;/usr/local/include/ginac/add.h;/usr/local/include/ginac/archive.h;/usr/local/include/ginac/assertion.h;/usr/local/include/ginac/basic.h;/usr/local/include/ginac/class_info.h;/usr/local/include/ginac/clifford.h;/usr/local/include/ginac/color.h;/usr/local/include/ginac/compiler.h;/usr/local/include/ginac/constant.h;/usr/local/include/ginac/container.h;/usr/local/include/ginac/ex.h;/usr/local/include/ginac/excompiler.h;/usr/local/include/ginac/expair.h;/usr/local/include/ginac/expairseq.h;/usr/local/include/ginac/exprseq.h;/usr/local/include/ginac/fail.h;/usr/local/include/ginac/factor.h;/usr/local/include/ginac/fderivative.h;/usr/local/include/ginac/flags.h;/usr/local/include/ginac/function.h;/usr/local/include/ginac/hash_map.h;/usr/local/include/ginac/idx.h;/usr/local/include/ginac/indexed.h;/usr/local/include/ginac/inifcns.h;/usr/local/include/ginac/integral.h;/usr/local/include/ginac/lst.h;/usr/local/include/ginac/matrix.h;/usr/local/include/ginac/mul.h;/usr/local/include/ginac/ncmul.h;/usr/local/include/ginac/normal.h;/usr/local/include/ginac/numeric.h;/usr/local/include/ginac/operators.h;/usr/local/include/ginac/power.h;/usr/local/include/ginac/print.h;/usr/local/include/ginac/pseries.h;/usr/local/include/ginac/ptr.h;/usr/local/include/ginac/registrar.h;/usr/local/include/ginac/relational.h;/usr/local/include/ginac/structure.h;/usr/local/include/ginac/symbol.h;/usr/local/include/ginac/symmetry.h;/usr/local/include/ginac/tensor.h;/usr/local/include/ginac/version.h;/usr/local/include/ginac/wildcard.h;/usr/local/include/ginac/parser.h;/usr/local/include/ginac/parse_context.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/include/ginac" TYPE FILE FILES
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/ginac.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/add.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/archive.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/assertion.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/basic.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/class_info.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/clifford.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/color.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/compiler.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/constant.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/container.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/ex.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/excompiler.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/expair.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/expairseq.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/exprseq.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/fail.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/factor.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/fderivative.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/flags.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/build/ginac/function.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/hash_map.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/idx.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/indexed.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/inifcns.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/integral.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/lst.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/matrix.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/mul.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/ncmul.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/normal.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/numeric.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/operators.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/power.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/print.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/pseries.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/ptr.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/registrar.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/relational.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/structure.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/symbol.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/symmetry.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/tensor.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/version.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/wildcard.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/parser/parser.h"
    "/home/yongjian/Yongjian_data/my_python/pythonknot/src/cpp_module/ginac/ginac/parser/parse_context.h"
    )
endif()

