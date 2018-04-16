:slug: docs

.. class:: center

[ user manual - `third party`_ - `technical papers`_ - components_ - related_ - `press/education`_ - contact_ ]

.. _manual:

User manual
~~~~~~~~~~~

Until now there is no or little user documentation available. The Qucs
application has an integrated help system giving the user useful but yet
limited help with the program. However, a useful beginners tutorial can
be found `here (pdf)`_. We are searching for people who want to support
the project by creating more documentation. The internal help system is
also multi-lingual, thus translations into languages other than English,
German, French and Spanish have to be done. If you are interested then
feel free to write a email to: `contact`_. It is planned to have user
manuals consisting of

- **the integrated multi-lingual help system**

  These should be little helpers with the program itself available during
  runtime including a getting started guide and brief descriptions of what
  is what in the graphical user interface (GUI). The documentation is
  written in simple HTML pages and focuses on the GUI.

- **an english user manual with some more details**

  The actual user manual should contain a more detailed description of the
  simulation backend including the available program options, components
  and simulation types. The user manual focuses on the simulator and
  should be written in the Texinfo (texi) format, i.e. means it can be
  easily converted into info and HTML pages.

- **tutorials about how to use Qucs**

  Topic-related tutorials dealing with certain issues, real life

- **tutorials about how to use Qucs**

  Topic-related tutorials dealing with certain issues, real life
  applications and how to handle these with Qucs. The tutorials will be
  available as pdf files and are written in LaTex. Available tutorials
  so far:

  - **workbook tutorial chapters**

    - Getting Started with Qucs: `getstarted.pdf`_
    - DC Analysis, Parameter Sweep and Device Models: `dcstatic.pdf`_
    - Getting Started with Digital Circuit Simulation: `digital.pdf`_
    - Transient Domain Flip-Flop Models for Mixed-Mode Simulation: `ffmodels.pdf`_
    - Modelling Operational Amplifiers: `opamp.pdf`_
    - Modelling the 555 Timer: `timer555.pdf`_
    - Qucs simulation of SPICE netlists: `spicetoqucs.pdf`_
    - Biasing a BJT Transistor: `bjtbias.pdf`_
    - BJT Modeling and Verification: `modelbjt.pdf`_
    - Power Amplifier Design: `poweramp.pdf`_
    - Low Noise Amplifier Design: `lna.pdf`_
    - Microstrip Design - 10dB Directional Coupler Design: `coupler.pdf`_
    - Measurement Expressions Reference Manual: `functions.pdf`_
    - Component, compact device and circuit modelling using symbolic equations: `equations.pdf`_

  - **workbook**

    - Preliminary WorkBook: `workbook.pdf`_
    - Russian translation of the preliminary WorkBook: `workbook_ru.pdf`_

      - provided by Vladimir Gololobov `*<vgololobov@mpark.ru>*`_ on 2006/10/18

  - **SPICE to Qucs test reports (by Mike Brinson)**

    - DC and independent voltage pulse generator test: `StoQ_test1.pdf`_
    - DC and independent voltage sin generator test: `StoQ_test2.pdf`_
    - SPICE 2g6 and 3f5 resistors: `StoQ_test3.pdf`_
    - SPICE 2g6 and 3f5 capacitors: `StoQ_test4.pdf`_
    - SPICE 2g6 and 3f5 inductors: `StoQ_test5.pdf`_

  - **standalone report chapters**

    - Verilog-AMS interface: `verilog.pdf`_
    - A Curtice level 1 MESFET model: `curtice.pdf`_
    - Verilog-A Modular Macromodel for Operational Amplifiers: `mod_amp.pdf`_
    - Verilog-A Logarithmic Amplifier Macromodel: `log_amp.pdf`_
    - Verilog-A Macromodel for Resistive Potentiometers: `potentiometer.pdf`_
    - Verilog-A compact device models for GaAs MESFETs: `MESFET.pdf`_
    - Verilog-A implementation of the EKV v2.6 long and short channel MOSFET models: `EKV26.pdf`_
    - Compact Verilog-A pn junction photodiode model: `photodiode.pdf`_
    - PV Cell simulation with QUCS - A generic model of PV Cell: `Photovoltaic_Cell_Model_Miguel Pareja.pdf`_

  - **reportbook**

    - Preliminary ReportBook: `reportbook.pdf`_

  - **other tutorials**

    - Notes on Constructing Qucs Verilog-A Compact Device Models and Circuit Macromodels: `Qucs_Verilog_ANotes.pdf`_
    - Using Qucs in Textmode: `textmode.pdf`_

--------------

.. _third party: thirdparty.html
.. _technical papers: technical.html
.. _components: components.html
.. _related: related.html
.. _press/education: press.html
.. _contact: contact.html
.. _here (pdf): docs/tutorial/getstarted.pdf
.. _getstarted.pdf: docs/tutorial/getstarted.pdf
.. _dcstatic.pdf: docs/tutorial/dcstatic.pdf
.. _digital.pdf: docs/tutorial/digital.pdf
.. _ffmodels.pdf: docs/tutorial/ffmodels.pdf
.. _opamp.pdf: docs/tutorial/opamp.pdf
.. _timer555.pdf: docs/tutorial/timer555.pdf
.. _spicetoqucs.pdf: docs/tutorial/spicetoqucs.pdf
.. _bjtbias.pdf: docs/tutorial/bjtbias.pdf
.. _modelbjt.pdf: docs/tutorial/modelbjt.pdf
.. _poweramp.pdf: docs/tutorial/poweramp.pdf
.. _lna.pdf: docs/tutorial/lna.pdf
.. _coupler.pdf: docs/tutorial/coupler.pdf
.. _functions.pdf: docs/tutorial/functions.pdf
.. _equations.pdf: docs/tutorial/equations.pdf
.. _textmode.pdf: docs/tutorial/textmode.pdf
.. _workbook.pdf: docs/tutorial/workbook.pdf
.. _workbook_ru.pdf: docs/workbook_ru.pdf
.. _*<vgololobov@mpark.ru>*: mailto:vgololobov@mpark.ru
.. _StoQ_test1.pdf: docs/report/StoQ_test1.pdf
.. _StoQ_test2.pdf: docs/report/StoQ_test2.pdf
.. _StoQ_test3.pdf: docs/report/StoQ_test3.pdf
.. _StoQ_test4.pdf: docs/report/StoQ_test4.pdf
.. _StoQ_test5.pdf: docs/report/StoQ_test5.pdf
.. _verilog.pdf: docs/report/verilog.pdf
.. _curtice.pdf: docs/report/curtice.pdf
.. _mod_amp.pdf: docs/report/mod_amp.pdf
.. _log_amp.pdf: docs/report/log_amp.pdf
.. _potentiometer.pdf: docs/report/potentiometer.pdf
.. _MESFET.pdf: docs/report/MESFET.pdf
.. _EKV26.pdf: docs/report/EKV26.pdf
.. _photodiode.pdf: docs/report/photodiode.pdf
.. _Photovoltaic_Cell_Model_Miguel Pareja.pdf: docs/Photovoltaic_Cell_Model_Miguel%20Pareja.pdf
.. _reportbook.pdf: docs/report/reportbook.pdf
.. _Qucs_Verilog_ANotes.pdf: docs/Qucs_Verilog_ANotes.pdf
