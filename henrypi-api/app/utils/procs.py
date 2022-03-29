import logging
import subprocess
from typing import Optional

logger = logging.getLogger(__name__)


def run_subprocess(cmd: [str], inspect_run: bool = True) -> Optional[subprocess.CompletedProcess]:
    try:
        logger.info(f'running cmd: {cmd}')
        run = subprocess.run(cmd, capture_output=True, text=True)
        logger.debug(f'running cmd finished: {run}')
    except FileNotFoundError as ex:
        logger.error(f'{ex}')
        return None

    if inspect_run:
        if run.returncode:
            logger.error(f'Failed to run: {cmd}')
            logger.error(f'[stdout] {run.stdout}')
            logger.error(f'[stderr] {run.stderr}')
            return None
        else:
            logger.debug(f'[stdout]\n{run.stdout}')

    return run
