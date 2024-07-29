import argparse
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import mimetypes
from .utils.utils import handle_image_path
import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

class Visionlit:
    def __init__(self, key: str):
        self.key = key
        self.validation_url = "https://refworkers.io/functions/getpremium_api.php?api_key="

    def _is_key_valid(self):
        try:
            response = requests.get(self.validation_url + self.key)
            response.raise_for_status()
            data = response.json()
            reqs = int(data.get('request_nr', 0))
            return data.get('valid', True) if reqs >= 1 else False
        except (requests.RequestException, ValueError) as e:
            return False

    def segment_image(self, image_path: str):
        if not self._is_key_valid():
            raise ValueError("Invalid key. Access denied.")
        url = 'https://api.filparty.com/vision/v0/segmention-masks'
        fields = [('api_key', self.key)]
        fields.append(('option', "0"))

        fields = handle_image_path(fields , image_path)
        if fields == False:
            return (f"File does not exist: {image_path}")
        encoder = MultipartEncoder(fields=fields)
        headers = {'Content-Type': encoder.content_type}


        with requests.Session() as session:
            response = session.post(url, data=encoder, headers=headers, verify=False)

            # Check the response status
        if response.status_code == 200:
            result = response.json()
            if result['success']:
                    # Directory for saving downloaded files
                save_dir = os.path.join('results', os.path.basename(image_path))
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                    # Download each file listed in the response
                for filename in result['filenames']:
                    file_url = f"{result['path']}/{filename}"
                    file_response = requests.get(file_url, stream=True, verify=False)
                    if file_response.status_code == 200:
                        file_path = os.path.join(save_dir, filename)
                        with open(file_path, 'wb') as f:
                            for chunk in file_response.iter_content(chunk_size=8192):
                                if chunk:  # filter out keep-alive new chunks
                                    f.write(chunk)
                    else:
                        print(f"Failed to download {filename}")
                return f"Files downloaded to {save_dir}"
            else:
                raise Exception(
                    f"API responded with an error: {result.get('message', 'No error message provided')}")
        else:
                raise Exception(f"HT Error: {response.status_code}, {response.text}")


    def analyze_image(self, image_path: str):
        if not self._is_key_valid():
            raise ValueError("Invalid key. Access denied.")
        return "Image analysis not implemented yet."

    def list_methods(self):
        methods = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("_")]
        return methods

def main():
    parser = argparse.ArgumentParser(description="Run Visionlit operations.")
    parser.add_argument('key', type=str, help='API key to validate.')
    parser.add_argument('image_path', type=str, help='Path to the image file or directory containing images.')
    parser.add_argument('method', type=str, nargs='?', help='Method to execute on the image.')
    parser.add_argument('--list', action='store_true', help='List available methods and exit.')

    args = parser.parse_args()

    vision = Visionlit(args.key)

    if args.list:
        methods = vision.list_methods()
        print("Available methods:")
        for method in methods:
            print(method)
        return

    if not args.method:
        print("No method provided. Use --list to see available methods.")
        return

    method_to_call = getattr(vision, args.method, None)
    if method_to_call:
        result = method_to_call(args.image_path)
        print(result)
    else:
        return ValueError(f"Method {args.method} not found in Visionlit class.")

if __name__ == "__main__":
    main()
