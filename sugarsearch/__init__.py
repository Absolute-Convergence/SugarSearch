"""Public contracts for SugarSearch."""

from sugarsearch.config_loader import (
    ConfigurationError,
    load_configuration,
)
from sugarsearch.models import (
    AlgorithmSpec,
    CandidateConfiguration,
    Direction,
    Objective,
    OptimizationContract,
    ParameterDefinition,
    ParameterKind,
    ProjectConfiguration,
    StopPolicy,
    WorkerSpec,
)
from sugarsearch.results import OptimizationResult, ParetoFront

__all__ = [
    "AlgorithmSpec",
    "CandidateConfiguration",
    "ConfigurationError",
    "Direction",
    "Objective",
    "OptimizationContract",
    "OptimizationResult",
    "ParameterDefinition",
    "ParameterKind",
    "ParetoFront",
    "ProjectConfiguration",
    "StopPolicy",
    "WorkerSpec",
    "load_configuration",
]
