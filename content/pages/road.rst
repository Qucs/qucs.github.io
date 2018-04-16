:slug: road

.. role:: blue
.. role:: green
.. role:: strike

--------------

.. _roadmap:

Overall roadmap
~~~~~~~~~~~~~~~

The development of Qucs goes through several steps. The following table gives a rough outline of these stages.

-  :blue:`Stage 5 - Design realization, production, verification.`


   -  Layout editor for PCB and chip. |image0|
   -  Layout tools: DRC, ERC, LVS, ... |image0|
   -  Monte Carlo simulation (device mismatch and process mismatch) based on real technology data. |image0|
   -  Automated data aquisition from measurement equipment; easy to use measurement setups. |image0|


-  :blue:`Stage 4 - Implementation of industry standard device models.`


   -  Implementation of BSIM series. |image0|
   -  Implementation of HICUM. |image1|
   -  Implementation of MEXTRAM. |image0|
   -  Implementation of VBIC. |image0|
   -  Implementation of EPFL-EKV. |image1|

-  :blue:`Stage 3 - Support for more design- and synthesis tools.`

   -  Attenuator design tool. |image1|
   -  Smith-Chart tool for noise and power matching. |image1|
   -  Filter synthesis tool. |image1|
   -  Improve interaction with other software (data conversion). |image0|
   -  Optimizer -- currently using `ASCO <http://asco.sourceforge.net>`__. |image1|
   -  Transmission line calculator. |image1|
   -  Device model and subcircuit library manager. |image1|

-  :green:`Stage 2 - Implementation of powerful circuit analysis tools.`

   -  EM field simulator. |image0|
   -  Transient simulation using convolution for devices defined in the frequency domain. |image0|
   -  Digital simulation. |image1|
   -  Improvements in the GUI regarding usability and design. |image0|
   -  Large signal S-parameter simulation (LSSP) based on harmonic balance. |image0|
   -  Symbolically defined devices. |image1|
   -  Verilog-AMS interface. |image1|

-  :green:`Stage 1 - Setup a simple GUI and a simulator.`

   -  Support for multiple languages. |image1|
   -  Support for standard types of simulations. Each of them implemented in the simulation backend. Communication between GUI and simulator using files or pipes.

      -  S-Parameter |image1|
      -  AC |image1|
      -  DC |image1|
      -  Transient |image1|
      -  Harmonic Balance |image0|
      -  AC Noise |image1|
      -  S-Parameter Noise |image1|

   -  Create data representation visualisations (diagrams). |image1|
   -  Implement an easy to use schematic editor. |image1|

Legend
~~~~~~

    | |image0| indicates that nothing or very little effort has been made.
    | |image1| indicates availability.
    | :green:`Green text` is currently worked on or even finished.
    | :blue:`Blue text` is future work.

.. _specific:

Specific TODO items
~~~~~~~~~~~~~~~~~~~

We are looking for people who can help us with the following things. If you have even a slight idea about one of these, then please (`subscribe <https://lists.sourceforge.net/lists/listinfo/qucs-devel>`__ and) contact us at `<qucs-devel@lists.sourceforge.net> <mailto:qucs-devel@lists.sourceforge.net>`__.

-  :strike:`model of microstrip cross junction`
-  writing tutorials about how to use Qucs or design guides, see `here <docs.html#manual>`__ for details
-  import/export filters for datasets, netlists schematics of other EDA software
-  creation of example schematics
-  maintenance of the Debian package on a regular basis
-  variable step-size coefficients for Adams-Bashford (implicit multi-step integrator)
-  paint logos and icons for the GUI
-  checking Qucs to compile and run on a variety of systems and platforms
-  translation of the GUI and the internal help system
-  filter transformations: LC filters to microstrip and/or active filters
-  coplanar models for non-zero metalization thickness
-  publications and/or help for harmonic balance noise analysis
-  EM field simulator (something like ADS Momentum)
-  synthesis tools, e.g. :strike:`attenuators`, active filters
-  implementation of transmission lines for transient simulation
-  implementations of non-linear models like MOSFETs
-  :strike:`digital simulation engine via VHDL` -- decided to use FreeHDL for now
-  regression test framework and initial test cases for the simulation engine
-  maintenance of the FreeBSD (\*BSD) package

--------------

.. |image0| image:: images/unchecked.png
.. |image1| image:: images/checked.png

