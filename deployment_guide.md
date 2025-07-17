# GoldenYears IQ Deployment Guide

This guide provides detailed instructions for deploying the GoldenYears IQ application in various environments.

## Deployment Options

GoldenYears IQ can be deployed in several ways:

1. **Streamlit Cloud** (Recommended for public access)
2. **Self-hosting** on your own server
3. **Docker** deployment
4. **Local deployment** for personal use

## 1. Streamlit Cloud Deployment

Streamlit Cloud is the easiest way to deploy your application and make it accessible to users over the internet.

### Prerequisites

- A GitHub account
- Your GoldenYears IQ code in a GitHub repository
- A Streamlit Cloud account (free tier available)

### Deployment Steps

1. **Prepare your repository**:
   - Ensure your repository has the following structure:
     - `app.py` (main Streamlit application) at the root or in a specified directory
     - `requirements.txt` with all dependencies
     - Any other necessary files and directories

2. **Sign up for Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign up using your GitHub account

3. **Deploy your application**:
   - Click "New app"
   - Select your repository, branch, and the path to your main app file (e.g., `app/app.py`)
   - Click "Deploy"

4. **Configure your app** (optional):
   - Set up secrets for API keys (e.g., OpenAI API key)
   - Configure advanced settings like Python version

5. **Share your application**:
   - Once deployed, you'll get a public URL for your application
   - Share this URL with your users

### Updating Your Deployment

To update your application on Streamlit Cloud:

1. Push changes to your GitHub repository
2. Streamlit Cloud will automatically detect changes and redeploy your app

## 2. Self-Hosting Deployment

Self-hosting gives you more control over your deployment environment.

### Prerequisites

- A server with Python 3.8 or higher installed
- SSH access to the server
- Basic knowledge of server administration

### Deployment Steps

1. **Set up your server**:
   ```bash
   # Update package lists
   sudo apt update
   
   # Install Python and pip if not already installed
   sudo apt install python3 python3-pip
   
   # Install virtual environment
   sudo apt install python3-venv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/goldenyears-iq.git
   cd goldenyears-iq
   ```

3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   cd app
   streamlit run app.py
   ```

6. **Set up a service** (for running continuously):
   Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/goldenyears.service
   ```
   
   Add the following content:
   ```
   [Unit]
   Description=GoldenYears IQ Streamlit App
   After=network.target
   
   [Service]
   User=yourusername
   WorkingDirectory=/path/to/goldenyears-iq/app
   ExecStart=/path/to/goldenyears-iq/venv/bin/streamlit run app.py
   Restart=always
   RestartSec=5
   
   [Install]
   WantedBy=multi-user.target
   ```
   
   Enable and start the service:
   ```bash
   sudo systemctl enable goldenyears.service
   sudo systemctl start goldenyears.service
   ```

7. **Set up a reverse proxy** (optional, for custom domain and HTTPS):
   Install Nginx:
   ```bash
   sudo apt install nginx
   ```
   
   Create a Nginx configuration:
   ```bash
   sudo nano /etc/nginx/sites-available/goldenyears
   ```
   
   Add the following content:
   ```
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header Host $host;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_read_timeout 86400;
       }
   }
   ```
   
   Enable the site and restart Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/goldenyears /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```
   
   Set up HTTPS with Certbot:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```

## 3. Docker Deployment

Docker provides a consistent deployment environment across different platforms.

### Prerequisites

- Docker installed on your server
- Basic knowledge of Docker

### Deployment Steps

1. **Create a Dockerfile** in the root of your project:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t goldenyears-iq .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -p 8501:8501 goldenyears-iq
   ```

4. **Deploy with Docker Compose** (optional):
   Create a `docker-compose.yml` file:
   ```yaml
   version: '3'
   services:
     goldenyears:
       build: .
       ports:
         - "8501:8501"
       environment:
         - OPENAI_API_KEY=your_api_key
       restart: always
   ```
   
   Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

## 4. Local Deployment

For personal use or development.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Deployment Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/goldenyears-iq.git
   cd goldenyears-iq
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   cd app
   streamlit run app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://localhost:8501`

## Environment Variables

The following environment variables can be configured for GoldenYears IQ:

- `OPENAI_API_KEY`: Your OpenAI API key for generating retirement stories
- `STREAMLIT_SERVER_PORT`: Port for the Streamlit server (default: 8501)
- `STREAMLIT_SERVER_HEADLESS`: Set to true for headless server mode
- `STREAMLIT_BROWSER_GATHER_USAGE_STATS`: Set to false to disable usage statistics

## Troubleshooting

### Common Deployment Issues

1. **Application won't start**:
   - Check that all dependencies are installed correctly
   - Verify that you're using a compatible Python version
   - Check for errors in the console output

2. **Can't access the application remotely**:
   - Ensure the server's firewall allows traffic on port 8501
   - Check that the application is binding to 0.0.0.0 instead of localhost
   - Verify that any reverse proxy is configured correctly

3. **OpenAI API issues**:
   - Verify that your API key is set correctly
   - Check that you're using a supported model
   - Ensure your account has sufficient credits

4. **Performance issues**:
   - Consider increasing server resources for better performance
   - Optimize any heavy calculations or database operations
   - Use caching for expensive operations

## Security Considerations

1. **API Keys**:
   - Never hardcode API keys in your code
   - Use environment variables or Streamlit's secrets management
   - Restrict API key permissions to only what's needed

2. **User Data**:
   - Be transparent about data usage
   - Consider adding authentication for sensitive applications
   - Implement proper data validation to prevent injection attacks

3. **Server Hardening**:
   - Keep your server and dependencies updated
   - Use HTTPS for all production deployments
   - Implement proper firewall rules

## Maintenance

1. **Regular Updates**:
   - Keep dependencies updated regularly
   - Check for security advisories
   - Test updates in a staging environment before deploying to production

2. **Monitoring**:
   - Set up basic monitoring for your application
   - Monitor server resources (CPU, memory, disk)
   - Consider logging important events for troubleshooting

3. **Backups**:
   - Regularly backup any user data
   - Document your deployment setup for disaster recovery

---

© 2025 GoldenYears IQ | Premium Retirement Income Planning Software

