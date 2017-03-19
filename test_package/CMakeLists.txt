# =============================================================================
# GLFW Test
# =============================================================================
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

PROJECT(GLFWTest)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake) #Clion, with conanbuildinfo.cmake in build folder
    include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Not CLion
endif()
conan_basic_setup()

ADD_EXECUTABLE(GLFWTest example.cpp)

find_package(OpenGL REQUIRED)
include_directories( ${OPENGL_INCLUDE_DIRS} )

TARGET_COMPILE_DEFINITIONS(GLFWTest PUBLIC "${CONAN_DEFINES}")
TARGET_LINK_LIBRARIES(GLFWTest PUBLIC ${CONAN_LIBS} ${OPENGL_LIBRARIES})
SET_TARGET_PROPERTIES(GLFWTest PROPERTIES LINK_FLAGS "${CONAN_EXE_LINKER_FLAGS}")