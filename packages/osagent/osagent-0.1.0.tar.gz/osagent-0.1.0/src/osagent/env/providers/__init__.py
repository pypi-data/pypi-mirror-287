from osagent.env.providers.base import VMManager, Provider
from osagent.env.providers.vmware.manager import VMwareVMManager
from osagent.env.providers.vmware.provider import VMwareProvider
from osagent.env.providers.aws.manager import AWSVMManager
from osagent.env.providers.aws.provider import AWSProvider
from osagent.env.providers.azure.manager import AzureVMManager
from osagent.env.providers.azure.provider import AzureProvider
from osagent.env.providers.virtualbox.manager import VirtualBoxVMManager
from osagent.env.providers.virtualbox.provider import VirtualBoxProvider
from osagent.env.providers.local.manager import LocalManager
from osagent.env.providers.local.provider import LocalProvider


def create_vm_manager_and_provider(provider_name: str, region: str):
    """
    Factory function to get the Virtual Machine Manager and Provider instances based on the provided provider name.
    """
    provider_name = provider_name.lower().strip()
    if provider_name == "vmware":
        return VMwareVMManager(), VMwareProvider(region)
    elif provider_name == "virtualbox":
        return VirtualBoxVMManager(), VirtualBoxProvider(region)
    elif provider_name in ["aws", "amazon web services"]:
        return AWSVMManager(), AWSProvider(region)
    elif provider_name == "azure":
        return AzureVMManager(), AzureProvider(region)
    elif provider_name == "local":
        return LocalManager(), LocalProvider(region)
    else:
        raise NotImplementedError(f"{provider_name} not implemented!")
