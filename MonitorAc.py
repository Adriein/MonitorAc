from ProcessPackage import ActiveProcesses
from TablePackage import Table


class MonitorAc:
    def __init__(self):
        self.active_processes = ActiveProcesses.read()

    def start(self) -> None:
        data = [['PID', 'Name']]

        table_data = [
            ["Name", "Age", "Country"],
            ["John", 28, "USA"],
            ["Emily", 32, "Canada"],
            ["Michael", 45, "UK"],
        ]

        for process in self.active_processes.values:
            data.append([process.pid, process.name])

        Table.create(table_data).print()


MonitorAc().start()
