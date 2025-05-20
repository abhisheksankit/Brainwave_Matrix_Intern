# Phishing Link Scanner

This is a basic **Phishing Link Scanner** developed in Python as part of the **Brainwave_Matrix_Intern** Cyber Security Internship.

## Features

- Checks for known phishing patterns in URLs
- Detects use of misleading domains
- Optionally checks domain age (with WHOIS)
- Simple terminal interface (Termux compatible)

## Technologies Used

- Python 3
- Regular Expressions (re)
- `validators` library
- `whois` (optional for domain age)
- Termux on Android

## Setup Instructions (Termux)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python git -y

# Install required Python libraries
pip install validators python-whois

# Clone this repository
git clone https://github.com/abhisheksankit/Brainwave_Matrix_Intern.git
cd Brainwave_Matrix_Intern

# Run the script
python phishing_scanner.py# Phishing Link Scanner by Ankit Sagili
# Brainwave_Matrix_Intern
