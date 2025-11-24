from PIL import Image

# --- CONFIGURATION ---
# The secret integer key used for encryption and decryption.
# This key MUST be the same for both operations.
SECRET_KEY = 155 

def xor_encrypt_decrypt_image(input_path, output_path, key):
    """
    Encrypts or decrypts an image using a simple XOR operation 
    on the RGB color components of every pixel.
    
    Since A XOR B XOR B = A, the same function works for both.
    
    Args:
        input_path (str): Path to the image file to process.
        output_path (str): Path where the processed image will be saved.
        key (int): The secret integer key for the XOR operation.
    """
    try:
        # 1. Open the image
        img = Image.open(input_path)
        
        # Ensure the image is in RGB format for consistent processing
        img = img.convert("RGB")
        
        # Get image dimensions
        width, height = img.size
        
        # Create a new image to store the result
        output_img = Image.new("RGB", (width, height))
        
        # 2. Process Pixels
        # Use load() for efficient pixel access
        input_pixels = img.load()
        output_pixels = output_img.load()
        
        print(f"Processing {width}x{height} pixels...")

        # Loop through every pixel
        for x in range(width):
            for y in range(height):
                # Get the original RGB values
                r_orig, g_orig, b_orig = input_pixels[x, y]
                
                # Apply the XOR operation to each component
                r_proc = r_orig ^ key
                g_proc = g_orig ^ key
                b_proc = b_orig ^ key
                
                # Set the processed pixel in the output image
                output_pixels[x, y] = (r_proc, g_proc, b_proc)

        # 3. Save Image
        output_img.save(output_path)
        print(f"Successfully saved processed image to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- EXECUTION EXAMPLE ---

# 1. ENCRYPTION
input_file = "original_image.png"  # Change to your image file
encrypted_file = "encrypted_image.png"

# NOTE: You must have an image named 'original_image.png' in the same directory
print("--- Starting Encryption ---")
xor_encrypt_decrypt_image(input_file, encrypted_file, SECRET_KEY)


# 2. DECRYPTION
decrypted_file = "decrypted_image.png"

# Use the encrypted file as input and apply the SAME function and KEY
print("\n--- Starting Decryption ---")
xor_encrypt_decrypt_image(encrypted_file, decrypted_file, SECRET_KEY)
# The decrypted_image.png should look identical to the original_image.png