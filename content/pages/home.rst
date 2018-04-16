:url: .
:save_as: index.html

.. table::
   :class: lntable

   +-----------------------------------+----------------------------------------+
   | **Latest stable release: 0.0.19** | `Official SourceForge repository`_     |
   +-----------------------------------+----------------------------------------+
   | `Source`_                         | `GitHub Mirror`_                       |
   +-----------------------------------+----------------------------------------+
   | `Windows`_ `Ubuntu`_ `OS X`_      | `Qucs Wiki`_                           |
   +-----------------------------------+----------------------------------------+

What's Qucs?
~~~~~~~~~~~~
Qucs stands for Quite Universal Circuit Simulator. So far Qucs is not
yet finished, but it is already packed with features. Take a look at
the `screenshots`_ to get a feel for what it can do.

Qucs is an integrated circuit simulator which means you are able to
setup a circuit with a graphical user interface (GUI) and simulate the
large-signal, small-signal and noise behaviour of the circuit. After
that simulation has finished you can view the simulation results on a
presentation page or window.



+ Qucs, briefly for Quite Universal Circuit Simulator, is a circuit
  simulator with graphical user interface (GUI). The GUI is based on Qt
  by `Digia`_. The software aims to support all kinds of circuit
  simulation types, e.g. DC, AC, S-parameter, Harmonic Balance analysis,
  noise analysis, etc.
  +
+ Qucsator, the simulation backend, is a command line circuit
  simulator. It takes a network list in a certain format as input and
  outputs a Qucs dataset. It has been programmed for usage in the Qucs
  project but may also be used by other applications.

The Qucs GUI is well advanced and allows setting up schematics and
presenting simulation results in various types of diagrams. DC, AC,
S-parameter, noise and transient analysis is possible, mathematical
equations and use of a subcircuit hierarchy (with parameterised
subcircuits) are available. Qucs can also import existing SPICE models
for use in your simulations.

While Qucs is well developed, we still strive to improve the project,
and will always welcome offers of help. Qucs doesn't just need help
with programming, it also needs graphics, high quality example
schematics, tutorials for the website and lots more.

Qucs comes with a huge array of components and models including HICUM,
BSIM2, BSIM3, and soon BSIM6. It also provides many semiconductor
based components and models such as OpAmps, Diodes, MOSFETs, PMOSFETs
and many more. Some example schematics can be found `here`_ which
demonstrate some of the abilities of Qucs, and many more examples are
provided with the program.


Operating Systems
~~~~~~~~~~~~~~~~~
Qucs is currently developed under the GNU/Linux OS using the standard
autotools with no special effort to support other operating systems.
However Qucs is said to be successfully compiled and run on Windows,
Solaris, NetBSD, FreeBSD, MacOS, and Cygwin... help is needed !


License
~~~~~~~
Qucs is released under the GPL license and so it is free for free
programmers and users !


Reference
~~~~~~~~~
Qt is a registered trademark of Digia.

--------------

.. _Source: https://sourceforge.net/projects/qucs/files/qucs/
.. _Windows: http://sourceforge.net/projects/qucs/files/qucs-binary/
.. _Ubuntu: https://launchpad.net/~qucs/+archive/qucs/+packages
.. _OS X: http://sourceforge.net/projects/qucs/files/qucs-binary/
.. _Official SourceForge repository: http://sourceforge.net/projects/qucs/
.. _GitHub Mirror: https://github.com/Qucs/qucs/
.. _Qucs Wiki: https://github.com/Qucs/qucs/wiki

.. _Previous news items: news.html
.. _Qucs Core: http://qucs.github.io/qucs-doxygen/qucs-core/index.html
.. _package manager for Mac OSX: : build.html#build_mac
.. _Qucs GUI: http://qucs.github.io/qucs-doxygen/qucs/index.html
.. _Darwin (Mac OSX): https://github.com/Qucs/qucs/wiki/Build-Darwin
.. _Coveralls: https://coveralls.io/r/Qucs/qucs?branch=master
.. _code documentation: : devs.html#code_doc
.. _screenshots: : screenshots.html
.. _GitHub repository: https://github.com/Qucs/qucs.github.io
.. _Digia: http://qt.digia.com/
.. _Linux : https://github.com/Qucs/qucs/wiki/Build-Linux
.. _local_complex_20130624: https://sourceforge.net/p/qucs/git/ci/local_complex_20130624/tree/
.. _13th MOS-AK Workshop, Graz (A): http://www.mos-ak.org/graz_2015
.. _online: http://www.mos-ak.org/graz_2015/presentations/T_5_Brinson_MOS-AK_Graz_2015.pdf
.. _Travis CI: https://travis-ci.org/Qucs/qucs
.. _here: examples.html#example
.. _News: https://github.com/Qucs/qucs/blob/qucs-0.0.18/qucs/NEWS.md
.. _Ubuntu PPA: install.html#install_ubuntu


