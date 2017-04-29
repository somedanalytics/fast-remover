#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Orcun Gumus
#

"""A function for remove nodes which have k degree"""
import networkx
import numpy
import networkx
from scipy import sparse

# Tensor definition
from theano import tensor, function

x0 = tensor.matrix(name='x0', dtype='float32')
y = x0.sum(axis=1)
rowsum = function([x0], y)


def fastremover(network, k, WIDTH=1000):
    """
    A function for remove nodes which have k degree
    :param network: A network
    :type network: networkx.Graph
    :param k: degree filter
    :type k: int
    :return: network
    """

    A = networkx.to_scipy_sparse_matrix(network, dtype=numpy.float32, format='csr')
    nodes = network.nodes()

    def num_blocks(rows_per_matrix, size_tuple):
        if (size_tuple[0] // rows_per_matrix) == size_tuple[0] / rows_per_matrix:
            return size_tuple[0] // rows_per_matrix
        else:
            return (size_tuple[0] // rows_per_matrix) + 1

    rows_per_matrix = WIDTH if A.shape[0] > WIDTH else A.shape[0]
    num_blocks = num_blocks(rows_per_matrix=rows_per_matrix, size_tuple=A.shape)
    for row_block in range(0, num_blocks):
        start_row = row_block * rows_per_matrix
        end_row = (start_row + rows_per_matrix) if (start_row + rows_per_matrix) <= A.shape[0] else A.shape[0]

        x0_ = A[start_row:end_row, :].toarray()
        vals = rowsum(x0=x0_)
        for idx, val in enumerate(vals):
            if val <= k:
                network.remove_node(nodes[start_row+idx])

    return network

