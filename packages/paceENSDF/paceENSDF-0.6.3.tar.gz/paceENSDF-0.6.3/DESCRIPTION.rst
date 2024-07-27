============================================================
paceENSDF: Python Archive of Coincident Emissions from ENSDF
============================================================

The `paceENSDF` (Python Archive of Coincident Emissions from ENSDF) project [HUR2023]_ is a Python package enabling access, manipulation, analysis, and visualization of the radioactive decay data from the Evaluated Nuclear Structure Data File (ENSDF) library [TUL2001]_.  A total of 3254 data sets encompassing :math:`\alpha` (834), :math:`\beta-` (1141), and :math:`\epsilon`/:math:`\beta+` (1279) have been extracted from the ENSDF archive [TUL2001]_, parsed and translated into a representative JavaScript Object Notation (JSON) format (descibed below).  The JSON-formatted data sets constitute a total of 92,264 deexcitation :math:`\gamma` rays associated with 41,094 levels.  Additionally, we also provide a Reference Input Parameter Library [CAP2008]_ RIPL-translated format of the corresponding decay-scheme data.  These data sets are bundled together with the analysis toolkit.  A schematic illustrating the portion of the nuclear chart of relevance to the aforementioned decay data from ENSDF is shown in the figure below.

.. image:: https://github.com/AaronMHurst/pace_ensdf/blob/main/decay_nuclides.png?raw=true
   :width: 500 px
   :scale: 100%
   :alt: Schematic of portion of nuclear chart of relevance to the ENSDF-decay data sets
   :align: center

The `paceENSDF` package provides users with a convenient means to access and manipulate the decay data from ENSDF with various methods to return all associated nuclear structure decay-scheme data including levels, spins, parities, :math:`\gamma-` ray information, etc.  An overview of the available methods is provided in `Jupyter Notebooks` distributed with this package (inside the `notebook` folder).

All ENSDF decay-scheme data sets containing :math:`\gamma`-ray information have also been used to generate coincidence :math:`\gamma`-:math:`\gamma` and :math:`\gamma`-*X*-ray JSON data structures from the corresponding decay data set [HUR2023]_.  However, not every decay dataset in ENSDF contains :math:`\gamma`-ray data.  Of the total decay datasets only 2394 have the :math:`\gamma`-ray information needed to derive these coincidence datasets.  This number represents around 73.6% of the ENSDF archive (version: September 2023) and these decay datasets are summarized in the Figure below.  From this schematic it is clear that the :math:`\alpha`-decay datasets are most heavily impacted by the :math:`\gamma`-ray condition.

.. image:: https://github.com/AaronMHurst/pace_ensdf/blob/main/coinc_decay_nuclides.png?raw=true
   :width: 500 px
   :scale: 100%
   :alt: Schematic showing ENSDF-decay data sets containing :math:`gamma`-ray information
   :align: center

In addition to the coincidence energies and absolute intensities, together with associated uncertainties, these data structures contain additional meta data parsed from the original ENSDF data structure allowing users to search for single energies (both :math:`\gamma` and *X*-ray) as well as coincidence pairs.  Refer to the corresponding `Jupyter Notebook` provided with this project to see example use cases.

-------------------------
Notes on ENSDF quantities
-------------------------

Although most quantities in ENSDF are normally-distributed symmetrical quantities associated with the equality `=` operator, the following exceptions (frequent in many cases) are also accounted for:

* All asymmetric quantities parsed in the original ENSDF dataset are symmetrized and their associated median-symmertized values and uncertainties are reported in the derived JSON data structures.
* All approximate `AP` values parsed in the original ENSDF dataset are reported with an assumed 50% uncertainty.
* All values parsed as limits (i.e., `LT`, `GT`, `GE`, `GE`) in the original ENSDF dataset are reported with an assumed 100% uncertainty.

-----------------------------------
Building, installation, and testing
-----------------------------------

The `paceENSDF` project can be conveniently built and installed using the `pip` command in a Unix terminal:

.. code:: bash

          $ pip install paceENSDF

Alternatively, because this project is also maintained on `GitHub <https://github.com/AaronMHurst/pace_ensdf>`_, it can be installed by cloning the repository and executing the installation script provide as described in the `README.md` documentation on the landing page:

