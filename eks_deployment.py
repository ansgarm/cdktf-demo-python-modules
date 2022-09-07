from constructs import Construct


class EksDeployment(Construct):
    def __init__(self, scope, id, deployment_name=None, replicas=1, container=None, container_port=80):
        '''
        :param deployment_name: Name of the deployment
        :param replicas: Number of replicated pods
        :param container: Name of the container image
        :param container_port: Port exposed on the running container. Defaults to 80
        '''
        super().__init__(scope, id)

        # todo: create required constructs for a Kubernetes deployment
        # within e.g. a shared EKS cluster
