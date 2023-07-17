import zlib

def compress_file(input_path, output_path):
    with open(input_path, 'rb') as file_in:
        data = file_in.read()
        compressed_data = zlib.compress(data)

    with open(output_path, 'wb') as file_out:
        file_out.write(compressed_data)

def decompress_file(input_path, output_path):
    with open(input_path, 'rb') as file_in:
        compressed_data = file_in.read()
        decompressed_data = zlib.decompress(compressed_data)

    with open(output_path, 'wb') as file_out:
        file_out.write(decompressed_data)

# Prompt for compression or decompression
action = input("Choose an action (compress/decompress): ")

if action.lower() == "compress":
    file_path = input("Enter the path of the file to compress: ")
    output_path = f"{file_path}.compressed"

    # Compress the file
    compress_file(file_path, output_path)
    print(f"File compressed and saved as: {output_path}")

elif action.lower() == "decompress":
    file_path = input("Enter the path of the file to decompress: ")
    output_path = input("Enter the path to save the decompressed file: ")

    # Decompress the file
    decompress_file(file_path, output_path)
    print(f"File decompressed and saved as: {output_path}")

else:
    print("Invalid action. Please choose either 'compress' or 'decompress'.")
