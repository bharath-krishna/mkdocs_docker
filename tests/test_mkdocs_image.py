import subprocess
import docker
from time import sleep
from pathlib import Path


PWDIR_VOL = {str(Path("./").absolute()/"tests"/"test_resources"): {"bind": "/shared_dir"}}

def test_produce(test_name):
    client = docker.from_env()
    ports = {'8000/tcp': 8000}
    cnt = client.containers.run("mkdocs_image", "produce", remove=True, volumes=PWDIR_VOL, ports=ports, detach=True)
    assert "Producing compressed static files - /shared_dir/site.tar.gz" in str(cnt.logs())
    cnt.kill()
