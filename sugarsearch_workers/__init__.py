"""Dependency-free opaque workers distributed alongside SugarSearch.

Workers remain outside :mod:`sugarsearch` so the optimizer never
imports or inspects the implementation it launches.
"""
