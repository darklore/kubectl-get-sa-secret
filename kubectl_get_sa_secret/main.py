import subprocess

import click


@click.command()
@click.option(
    "--namespace",
    "-n",
    "namespace",
    help="If present, the namespace scope for this CLI request",
)
@click.option(
    "--service-account",
    "-a",
    "service_account",
    required=True,
    help="Service Account name of secret you want to get",
)
def main(namespace: str, service_account: str, index: int = 0):
    cmd = f"kubectl get serviceaccount {service_account}"
    if namespace is not None and len(namespace) > 0:
        cmd += f' -n "{namespace}"'
    cmd += f" -o jsonpath='{{.secrets[{index}].name}}'"

    ret = subprocess.run(cmd, capture_output=True, shell=True, check=True)
    secret = ret.stdout.decode("utf-8")

    cmd = f"kubectl get secret {secret}"
    if namespace is not None and len(namespace) > 0:
        cmd += f' -n "{namespace}"'
    cmd += " -o jsonpath='{.data.token}'"

    ret = subprocess.run(cmd, capture_output=True, shell=True, check=True)
    token = ret.stdout.decode("utf-8")
    print(token, end="")

    # cmd = "kubectl get secrets "

    # if namespace is not None and len(namespace) > 0:
    #     cmd += f'-n "{namespace}" '

    # cmd += f"-o jsonpath=\"{{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='{service_account}')].data.token}}\""

    # # print(cmd)
    # ret = subprocess.run(cmd, capture_output=True, shell=True, check=True)
    # token = ret.stdout.decode("utf-8")
    # print(token, end="")


if __name__ == "__main__":
    main()
