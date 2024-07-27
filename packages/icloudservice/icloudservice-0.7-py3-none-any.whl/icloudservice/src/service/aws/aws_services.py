import json
import boto3
import time
from icloudservice.src.tools.format.table_formatter import ITableData
from icloudservice.src.tools.progress.progress import ProgressIndicator
from icloudservice.src.tools.print.console import Console
from icloudservice.src.tools.util import  FileUtils as util
from icloudservice.src.tools.format.color_text import AnsiColors as color
class AWSService:
    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key

    def create_client(self, service_name: str):
        return boto3.client(
            service_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

class S3Service():
    def __init__(self, aws_service: AWSService, bucket_name: str):
        self.client = aws_service.create_client('s3')
        self.bucket_name = bucket_name
        self.console = Console()

    def upload(self, local_path: str, remote_path: str, use_local_filename: bool = True):
        local_file_name = util.get_file_name(local_path)
        # Check if remote_path is a directory and whether to use the local file name
        if remote_path.endswith('/') and use_local_filename:
            # If remote_path is a directory, append the local file name to it
            remote_path = util.get_path(remote_path, local_file_name)
        with ProgressIndicator(message="Uploading file") as progress:
            try:
                self.client.upload_file(local_path, self.bucket_name, remote_path)
            except Exception as e:
                progress.stop(final_message=f"Upload failed: {str(e)}", final_message_color=color.FAIL)

    def download(self, remote_path: str, local_path: str = None):
        if local_path is None:
            local_path = util.get_local_path_default(remote_path)
        with ProgressIndicator(message="Downloading file") as progress:
            try:
                self.client.download_file(self.bucket_name, remote_path, local_path)
            except Exception as e:
                progress.stop(final_message=f"Download failed: {str(e)}", final_message_color=color.FAIL)

    def list_files(self, directory: str,include_directories: bool = False) -> ITableData:
        """
        Lists objects in a specified directory of the S3 bucket and collects relevant details.

        Args:
            directory (str): The directory prefix to list objects from.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing details of each object.
        """
        with ProgressIndicator(message="Waiting for listing objects...") as progress:
            progress.start()
            
            # Initialize the list to store object details
            s3list_objects = []

            # Retrieve the list of objects
            response = self.client.list_objects_v2(Bucket=self.bucket_name, Prefix=directory)
            
            # Check if 'Contents' is in the response
            objects = response.get('Contents', [])
            folders = set()
            directory_prefix_length = len(directory)
            # Process each object
            for obj in objects:
                key = obj.get('Key')
                if key.endswith('/') and include_directories and len(key) > directory_prefix_length:
                    if key[directory_prefix_length:].count('/') == 1:
                        folders.add(key)
                else:
                    # Add the object details to the list
                    if len(key) > directory_prefix_length and key[directory_prefix_length] != '/':
                        # Ensure that the object is directly in the directory and not in a subdirectory
                        # Get the position of the next '/' after the directory prefix
                        next_slash_index = key.find('/', directory_prefix_length)
                        if next_slash_index == -1:
                            
                            obj_details = {
                                'Key': util.get_file_name(key),
                                'Type':util.get_file_extension(key),
                                'Size': util.format_size(obj.get('Size')) if obj.get('Size') is not None else 'Unknown',
                                'LastModified': obj.get('LastModified')
                            }
                            s3list_objects.append(obj_details)
            
            #Add folder details to the list
            for folder in folders:
                folder_details = {
                    'Key': folder,
                    'Type':'folder',
                    'Size': None,                          # Folders don't have a size
                    'LastModified': None
                }
                s3list_objects.append(folder_details)
            
        return ITableData(s3list_objects)

    def list_buckets(self):
        response = self.client.list_buckets()
        return [bucket['Name'] for bucket in response.get('Buckets', [])]

class LambdaService:
    def __init__(self, aws_service: AWSService):
        self.client = aws_service.create_client('lambda')

    def invoke(self, function_name: str, payload: dict):
        response = self.client.invoke(FunctionName=function_name, Payload=json.dumps(payload))
        return response['Payload'].read().decode()

class EC2Service:
    def __init__(self, aws_service: AWSService):
        self.client = aws_service.create_client('ec2')
        self.console = Console()

    def start_instance(self, instance_id: str) -> ITableData:
        progress = ProgressIndicator(message="Waiting for instance to start")
        progress.start()
        response = self.client.start_instances(InstanceIds=[instance_id])

        start_info = response['StartingInstances'][0]
        instance_id = start_info['InstanceId']
        current_state = start_info['CurrentState']['Name']
        previous_state = start_info['PreviousState']['Name']

        start_info_dict = []
        start_info_dict.append({
            "Instance ID": instance_id,
            "Current State": current_state,
            "Previous State": previous_state
        })

        print(ITableData(start_info_dict))

        while True:
            instance_description = self.client.describe_instances(InstanceIds=[instance_id])
            instance = instance_description['Reservations'][0]['Instances'][0]
            instance_state = instance['State']['Name']

            if instance_state == 'running':
                instance_dns = instance.get('PublicDnsName', 'No DNS available')
                instance_name = self._get_instance_name(instance)
                instance_details = []
                instance_details.append({
                    "Instance ID": instance_id,
                    "State": instance_state,
                    "Name": instance_name,
                    "DNS": instance_dns
                })
                progress.stop(f"\nInstance {instance_id} is now fully running!")
                return ITableData(instance_details)
            self.console.info(f"\nInstance {instance_id} is {instance_state}. Waiting for it to be fully running...")
            time.sleep(10)
        
        
    def _get_instance_name(self, instance):
        # Buscar el nombre en las etiquetas
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                return tag['Value']
        return 'No Name Tag'
    
    def stop_instance(self, instance_id: str) ->ITableData:
        response = self.client.stop_instances(InstanceIds=[instance_id])
        instance_init = []

        for instance in response['StoppingInstances']:
            instance_data = {
                "Instance ID": instance['InstanceId'],
                "Current State": instance['CurrentState']['Name'],
                "Previous State": instance['PreviousState']['Name']
            }
            instance_init.append(instance_data)
        print(ITableData(instance_init))
        instance_stop = []
        progress = ProgressIndicator(message="Waiting for instance to stop")
        progress.start()
        while True:
            instance_description = self.client.describe_instances(InstanceIds=[instance_id])
            instance = instance_description['Reservations'][0]['Instances'][0]
            instance_state = instance['State']['Name']

            if instance_state == 'stopped':
                instance_stop.append({
                    "Instance ID": instance_id,
                    "State": instance_state,
                    "Name": self._get_instance_name(instance),
                    "DNS": instance.get('PublicDnsName', 'No DNS available')
                })
                break
            time.sleep(10)
        progress.stop(f'Instance {instance_id} is now fully stopped!')
        return ITableData(instance_stop)
                
    def describe_instances(self, instance_id: str = None) ->ITableData:
        progress = ProgressIndicator(message="Waiting ") 
        progress.start()
        # Fetch instances
        if instance_id:
            response = self.client.describe_instances(InstanceIds=[instance_id])
        else:
            response = self.client.describe_instances()
        
        
        instances = []
        # find all instances or the enter instance_ids 
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                instance_name = self._get_instance_name(instance)
                instance_dns = instance.get('PublicDnsName', 'No DNS available')
                instance_ip = instance.get('PublicIpAddress', 'No IP available')
                os_info = self.get_instance_os(instance['InstanceId'])
                instances.append({
                    "Instance ID": instance_id,
                    "Name": instance_name,
                    "Status":instance_state,
                    "Public DNS": instance_dns,
                    "Public IP": instance_ip,
                    "Type OS": os_info
                })
        progress.stop('Finished successfully')             
        return ITableData(instances)

    def get_instance_os(self, instance_id):
        response = self.client.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        ami_id = instance['ImageId']
        # Fetch AMI details
        ami_response = self.client.describe_images(ImageIds=[ami_id])
        ami = ami_response['Images'][0]
        # AMI description may contain OS information
        os_description = ami.get('Description', 'No OS information available')
        return os_description
    
    def list_instances(self) -> ITableData:
        return self.describe_instances()

class SQSService:
    def __init__(self, aws_service: AWSService):
        self.client = aws_service.create_client('sqs')

    def send_message(self, queue_url: str, message_body: str):
        self.client.send_message(QueueUrl=queue_url, MessageBody=message_body)

    def receive_message(self, queue_url: str):
        response = self.client.receive_message(QueueUrl=queue_url)
        return response.get('Messages', [])

class SNSService:
    def __init__(self, aws_service: AWSService):
        self.client = aws_service.create_client('sns')

    def publish_message(self, topic_arn: str, message: str):
        self.client.publish(TopicArn=topic_arn, Message=message)

    def list_topics(self):
        response = self.client.list_topics()
        return [topic['TopicArn'] for topic in response.get('Topics', [])]

class AWSCloud(AWSService):
    def __init__(self, access_key: str, secret_key: str):
        super().__init__(access_key, secret_key)

    def S3Service(self, bucket_name: str):
        return S3Service(self, bucket_name)

    def LambdaService(self):
        return LambdaService(self)

    def EC2Service(self):
        return EC2Service(self)

    def SQSService(self):
        return SQSService(self)

    def SNSService(self):
        return SNSService(self)
