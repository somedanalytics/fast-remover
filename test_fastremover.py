#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Orcun Gumus
import unittest
import networkx
import time

from fastremover import fastremover


class TestFastRemoverMethod(unittest.TestCase):

    def test_basic_usage(self):
        network = networkx.Graph(
            [(0, 2),
             (1, 2),
             (2, 3),
             (2, 4),
             (3, 6),
             (3, 5),
             (4, 6),
             (4, 7),
             (6, 8),
             (5, 8),
             (6, 9),
             (7, 9),
             (9, 10),
             (8, 10),
             (10, 11),
             (10, 12)])

        # Example Graph:
        # https://snag.gy/YMubXO.jpg

        graph = fastremover(network, 1)
        self.assertNotIn(0, graph.nodes())
        self.assertNotIn(1, graph.nodes())

    def test_complex_usage(self):
        graph = networkx.fast_gnp_random_graph(10000, 0.01)
        node_count = len(graph.nodes())
        print(node_count)
        start = time.time()
        graph = fastremover(graph, 5)
        end = time.time()

        node_count = len(graph.nodes())
        print(end-start, node_count)


if __name__ == '__main__':
    unittest.main()
