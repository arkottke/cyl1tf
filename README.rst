cyL1TF
======

|PyPi Cheese Shop| |Build Status| |Code Quality| |Test Coverage| |License| |DOI|

A Python library using Cython for using ℓ₁ (L1) trend filtering algorithm developed by Kim et al. (2009):

    Kim, S. J., Koh, K., Boyd, S., & Gorinevsky, D. (2009). ℓ₁ trend filtering. SIAM review, 51(2), 339-360. DOI:  `10.1137/070690274`_

.. _`10.1137/070690274`: https://doi.org/10.1137/070690274


Usage
-----

.. code-block:: python

    import cyl1tf
    fit = cyl1tf.calc_fit(xy, rel_scale=0.01)

    
See `example.ipynb`_.

.. _`example.ipynb`: https://github.com/arkottke/cyl1tf/blob/dev/example.ipynb

Citation
--------

Please cite this software using the DOI_.

.. _DOI: https://zenodo.org/badge/latestdoi/5086299

.. |PyPi Cheese Shop| image:: https://img.shields.io/pypi/v/cyl1tf.svg
   :target: https://img.shields.io/pypi/v/cyl1tf.svg
.. |Build Status| image:: https://travis-ci.org/arkottke/cyl1tf.svg?branch=master
   :target: https://travis-ci.org/arkottke/cyl1tf
.. |Code Quality| image:: https://app.codacy.com/project/badge/Grade/ab76944a60224759997a51e771bd4aff    
   :target: https://www.codacy.com/manual/arkottke/cyl1tf
.. |Test Coverage| image:: https://api.codacy.com/project/badge/Coverage/ab76944a60224759997a51e771bd4aff    
   :target: https://www.codacy.com/manual/arkottke/cyl1tf
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
.. |DOI| image:: https://zenodo.org/badge/5086299.svg
   :target: https://zenodo.org/badge/latestdoi/5086299
