# - Build a config.h file
# 

ADD_DEFINITIONS("-DHAVE_CONFIG_H")

#Platform checks
INCLUDE (CheckTypeSize)
CHECK_TYPE_SIZE("int" SIZEOF_INT)
CHECK_TYPE_SIZE("long int" SIZEOF_LONG_INT)

INCLUDE (CheckFunctionExists)
CHECK_FUNCTION_EXISTS("strndup" HAVE_STRNDUP)
CHECK_FUNCTION_EXISTS("strlcpy" HAVE_STRLCPY)
CHECK_FUNCTION_EXISTS("setenv" HAVE_SETENV)
CHECK_FUNCTION_EXISTS("ldexpf" HAVE_LDEXPF)

INCLUDE(CheckIncludeFiles)
CHECK_INCLUDE_FILES("unistd.h" HAVE_UNISTD_H)
CHECK_INCLUDE_FILES("malloc.h" HAVE_MALLOC_H)
IF(UNIX)
	FIND_FILE(RPI NAMES bcm_host.h PATHS "/opt/vc/include")
ENDIF()

#Unneeded on windows
IF(NOT WIN32)
	INCLUDE (CheckCXXSourceCompiles)
	CHECK_CXX_SOURCE_COMPILES("typedef void *(* voidvoid)(void);

		void *object = 0;
		voidvoid function;
		function = (voidvoid) object;
		" PERMITS_OBJECT_TO_FUNCTION_CAST)

	IF( NOT PERMITS_OBJECT_TO_FUNCTION_CAST )
		SET(HAVE_FORBIDDEN_OBJECT_TO_FUNCTION_CAST 1)
	ENDIF( NOT PERMITS_OBJECT_TO_FUNCTION_CAST )
ENDIF(NOT WIN32)

IF (MINGW)
	SET (WIN32_USE_STDIO Yes)
ENDIF ()
if (WIN32_USE_STDIO OR APPLE)
	SET (NOCOLOR Yes)
ENDIF()

CONFIGURE_FILE(${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_config.h.in
	${CMAKE_CURRENT_BINARY_DIR}/config.h ESCAPE_QUOTES)
