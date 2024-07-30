import numpy as np
import sys
import unittest

sys.path.insert(1, '../euclidean_hausdorff')
from eucl_haus import upper_heuristic, upper_exhaustive
from transformation import Transformation
from point_cloud import PointCloud


class TestEuclHaus(unittest.TestCase):

    def test_box_heuristic_deh(self):
        box = np.array([[1, 1],
                        [-1, 1],
                        [-1, -1],
                        [1, -1]])
        T = Transformation(np.array([1, 2]), [np.pi / 7], False)
        transformed_box = T.apply(box)

        dEH, _ = upper_heuristic(box, transformed_box, n_parts=10)
        assert np.isclose(0, np.round(dEH, 2))

    def test_box_exact_deh(self):
        box = np.array([[1, 1],
                        [-1, 1],
                        [-1, -1],
                        [1, -1]])
        T = Transformation(np.array([1, 2]), [np.pi / 7], False)
        transformed_box = T.apply(box)

        dEH, _ = upper_exhaustive(box, transformed_box, target_err=.4)
        assert np.isclose(0, np.round(dEH, 1))

    def test_cube_heuristic_deh(self):
        cube = np.array([[0, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0],
                         [0, 1, 0],
                         [1, 0, 1],
                         [1, 1, 1],
                         [0, 0, 1],
                         [0, 1, 1]])
        T = Transformation(np.array([1, 2, 3]), [np.pi / 7, np.pi / 3, 0], False)
        transformed_cube = T.apply(cube)
        dEH, _ = upper_heuristic(cube, transformed_cube)
        assert np.isclose(0, np.round(dEH, 2))

    def test_random_clouds_heuristic(self):
        A_coords = np.random.randn(100, 3)
        T = Transformation(np.array([-1, 2, -3]), [np.pi / 3, np.pi / 3, np.pi / 3], True)
        B_coords = T.apply(A_coords)
        A, B = map(PointCloud, [A_coords, B_coords])
        dH = max(A.asymm_dH(B), B.asymm_dH(A))
        dEH, _ = upper_heuristic(A_coords, B_coords, n_parts=3)
        assert dEH < dH


if __name__ == "__main__":
    np.random.seed(0)
    unittest.main()
