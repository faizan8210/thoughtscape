import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")


def generate_image(
    prompt: str,
    output_path: str = "generated_image.jpg",
    width: int = 1920,
    height: int = 1080,
):
    """Generate an image using Azure FLUX.2-pro."""

    if not AZURE_ENDPOINT:
        raise ValueError("AZURE_ENDPOINT is missing from .env")

    if not AZURE_API_KEY:
        raise ValueError("AZURE_API_KEY is missing from .env")

    # Remove trailing slash if present
    endpoint = AZURE_ENDPOINT.rstrip("/")

    url = (
        f"{endpoint}"
        "/providers/blackforestlabs/v1/flux-2-pro"
        "?api-version=preview"
    )

    payload = {
        "model": "FLUX.2-pro",
        "prompt": prompt,
        "width": width,
        "height": height,
        "output_format": "jpeg",
        "num_images": 1,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}",
    }

    print("Generating image...")
    print("Endpoint:", endpoint)

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=300,
        )
    except requests.RequestException as e:
        raise RuntimeError(
            f"Could not connect to Azure: {e}"
        )

    # IMPORTANT: show Azure's actual error
    if not response.ok:
        print("\nAzure returned an error!")
        print("Status code:", response.status_code)
        print("Response:", response.text)

        raise RuntimeError(
            f"Azure image generation failed: "
            f"HTTP {response.status_code}"
        )

    result = response.json()

    print("Image generation successful!")

    try:
        data = result.get("data")

        if not data:
            if result.get("stop_reason") == "refusal":
                raise RuntimeError(
                    "Azure refused this image prompt because of its content safety policy."
                )
            raise RuntimeError(f"Azure returned no image data. " f"Stop reason: {result.get('stop_reason')}")
        
        image_data = result["data"][0]
    except (KeyError, IndexError, TypeError):
        print("Unexpected Azure response:")
        print(result)
        raise RuntimeError(
            "Azure response did not contain image data."
        )

    # Base64 response
    if "b64_json" in image_data:

        image_bytes = base64.b64decode(
            image_data["b64_json"]
        )

        with open(output_path, "wb") as file:
            file.write(image_bytes)

    # URL response
    elif "url" in image_data:

        image_url = image_data["url"]

        image_response = requests.get(
            image_url,
            timeout=300,
        )

        if not image_response.ok:
            raise RuntimeError(
                f"Failed to download image: "
                f"HTTP {image_response.status_code}"
            )

        with open(output_path, "wb") as file:
            file.write(image_response.content)

    else:
        print("Unexpected image response:")
        print(result)

        raise RuntimeError(
            "Azure did not return an image URL or base64 image."
        )

    print(f"Image saved to: {output_path}")

    return output_path