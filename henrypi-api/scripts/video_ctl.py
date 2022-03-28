import logging
import re
import subprocess
from typing import Optional, List

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    )

logger = logging.getLogger(__name__)


def main():
    start_video_devices()


def start_video_devices():
    devices = get_video_devices()

    port = 9000
    for dev in devices:
        mjpeg_id = get_device_mjpeg_id(dev)

        if mjpeg_id is None:
            continue

        logger.info(f'dev:{dev} mjpeg_id:{mjpeg_id}')

        res = get_resolutions(dev, mjpeg_id)

        max_res = max_resolutions(res)

        logger.info(f'dev:{dev} mjpeg_id:{mjpeg_id} max:{max_res}')

        start_video_service(dev, max_res, port)

        port += 1


def _run_subprocess(cmd: [str]) -> Optional[subprocess.CompletedProcess]:
    try:
        logger.info(f'running cmd: {cmd}')
        run = subprocess.run(cmd, capture_output=True, text=True)
        logger.debug(f'running cmd finished: {run}')
    except FileNotFoundError as ex:
        logger.error(f'{ex}')
        return None

    if run.returncode:
        logger.error(f'Failed to run: {cmd}')
        logger.error(f'[stdout] {run.stdout}')
        logger.error(f'[stderr] {run.stderr}')
        return None

    logger.debug(f'[stdout]\n{run.stdout}')

    return run


def get_video_devices() -> Optional[List[str]]:
    cmd: [str] = [
        'v4l2-ctl',
        '--list-devices'
    ]

    run = _run_subprocess(cmd)

    pattern = re.compile('/dev/video[0-9]+')

    devices: [str] = []
    for line in run.stdout.splitlines():
        found = pattern.findall(line)
        if found:
            devices.append(*found)

    logger.debug(f'devices found: {devices}')

    return devices


def get_device_mjpeg_id(dev: str) -> Optional[int]:
    cmd: [str] = [
        'v4l2-ctl',
        '-d', dev,
        '--list-formats'
    ]

    run = _run_subprocess(cmd)

    pattern = re.compile("\[([0-9]+)]: 'MJPG'")

    for line in run.stdout.splitlines():
        found = pattern.findall(line)
        if found:
            logger.debug(f'found {found}')
            return found[0]

    return None


def get_resolutions(dev: str, mjpeg_id: int) -> Optional[List[dict]]:
    cmd: [str] = [
        'v4l2-ctl',
        '-d', dev,
        '--list-framesizes', mjpeg_id
    ]

    run = _run_subprocess(cmd)

    pattern = re.compile("Size: Discrete ([0-9]+)x([0-9]+)")

    resolutions: [dict] = []
    for line in run.stdout.splitlines():
        found = pattern.findall(line)
        if found:
            logger.debug(f'found {found}')
            width = int(found[0][0])
            height = int(found[0][1])

            resolutions.append({
                'width': width,
                'height': height,
                'pixels': width * height,
            })

    return resolutions


def max_resolutions(resolutions: List[dict]) -> str:
    max_obj = max(resolutions, key=lambda x: x['pixels'])
    return f"{max_obj['width']}x{max_obj['height']}"


def start_video_service(dev: str, resolution: str, port: str):
    cmd: [str] = [
        '/usr/local/bin/mjpg_streamer',
        '-i', f'input_uvc.so --device {dev} --fps 100 --resolution {resolution}',
        '-o', f'output_http.so --port {port} --www /usr/local/share/mjpg-streamer/www',
        '--background',
    ]

    run = _run_subprocess(cmd)

    logger.info(f'run {run}')
    logger.info(f'[stdout] {run.stdout}')
    logger.info(f'[stderr] {run.stderr}')


if __name__ == '__main__':
    main()
