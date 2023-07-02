from ProcessPackage import ActiveProcesses
from TablePackage import Table


class MonitorAc:
    def __init__(self):
        self.active_processes = ActiveProcesses.read()

    def start(self) -> None:
        data = [['PID', 'Name']]

        for process in self.active_processes.values:
            data.append([process.pid, process.name])

        Table.create(data).print()


MonitorAc().start()
