from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf):
    """Convert all images in a folder into a single PDF."""
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("No image files found in the folder.")
        return

    image_files.sort()  # Sort alphabetically
    images = []

    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        img = Image.open(img_path).convert('RGB')  # Convert to RGB for PDF
        images.append(img)

    # Save first image and append others
    first_image = images.pop(0)
    first_image.save(output_pdf, save_all=True, append_images=images)
    print(f"✅ PDF created successfully: {output_pdf}")


if __name__ == "__main__":
    folder = input("Enter folder path containing images: ").strip()
    output = input("Enter output PDF name (e.g., output.pdf): ").strip()
    
    if not output.endswith(".pdf"):
        output += ".pdf"

    images_to_pdf(folder, output)
