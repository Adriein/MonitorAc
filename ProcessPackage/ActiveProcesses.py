import os
from typing import Union
from .Process import Process
from .ProcessNotFound import ProcessNotFound


class ActiveProcesses:
    __LINUX_VIRTUAL_FILESYSTEM = '/proc'
    __NULL_BYTES = '\x00'
    __TIBIA_PROCESS = 'Tibia'

    def __init__(self, values: list[Process]):
        self.values = values

    @staticmethod
    def read() -> 'ActiveProcesses':
        process_list = []

        for pid in os.listdir(ActiveProcesses.__LINUX_VIRTUAL_FILESYSTEM):
            if pid.isdigit():
                try:
                    with open(f"{ActiveProcesses.__LINUX_VIRTUAL_FILESYSTEM}/{pid}/cmdline", "r") as cmdline_file:
                        cmdline = cmdline_file.read().replace(ActiveProcesses.__NULL_BYTES, ' ').strip()

                        process_list.append(Process(pid, cmdline))
                except IOError:
                    continue

        return ActiveProcesses(process_list)

    def get_tibia_process(self) -> Union[Process, ProcessNotFound]:
        for process in self.values:
            if self.__TIBIA_PROCESS in process.name:
                return process

        raise ProcessNotFound(self.__TIBIA_PROCESS)
