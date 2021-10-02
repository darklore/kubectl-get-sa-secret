import subprocess

import click


@click.command()
@click.option("--namespace",
              "-n",
              "namespace",
              help="If present, the namespace scope for this CLI request")
@click.option("--service-account",
              "-a",
              "service_account",
              required=True,
              help="Service Account name of secret you want to get")
def main(namespace: str, service_account: str):
    cmd = "kubectl get secrets "

    if namespace is not None and len(namespace) > 0:
        cmd += f"-n \"{namespace}\" "

    cmd += f"-o jsonpath=\"{{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='{service_account}')].data.token}}\""

    # print(cmd)
    ret = subprocess.run(cmd, capture_output=True, shell=True, check=True)
    token = ret.stdout.decode('utf-8')
    print(token, end='')


if __name__ == '__main__':
    main()
