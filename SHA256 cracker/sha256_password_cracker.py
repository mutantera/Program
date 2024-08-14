from pwn import *
import sys
import hashlib  # Import hashlib to calculate the SHA-256 hash

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage Error!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

# Store the target hash and initialize variables
target_hash = sys.argv[1]
wordlist_file = "rockyou.txt"
attempt_count = 0

# Start the logging process for brute-forcing the hash
with log.progress("Attempting to match hash: {}!\n".format(target_hash)) as logger:
    # Open the password wordlist file
    with open(wordlist_file, "r", encoding="latin-1") as passwords:
        # Iterate over each password in the list
        for password in passwords:
            # Clean up the password and encode it to 'latin-1'
            password = password.strip("\n").encode('latin-1')
            
            # Compute the SHA-256 hash of the current password using hashlib
            current_hash = hashlib.sha256(password).hexdigest()
            
            # Update the logger with the current attempt details
            logger.status("[{}] {} == {}".format(attempt_count, password.decode('latin-1'), current_hash))
            
            # Check if the current hash matches the target hash
            if current_hash == target_hash:
                # If a match is found, log success and exit
                logger.success("Password found after {} attempts! '{}' hashes to '{}'!".format(attempt_count, password.decode('latin-1'), current_hash))
                exit()
            
            # Increment the attempt count
            attempt_count += 1

# If no match is found, log the failure
logger.failure("No matching password found!")
