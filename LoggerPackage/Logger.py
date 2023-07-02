from datetime import datetime


class Logger:
    @staticmethod
    def write_in_disk(log: str) -> None:
        current_date = datetime.now().astimezone().strftime("%d %B %Y").replace(' ', '_')
        log_filename = f"{current_date}_battle_eye_activated.txt"

        print(log_filename)

        # with open(log_filename, 'w') as file:
          #  time_stamp = datetime.now().astimezone().strftime("%d %B %Y, %H:%M:%S")
           # file.write(f'[{time_stamp}] {log} \n')
