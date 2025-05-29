# ================================
# Required Installations:
# pip install speedtest-cli
# (Optional for system CLI method)
# sudo apt install speedtest-cli  # For Linux users
# ================================

import subprocess
import speedtest

def run_speedtest_with_module():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Find the best server based on ping
    print("Finding the best server based on ping...")
    best = st.get_best_server()
    print(f"Best server found: {best['host']} located in {best['country']}")

    # Perform download test
    print("Performing download test...")
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbps

    # Perform upload test
    print("Performing upload test...")
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbps

    # Get ping result
    ping = st.results.ping

    # Display results
    print("\n--- Speed Test Results Using Python Module ---")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping:.2f} ms")

def run_speedtest_with_cli():
    # Run the system-installed 'speedtest-cli' command
    print("\nRunning speedtest-cli via system command...")
    try:
        result = subprocess.run(["speedtest-cli"], capture_output=True, text=True)
        print("\n--- Speed Test Results Using CLI Command ---")
        print(result.stdout)
    except FileNotFoundError:
        print("Error: 'speedtest-cli' not found. Please install it using:\n  sudo apt install speedtest-cli")

if __name__ == "__main__":
    print("===== Speed Test Utility =====")
    # Run both methods
    run_speedtest_with_module()
    run_speedtest_with_cli()
