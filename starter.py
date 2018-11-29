#!/usr/bin/env python

import os
from kubernetes import client, config, watch

def main():
    ns = os.getenv("K8S_NAMESPACE")
    if ns is None:
        ns = ""
    config.load_kube_config()
    api = client.CoreV1Api()
    pvcs = api.list_namespaced_persistent_volume_claim(
      namespace=ns, watch=False)
    
    print("---- PVCs ---")
    print("%-16s\t%-40s\t%-6s" % ("Name", "Volume", "Size"))
    for pvc in pvcs.items:
        print("%-16s\t%-40s\t%-6s" %
              (pvc.metadata.name, pvc.spec.volume_name,    
               pvc.spec.resources.requests['storage']))

if __name__ == '__main__':
    main()