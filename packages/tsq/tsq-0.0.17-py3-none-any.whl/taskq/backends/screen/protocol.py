import shlex
import base64

from ..base import register_backend, BackendBase


@register_backend('screen')
class ScreenBackend(BackendBase):
    def __init__(self, name, config):
        super().__init__(name, config)
        socket = self.config.get('socket', 'default')
        self.env.setdefault('SCREENDIR', f'/tmp/screen-{socket}.sock')

    def backend_getset(self, key, value=None):
        pass

    def backend_info(self):
        raise NotImplementedError

    def backend_kill(self, args):
        raise NotImplementedError

    def backend_command(self, command, commit=True):
        raise NotImplementedError

    def job_info(self, ids=None, filters=None):
        raise NotImplementedError

    def full_info(
        self, ids=None, filters=None, extra_func=None, tqdm_disable=False
    ):
        print(self.exec('-ls', check=False))

    def output(self, info, tail, shell=False):
        raise NotImplementedError

    def add(self, command, gpus, slots, commit=True):
        key = base64.b64encode(command.encode()).decode().rstrip('=')
        torun = ['-dmS', key] + shlex.split(command)
        print(self.exec(*torun, commit=commit))

    def kill(self, info, commit=True):
        raise NotImplementedError

    def remove(self, info, commit=True):
        raise NotImplementedError
