import boto3
from dotenv import load_dotenv
load_dotenv()

# Set your AWS credentials
aws_access_key_id = os.environ.get('ACCESS_KEY')
aws_secret_access_key = os.environ.get('SECRET_KEY')
aws_region = os.environ.get('REGION')
bucket_name = os.environ.get('BUCKET_NAME')

# Specify the file you want to upload
file_path = 'ramirez/gato-naranja.jpg'

# Create an S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region)

# Upload the file
try:
    response = s3_client.upload_file(file_path, bucket_name, file_path)
    print(f"File uploaded successfully. URL: https://{bucket_name}.s3-{aws_region}.amazonaws.com/{file_path}")
except Exception as e:
    print(f"Error uploading file: {e}")