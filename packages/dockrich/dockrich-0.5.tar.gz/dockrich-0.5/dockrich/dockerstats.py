import subprocess
import json
from time import sleep
from rich.live import Live
from rich.text import Text

class Response:
    def __init__(self, data: dict):
        self.BlockIO = data.get("BlockIO")  # Set to a default or computed value
        self.CPUUsage = data.get("CPUPerc")
        self.MemoryUsage = data.get("MemUsage")
        self.NetIO = data.get("NetIO")
        self.Container = data.get("Name")
        self.PIDs = data.get("PIDs")

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"

class Response:
    def __init__(self, data: dict):
        self.BlockIO = data.get("BlockIO")  # Set to a default or computed value
        self.CPUUsage = data.get("CPUPerc")
        self.MemoryUsage = data.get("MemUsage")
        self.NetIO = data.get("NetIO")
        self.Container = data.get("Name")
        self.PIDs = data.get("PIDs")

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"

class Dockerstats:
    def __init__(self, containerid_or_name: str):
        self.containerid_or_name = containerid_or_name

    def getstats(self) -> Response:
        docker_command = [
            "docker", "stats", "--no-stream", "--format", '{{json .}}', self.containerid_or_name
        ]
        try:
            output = subprocess.run(
                docker_command, capture_output=True, check=True, text=True
            )
            value = json.loads(output.stdout)  # The output is already in JSON format
            return Response(value)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr.strip()}")

    def getlivestatus(self):
        def get_docker_stats():
            result = subprocess.run(
                ["docker", "stats", "--no-stream", "--format", "{{json .}}", self.containerid_or_name],
                capture_output=True,
                text=True
            )
            return json.loads(result.stdout)
        
        with Live(refresh_per_second=1) as live:
            while True:
                stats = get_docker_stats()
                text = Text(f"Container: {stats['Name']}\n"
                            f"CPU Usage: {stats['CPUPerc']}\n"
                            f"Memory Usage: {stats['MemUsage']}\n"
                            f"Net I/O: {stats['NetIO']}\n"
                            f"Block I/O: {stats['BlockIO']}\n"
                            f"PIDs: {stats['PIDs']}", style="bold magenta")
                live.update(text)
                sleep(1)
