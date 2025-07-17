"""
Run script for the Income Planner application.

This script runs the Streamlit application.
"""

import os
import subprocess
import sys

def main():
    """Run the Streamlit application."""
    print("Starting Income Planner application...")
    
    # Get the absolute path to the app.py file
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "app.py")
    
    # Check if the file exists
    if not os.path.exists(app_path):
        print(f"Error: Could not find {app_path}")
        sys.exit(1)
    
    # Run the Streamlit application
    try:
        subprocess.run(["streamlit", "run", app_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Application stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()

