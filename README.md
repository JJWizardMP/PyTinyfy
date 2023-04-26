# PyTinyfy

PyTinyfy is a lightweight and easy-to-use Python script that optimizes JPEG and PNG image files to reduce their size and improve page load times. The script uses the TinyPNG API to compress and optimize images without compromising their visual quality. PyTinyfy can also upload the optimized images to a CDN bucket, making them instantly available to your website visitors.

## Compress and Upload Images to DigitalOcean Spaces CDN

This script downloads all JPEG images from a specified directory in a DigitalOcean Space, compresses them using TinyPNG, and uploads the compressed images to the same path on a CDN hosted in the same DigitalOcean Space. The uploaded images are set to public-read ACL.

## Dependencies

The following Python modules are required to run PyTinyfy:

- `boto3` (version 1.18.60 or later): Used to interact with Amazon S3 and upload files to the CDN.
- `dotenv` (version 0.19.1 or later): Used to load environment variables from a `.env` file.
- `Pillow` (version 8.4.0 or later): Used to open and save images in various formats.
- `tinify` (version 1.7.0 or later): Used to compress images with TinyPNG.

You can install all of these modules using pip:

## Prerequisites

Before running this script, you need to:

- Have Python 3.8 or later installed on your machine.
- Have a DigitalOcean Space with a CDN enabled. You also need to know the name of your DigitalOcean Space, the access key, and the secret key.

- Have a TinyPNG API key. You can get one by registering at https://tinypng.com/developers.

## Installation

1. Clone the repository: 
   ```sh
   git clone https://github.com/JJWizardMP/PyTinyfy.git 
   ```
2. Install the required dependencies: 
   ```sh
   pip install -r requirements.txt
    ```

## Usage

To use this script, you need to:

1. Open the script in a text editor.
2. Create an .env file with the variables `REGION`, `ENDPOINT`, `ACCESS_KEY`, `SECRET_KEY`, `BUCKET_NAME`, `TINYPNG_API_KEY` with the appropriate values for your DigitalOcean Space and TinyPNG account.
3. Set the `directory_path` variable to the directory path in your DigitalOcean Space where the JPEG images are stored.
4. Save the script.
5. Open a terminal window and navigate to the directory where the script is saved.
6. Run the script using the following command:

    ```
    python pytinyfy.py
    ```

The script will download all JPEG images from the specified directory in your DigitalOcean Space, compress them using TinyPNG, and upload the compressed images to the same path on the CDN hosted in the same DigitalOcean Space. The uploaded images will be set to public-read ACL.

## Features

- Optimizes JPEG and PNG images using the TinyPNG API
- Customizable compression level and other settings
- Can upload optimized images to a CDN bucket for instant access
- Supports environment variables and a `.env` file for secure API key management
- Easy to integrate into an automated build process or run on-demand

PyTinyfy is ideal for web developers and designers who want to improve the performance of their websites by optimizing the images they use. Whether you're building a new site from scratch or optimizing an existing one, PyTinyfy can help you reduce image file sizes and improve page load times.

## License

This script is licensed under GPL-2.0 License. See LICENSE file for details.
