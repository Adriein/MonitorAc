from ProcessPackage import ActiveProcesses
from LoggerPackage import Logger


class MonitorAc:
    def __init__(self):
        self.active_processes = ActiveProcesses.read()

    def watch(self) -> None:
        try:
            print('Start monitoring battle eye activity')
            Logger.write_in_disk('Start monitoring battle eye activity')

            while True:
                tibia_process = self.active_processes.get_tibia_process()

                tibia_process.get_child_processes()

                for process in self.active_processes.values:
                    if 'BE' in process.name:
                        Logger.write_in_disk(str(process))

        except KeyboardInterrupt:
            print('Graceful shutdown')
            Logger.write_in_disk('Graceful shutdown')

            raise SystemExit
        except Exception as error:
            print(str(error))
            Logger.write_in_disk(str(error))

            raise SystemExit from error


MonitorAc().watch()
