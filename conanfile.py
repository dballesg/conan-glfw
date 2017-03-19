from conans import ConanFile, CMake, tools
import os, sys


class GlfwConan(ConanFile):
    name = "glfw"
    version = "3.2.1"
    license = "zlib/libpng"
    description = "Conan.io package for GLFW library."
    url = "https://github.com/dballesg/conan-glfw"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    folder = "glfw"
    generators = "cmake", "txt"

    def source(self):
        self.run("git clone https://github.com/glfw/glfw")
        self.run("git checkout tags/{}".format(self.version), cwd="glfw")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        # tools.replace_in_file("glfw/CMakeLists.txt", "PROJECT(glfw)", '''PROJECT(glfw) include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) conan_basic_setup()''')

    def system_requirements(self):

        if self.settings.os == "Linux":
            self.run('sudo apt-get install xorg-dev')
            self.run('sudo apt-get install libgl1-mesa-dev')
            self.run('sudo apt-get install libglew-dev')

        elif self.settings.os == "Macos":
            print("  Mac OS not implemented yet. Please help out! **** ")
            sys.exit(1)

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run("echo --------------------")
        self.run("echo glfw-%s" % self.version)
        self.run("echo --------------------")
        self.run("cd %s && mkdir build" % self.folder)
        self.run("cd %s/build && cmake .. %s %s" % (self.folder, cmake.command_line, shared))
        self.run("cd %s/build && cmake --build . %s" % (self.folder, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src="glfw/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("glfw3", "OpenGL32", "GLEW")
        elif self.settings.os == "Linux":
            self.cpp_info.libs = ["glfw3", "rt", "m", "dl", "Xrandr", "Xinerama", "Xxf86vm", "Xext", "Xcursor",
                                  "Xrender", "Xfixes", "X11", "pthread", "xcb", "Xau", "Xdmcp", "GL", "GLEW"]
        elif self.settings.os == "Macos":
            self.cpp_info.libs = ["glfw3", "GL", "GLEW"]
