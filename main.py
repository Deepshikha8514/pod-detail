from kubernetes import client, config
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from kubernetes.config import load_incluster_config


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# config.load_kube_config()
# # # load_incluster_config()
# v1=client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#!/usr/bin/env python3

# import os
# import sys
#
# import yaml
# from kubernetes import client, config
# from openshift.dynamic import DynamicClient
#
# # Check if code is running in OpenShift
# if "OPENSHIFT_BUILD_NAME" in os.environ:
#     config.load_incluster_config()
#     file_namespace = open(
#         "/run/secrets/kubernetes.io/serviceaccount/namespace", "r"
#     )
#     if file_namespace.mode == "r":
#         namespace = file_namespace.read()
#         print("namespace: %s\n" %(namespace))
# else:
#     config.load_kube_config()
#
# # Create a client config
# k8s_config = client.Configuration()
#
# k8s_client = client.api_client.ApiClient(configuration=k8s_config)
# dyn_client = DynamicClient(k8s_client)
#
# v1_projects = dyn_client.resources.get(api_version="project.openshift.io/v1", kind="Project")
#
# project_list = v1_projects.get()
#
# for project in project_list.items:
#     print("Project Name: %s" % (project.metadata.name))
from kubernetes import client, config
load_incluster_config()

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
