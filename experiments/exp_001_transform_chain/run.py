"""Verify that base -> odom -> map equals the directly composed transform."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from localization_learning.geometry.transforms import (  # noqa: E402
    compose_transforms,
    make_transform,
    transform_points,
)


def rotation_z(angle_degrees: float) -> np.ndarray:
    """Create a rotation around the +Z axis."""
    angle_radians = np.deg2rad(angle_degrees)
    cosine = np.cos(angle_radians)
    sine = np.sin(angle_radians)
    return np.array(
        [
            [cosine, -sine, 0.0],
            [sine, cosine, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )


def main() -> None:
    """Run one deterministic transform-chain example."""
    np.set_printoptions(precision=6, suppress=True)

    t_odom_base = make_transform(rotation_z(30.0), [2.0, 1.0, 0.0])
    t_map_odom = make_transform(rotation_z(-10.0), [10.0, -3.0, 0.5])
    point_base = np.array([1.0, 0.5, 0.2])

    point_odom = transform_points(t_odom_base, point_base)
    point_map_sequential = transform_points(t_map_odom, point_odom)

    t_map_base = compose_transforms(t_map_odom, t_odom_base)
    point_map_direct = transform_points(t_map_base, point_base)
    difference = point_map_direct - point_map_sequential

    print("约定: T_a_b 将 B 系中的点变换到 A 系")
    print("\nT_odom_base:\n", t_odom_base)
    print("\nT_map_odom:\n", t_map_odom)
    print("\nT_map_base = T_map_odom @ T_odom_base:\n", t_map_base)
    print("\np_base:", point_base)
    print("p_odom:", point_odom)
    print("p_map（逐步变换）:", point_map_sequential)
    print("p_map（直接复合）:", point_map_direct)
    print("差值:", difference)
    print(
        "两种路径是否一致:",
        bool(np.allclose(point_map_direct, point_map_sequential, atol=1e-12)),
    )


if __name__ == "__main__":
    main()
