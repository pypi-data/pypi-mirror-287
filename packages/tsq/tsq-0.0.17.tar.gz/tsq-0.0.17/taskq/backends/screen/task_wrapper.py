import os
import json
from typing import Optional, Mapping, Any


try:
    SCREENDIR = os.environ['SCREENDIR']
except KeyError as e:
    raise ValueError('SCREENDIR not set.') from e


class Wrapper:
    def __init__(
        self, task_id=None, slots=1, gpus=0,
        command=None, additional_info: Optional[Mapping[str, Any]] = None,
    ):
        super().__init__()
        self.info = {
            **(additional_info or {}),
            'task_id': task_id or self._new_task_id(),
            'slots': slots,
            'gpus': gpus,
            'command': command,
            'status': 'queued',
        }

    def _new_task_id(self):
        files = os.listdir(SCREENDIR)
        jobs = [int(f.split('.')[0]) for f in files if f.startswith('tq.')]
        if not jobs:
            return 0
        return max(jobs) + 1

    def _update_info_file(self, info):
        path = f'{SCREENDIR}/tq.{self.info["task_id"]}'
        try:
            with open(path, 'r', encoding='utf-8') as f:
                old_info = json.load(f)
        except FileNotFoundError:
            old_info = {}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(
                {**old_info, **info}, f,
                indent=4, sort_keys=False, ensure_ascii=False)
