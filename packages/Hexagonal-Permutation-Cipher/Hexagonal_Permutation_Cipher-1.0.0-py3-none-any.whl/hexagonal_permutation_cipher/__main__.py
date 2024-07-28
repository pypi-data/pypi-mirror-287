import argparse
import hashlib
import logging
from hexagonal_permutation_cipher.encryption import encrypt, decrypt
from hexagonal_permutation_cipher.grid import create_hexagonal_grid
from hexagonal_permutation_cipher.visualization import animate_permutation
from hexagonal_permutation_cipher.benchmark import benchmark

def setup_logging():
    """
    Setup logging configuration.
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

def usage_examples():
    """
    Provide usage examples for the tool.
    """
    examples = '''
Usage Examples:
---------------
1. Encrypt a message:
    python -m hexagonal_permutation_cipher encrypt "Hello, World!" "mysecretkey"

2. Decrypt a message:
    python -m hexagonal_permutation_cipher decrypt "ENCRYPTED_BASE64_TEXT" "mysecretkey"

3. Visualize the permutation process:
    python -m hexagonal_permutation_cipher visualize 3 "mysecretkey"

4. Run a benchmark test:
    python -m hexagonal_permutation_cipher benchmark
    '''
    return examples

def parse_arguments():
    """
    Parse command-line arguments with detailed help.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    description = '''
    Hexagonal Permutation Cipher Tool
    ---------------------------------

    ****** THIS IS A HOBBYIST AND ENTHUSIAST PROJECT ******

    This tool implements a unique encryption and decryption algorithm 
    based on hexagonal grid permutations combined with AES encryption.

    The encryption process involves mapping the plaintext into a hexagonal 
    grid, permuting the grid using a key-derived seed, and then applying AES 
    encryption. The decryption process reverses these steps to retrieve the 
    original plaintext.

    URL: https://github.com/00-python/Hexagonal-Permutation-Cipher

    ''' + usage_examples()

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encryption command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt plaintext with a given key")
    encrypt_parser.add_argument("plaintext", help="The plaintext to encrypt")
    encrypt_parser.add_argument("key", help="The encryption key")

    # Decryption command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt ciphertext with a given key")
    decrypt_parser.add_argument("ciphertext", help="The Base64 encoded ciphertext to decrypt")
    decrypt_parser.add_argument("key", help="The decryption key")

    # Visualization command (including 3D option)
    visualize_parser = subparsers.add_parser("visualize", help="Visualize the hexagonal permutation process")
    visualize_parser.add_argument("size", type=int, help="Size of the hexagonal grid")
    visualize_parser.add_argument("key", help="The key used for permutation")
    visualize_parser.add_argument("--3d", action='store_true', help="Visualize in 3D")

    # Benchmark command
    subparsers.add_parser("benchmark", help="Run encryption and decryption benchmarks")

    return parser.parse_args()

def handle_encrypt(plaintext: str, key: str):
    """
    Handle encryption logic.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (str): The encryption key.
    """
    try:
        logging.info("Starting encryption process")
        logging.info(f"Plaintext: {plaintext}")
        encrypted_text = encrypt(plaintext, key)
        logging.info(f"Encrypted text: {encrypted_text}")
        print(f"Encrypted text: {encrypted_text}")
    except Exception as e:
        logging.error(f"Encryption failed: {e}")

def handle_decrypt(ciphertext: str, key: str):
    """
    Handle decryption logic.

    Args:
        ciphertext (str): The Base64 encoded ciphertext to decrypt.
        key (str): The decryption key.
    """
    try:
        logging.info("Starting decryption process")
        logging.info(f"Ciphertext: {ciphertext}")
        decrypted_text = decrypt(ciphertext, key)
        logging.info(f"Decrypted text: {decrypted_text}")
        print(f"Decrypted text: {decrypted_text}")
    except Exception as e:
        logging.error(f"Decryption failed: {e}")

def handle_visualize(size: int, key: str):
    """
    Handle visualization logic for hexagonal permutation.

    Args:
        size (int): Size of the hexagonal grid.
        key (str): The key used for permutation.
    """
    try:
        logging.info("Starting visualization process")
        grid = create_hexagonal_grid(size)
        aes_key = hashlib.sha256(key.encode()).digest()
        animate_permutation(grid, aes_key)
    except Exception as e:
        logging.error(f"Visualization failed: {e}")

def handle_visualize_3d(size: int, key: str):
    """
    Handle 3D visualization logic for hexagonal permutation.

    Args:
        size (int): Size of the hexagonal grid.
        key (str): The key used for permutation.
    """
    try:
        logging.info("Starting 3D visualization process")
        from hexagonal_permutation_cipher.visualization_3d import animate_permutation_3d
        animate_permutation_3d(size=size, key=key)
    except Exception as e:
        logging.error(f"3D Visualization failed: {e}")

def handle_benchmark():
    """
    Handle running benchmarks.
    """
    try:
        logging.info("Starting benchmark process")
        benchmark()
    except Exception as e:
        logging.error(f"Benchmark failed: {e}")

def main():
    """
    Entry point for the hexagonal permutation cipher package.
    """
    setup_logging()
    args = parse_arguments()

    if args.command == "encrypt":
        logging.info("Encrypt command selected")
        handle_encrypt(args.plaintext, args.key)
    elif args.command == "decrypt":
        logging.info("Decrypt command selected")
        handle_decrypt(args.ciphertext, args.key)
    elif args.command == "visualize":
        logging.info("Visualize command selected")
        if args.mode_3d:
            from hexagonal_permutation_cipher.visualization_3d import animate_permutation_3d
            handle_visualize_3d(args.size, args.key)
        else:
            handle_visualize(args.size, args.key)
    elif args.command == "benchmark":
        logging.info("Benchmark command selected")
        handle_benchmark()
    else:
        logging.error(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()