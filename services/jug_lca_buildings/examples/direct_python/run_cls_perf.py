"""Benchmark runner for JSON export performance."""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))

from jug_lca_buildings.application import EmissionsApplicationService


def parse_args():
    p = argparse.ArgumentParser(
        description='Benchmark jug_lca_buildings application class (JSON output)'
    )
    p.add_argument(
        '--test-id',
        required=True,
        help='Test ID, e.g. WINNEW-CLS-JSON-COLD-N40-R01',
    )
    p.add_argument(
        '--payload',
        required=True,
        help='Absolute or relative path to GeoJSON/JSON payload',
    )
    p.add_argument(
        '--artifact-dir',
        default='perf_runs/cls_artifacts',
        help=(
            'Cache directory used by EmissionsApplicationService '
            '(default: perf_runs/cls_artifacts)'
        ),
    )
    p.add_argument(
        '--cold',
        action='store_true',
        help='Delete artifact cache before running',
    )
    p.add_argument(
        '--with-logging',
        action='store_true',
        help='Enable jugs_chassis file logging',
    )
    p.add_argument(
        '--log-dir-base',
        default='.',
        help='Base dir for logs when --with-logging is used (default: current dir)',
    )
    return p.parse_args()


def load_payload(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def clear_cache(artifact_dir: Path):
    shutil.rmtree(artifact_dir, ignore_errors=True)


def main():
    args = parse_args()

    payload_path = Path(args.payload).expanduser().resolve()
    artifact_dir = Path(args.artifact_dir).expanduser().resolve()

    if not payload_path.exists():
        raise FileNotFoundError(f'Payload file not found: {payload_path}')

    os.environ['JUG_LCA_ARTIFACTS_DIR'] = str(artifact_dir)

    if args.with_logging:
        os.environ['LOG_DIR_BASE'] = str(
            Path(args.log_dir_base).expanduser().resolve()
        )
        from jugs_chassis.logging.config import configure_logging

        configure_logging()

    if args.cold:
        clear_cache(artifact_dir)

    payload = load_payload(payload_path)
    computation_result = EmissionsApplicationService.compute_emissions(payload)

    print(
        json.dumps(
            {
                'request_hash': computation_result.request_hash,
                'cache_hit': computation_result.cache_hit,
                'emissions_data': computation_result.emissions_data,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == '__main__':
    main()
