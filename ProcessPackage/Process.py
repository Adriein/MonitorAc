import os
import re
import traceback


class Process:
    __PROCESS_STATE_REGEX = r'\b[A-Z]\b'

    def __init__(self, pid: str, name: str):
        self.pid = pid
        self.name = name

    def __str__(self) -> str:
        return f'Process(pid={self.pid}, name={self.name})'

    def get_child_processes(self) -> list['Process']:
        child_processes = []

        try:
            print(f'TIBIA PROCESS ID {self.pid}')
            for entry in os.scandir('/proc'):
                if entry.is_dir() and entry.name.isdigit():
                    child_pid = int(entry.name)
                    stat_file = os.path.join(entry.path, 'stat')

                    with open(stat_file, 'r') as f:
                        stat_data = f.read()

                    stat_fields = stat_data.split()

                    ppid_position = None

                    for index, field in enumerate(stat_fields):
                        match = re.search(self.__PROCESS_STATE_REGEX, field)

                        if bool(match):
                            ppid_position = index + 1

                    parent_process_id = int(stat_fields[ppid_position])

                    print(f'Process watched pid {stat_fields[0]} parent pid {parent_process_id}')

                    if parent_process_id == int(self.pid):
                        print(stat_fields)
                        child_processes.append(Process(str(child_pid), ''))

            raise Exception

        except FileNotFoundError:
            pass

        except Exception as exception:
            traceback.print_exc()
            raise Exception

        return child_processes
