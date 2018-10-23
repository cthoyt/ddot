import unittest

import pandas as pd

from ddot import Ontology

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
        sim = pd.DataFrame(sim)
        Ontology.run_clixo(sim, 0.0, 1.0, square=True, square_names=genes)


if __name__ == '__main__':
    unittest.main()
