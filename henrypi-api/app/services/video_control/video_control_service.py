import logging
import re
from typing import Optional, List

from app.utils.procs import run_subprocess

logger = logging.getLogger(__name__)


class Resolution(object):

    def __init__(self, width: str, height: str):
        self._width = int(width)
        self._height = int(height)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def pixels(self) -> int:
        return self._width * self._height

    def __str__(self):
        return f'{self.width}x{self.height}'

    def to_json(self) -> dict:
        return {
            'width': self.width,
            'height': self.height,
            'pixels': self.pixels,
            'res': str(self),
        }


class VideoDevice(object):

    def __init__(self,
                 device: str,
                 mjpeg_id: int,
                 resolutions: List[Resolution]):
        self.device: str = device
        self.mjpeg_id: int = mjpeg_id
        self.resolutions: List[Resolution] = resolutions

    def __str__(self) -> str:
        res = [str(res) for res in self.resolutions]
        return f'device={self.device} mjpeg_id={self.mjpeg_id} resolutions={res}'

    def to_json(self) -> dict:
        return {
            'device': self.device,
            'mjpeg_id': self.mjpeg_id,
            'resolutions': [x.to_json() for x in self.resolutions]
        }


class VideoControlService(object):
    _singleton = None

    @staticmethod
    def get_instance():
        if VideoControlService._singleton is None:
            VideoControlService._singleton = VideoControlService()

        return VideoControlService._singleton

    def __init__(self):
        self._devices: List[VideoDevice] = []

    def _query_devices(self) -> List[VideoDevice]:
        out: List[VideoDevice] = []

        devices = self._get_video_devices()

        for dev in devices:
            mjpeg_id = self._get_device_mjpeg_id(dev)

            if mjpeg_id is None:
                continue

            resolutions = self._get_resolutions(dev, mjpeg_id)

            if resolutions is None:
                continue

            out.append(VideoDevice(
                device=dev,
                mjpeg_id=mjpeg_id,
                resolutions=resolutions,
            ))

        return out

    @staticmethod
    def _get_video_devices() -> Optional[List[str]]:
        cmd: [str] = [
            'v4l2-ctl',
            '--list-devices'
        ]

        run = run_subprocess(cmd)

        pattern = re.compile('/dev/video[0-9]+')

        devices: [str] = []
        for line in run.stdout.splitlines():
            found = pattern.findall(line)
            if found:
                devices.append(*found)

        logger.debug(f'devices found: {devices}')

        return devices

    @staticmethod
    def _get_device_mjpeg_id(dev: str) -> Optional[int]:
        cmd: [str] = [
            'v4l2-ctl',
            '-d', dev,
            '--list-formats'
        ]

        run = run_subprocess(cmd)

        pattern = re.compile("\[([0-9]+)]: 'MJPG'")

        for line in run.stdout.splitlines():
            found = pattern.findall(line)
            if found:
                logger.debug(f'found {found}')
                return found[0]

        return None

    @staticmethod
    def _get_resolutions(dev: str, mjpeg_id: int) -> Optional[List[Resolution]]:
        cmd: [str] = [
            'v4l2-ctl',
            '-d', dev,
            '--list-framesizes', mjpeg_id
        ]

        run = run_subprocess(cmd)

        pattern = re.compile("Size: Discrete ([0-9]+)x([0-9]+)")

        resolutions: [Resolution] = []
        for line in run.stdout.splitlines():
            found = pattern.findall(line)
            if found:
                logger.debug(f'found {found}')
                width = found[0][0]
                height = found[0][1]

                resolutions.append(Resolution(width, height))

        return resolutions

    def shutdown_all(self):
        cmd: [str] = [
            'killall', 'mjpg_streamer'
        ]

        run_subprocess(cmd, False)

        self._devices.clear()

    def auto_start_all(self):
        self.shutdown_all()

        devs = self._query_devices()

        inputs: List[str] = self._generate_input_args_for_cmd(devs)

        outputs: List[str] = [
            '-o', f'output_http.so --port 9000 --www /usr/local/share/mjpg-streamer/www',
        ]

        logger.info(f'Starting all devices...')

        cmd: [str] = [
            '/usr/local/bin/mjpg_streamer',
            '--background',
            *inputs,
            *outputs
        ]

        run = run_subprocess(cmd)

        pattern = re.compile('background \((\d+)\)')

        logger.info(f'run {run}')

        found = pattern.findall(run.stderr)
        logger.info(f'Started video server on proc={found}')

        self._devices = devs

    @staticmethod
    def _generate_input_args_for_cmd(devs: List[VideoDevice]) -> List[str]:
        inputs: List[str] = []
        for dev in devs:
            max_res = max(dev.resolutions, key=lambda res: res.pixels)

            inputs.append('-i')
            inputs.append(
                f'input_uvc.so --device {dev.device} --fps 100 --resolution {str(max_res)}',
            )

        return inputs

    def get_devices(self) -> List[VideoDevice]:
        return self._devices

