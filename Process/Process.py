class Process:
    def __init__(self, pid: str, name: str):
        self.pid = pid
        self.name = name

    def __str__(self) -> str:
        return f'Process(pid={self.pid}, name={self.name})'
