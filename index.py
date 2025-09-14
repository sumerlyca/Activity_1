from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, top_text="TOP TEXT", bottom_text="BOTTOM TEXT", output_path="meme.png"):
    
    canvas_width = 800
    canvas_height = 600
    
    top_text_height = 80
    bottom_text_height = 80
    
    image_height = canvas_height - top_text_height - bottom_text_height
    
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
    draw = ImageDraw.Draw(canvas)
    
    try:
        top_font = ImageFont.truetype("arial.ttf", 36)
        bottom_font = ImageFont.truetype("arial.ttf", 24) 
    except:
        try:
            top_font = ImageFont.truetype("Arial Bold.ttf", 36)
            bottom_font = ImageFont.truetype("Arial Bold.ttf", 24) 
        except:
            try:
                top_font = ImageFont.truetype("helvetica.ttf", 36)
                bottom_font = ImageFont.truetype("helvetica.ttf", 24) 
            except:
                top_font = ImageFont.load_default()
                bottom_font = ImageFont.load_default()
    
    try:
        main_img = Image.open(image_path)
        
        img_width, img_height = main_img.size
        available_width = canvas_width - 40 
        available_height = image_height - 20 
        
        width_scale = available_width / img_width
        height_scale = available_height / img_height
        scale = min(width_scale, height_scale)
        
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        main_img = main_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
    except Exception as e:
        print(f"Error loading image: {e}")
        new_width = 400
        new_height = 300
        main_img = Image.new('RGB', (new_width, new_height), 'lightgray')
        placeholder_draw = ImageDraw.Draw(main_img)
        placeholder_draw.text((new_width//2-80, new_height//2-10), "IMAGE NOT FOUND", fill='black')
    
    image_x = (canvas_width - new_width) // 2
    image_y = top_text_height + (image_height - new_height) // 2
    
    canvas.paste(main_img, (image_x, image_y))
    
    if top_text:
        top_bbox = draw.textbbox((0, 0), top_text, font=top_font)
        top_width = top_bbox[2] - top_bbox[0]
        top_x = (canvas_width - top_width) // 2
        top_y = (top_text_height - (top_bbox[3] - top_bbox[1])) // 2
        
        outline_width = 2
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    draw.text((top_x + dx, top_y + dy), top_text, fill='black', font=top_font)
        draw.text((top_x, top_y), top_text, fill='white', font=top_font)
    
    if bottom_text:
        bottom_bbox = draw.textbbox((0, 0), bottom_text, font=bottom_font)
        bottom_width = bottom_bbox[2] - bottom_bbox[0]
        bottom_x = (canvas_width - bottom_width) // 2
        bottom_y = canvas_height - bottom_text_height + (bottom_text_height - (bottom_bbox[3] - bottom_bbox[1])) // 2
        
        outline_width = 2
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    draw.text((bottom_x + dx, bottom_y + dy), bottom_text, fill='black', font=bottom_font)
        draw.text((bottom_x, bottom_y), bottom_text, fill='white', font=bottom_font)
    
    # Save the meme
    canvas.save(output_path, 'PNG', quality=95)
    print(f"Meme saved as: {output_path}")
    
    return canvas

def main():
    
    image_path = "image.png" 
    top_text = "POV"
    bottom_text = "Inaantok na kayo sa kaka-higa sa contemporary dance"
    output_filename = "CSELEC3_3A_PerochoSumerlyca_Activity1.png"
 
    # Generate the meme
    try:
        create_meme(image_path, top_text, bottom_text, output_filename)
        print(f"\nSuccess! Your meme has been created as '{output_filename}'!")
        print(f"Top text: '{top_text}'")
        print(f"Bottom text: '{bottom_text}'")
    except Exception as e:
        print(f"Error creating meme: {e}")

if __name__ == "__main__":
    main()