#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "CppKafka::cppkafka" for configuration ""
set_property(TARGET CppKafka::cppkafka APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(CppKafka::cppkafka PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libcppkafka.0.4.0.dylib"
  IMPORTED_SONAME_NOCONFIG "@rpath/libcppkafka.0.4.0.dylib"
  )

list(APPEND _cmake_import_check_targets CppKafka::cppkafka )
list(APPEND _cmake_import_check_files_for_CppKafka::cppkafka "${_IMPORT_PREFIX}/lib/libcppkafka.0.4.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
