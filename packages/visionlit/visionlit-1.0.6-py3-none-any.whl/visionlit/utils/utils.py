import shutil
from datetime import datetime
import os
import requests
import mimetypes

def handle_image_path(fields, image_path):
    # Create the 'images' directory if it does not exist
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    if isinstance(image_path, str):
        # Handling a single image path or URL
        image_paths = [image_path]
    else:
        # Assuming it's an iterable of paths or URLs
        image_paths = image_path

    for path in image_paths:
        if path.startswith('http://') or path.startswith('https://'):
            # Handle URL: download and save the image locally with a timestamp
            response = requests.get(path, stream=True)
            if response.status_code == 200:
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                local_filename = os.path.join(images_dir, f'image_{timestamp}.jpg')
                with open(local_filename, 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
                file_path = local_filename
            else:
                continue  # Skip this file if download failed
        else:
            # Handle local file or directory
            if os.path.isdir(path):
                # If it's a directory, process each file in the directory
                for filename in os.listdir(path):
                    full_path = os.path.join(path, filename)
                    if os.path.isfile(full_path):
                        # Process each file in the directory
                        dest_path = os.path.join(images_dir, filename)
                        shutil.copy2(full_path, dest_path)  # Copy to 'images' directory
                        file_path = dest_path
                        file_type, _ = mimetypes.guess_type(file_path)
                        fields.append(('file', (file_path, open(file_path, 'rb'), file_type)))
            elif os.path.exists(path):
                        # It's a single file and it exists
                dest_path = os.path.join(images_dir, os.path.basename(path))
                shutil.copy2(path, dest_path)  # Copy to 'images' directory
                file_path = dest_path
            else:
                return False
        # Add file to fields
        file_type, _ = mimetypes.guess_type(file_path)
        fields.append(('file', (file_path, open(file_path, 'rb'), file_type)))

    return fields