"""三维刚体变换的最小实现。

本模块采用列向量和左乘约定。 ``T_a_b`` 把 B 坐标系中的点变换到
A 坐标系： ``p_a = T_a_b @ p_b``（齐次坐标形式）。
"""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]


def _as_finite_float_array(value: ArrayLike, name: str) -> FloatArray:
    """Convert an array-like value to finite ``float64`` values."""
    try:
        array = np.asarray(value, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain numeric values") from exc

    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    return array


def _validate_rotation(rotation: ArrayLike, *, atol: float) -> FloatArray:
    """Validate that ``rotation`` is a proper 3-D rotation matrix."""
    matrix = _as_finite_float_array(rotation, "rotation")
    if matrix.shape != (3, 3):
        raise ValueError(f"rotation must have shape (3, 3), got {matrix.shape}")

    identity = np.eye(3, dtype=np.float64)
    if not np.allclose(matrix.T @ matrix, identity, atol=atol, rtol=0.0):
        raise ValueError("rotation must be orthonormal")

    determinant = float(np.linalg.det(matrix))
    if not np.isclose(determinant, 1.0, atol=atol, rtol=0.0):
        raise ValueError(
            "rotation must be a proper rotation with determinant +1, "
            f"got {determinant:.12g}"
        )
    return matrix


def make_transform(
    rotation: ArrayLike,
    translation: ArrayLike,
    *,
    atol: float = 1e-9,
) -> FloatArray:
    """Build a 4x4 homogeneous transform from rotation and translation.

    Args:
        rotation: Proper rotation matrix with exact shape ``(3, 3)``.
        translation: Translation vector with exact shape ``(3,)``.
        atol: Absolute tolerance used to validate the rotation matrix.

    Returns:
        A new ``float64`` homogeneous transform.

    Raises:
        ValueError: If a shape is wrong, a value is non-finite, or the rotation
            is not a proper rotation.
    """
    if atol <= 0:
        raise ValueError("atol must be positive")

    checked_rotation = _validate_rotation(rotation, atol=atol)
    checked_translation = _as_finite_float_array(translation, "translation")
    if checked_translation.shape != (3,):
        raise ValueError(
            "translation must have shape (3,), "
            f"got {checked_translation.shape}"
        )

    transform = np.eye(4, dtype=np.float64)
    transform[:3, :3] = checked_rotation
    transform[:3, 3] = checked_translation
    return transform


def validate_transform(transform: ArrayLike, *, atol: float = 1e-9) -> FloatArray:
    """Validate and return a copy of a homogeneous rigid transform.

    The exact shape must be ``(4, 4)``. The final row must be
    ``[0, 0, 0, 1]`` and the upper-left block must be a proper rotation.
    """
    if atol <= 0:
        raise ValueError("atol must be positive")

    matrix = _as_finite_float_array(transform, "transform")
    if matrix.shape != (4, 4):
        raise ValueError(f"transform must have shape (4, 4), got {matrix.shape}")

    expected_last_row = np.array([0.0, 0.0, 0.0, 1.0])
    if not np.allclose(matrix[3, :], expected_last_row, atol=atol, rtol=0.0):
        raise ValueError("transform last row must be [0, 0, 0, 1]")

    _validate_rotation(matrix[:3, :3], atol=atol)
    return matrix.copy()


def invert_transform(transform: ArrayLike, *, atol: float = 1e-9) -> FloatArray:
    """Return the inverse of a homogeneous rigid transform."""
    matrix = validate_transform(transform, atol=atol)
    rotation = matrix[:3, :3]
    translation = matrix[:3, 3]

    inverse = np.eye(4, dtype=np.float64)
    inverse[:3, :3] = rotation.T
    inverse[:3, 3] = -(rotation.T @ translation)
    return inverse


def compose_transforms(
    *transforms: ArrayLike,
    atol: float = 1e-9,
) -> FloatArray:
    """Compose transforms in matrix-multiplication order.

    For example, to form ``T_map_base`` from ``T_map_odom`` and
    ``T_odom_base``, call::

        T_map_base = compose_transforms(T_map_odom, T_odom_base)

    At least one transform is required. Every input is validated before
    multiplication, and the result is validated again to catch numerical or
    convention errors early.
    """
    if not transforms:
        raise ValueError("at least one transform is required")

    checked: Iterable[FloatArray] = (
        validate_transform(transform, atol=atol) for transform in transforms
    )
    result = np.eye(4, dtype=np.float64)
    for transform in checked:
        result = result @ transform
    return validate_transform(result, atol=max(atol, 1e-8))


def transform_points(
    transform: ArrayLike,
    points: ArrayLike,
    *,
    atol: float = 1e-9,
) -> FloatArray:
    """Apply a rigid transform to one point or a row-major point batch.

    Args:
        transform: Homogeneous transform with shape ``(4, 4)``.
        points: One point with shape ``(3,)`` or N row-major points with shape
            ``(N, 3)``. Shapes such as ``(3, 1)`` and ``(3, N)`` are rejected.
        atol: Absolute tolerance used to validate the transform.

    Returns:
        Transformed points with the same rank as ``points``.
    """
    matrix = validate_transform(transform, atol=atol)
    point_array = _as_finite_float_array(points, "points")

    if point_array.shape == (3,):
        return matrix[:3, :3] @ point_array + matrix[:3, 3]

    if point_array.ndim == 2 and point_array.shape[1] == 3:
        return point_array @ matrix[:3, :3].T + matrix[:3, 3]

    raise ValueError(
        "points must have shape (3,) or (N, 3), "
        f"got {point_array.shape}"
    )
