=============================================
Behavior Optimization and Learning for Robots
=============================================

.. raw:: html

    <center><img src="_static/logo.svg" width=500px /></center>

.. raw:: html

    <table>
    <tr valign="top">
    <td>

About
=====

BOLeRo makes behavior learning for robots easy. It combines behavior learning
algorithms with learning problems through defined interfaces that can be used
by a controller. The whole communication between a behavior and an environment
is done by requesting actions generated from the behavior and sensory
information generated by an environment.

Features
========

The highlights of BOLeRo are

* Dynamical Movement Primitives with a final velocity greater than 0 (see
  `Muelling et al.
  <http://www.ausy.informatik.tu-darmstadt.de/uploads/Publications/Muelling_IJRR_2013.pdf>`_)
  and correct handling of rotation in Cartesian space (see `Ude et al.
  <http://www-hcr.ijs.si/resources/papers/icra14b.pdf>`_) in C++ with a Python
  wrapper
* Contextual Relative Entropy Policy Search (see `Kupcsik et al.
  <http://www.ausy.informatik.tu-darmstadt.de/uploads/Publications/Kupcsik_AAAI_2013.pdf>`_)
* a clean and readable implementation of Covariance Matrix Adaption
  Evolution Strategies (CMA-ES, see
  `Wikipedia <https://en.wikipedia.org/wiki/CMA-ES>`_) and several of its
  variants
* it is easy to combine it with the simulation software
  `MARS <https://github.com/rock-simulation/mars>`_
* C++ interface to Python modules and Python interface to C++ modules
* configuration via YAML

.. raw:: html

    </td>
    <td valign="middle">

.. image:: _static/concept_sketch.svg
   :alt: Behavior Learning
   :align: right
   :width: 500px

.. raw:: html

    </td>
    </tr>
    </table>

Documentation
=============

Getting Started
---------------

.. toctree::
   :maxdepth: 1

   installation
   quickstart-controller
   quickstart

Overview
--------

.. toctree::
   :maxdepth: 1

   behavior_learning
   modules/representation
   modules/optimizer
   modules/behavior_search
   modules/environment
   modules/controller
   modules/datasets
   modules/wrapper
   imitation_learning

Examples
--------

.. toctree::
   :maxdepth: 1

   auto_examples/index
   notebooks/index

API
---

.. toctree::
   :maxdepth: 1

   api_py
   api_cpp
   mars_environment
   contributing

Funding
=======

.. image:: _static/241-logo-bmwi-jpg.jpg
   :alt: German Federal Ministry for Economic Affairs and Energy

.. image:: _static/logo_125_52.png
   :alt: German Federal Ministry for Economic Affairs and Energy
