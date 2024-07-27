import platform
import importlib.metadata
from dataclasses import dataclass
from .src.provider.aws.aws_provider import AWSCloud
from .src.provider.azure.azure_provider import  AzureCloud
from .src.tools.print.console import Console
from .src.tools.format.color_text import AnsiColors as color
# Get the Python version
python_version = platform.python_version()

@dataclass
class Service():
    console = Console()

    def info(self):
        try:
            version = importlib.metadata.version('icloudservice')
        except importlib.metadata.PackageNotFoundError:
            version = 'unknown'
        # Get class name
        service_name = 'Cloud integration services for AWS and AZURE'
        log_message = (
        f"{color.HEADER}Version library:{color.WARNING}{version} \n"
        f"{color.HEADER}Name:{color.WARNING}icloudservice \n"
        f"{color.HEADER}Description:{color.WARNING}{service_name} \n"
        f"{color.HEADER}Python Version:{color.WARNING}{python_version} \n"
        )
        self.console.write(log_message)

@dataclass
class Provider():
    console = Console()

    def AWS(self,access_key:str,secret_key:str):
        """
        Initializes an AWS Cloud client with the provided access key and secret key.

        Args:
            access_key (str): AWS access key ID.
            secret_key (str): AWS secret access key.

        Returns:
            AWSCloud: An instance of the AWSCloud class.
        """
        return AWSCloud(access_key,secret_key)
    
    def AZURE(self,subscription_id):
        """
        Initializes an Azure Cloud client with the provided subscription ID.

        Args:
            subscription_id: Azure subscription ID.

        Returns:
            AzureCloud: An instance of the AzureCloud class.
        """
        return AzureCloud(subscription_id)