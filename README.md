# XOR Image Encryption & Decryption Tool

This Python script allows you to encrypt and decrypt images using a simple XOR-based algorithm.
Because XOR is a reversible operation (A XOR B XOR B = A), the same function is used for both encryption and decryption, making this method extremely easy to use.
<img src="./encrypted_image.png">

The script takes an input image, applies an XOR operation to each pixel’s RGB values using a secret integer key, and outputs a processed image. Running the process again with the same key restores the original image.

### How It Works

Each pixel in the image is represented by three values: Red (R), Green (G), Blue (B)

The script applies:

new_value = original_value XOR SECRET_KEY


XOR is symmetric and reversible, so:

decrypted_value = encrypted_value XOR SECRET_KEY


Therefore, encrypting and decrypting use the same function.

### Features

- Encrypt any image using a secret integer key
- Decrypt the image back to its original state
- Uses Pillow (PIL) for image processing
- Works on PNG, JPG, BMP, and more
- One function handles both encryption and decryption

### Requirements

You must have Python 3.x installed, along with Pillow
  ``` 
  pip install pillow
  ```
### How to Use
1. Place your image in the same folder as the script.

Example:

original_image.png

2. Set your secret integer key

Inside the script:

SECRET_KEY = 155


You can change this to any integer 0–255.

3. Run the script

It performs:

Encryption
  ```
        xor_encrypt_decrypt_image("original_image.png", "encrypted_image.png", SECRET_KEY)
  ```
Decryption
  ```
    xor_encrypt_decrypt_image("encrypted_image.png", "decrypted_image.png", SECRET_KEY)
  ```
4. Output Files

encrypted_image.png — scrambled and unreadable

decrypted_image.png — restored to original

### Example Directory Structure
        /project
        │
        ├── xor_image_cipher.py
        ├── original_image.png
        ├── encrypted_image.png (created after running)
        └── decrypted_image.png (created after running)

### Important Notes

The same key MUST be used for both encryption and decryption.

If the key is lost, the image cannot be recovered.

Very large images may take longer to process since every pixel is modified.
