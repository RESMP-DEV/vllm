# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Lazy/optional imports: benchmark subcommands may pull in optional deps.
try:
    from vllm.entrypoints.cli.benchmark.latency import (
        BenchmarkLatencySubcommand)
except Exception:  # pragma: no cover - optional dependency path
    BenchmarkLatencySubcommand = None  # type: ignore

try:
    from vllm.entrypoints.cli.benchmark.serve import (
        BenchmarkServingSubcommand)
except Exception:  # pragma: no cover - optional dependency path
    BenchmarkServingSubcommand = None  # type: ignore

try:
    from vllm.entrypoints.cli.benchmark.throughput import (
        BenchmarkThroughputSubcommand)
except Exception:  # pragma: no cover - optional dependency path
    BenchmarkThroughputSubcommand = None  # type: ignore

__all__: list[str] = [
    name for name, obj in {
        "BenchmarkLatencySubcommand": BenchmarkLatencySubcommand,
        "BenchmarkServingSubcommand": BenchmarkServingSubcommand,
        "BenchmarkThroughputSubcommand": BenchmarkThroughputSubcommand,
    }.items() if obj is not None
]
