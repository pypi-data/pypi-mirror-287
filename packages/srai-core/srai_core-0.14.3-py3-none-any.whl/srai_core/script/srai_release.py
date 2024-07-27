import asyncio
import json
import os
import sys
from math import e

from srai_core.command_handler_base import CommandHandlerBase
from srai_core.command_handler_subprocess import CommandHandlerSubprocess
from srai_core.script.srai_build import srai_build
from srai_core.script.srai_release_code_public import srai_release_code_public
from srai_core.tools_docker import build_docker, release_docker_local_to_aws


async def srai_release(deployment: dict) -> None:
    await srai_build(deployment)

    for release_target in deployment["list_release_target"]:
        command_handler = CommandHandlerBase.from_dict(release_target["command_handler"])
        release_target_type = release_target["release_target_type"]
        if release_target_type == "release_code_public":
            await srai_release_code_public(command_handler)
        elif release_target_type == "release_docker_local_to_aws":
            await release_docker_local_to_aws(command_handler)
        else:
            print(f"Unknown release_type: {release_target_type}")
            sys.exit(1)


def get_deployment() -> dict:
    if len(sys.argv) == 2:
        path_file_deployment = sys.argv[1]
        with open(path_file_deployment) as file:
            return json.load(file)
    else:
        if os.path.isfile("deployment.json"):
            print("Found default 'deployment.json' file")
            path_file_deployment = "deployment.json"
            with open(path_file_deployment) as file:
                return json.load(file)
        else:
            command_handler = CommandHandlerSubprocess()
            if os.path.isfile("dockerfile"):
                print("Found no deployment file but a dockerfile docker release:")
                asyncio.run(build_docker(command_handler))
                sys.exit(0)
            else:
                print("Found no deployment file and no dockerfile doing default realese:")
                asyncio.run(srai_release_code_public(command_handler))
                sys.exit(0)


def main():
    deployment = get_deployment()
    asyncio.run(srai_release(deployment))


if __name__ == "__main__":
    main()
