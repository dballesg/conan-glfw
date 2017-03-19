# =============================================================================
# GLFW
# =============================================================================
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(GLFW VERSION 3.2.1 LANGUAGES C)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake) #Clion, with conanbuildinfo.cmake in build folder
    include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
else()
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # Not CLion
endif()
conan_basic_setup()

# Add the CMakeLists.txt from the glfw cloned repository
add_subdirectory(glfw)