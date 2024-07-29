import subprocess
import json
import re

class Response:
    def __init__(self, data: dict):
        self.Comment = data.get("Comment")
        self.CreatedAt = data.get("CreatedAt")
        self.CreatedBy = data.get("CreatedBy")
        self.CreatedSince = data.get("CreatedSince")
        self.Id = data.get("ID")
        self.Size = data.get("Size")
        
    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"

class Dockerhistory:
    def __init__(self, image_name: str):
        self.image_name = image_name

    def getvalues(self):
        docker_command = [
            "docker", "history", "--format", '{{json .}}', self.image_name
        ]
        try:
            output = subprocess.run(
                docker_command, capture_output=True, check=True, text=True
            )
            json_objects = re.findall(r'\{.*?\}', output.stdout)
            responses = [Response(json.loads(obj)) for obj in json_objects]
            return responses
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr.strip()}")

