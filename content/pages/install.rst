:slug: install

--------------

.. class:: center

[ `packages <download.html>`__ - `examples <examples.html>`__ - `build instructions <build.html>`__ - install instructions ]

.. _install:

Installation Instructions
-------------------------

.. _install_ubuntu:

-  **Install instructions for Ubuntu**

   The stable PPA (Personal Package Archive) for Ubuntu is located `here`_.

   Qucs 0.0.18 packages are available for Ubuntu versions 14.10
   (Utopic) and 14.04 (Trusty).

   Qucs 0.0.17 packages are available for Ubuntu versions 13.04 (Raring),
   12.10 (Quantal), and 12.04 (Precise).

   To add the package repository
   and install Qucs, use the following sequence of commands:

     ::

       sudo apt-add-repository ppa:qucs/qucs
       sudo apt-get update
       sudo apt-get install qucs

.. _install_Win32:

- **Install instructions for Windows**

  A portable package for Qucs is provided

    ::

      qucs--win32-mingw482-asco-freehdl-adms.zip

  Extract the package in a convenient location and run the qucs.bat script.
  The package contains ASCO, FreeHDL and ADMS.
  To use **FreeHDL** for VHDL simulation or **ADMS** for Verilog-A
  compilation a compiler is necessary.
  The required MinGW compiler can be found
  `here <http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.8.2/threads-posix/dwarf/i686-4.8.2-release-posix-dwarf-rt_v3-rev3.7z/>`__.
  Please follow the README.md file distributed along with the Windows
  package for further information.

  If **Icarus Verilog** is used for digital Verilog-HDL simulation
  the installer script must be installed on the computer
  additionally. Current versions can be obtained at
  http://bleyer.org/icarus/.

  In order to use the SPICE preprocessor **ps2sp** successfully a
  **TinyPerl** installation is required. It can be obtained at
  http://tinyperl.sourceforge.net/. It must be ensured that the
  **tinyperl.exe** is accessible via the PATH environment variable.

 .. _install_MacOS:

- **Install instructions for MacOSX**

  Download the latest binary package installer or your MacOSX systems, named

    ::

      qucs-<version>-macosx-<platform>.pkg

  Copy this file onto your desktop and double-click it. Follow the
  installer instructions.

--------------

.. _here: https://launchpad.net/~qucs/+archive/ubuntu/qucs/+packages

