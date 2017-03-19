# =============================================================================
# GLFW Test
# =============================================================================
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

PROJECT(GLFW_Test)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake) #Clion, with conanbuildinfo.cmake in build folder
    include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Not CLion
endif()
conan_basic_setup()

ADD_EXECUTABLE(example example.cpp)
TARGET_COMPILE_DEFINITIONS(example PUBLIC "${CONAN_DEFINES}")
TARGET_LINK_LIBRARIES(example PUBLIC ${CONAN_LIBS})
SET_TARGET_PROPERTIES(example PROPERTIES LINK_FLAGS "${CONAN_EXE_LINKER_FLAGS}")