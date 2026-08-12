"""Initialization and dependency composition outside the lifecycle FSM."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from sugarsearch.config_loader import load_configuration
from sugarsearch.controller import ApplicationController
from sugarsearch.models import ProjectConfiguration
from sugarsearch.persistence import RunDirectory, create_run_directory
from sugarsearch.records import TrialRecord
from sugarsearch.reporting import Reporter
from sugarsearch.results import OptimizationResult
from sugarsearch.search.registry import create_algorithm
from sugarsearch.stop_policy import StopPolicyEvaluator


@dataclass(frozen=True, slots=True)
class ApplicationSession:
    """One initialized run and its composed lifecycle controller."""

    configuration: ProjectConfiguration
    run_directory: RunDirectory
    controller: ApplicationController

    def run(self) -> OptimizationResult:
        return self.controller.run()


def initialize_application(
    configuration_path: str | Path,
    output_directory: str | Path,
    # EMILY ADDITION FOR BEAUTIFICATION PURPOSES
    on_trial_complete: Callable[[TrialRecord], None] | None = None,
) -> ApplicationSession:
    """Validate configuration, create outputs, and compose the controller."""
    configuration = load_configuration(configuration_path)
    algorithm = create_algorithm(configuration.algorithm)
    stop_policy = StopPolicyEvaluator(
        configuration.stop_policy, configuration.optimization
    )
    run_directory = create_run_directory(output_directory)
    reporter = Reporter(configuration, run_directory)
    reporter.write_resolved_configuration()
    controller = ApplicationController(
        contract=configuration.optimization,
        algorithm=algorithm,
        stop_policy=stop_policy,
        worker_spec=configuration.worker,
        run_directory=run_directory,
        reporter=reporter,
        on_trial_complete=on_trial_complete,
    )
    return ApplicationSession(
        configuration=configuration,
        run_directory=run_directory,
        controller=controller,
    )
