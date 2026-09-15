from service.image_genrate import generate_image

def image_api_call(final_prompt):
     
    if not isinstance(final_prompt, str) or not final_prompt.strip():
        raise ValueError(
            f"Invalid image prompt: {final_prompt!r}"
        )

    
    image_path = generate_image(
        prompt = final_prompt,
        output_path = "wallpaper.jpg",
        width=1920,
        height=1080 
        )
    return image_path
            