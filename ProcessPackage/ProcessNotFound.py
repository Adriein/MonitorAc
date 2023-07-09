class ProcessNotFound(Exception):
    def __init__(self, process_name: str):
        super(ProcessNotFound, self).__init__(f'Process with name: {process_name} not found')
