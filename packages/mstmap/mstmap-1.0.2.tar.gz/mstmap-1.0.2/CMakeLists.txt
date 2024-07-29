cmake_minimum_required(VERSION 3.4...3.18)
project(mstmap)

add_subdirectory(pybind11)

pybind11_add_module(mstmap MODULE
    src/mstmap_wrapper.cpp
    src/mstmap.cpp
    src/constants.h
    src/genetic_map_DH.cpp
    src/genetic_map_RIL.cpp
    src/linkage_group_DH.cpp
    src/linkage_group_RIL.cpp
    src/MSTOpt.cpp
)

set_target_properties(mstmap PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}" SUFFIX "${PYTHON_MODULE_EXTENSION}")
