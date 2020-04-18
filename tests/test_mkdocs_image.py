import subprocess
import docker
from time import sleep


PWDIR_VOL = {"/tests/test_resources": {"bind": "/shared_dir"}}

def test_produce(test_name):
    client = docker.from_env()
    ports = {'8000/tcp': 8000}
    cnt = client.containers.run("mkdocs_image", "produce", name="mkdocs_container", remove=True, volumes=PWDIR_VOL, ports=ports, detach=True)
    assert "Producing compressed static files - /shared_dir/site.tar.gz" in str(cnt.logs())
    cnt.kill()

# def test_serve(test_name, call_api):
#     client = docker.from_env()
#     ports = {'8000/tcp': 8000}
#     try:
#         cnt = client.containers.run("mkdocs_image", "serve", name="mkdocs_container", remove=True, volumes=PWDIR_VOL, ports=ports, detach=True)
#         if "No such file or directory" in str(cnt.logs()):
#             print("Compressed .tar.gz file not found. Please produce one first using 'produce' command")
#             assert False
#         else:
#             assert "Serving documents using python from compressed docs - /shared_dir/site.tar.gz" in str(cnt.logs())
#             # Wait for a while for container to start
#             sleep(5)
#             resp, resp_code = call_api(url="http://172.17.0.1:8000")
#             assert resp_code == 200
#             assert "This is a test page" in str(resp)
#     except Exception as err:
#         print(err)
#         assert False
#     cnt.kill()

# def test_run(test_name, call_api):
#     client = docker.from_env()
#     ports = {'8000/tcp': 8000}
#     try:
#         cnt = client.containers.run("mkdocs_image", "run", name="mkdocs_container", remove=True, volumes=PWDIR_VOL, ports=ports, detach=True)
#         assert "Running mkdockerize.sh script" in str(cnt.logs())
#         # Wait for a while for container to start
#         sleep(5)
#         resp, resp_code = call_api(url="http://172.17.0.1:8000")
#         assert resp_code == 200
#         assert "This is a test page" in str(resp)
#     except Exception as err:
#         print(err)
#         assert False
#     cnt.kill()
