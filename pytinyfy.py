import os
import boto3
import tinify
from dotenv import load_dotenv
load_dotenv()

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client('s3',
                        region_name=os.environ.get('REGION'),
                        aws_access_key_id=os.environ.get('ACCESS_KEY'),
                        aws_secret_access_key=os.environ.get('SECRET_KEY'))

# Set the name of your DigitalOcean Space and directory path.
bucket_name = os.environ.get('BUCKET_NAME')
directory_path = 'ramirez'

# Use the list_objects_v2 method of the client to retrieve all objects in the specified directory.
objects = client.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)

# Set your TinyPNG API key.
tinify.key = os.environ.get('TINYPNG_API_KEY')

try:
    # Loop through the objects and download any JPEG images.
    for obj in objects['Contents']:
        # Check if the object is a JPEG image.
        if obj['Key'].lower().endswith('.jpg') or obj['Key'].lower().endswith('.jpeg'):
            # Create the directories based on the object key's prefix.
            prefix = os.path.dirname(obj['Key'])
            os.makedirs(prefix, exist_ok=True)

            # Download the object to a file with the same name as the object.
            filename = os.path.basename(obj['Key'])
            client.download_file(bucket_name, obj['Key'], os.path.join(prefix, filename))
            print(f"Downloaded {filename} from {bucket_name}/{directory_path} to {prefix}")

            # Compress the image using TinyPNG and overwrite the original file.
            source = tinify.from_file(os.path.join(prefix, filename))
            source.to_file(os.path.join(prefix, filename))
            print(f"Compressed {filename} using TinyPNG")

            # Upload the compressed image to the same path on the CDN.
            cdn_path = obj['Key']
            client.upload_file(os.path.join(prefix, filename), bucket_name, cdn_path)
            print(f"Uploaded {filename} to CDN path {cdn_path}")
except Exception as e:
    print(f"Error request to bucket: {e}")