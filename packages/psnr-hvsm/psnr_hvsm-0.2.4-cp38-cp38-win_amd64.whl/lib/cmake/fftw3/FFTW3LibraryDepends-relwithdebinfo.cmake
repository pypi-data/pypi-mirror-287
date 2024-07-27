#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "FFTW3::fftw3" for configuration "RelWithDebInfo"
set_property(TARGET FFTW3::fftw3 APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(FFTW3::fftw3 PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "C"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/fftw3.lib"
  )

list(APPEND _cmake_import_check_targets FFTW3::fftw3 )
list(APPEND _cmake_import_check_files_for_FFTW3::fftw3 "${_IMPORT_PREFIX}/lib/fftw3.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
