import subprocess
import json


class Response:
    def __init__(self, data: dict):
        self.Id = data.get("Id")
        self.Created = data.get("Created")
        self.Path = data.get("Path")
        self.Args = data.get("Args")
        self.State = data.get("State")
        self.Image = data.get("Image")
        self.ResolvConfPath = data.get("ResolvConfPath")
        self.HostnamePath = data.get("HostnamePath")
        self.HostsPath = data.get("HostsPath")
        self.LogPath = data.get("LogPath")
        self.Name = data.get("Name")
        self.RestartCount = data.get("RestartCount")
        self.Driver = data.get("Driver")
        self.Platform = data.get("Platform")
        self.MountLabel = data.get("MountLabel")
        self.ProcessLabel = data.get("ProcessLabel")
        self.AppArmorProfile = data.get("AppArmorProfile")
        self.ExecIDs = data.get("ExecIDs")
        self.HostConfig = data.get("HostConfig")
        self.GraphDriver = data.get("GraphDriver")
        self.SizeRw = data.get("SizeRw")
        self.SizeRootFs = data.get("SizeRootFs")
        self.Mounts = data.get("Mounts")
        self.Config = data.get("Config")
        self.NetworkSettings = data.get("NetworkSettings")

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"


class Dockerinspector:
    def __init__(self, containerid_or_name: str):
        self.containerid_or_name = containerid_or_name

    def getvalues(self) -> Response:
        docker_command = [
            "docker", "inspect", "--size", "--format", '{{json .}}', self.containerid_or_name
        ]
        try:
            output = subprocess.run(
                docker_command, capture_output=True, check=True, text=True
            )
            value = json.loads(output.stdout)  # The output is already in JSON format
            return Response(value)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr.strip()}")