`<https://github.com/AaronMHurst/pace_ensdf>`_

A suite of Python modules containing 283 unit tests is also bundled with the software.  Instructions for running the test script are also provided on the `GitHub <https://github.com/AaronMHurst/pace_ensdf>`_ landing page.  This project has been successfully built and tested against multiple virtual Python environments from `Python-3.5` to `Python-3.10`.

-----------------
Running paceENSDF
-----------------

Following installation, the `paceENSDF` scripts can be ran from any location by importing the package and making an instance of the `ENSDF` class:

.. code-block:: bash
                
        $ python


.. code-block:: python
        
        import paceENSDF as pe
        e = pe.ENSDF()

Most methods also require passing the `JSON`-formatted ENSDF source datasets or the `JSON`-formatted coincidence datasets as a list-object argument which first needs to be created accordingly:

.. code-block:: python

        edata = e.load_ensdf()  # ENSDF data
        cdata = e.load_pace()   # Coincidence data

The utility of the `paceENSDF` methods illustrating examples concerning access, manipulation, analysis, and visualization of the ENSDF data is demonstrated in the `Jupyter Notebooks` provided on `GitHub <https://github.com/AaronMHurst/pace_ensdf>`_.  These notebooks also have a `matplotlib` Python-package dependency and utilize inline-plotting methods and builtin `Jupyter Notebook` magic commands.

----------
Docstrings
----------

All `paceENSDF` classes and functions have supporting docstrings.  Please refer to the individual dosctrings for more information on any particular function including how to use it.  The dosctrings for each method generally have the following structure:

* A short explanation of the function.
* A list and description of arguments that need to be passed to the function.
* The return value of the function.
* An example(s) invoking use of the function.

To retrieve the method resolution order and a list of the available methods inherited from the individual classes contained in the modules simply execute the following command in a Python interpreter:

.. code-block:: bash

        $ python

.. code-block:: python

        help(e)
                
Or, to retrieve the docstring for a particular method, e.g., the callable `get_gg`:

.. code-block:: python

        help(e.get_gg)

-----------
RIPL format
-----------

Because many nuclear reaction codes source decay-scheme information in a particular Reference Input Parameter Library (RIPL) [CAP2008]_ format, representative RIPL-translated datasets have also been generated for each corresponding ENSDF-decay dataset and these files are also bundled with the software.  See the `GitHub <https://github.com/AaronMHurst/pace_ensdf>`_ landing page for more information.

-----------
JSON format
-----------

All original ENSDF radioactive-decay datasets have been translated into a representative JavaScript Object Notation (JSON) format using an intuitive syntax to describe the quantities sourced from the primary and continuation records of the ENSDF-formatted data sets [TUL2001]_.  The corresponding JSON-formatted radioative-decay datasets are bundled with this software package together with JSON-formatted coincidence :math:`\gamma-`:math:`\gamma` and :math:`\gamma-` *X*-ray data sets derived from the respective decay-scheme information in the original ENSDF library.  The JSON data structures support the following data types:

* *string*
* *number*
* *boolean*
* *null*
* *object* (JSON object)
* *array*

The JSON-formatted schemas are explained in detail on the `GitHub <https://github.com/AaronMHurst/pace_ensdf>`_ landing page.


----------
References
----------

.. [HUR2023]
   A.M. Hurst, B.D. Pierson, B.C. Archambault, L.A. Bernstein, S.M. Tannous, *"A decay datababase of coincident* :math:`\gamma`-:math:`\gamma` *and* :math:`\gamma`-*X-ray branching ratios for in-field spectroscopy applications"*, Eur. Phys. J. (Web of Conf.) **284**, 18002 (2023); https://doi.org/10.1051/epjconf/202328418002

.. [TUL2001]
   J.K. Tuli, *"Evaluated Nuclear Structure Data File"*, BNL-NCS-51655-01/02-Rev (2001); https://www.nndc.bnl.gov/ensdf/

.. [CAP2008]
   R.Capote *et al*., *"RIPL - Reference Input Parameter Library for Calculation of Nuclear Reactions and Nuclear Data Evaluations"*, Nucl. Data Sheets **110**, 3107 (2009).
