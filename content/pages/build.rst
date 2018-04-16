:slug: build

--------------

.. class:: center

[ `packages <download.html>`__ - `examples <examples.html>`__ - build instructions - `install instructions <install.html>`__ ]

.. _build-req:

Build Prerequisites
-------------------

-  **Source Build Requirements**

   -  Linux, macOS, Windows, FreeBSD
   -  Qt4 installation, version >= 4.6 (with Qt3Support)
   -  C++ compiler
   -  Autoconf version 2.64 (at least)
   -  GNU automake 1.7.0 (at least)
   -  flex 2.5.31 (but at least 2.5.9)
   -  GNU Bison 1.875d
   -  GNU M4 (any version)
   -  GNU gperf 3.0.1
   -  ADMS 2.3.6

-  **Documentation Build Requirements**

   -  Autoconf
   -  Automake
   -  LaTex installation.

      -  IEEEtran bibstyle
      -  savesym
      -  hyperref

   -  GNU Octave
   -  epsTk 2.0.1 (at least)


.. _build_tarball:

Build Current Release From Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


-  **Get The Latest Source Tarball:** `Qucs Source <https://sourceforge.net/projects/qucs/files/qucs/>`__
-  **Updated build instructions for**: `Darwin (Mac OSX) <https://github.com/Qucs/qucs/wiki/Build-Darwin>`__, `Linux <https://github.com/Qucs/qucs/wiki/Build-Linux>`__, `Windows <https://github.com/Qucs/qucs/wiki/Build-Windows>`__

.. _build_git:

Build Development Sources From Git Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Follow the instruction in:** `README.md <https://github.com/Qucs/qucs/blob/master/README.md>`__

.. _build_mac:

Build Instructions For MacOSX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is recommended the use of a package manager to handle the instalation of the dependencies and build the tools.

We recoment either `MacPorts <http://www.macports.org/>`__ or `Homebrew <http://brew.sh/>`__. Please contact the package maintainer if it is not yet updated to the latest version of Qucs.

Note that due to limitation in Qt4 your platform should be newer than Mac OS 10.5 64-bit.

Follow the package manager instructions on how to get it set up and running. the `MacPorts <http://www.macports.org/>`__ and `Homebrew <http://brew.sh/>`__ package managers.

Note that there is a MacPorts `Port <https://trac.macports.org/browser/trunk/dports/science/qucs/Portfile>`__ and a Homebrew `Formula <https://github.com/guitorri/homebrew-tap/blob/master/qucs.rb>`__ available to manage the build and install of Qucs.

-  **Building using MacPorts**

   To install Qucs, you need to install MacPorts (after Xcode and Command Line Tools, see below).

   #. | *Installing MacPorts and Qucs*
      | With MacPorts you can install MacOS versions of many known open source projects by using simple commands.
      | Get it here: http://www.macports.org/
      | Please follow the installation instructions to get Xcode and the Command Line Tools. After its installation, MacPorts needs to be updated to the most recent version. Open a Terminal shell and type the following commmand (you will be asked for your password):

      ::

                  $ sudo port -d selfupdate
                  

      Now it is time to get Qucs. In the shell, type this command:

      ::

                  $ sudo port install qucs
                  

      Users willing to install the ASCO version shipped with Qucs (instaed of the one available in MacPorts) can use the command:

      ::

                  $ sudo port install qucs +shipped_asco
                  

      | MacPorts will fetch, decompress, compile and install a lot of packages which are needed to install Qucs. Be patient, this will take some time.
      | After installation Qucs will be placed into:

      ::

          /opt/local/bin

      | 
      | Symbolic links to the applications are created into:

      ::

          /Applications/MacPorts

      | 

   You're done with MacPorts!

-  **Building using Homebrew**

   To install Qucs, you need to install Homebrew (after Xcode and Command Line Tools, see instructions).

   #. *Installing Homebrew and Qucs*

      Follow the instruction to install Homebrew: http://brew.sh/

      Update the homebrew formulas, add a homebrew tap containing the Qucs formula.

      ::

        $ brew update
        $ brew tap guitorri/tap

      It is necessary to rebuild Qt4 with Qt3Support. The default prebuild Qt bottle does not include it. This step might take ~20min depending on your machine.

      ::

        $ brew tap cartr/qt4
        $ brew tap-pin cartr/qt4
        $ brew install qt --with-qt3support

      Build and install Qucs.

      ::

        $ brew install qucs

      Homebrew can create symbolic links of installed packages into /Applications, run:

      ::

        $ brew linkapps

   You're done with Homebrew!

--------------

.. Just because a document cannot end with a transition
