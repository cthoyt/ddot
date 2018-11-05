# -*- coding: utf-8 -*-

"""Tests for DDOT."""

import unittest
import warnings

import pandas as pd

from ddot import Ontology

warnings.filterwarnings('ignore', category=DeprecationWarning)

# Connections from child terms to parent terms
hierarchy = [('S3', 'S1'),
             ('S4', 'S1'),
             ('S5', 'S1'),
             ('S5', 'S2'),
             ('S6', 'S2'),
             ('S1', 'S0'),
             ('S2', 'S0')]

# Connections from genes to terms
mapping = [('A', 'S3'),
           ('B', 'S3'),
           ('C', 'S3'),
           ('C', 'S4'),
           ('D', 'S4'),
           ('E', 'S5'),
           ('F', 'S5'),
           ('G', 'S6'),
           ('H', 'S6')]


class TestDdot(unittest.TestCase):
    def setUp(self):
        self.ont = Ontology(hierarchy, mapping)

    def test_from_sim(self):
        """Test that the run_clixo function can run."""
        sim, genes = self.ont.flatten()

        genes = list(genes)
        print(genes)

        sim = pd.DataFrame(sim, columns=genes, index=genes)

        ddo = Ontology.run_clixo(
            sim,
            'test_df_output.txt',
            'test_clixo_output.txt',
            'test_output.txt',
            square=True,
            square_names=genes,
        )
        print('ddo:\n', ddo)


if __name__ == '__main__':
    unittest.main()
