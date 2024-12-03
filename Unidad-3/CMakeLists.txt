cmake_minimum_required(VERSION 3.10)
project(stl_bindings)

#Buscar dónde está instalado el PyBind11
set(pybind11_DIR "/usr/local/lib/python3.10/dist-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

# Agregar el módulo
add_library(stl_bindings MODULE CamiloMartinezEstay.cpp)
set_target_properties(stl_bindings PROPERTIES PREFIX "" SUFFIX ".so")

# Enlazar con PyBiind11
target_link_libraries(stl_bindings PRIVATE pybind11::module)
