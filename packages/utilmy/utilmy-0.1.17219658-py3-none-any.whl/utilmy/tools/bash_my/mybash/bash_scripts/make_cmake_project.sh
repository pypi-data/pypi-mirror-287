#!/bin/sh

# A simple shell script for generating C++ projects with CMake. It generates
# the CMakeList.txt, Doxigen files, folder structure and initial filenames

KEPT_DIR=$PWD
YEAR=$(date +'%Y')

echo Project name?
read PROJECT_NAME
echo Project description?
read PROJECT_DESCRIPTION
echo Maintainer?
read PROJECT_MAINTAINER
echo Mainteiner email?
read EMAIL_MAINTAINER
echo Installation directory "["${KEPT_DIR}"]"?
read INSTALL_DIR
if [ -z "$INSTALL_DIR" ]; then
	INSTALL_DIR=$KEPT_DIR
fi
echo Creating folder structure for project \"$PROJECT_NAME\" in \"$INSTALL_DIR\"...
cd $INSTALL_DIR
mkdir $PROJECT_NAME
cd $PROJECT_NAME
mkdir doc out src
mkdir out/share
mkdir out/demo

# --- BEGIN: Creating INSTALL ---
echo "${PROJECT_NAME} - ${PROJECT_DESCRIPTION}

Installation from CMake (Multiplatform)
---------------------------------------

Navigate to the project. An out-of-source build is recommended however not mandatory. To do this, create and enter a 'build' directory. 'cmake ..' should create a 'Makefile' or '.sln' there. A 'make' or 'build' should make output '${PROJECT_NAME}' appear in ./out/ correspondent directory." > INSTALL
# --- END: Creating INSTALL ---


# --- BEGIN: Creating AUTHORS ---
echo "${PROJECT_NAME} - ${PROJECT_DESCRIPTION}

Authors
-------

Main maintainer is ${PROJECT_MAINTAINER} <${EMAIL_MAINTAINER}>" > AUTHORS
# --- END: Creating AUTHORS ---


# --- BEGIN: Creating src/main.cpp ---
cd src
echo "//
// ${PROJECT_NAME}:main.cpp
//
// Author: ${PROJECT_MAINTAINER} <${EMAIL_MAINTAINER}>, (C) ${YEAR}
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
//

#include <iostream>
#include \"${PROJECT_NAME}.h\"

int main(int argc, char *argv[]) {

  return 0;
}
" > main.cpp
cd ..
# --- END: Creating src/main.cpp ---

# --- BEGIN: Creating src/${PROJECT_NAME}.cpp ---
cd src
echo "//
// ${PROJECT_NAME}.cpp
//
// Author: ${PROJECT_MAINTAINER} <${EMAIL_MAINTAINER}>, (C) ${YEAR}
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
//

#include \"${PROJECT_NAME}.h\"

" > ${PROJECT_NAME}.cpp
cd ..
# --- END: Creating src/${PROJECT_NAME}.cpp ---

# --- BEGIN: Creating src/${PROJECT_NAME}.cpp ---
cd src
echo "//
// ${PROJECT_NAME}.h
//
// Author: ${PROJECT_MAINTAINER} <${EMAIL_MAINTAINER}>, (C) ${YEAR}
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
//
" > ${PROJECT_NAME}.h
echo "${PROJECT_NAME}_H" | tr '[a-z]' '[A-Z]' > temp
echo "#ifndef $(cat temp)" >> ${PROJECT_NAME}.h 
echo "#define $(cat temp)" >> ${PROJECT_NAME}.h 
echo "




" >> ${PROJECT_NAME}.h
echo "#endif //$(cat temp)" >> ${PROJECT_NAME}.h 
rm temp

cd ..
# --- END: Creating src/${PROJECT_NAME}.h ---


# --- BEGIN: Creating mk/CMakeLists.txt ---
echo "# Generated by \"mkproy.sh\" v0.3
CMAKE_MINIMUM_REQUIRED (VERSION 2.6)
SET(CMAKE_BUILD_TYPE Debug)
SET(KEYWORD $PROJECT_NAME)

