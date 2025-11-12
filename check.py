import math
import time

# --- Attacker's "Hardware" ---
# Guesses per second for a WPA2 hash
# (Based on real-world benchmarks)
LOW_END_GPU_HASHES_PER_SEC = 150_000
HIGH_END_GPU_HASHES_PER_SEC = 1_100_000

def get_character_set_size(password):
    """Analyzes a password and returns the size of its character set."""
    size = 0
    if any(c.islower() for c in password):
        size += 26  # a-z
    if any(c.isupper() for c in password):
        size += 26  # A-Z
    if any(c.isdigit() for c in password):
        size += 10  # 0-9
    if any(not c.isalnum() for c in password):
        size += 32  # Common special characters
    
    # If the password is very simple (e.g., only numbers),
    # an attacker knows this and will only try numbers.
    # This logic gives a more realistic (and scary) estimate.
    
    if all(c.isdigit() for c in password):
        return 10
    if all(c.islower() for c in password):
        return 26

    # Default to 94 (all printable ASCII) if we're not sure
    if size == 0: 
        return 94
        
    return size

def convert_seconds_to_readable(seconds):
    """Converts a large number of seconds into a human-friendly string."""
    if seconds < 0.001:
        return "Instantly"
    
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f} minutes"
        
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.1f} hours"
        
    days = hours / 24
    if days < 365:
        return f"{days:.1f} days"
        
    years = days / 365
    if years < 1_000_000:
        return f"{years:,.1f} years"
    
    if years < 1_000_000_000:
        return f"{years/1_000_000:,.1f} million years"
        
    return f"{years/1_000_000_000:,.1f} billion years"

def main():
    print("--- WPA2 Password Crack-Time Simulator ---")
    print("This tool demonstrates the risk of offline brute-force attacks.")
    print("\nAttacker 'Hardware' Profiles:")
    print(f" [1] Standard GPU: {LOW_END_GPU_HASHES_PER_SEC:15,d} guesses/sec")
    print(f" [2] High-End GPU: {HIGH_END_GPU_HASHES_PER_SEC:15,d} guesses/sec")
    print("-" * 44)

    try:
        while True:
            password = input("\nEnter a password to test (or 'q' to quit): ")
            if password.lower() == 'q':
                break
            if not password:
                continue

            length = len(password)
            charset_size = get_character_set_size(password)
            
            # Total combinations = (size_of_character_set) ^ (password_length)
            total_combinations = math.pow(charset_size, length)

            print(f"\n  Password Length: {length}")
            print(f"  Character Set Size: {charset_size}")
            print(f"  Total Combinations: {total_combinations:,.0f}")
            print("-" * 44)
            
            # Calculate time
            time_low = total_combinations / LOW_END_GPU_HASHES_PER_SEC
            time_high = total_combinations / HIGH_END_GPU_HASHES_PER_SEC
            
            print(f"  [Standard GPU]: {convert_seconds_to_readable(time_low)}")
            print(f"  [High-End GPU]: {convert_seconds_to_readable(time_high)}")
            print("-" * 44)

    except KeyboardInterrupt:
        print("\nSimulator stopped.")

if __name__ == "__main__":
    main()