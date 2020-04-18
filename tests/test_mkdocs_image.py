import subprocess
import docker
from time import sleep

# This path will be replaced with actual docs path by users
PWDIR_VOL = {"/home/docker/workspace/mkdocs_docker/tests/test_resources/": {"bind": "/shared_dir"}}

def test_produce(test_name):
    client = docker.from_env()
    ports = {'8000/tcp': 8000}
    cnt = client.containers.run("mkdocs_image", "produce", name="mkdocs_container", remove=True, volumes=PWDIR_VOL, ports=ports, detach=True)
    assert "Producing compressed static files - /shared_dir/site.tar.gz" in str(cnt.logs())
    cnt.kill()

def test_serve(test_name, call_api):
    try:
        resp, resp_code = call_api(url="http://mkdocs:8000")
        assert resp_code == 200
        assert "This is a test page" in str(resp)
    except Exception as err:
        print(err)
        assert False

def test_run(test_name, call_api):
    try:
        resp, resp_code = call_api(url="http://mkdocs:8000")
        assert resp_code == 200
        assert "This is a test page" in str(resp)
    except Exception as err:
        print(err)
        assert False