# Start a project
PROJECT(\${KEYWORD})

# Default build mode is RelWithDebInfo
IF("${CMAKE_BUILD_TYPE}" STREQUAL "")
  SET(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING "build type default to RelWithDebInfo, set to Release to improve performance" FORCE)
ENDIF("${CMAKE_BUILD_TYPE}" STREQUAL "")

# Define system type
IF(\${CMAKE_SYSTEM_NAME} MATCHES \"Linux\")
        #ADD_DEFINITIONS(-DSYSTEMTYPE_LINUX)
	# Set system folder name
	set(SYSTEM_FOLDER_NAME linux)
ELSEIF(\${CMAKE_SYSTEM_NAME} MATCHES \"Windows\")
	#ADD_DEFINITIONS(-DSYSTEMTYPE_WINDOWS)
	# Set system folder name
	set(SYSTEM_FOLDER_NAME windows)
ENDIF(\${CMAKE_SYSTEM_NAME} MATCHES \"Linux\")

# Define standard paths.
set(MY_OUT_PATH \${CMAKE_CURRENT_SOURCE_DIR}/out/\${SYSTEM_FOLDER_NAME})
set(MY_SRC_PATH \${CMAKE_CURRENT_SOURCE_DIR}/src)

# Search for source code.
FILE(GLOB_RECURSE folder_source \${MY_SRC_PATH}/*.cpp)
FILE(GLOB_RECURSE folder_header \${MY_SRC_PATH}/*.h)
SOURCE_GROUP(\"Source Files\" FILES \${folder_source})
SOURCE_GROUP(\"Header Files\" FILES \${folder_header})

# Automatically add include directories if needed.
FOREACH(header_file \${folder_header})
  GET_FILENAME_COMPONENT(p \${header_file} PATH)
  INCLUDE_DIRECTORIES(\${p})
ENDFOREACH(header_file \${folder_header})

# Set location for binary output
set(EXECUTABLE_OUTPUT_PATH \${MY_OUT_PATH})

# Set up our main executable.
IF (folder_source)
  ADD_EXECUTABLE(\${KEYWORD} \${folder_source} \${folder_header})
ELSE (folder_source)
  MESSAGE(FATAL_ERROR \"No source code files found. Please add something\")
ENDIF (folder_source)

# Link executable to external libraries
target_link_libraries (\${KEYWORD} \${OpenCV_LIBS}) 
IF(\${CMAKE_SYSTEM_NAME} MATCHES \"Linux\")
 #ADD_DEFINITIONS(-DSYSTEMTYPE_LINUX)
ELSEIF(\${CMAKE_SYSTEM_NAME} MATCHES \"Windows\")
 #target_link_libraries (\${KEYWORD} ACE) # ACEd for debug on win32
 #target_link_libraries (\${KEYWORD} winmm)
ENDIF(\${CMAKE_SYSTEM_NAME} MATCHES \"Linux\")
" > CMakeLists.txt
# --- END: Creating CMakeLists.txt ---

# --- BEGIN: Creating doc/Doxyfile ---
cd doc
echo "
# Doxyfile 1.4.6

#---------------------------------------------------------------------------
# Project related configuration options
#---------------------------------------------------------------------------
PROJECT_NAME           = ${PROJECT_NAME}
PROJECT_NUMBER         = 1
OUTPUT_DIRECTORY       = .
CREATE_SUBDIRS         = NO
OUTPUT_LANGUAGE        = English
USE_WINDOWS_ENCODING   = NO
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
ABBREVIATE_BRIEF       = \"The \$name class\" \
                         \"The \$name widget\" \
                         \"The \$name file\" \
                         is \
                         provides \
                         specifies \
                         contains \
                         represents \
                         a \
                         an \
                         the
ALWAYS_DETAILED_SEC    = NO
INLINE_INHERITED_MEMB  = YES
FULL_PATH_NAMES        = YES
STRIP_FROM_PATH        = 
STRIP_FROM_INC_PATH    = 
SHORT_NAMES            = NO
JAVADOC_AUTOBRIEF      = YES
MULTILINE_CPP_IS_BRIEF = NO
DETAILS_AT_TOP         = NO
INHERIT_DOCS           = YES
SEPARATE_MEMBER_PAGES  = NO
TAB_SIZE               = 8
ALIASES                = 
OPTIMIZE_OUTPUT_FOR_C  = NO
OPTIMIZE_OUTPUT_JAVA   = NO
BUILTIN_STL_SUPPORT    = YES
DISTRIBUTE_GROUP_DOC   = NO
SUBGROUPING            = YES
#---------------------------------------------------------------------------
# Build related configuration options
#---------------------------------------------------------------------------
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_STATIC         = YES
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_LOCAL_METHODS  = NO
HIDE_UNDOC_MEMBERS     = NO
HIDE_UNDOC_CLASSES     = NO
HIDE_FRIEND_COMPOUNDS  = NO
HIDE_IN_BODY_DOCS      = NO
INTERNAL_DOCS          = NO
CASE_SENSE_NAMES       = YES
HIDE_SCOPE_NAMES       = NO
SHOW_INCLUDE_FILES     = YES
INLINE_INFO            = YES
SORT_MEMBER_DOCS       = YES
SORT_BRIEF_DOCS        = NO
SORT_BY_SCOPE_NAME     = NO
GENERATE_TODOLIST      = YES
GENERATE_TESTLIST      = YES
GENERATE_BUGLIST       = YES
GENERATE_DEPRECATEDLIST= YES
ENABLED_SECTIONS       = 
MAX_INITIALIZER_LINES  = 30
SHOW_USED_FILES        = YES
SHOW_DIRECTORIES       = NO
FILE_VERSION_FILTER    = 
#---------------------------------------------------------------------------
# configuration options related to warning and progress messages
#---------------------------------------------------------------------------
QUIET                  = NO
WARNINGS               = YES
WARN_IF_UNDOCUMENTED   = YES
WARN_IF_DOC_ERROR      = YES
WARN_NO_PARAMDOC       = NO
WARN_FORMAT            = \"\$file:\$line: \$text\"
WARN_LOGFILE           = 
#---------------------------------------------------------------------------
# configuration options related to the input files
#---------------------------------------------------------------------------
INPUT                  = ../src 
FILE_PATTERNS          = *.cpp \
                         *.cxx \
                         *.h \
                         *.hpp \
                         *.inl 
			 
RECURSIVE              = NO
EXCLUDE                = 
	
EXCLUDE_SYMLINKS       = NO
EXCLUDE_PATTERNS       = *.svn* CMake*
EXAMPLE_PATH           = 
EXAMPLE_PATTERNS       = *
EXAMPLE_RECURSIVE      = NO
IMAGE_PATH             = 
INPUT_FILTER           = 
FILTER_PATTERNS        = 
FILTER_SOURCE_FILES    = NO
#---------------------------------------------------------------------------
# configuration options related to source browsing
#---------------------------------------------------------------------------
SOURCE_BROWSER         = NO
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = YES
REFERENCED_BY_RELATION = YES
REFERENCES_RELATION    = YES
USE_HTAGS              = NO
VERBATIM_HEADERS       = YES
#---------------------------------------------------------------------------
# configuration options related to the alphabetical class index
#---------------------------------------------------------------------------
ALPHABETICAL_INDEX     = YES
COLS_IN_ALPHA_INDEX    = 4
IGNORE_PREFIX          = 
#---------------------------------------------------------------------------
# configuration options related to the HTML output
#---------------------------------------------------------------------------
GENERATE_HTML          = YES
HTML_OUTPUT            = html
HTML_FILE_EXTENSION    = .html
HTML_HEADER            = 
HTML_FOOTER            = 
HTML_STYLESHEET        = 
HTML_ALIGN_MEMBERS     = YES
GENERATE_HTMLHELP      = NO
CHM_FILE               = 
HHC_LOCATION           = 
GENERATE_CHI           = NO
BINARY_TOC             = NO
TOC_EXPAND             = NO
DISABLE_INDEX          = NO
ENUM_VALUES_PER_LINE   = 4
GENERATE_TREEVIEW      = NO
TREEVIEW_WIDTH         = 250
#---------------------------------------------------------------------------
# configuration options related to the LaTeX output
#---------------------------------------------------------------------------
GENERATE_LATEX         = NO
LATEX_OUTPUT           = latex
LATEX_CMD_NAME         = latex
MAKEINDEX_CMD_NAME     = makeindex
COMPACT_LATEX          = NO
PAPER_TYPE             = a4wide
EXTRA_PACKAGES         = 
LATEX_HEADER           = 
PDF_HYPERLINKS         = NO
USE_PDFLATEX           = NO
LATEX_BATCHMODE        = NO
LATEX_HIDE_INDICES     = NO
#---------------------------------------------------------------------------
# configuration options related to the RTF output
#---------------------------------------------------------------------------
GENERATE_RTF           = NO
RTF_OUTPUT             = rtf
COMPACT_RTF            = NO
RTF_HYPERLINKS         = NO
RTF_STYLESHEET_FILE    = 
RTF_EXTENSIONS_FILE    = 
#---------------------------------------------------------------------------
# configuration options related to the man page output
#---------------------------------------------------------------------------
GENERATE_MAN           = NO
MAN_OUTPUT             = man
MAN_EXTENSION          = .3
MAN_LINKS              = NO
#---------------------------------------------------------------------------
# configuration options related to the XML output
#---------------------------------------------------------------------------
GENERATE_XML           = NO
XML_OUTPUT             = xml
XML_SCHEMA             = 
XML_DTD                = 
XML_PROGRAMLISTING     = YES
#---------------------------------------------------------------------------
# configuration options for the AutoGen Definitions output
#---------------------------------------------------------------------------
GENERATE_AUTOGEN_DEF   = NO
#---------------------------------------------------------------------------
# configuration options related to the Perl module output
#---------------------------------------------------------------------------
GENERATE_PERLMOD       = NO
PERLMOD_LATEX          = NO
PERLMOD_PRETTY         = YES
PERLMOD_MAKEVAR_PREFIX = 
#---------------------------------------------------------------------------
# Configuration options related to the preprocessor   
#---------------------------------------------------------------------------
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = NO
EXPAND_ONLY_PREDEF     = NO
SEARCH_INCLUDES        = YES
INCLUDE_PATH           = 
INCLUDE_FILE_PATTERNS  = 
PREDEFINED             = 
EXPAND_AS_DEFINED      = 
SKIP_FUNCTION_MACROS   = YES
#---------------------------------------------------------------------------
# Configuration options related to the dot tool   
#---------------------------------------------------------------------------
CLASS_DIAGRAMS         = NO
HIDE_UNDOC_RELATIONS   = YES
HAVE_DOT               = YES
CLASS_GRAPH            = YES
COLLABORATION_GRAPH    = YES
GROUP_GRAPHS           = YES
UML_LOOK               = NO
TEMPLATE_RELATIONS     = YES
INCLUDE_GRAPH          = YES
INCLUDED_BY_GRAPH      = YES
CALL_GRAPH             = NO
GRAPHICAL_HIERARCHY    = YES
DIRECTORY_GRAPH        = YES
DOT_IMAGE_FORMAT       = png
DOT_PATH               = 
DOTFILE_DIRS           = 
MAX_DOT_GRAPH_WIDTH    = 1024
MAX_DOT_GRAPH_HEIGHT   = 1024
MAX_DOT_GRAPH_DEPTH    = 1000
DOT_TRANSPARENT        = NO
DOT_MULTI_TARGETS      = NO
GENERATE_LEGEND        = YES
DOT_CLEANUP            = YES
#---------------------------------------------------------------------------
# Configuration::additions related to the search engine   
#---------------------------------------------------------------------------
SEARCHENGINE           = N
" > Doxyfile
cd ..
# --- END: Creating doc/Doxyfile ---

