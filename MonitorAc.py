from ProcessPackage import ActiveProcesses


class MonitorAc:
    def __init__(self):
        self.active_processes = ActiveProcesses.read()

    def start(self) -> None:
        for process in self.active_processes.values:
            print(str(process))


MonitorAc().start()
