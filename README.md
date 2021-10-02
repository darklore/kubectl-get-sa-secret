# kubectl-get-sa-secret

## Prerequisites
`kubectl` command is already installed.

## Install
```
$ pipx install git+https://github.com/darklore/kubectl-get-sa-secret
```

## Usage
```
$ kubectl get-sa-secret -n kubernetes-dashboard -a kubernetes-dashboard-admin-user | base64 --decode
```


```
Usage: kubectl-get_sa_secret [OPTIONS]

Options:
  -n, --namespace TEXT        If present, the namespace scope for this CLI
                              request
  -a, --service-account TEXT  Service Account name of secret you want to get
                              [required]
  --help                      Show this message and exit.
```
