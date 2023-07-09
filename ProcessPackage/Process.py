import os


class Process:
    def __init__(self, pid: str, name: str):
        self.pid = pid
        self.name = name

    def __str__(self) -> str:
        return f'Process(pid={self.pid}, name={self.name})'

    def get_child_processes(self) -> list['Process']:
        child_processes = []

        try:
            for entry in os.scandir('/proc'):
                if entry.is_dir() and entry.name.isdigit():
                    child_pid = int(entry.name)
                    stat_file = os.path.join(entry.path, 'stat')

                    with open(stat_file, 'r') as f:
                        stat_data = f.read()

                    stat_fields = stat_data.split()
                    print(stat_fields)
                    parent_process_id = int(stat_fields[4])

                    if parent_process_id == self.pid:
                        print(stat_fields)
                        child_processes.append(Process(str(child_pid), ''))

        except FileNotFoundError:
            pass

        except Exception as exception:
            print(exception)
            raise Exception

        return child_processes
