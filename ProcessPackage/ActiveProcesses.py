import os
from .Process import Process


class ActiveProcesses:
    __LINUX_VIRTUAL_FILESYSTEM = '/proc'
    __NULL_BYTES = '\x00'

    def __init__(self, values: list[Process]):
        self.values = values

    @staticmethod
    def read() -> 'ActiveProcesses':
        process_list = []

        for pid in os.listdir(ActiveProcesses.__LINUX_VIRTUAL_FILESYSTEM):
            if pid.isdigit():
                try:
                    with open(f"{ActiveProcesses.__LINUX_VIRTUAL_FILESYSTEM}/{pid}/comm", "r") as cmdline_file:
                        cmdline = cmdline_file.read().replace(ActiveProcesses.__NULL_BYTES, ' ').strip()
                        process_list.append(Process(pid, cmdline))
                except IOError:
                    continue

        return ActiveProcesses(process_list)
