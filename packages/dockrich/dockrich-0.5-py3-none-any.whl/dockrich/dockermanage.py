import subprocess
import json
import re

class Response:
    def __init__(self, data: dict):
        self.Command = data.get("Command")
        self.CreatedAt = data.get("CreatedAt")
        self.Id = data.get("ID")
        self.Image = data.get("Image")
        self.Labels = data.get("Labels")
        self.LocalVolumes = data.get("LocalVolumes")
        self.Mounts = data.get("Mounts")
        self.Names = data.get("Names")
        self.Networks = data.get("Networks")
        self.Ports = data.get("Ports")
        self.RunningFor = data.get("RunningFor")
        self.Size = data.get("Size")
        self.State = data.get("State")
        self.Status = data.get("Status")

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"


class Dockermanage:
    def __init__(self, containerid_or_name: str):
        self.containerid_or_name = containerid_or_name

    def ps(self) -> Response:
        docker_command = [
            "docker", "ps","--format",'{{json .}}',"--filter", f"name={self.containerid_or_name}" 
        ]
        try:
            output = subprocess.run(
                docker_command, capture_output=True, check=True, text=True
            )
            value = json.loads(output.stdout)  # The output is already in JSON format
            return Response(value)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr.strip()}")
