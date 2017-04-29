=====================
Fast Remover
=====================
.. image:: https://travis-ci.org/somedanalytics/fast-remover.svg?branch=master
    :target: https://travis-ci.org/somedanalytics/fast-remover

This repository created for remove nodes from graph

The purpose is to prevent CPU violation to remove nodes.

.. image:: https://snag.gy/CvGDtH.jpg

Removing nodes from graph by edges is a massive op. 10^5 nodes means 10^10 possible edges

``new_graph = fastremover(graph, k=2)``
k means minimum degree in the graph (inclusive)

Implementation is using scipy lil and csr sparse matrix.

Note that return type is csr matrix from version 1.0.1

Install
===============

``pip install fast-remover``