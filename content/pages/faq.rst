:slug: faq

--------------

Frequently asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~

`1. On which OS will Qucs run? <#q001>`__
`2. What kind of software is need to be installed on my system to run Qucs? <#q002>`__
`3. Why don't you use Spice to simulate the schematics? <#q003>`__
`4. How can I set the language for Qucs? <#q004>`__
`5. Qucs does not start on my MacOSX. What's wrong? <#q005>`__
`6. I try to run the ASCO optimizer and it gave me the following error: 'qucsator' is not recognized as an internal or external command, operable program or batch file. <#q006>`__
`7. I use the Windows version of Qucs. After installing it, I can't use it when logged in as different user. Simulation cannot be started, projects are away and/or icons don't appear properly in the GUI. What's wrong? <#q007>`__
`8. What do I do if my question isn't answered here? <#q008>`__

Answers
~~~~~~~

.. _q001:

| **1. On which OS will Qucs run?**
| Qucs is currently developed on GNU/Linux systems using the GNU autotools (and CMake experimentally). For this reason it is very likely that Qucs runs on all kinds of Unix systems supporting an appropriate system interface and an installed Qt® environment. It has been verified that Qucs can be installed on GNU/Linux, Solaris 2.9, MacOS 10.5, NetBSD, FreeBSD and Cygwin (Unix emulation layer for Windows). Qucs is also available natively on x86 Windows (XP/Vista/7/8) systems and experimentaly on x86\_64 versions of these.

.. _q002:

| **2. What kind of software is need to be installed on my system to run Qucs?**
| Currently Qt4 (version 4.6 and higher) are known to work well. To compile qucs you will need some additional packages like qt4-dev-tools, bison, flex, gperf and adms-2.3.0 (included into Qucs)

.. _q003:

| **3. Why don't you use Spice to simulate the schematics?**
| There are several debatable reason for this. When looking at the Spice3f.5 source code (i.e. the last version with technical support from the University of California) it seems like the program was made as a proof of concept rather than a ready to use application. In fact the code is not easy to extend though possibly reliable and tested for a great variaty of schematics. The original Spice misses a S-parameter and harmonic balance simulation which may be necessary for microwave engineers, thus Spice would not be an all-in-one solution. Of cource there are trillions of derivates of the last official Spice version extending and bug-fixing it: but which shall we use? Last but not least the licence issue. The copyright holder for the Spice code are the Regents of the University of California. The code comes for free but isn't in fact meant to be re-used.

Some more restriction of Spice3f.5

-  limited number of nodes and devices (student version)
-  though implemented and possibly ready-to-use the integration order (for the Gear formulae) won't exceed 2 in the transient simulation code
-  there are no such components as phaseshifter, isolator, circulator, microstrip components, etc.
-  the frontend isn't as good as it could be

.. _q004:

| **4. How can I set the language for Qucs?**
| If you want to change the language for the Qucs GUI you need to quit Qucs and then

  ::

    $ export LANG=de

| for German for example. Then start Qucs again. Also you can change the language in the application settings dialog (in the file menu).


.. _q005:

| **5. Qucs does not start on my MacOSX. What's wrong?**
| Please contact the developers. Provide details and if available a crash report.

.. _q006:

| **6. I try to run the ASCO optimizer and it gave me the following error: 'qucsator' is not recognized as an internal or external command, operable program or batch file.**
| The optimizer ASCO runs the 'qucsator' program to perform optimizations. Therefore the 'qucsator' program which is the backend simulator for Qucs needs to reside in the program PATH environment.
| Under GNU/Linux or similar do

  ::

    $ export PATH=$PATH:/path/to/qucsator

| On Win32 systems go to "Start", "Settings", "System properties", click on "Advanced" tab. In the "Advanced" section click the "Environment Variables" button. There edit or add the ``PATH`` environment variable to point to the path where 'qucsator.exe' resides.


.. _q007:

| **7. I use the Windows version of Qucs. After installing it, I can't use it when logged in as different user. Simulation cannot be started, projects are away and/or icons don't appear properly in the GUI. What's wrong?**
| Don't panic! Under Windows environment variables are used to steer "relocation", meaning how a program knows where it resides. During installation these environment variable are set up. These are user specific (even when installed as "Administrator"). If you want to use Qucs two variables are most important: ``QUCSDIR`` and ``HOME``.

``QUCSDIR`` specifies where qucs is installed. On Win32 systems go to "Start", "Settings", "System properties", click on "Advanced" tab. In the "Advanced" section click the "Environment Variables" button. There edit or add the ``QUCSDIR`` environment variable to point to the path Qucs is installed (e.g., ``C:\Programs\Qucs``).

The ``HOME`` variable is used to identify where settings and project data are stored. Even for network drives you can let point it to e.g. ``H:\``. In this folder a directory ``.qucs/`` is created and used to store project related files.

.. _q008:

| **8. What do I do if my question isn't answered here?**
| You may go through the `mailing list archive`_. If that doesn't help, `contact us`_.

--------------

.. _mailing list archive: http://sourceforge.net/mail/?group_id=90337
.. _contact us: contact.html
