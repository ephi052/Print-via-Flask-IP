# Print via Flask IP

This project demonstrates how to create a Flask application that uploads files and prints them using a network printer's IP address, username, and password.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deploy with Docker and Nginx](#deploy-with-docker-and-nginx)
- [Print to Network Printer](#print-to-network-printer)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python (3.8 or higher)
- Docker

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ephi052/Print-via-Flask-IP.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Print-via-Flask-IP
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:

   ```bash
   python your_app_filename.py
   ```

   Access the app by visiting `http://127.0.0.1:5000` in your web browser.

2. Upload a file and provide printer credentials to print the uploaded file using the network printer.

## Deploy with Docker and Nginx

1. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   Your app will be available at `http://your_domain.com`.

2. Configure your DNS settings to point to your server's IP address.

## Print to Network Printer

Adapt your Flask app code to use the correct printer IP, username, and password to print to the network printer.

## Contributing

Contributions are welcome! If you have improvements or suggestions, please create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
