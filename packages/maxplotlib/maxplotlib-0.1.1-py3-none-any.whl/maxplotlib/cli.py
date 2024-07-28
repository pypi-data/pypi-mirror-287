import argparse
import base64
import json
import os
import subprocess

def main():
    server_ip = os.getenv('SERVER_IP', 'default_server_ip_here')

    parser = argparse.ArgumentParser(description="CLI tool to make and save plots using an external service.")
    parser.add_argument('prompt', type=str, help='Prompt describing the plot to generate.')
    parser.add_argument('--output', type=str, default='output', help='Output directory to save the image.')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    curl_command = [
        'curl', '-s', '-X', 'POST',
        f'http://{server_ip}:8000/plot/', '-F',
        f'prompt={args.prompt}', '-o', f'{args.output}/response.json'
    ]
    subprocess.run(curl_command, check=True)

    with open(f'{args.output}/response.json', 'r') as file:
        data = json.load(file)
        image_data = data['image']
        image_bytes = base64.b64decode(image_data)
        with open(f'{args.output}/output.png', 'wb') as img_file:
            img_file.write(image_bytes)
    print(f"Image saved in '{args.output}/'")

if __name__ == '__main__':
    main()
