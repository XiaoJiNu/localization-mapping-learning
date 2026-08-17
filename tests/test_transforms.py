"""Tests for the rigid-transform learning utilities.

The suite uses ``unittest`` assertions so it can also run without third-party
test runners; pytest discovers and reports the same tests in CI.
"""

from __future__ import annotations

import unittest

import numpy as np
from numpy.testing import assert_allclose

from localization_learning.geometry.transforms import (
    compose_transforms,
    invert_transform,
    make_transform,
    transform_points,
    validate_transform,
)


def rotation_z(angle_radians: float) -> np.ndarray:
    """Return a rotation around +Z for deterministic test fixtures."""
    cosine = np.cos(angle_radians)
    sine = np.sin(angle_radians)
    return np.array(
        [
            [cosine, -sine, 0.0],
            [sine, cosine, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )


class TransformTest(unittest.TestCase):
    def setUp(self) -> None:
        self.t_odom_base = make_transform(
            rotation_z(np.deg2rad(90.0)),
            [2.0, 1.0, 0.0],
        )
        self.t_map_odom = make_transform(
            rotation_z(np.deg2rad(-30.0)),
            [10.0, -3.0, 0.5],
        )

    def test_make_transform_places_rotation_and_translation(self) -> None:
        assert_allclose(
            self.t_odom_base[:3, :3],
            rotation_z(np.deg2rad(90.0)),
            atol=1e-12,
        )
        assert_allclose(self.t_odom_base[:3, 3], [2.0, 1.0, 0.0])
        assert_allclose(self.t_odom_base[3], [0.0, 0.0, 0.0, 1.0])

    def test_inverse_is_two_sided_identity(self) -> None:
        inverse = invert_transform(self.t_odom_base)
        assert_allclose(inverse @ self.t_odom_base, np.eye(4), atol=1e-12)
        assert_allclose(self.t_odom_base @ inverse, np.eye(4), atol=1e-12)

    def test_composition_matches_sequential_point_transform(self) -> None:
        point_base = np.array([1.0, 0.5, -0.25])
        point_odom = transform_points(self.t_odom_base, point_base)
        point_map_sequential = transform_points(self.t_map_odom, point_odom)

        t_map_base = compose_transforms(self.t_map_odom, self.t_odom_base)
        point_map_direct = transform_points(t_map_base, point_base)

        assert_allclose(point_map_direct, point_map_sequential, atol=1e-12)

    def test_transform_points_accepts_single_point_and_row_major_batch(self) -> None:
        points = np.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 2.0, 1.0],
            ]
        )
        batch_result = transform_points(self.t_odom_base, points)
        individual_result = np.vstack(
            [transform_points(self.t_odom_base, point) for point in points]
        )

        self.assertEqual(batch_result.shape, (3, 3))
        self.assertEqual(transform_points(self.t_odom_base, points[0]).shape, (3,))
        assert_allclose(batch_result, individual_result, atol=1e-12)

    def test_transform_points_accepts_empty_batch(self) -> None:
        result = transform_points(self.t_odom_base, np.empty((0, 3)))
        self.assertEqual(result.shape, (0, 3))

    def test_make_transform_rejects_invalid_rotation_shape(self) -> None:
        with self.assertRaisesRegex(ValueError, r"rotation must have shape \(3, 3\)"):
            make_transform(np.eye(4), np.zeros(3))

    def test_make_transform_rejects_non_orthonormal_rotation(self) -> None:
        bad_rotation = np.eye(3)
        bad_rotation[0, 0] = 2.0
        with self.assertRaisesRegex(ValueError, "rotation must be orthonormal"):
            make_transform(bad_rotation, np.zeros(3))

    def test_make_transform_rejects_reflection(self) -> None:
        reflection = np.diag([-1.0, 1.0, 1.0])
        with self.assertRaisesRegex(ValueError, r"determinant \+1"):
            make_transform(reflection, np.zeros(3))

    def test_make_transform_rejects_column_translation(self) -> None:
        with self.assertRaisesRegex(ValueError, r"translation must have shape \(3,\)"):
            make_transform(np.eye(3), np.zeros((3, 1)))

    def test_make_transform_rejects_non_finite_translation(self) -> None:
        with self.assertRaisesRegex(ValueError, "only finite"):
            make_transform(np.eye(3), [0.0, np.nan, 0.0])

    def test_validate_transform_rejects_wrong_shape_and_last_row(self) -> None:
        with self.assertRaisesRegex(ValueError, r"shape \(4, 4\)"):
            validate_transform(np.eye(3))

        bad_last_row = np.eye(4)
        bad_last_row[3, 0] = 1.0
        with self.assertRaisesRegex(ValueError, "last row"):
            validate_transform(bad_last_row)

    def test_compose_transforms_requires_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one"):
            compose_transforms()

    def test_transform_points_rejects_column_and_transposed_batches(self) -> None:
        for bad_shape in ((3, 1), (3, 2), (1, 1, 3)):
            with self.subTest(shape=bad_shape):
                with self.assertRaisesRegex(ValueError, "points must have shape"):
                    transform_points(self.t_odom_base, np.zeros(bad_shape))

    def test_transform_points_rejects_non_finite_values(self) -> None:
        with self.assertRaisesRegex(ValueError, "only finite"):
            transform_points(self.t_odom_base, [0.0, np.inf, 0.0])

    def test_all_tolerance_arguments_must_be_positive(self) -> None:
        with self.assertRaisesRegex(ValueError, "atol must be positive"):
            make_transform(np.eye(3), np.zeros(3), atol=0.0)
        with self.assertRaisesRegex(ValueError, "atol must be positive"):
            validate_transform(np.eye(4), atol=-1.0)


if __name__ == "__main__":
    unittest.main()
