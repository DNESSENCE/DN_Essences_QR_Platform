# Installation Guide

## D&N Essences QR Platform

Complete installation instructions for all platforms.

### Table of Contents
1. [System Requirements](#system-requirements)
2. [Windows Installation](#windows-installation)
3. [macOS Installation](#macos-installation)
4. [Linux Installation](#linux-installation)
5. [MongoDB Setup](#mongodb-setup)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum
- **OS**: Windows 10, macOS 10.14, Linux (Ubuntu 18.04+)
- **RAM**: 2GB
- **Storage**: 500MB
- **Python**: 3.13+ (for source installation)
- **Internet**: Required for MongoDB connection

### Recommended
- **OS**: Windows 11, macOS 12+, Ubuntu 22.04+
- **RAM**: 4GB+
- **Storage**: 2GB
- **GPU**: Optional (not required)
- **Display**: 1080p+

---

## Windows Installation

### Method 1: Standalone Installer (Easiest)

1. Download `DN_Essences_QR_Platform_Setup.exe` from releases
2. Double-click to run the installer
3. Accept the license agreement
4. Choose installation directory
5. Select Start Menu folder
6. Click "Install"
7. Check "Launch application" and click "Finish"
8. Configure MongoDB connection on first run

### Method 2: From Source

#### Prerequisites
- Python 3.13+ installed and in PATH
- Git for Windows
- MongoDB URI (see [MongoDB Setup](#mongodb-setup))

#### Steps

1. **Clone Repository**
   ```powershell
   git clone https://github.com/dn-essences/qr-platform.git
   cd qr-platform
   ```

2. **Create Virtual Environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```powershell
   $env:MONGODB_URI = "mongodb+srv://user:password@cluster.mongodb.net/qr_platform"
   ```
   
   Or create `.env` file in project root:
   ```
   MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/qr_platform
   ```

5. **Run Application**
   ```powershell
   python app.py
   ```

6. **Create Desktop Shortcut (Optional)**
   - Right-click on app.py
   - "Send to" → "Desktop (create shortcut)"
   - Rename to "D&N Essences QR Platform"

---

## macOS Installation

### Method 1: Homebrew (Recommended)

```bash
# Install homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.13
brew install python@3.13

# Clone and setup
git clone https://github.com/dn-essences/qr-platform.git
cd qr-platform

# Virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set MongoDB URI
export MONGODB_URI="mongodb+srv://user:password@cluster.mongodb.net/qr_platform"

# Run
python app.py
```

### Method 2: From Source

1. Install Python 3.13 from [python.org](https://python.org)
2. Follow same steps as Homebrew (skip brew install)
3. Create `.zprofile` alias:
   ```bash
   echo 'alias qr-platform="cd ~/qr-platform && source venv/bin/activate && python app.py"' >> ~/.zprofile
   ```

### Creating App Bundle (Optional)

```bash
# Install PyInstaller
pip install pyinstaller

# Build application bundle
pyinstaller build.spec

# Copy to Applications
cp -r dist/DN_Essences_QR_Platform.app /Applications/
```

---

## Linux Installation

### Ubuntu/Debian

```bash
# Install Python 3.13 and dependencies
sudo apt update
sudo apt install python3.13 python3.13-venv python3-pip

# Clone repository
git clone https://github.com/dn-essences/qr-platform.git
cd qr-platform

# Virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export MONGODB_URI="mongodb+srv://user:password@cluster.mongodb.net/qr_platform"

# Run
python3.13 app.py
```

### Fedora/RHEL

```bash
# Install dependencies
sudo dnf install python3.13 python3.13-devel gcc

# Continue with virtual environment setup (same as Ubuntu)
```

### Create Desktop Launcher

Create `/usr/share/applications/qr-platform.desktop`:

```ini
[Desktop Entry]
Version=1.0
Name=D&N Essences QR Platform
Exec=/home/user/qr-platform/venv/bin/python /home/user/qr-platform/app.py
Icon=qr-code
Type=Application
Categories=Utility;
Terminal=false
```

---

## MongoDB Setup

### Cloud Setup (Recommended)

1. Visit [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up for free account
3. Create organization and project
4. Click "Build a Database"
5. Choose "Free" tier and "AWS" region closest to you
6. Create cluster (takes 1-3 minutes)
7. Create database user:
   - Username: `qr_user`
   - Password: Generate strong password
   - Click "Create User"
8. Add IP address:
   - Click "Add My Current IP Address"
   - Or add `0.0.0.0/0` for any IP
9. Get connection string:
   - Click "Connect"
   - Select "Drivers"
   - Copy connection string
   - Replace `<password>` with your password
   - Replace `<database>` with database name

### Local Setup (Docker)

```bash
# Install Docker from docker.com
# Run MongoDB container
docker run -d -p 27017:27017 --name mongodb mongo:7.0

# Connection string
MONGODB_URI=mongodb://localhost:27017/qr_platform
```

### Connection Testing

After setup, test connection from application:
1. Go to Settings page
2. Click "Test Connection"
3. Should show "✅ Connected to qr_platform (X collections)"

---

## Troubleshooting

### Python Not Found

**Windows:**
```powershell
# Check Python is installed
python --version

# If not, reinstall from python.org
# Ensure "Add Python to PATH" is checked during installation
```

**macOS/Linux:**
```bash
python3 --version
# Use python3 instead of python
```

### MongoDB Connection Failed

- **Check URI format**: `mongodb+srv://user:password@cluster.mongodb.net/database`
- **Check credentials**: Username and password are correct
- **Check IP whitelist**: Add your IP to MongoDB Atlas
- **Check internet**: Ensure connection to MongoDB servers
- **Check firewall**: Disable temporarily to test
- **Verify environment variable**:
  ```bash
  # Windows
  echo %MONGODB_URI%
  
  # macOS/Linux
  echo $MONGODB_URI
  ```

### Virtual Environment Issues

```bash
# Deactivate and reactivate
deactivate
source venv/bin/activate  # macOS/Linux
# or
.\venv\Scripts\activate  # Windows
```

### Permission Denied (Linux/macOS)

```bash
# Make app executable
chmod +x app.py

# Run with full path
/usr/bin/python3.13 app.py
```

### Dependencies Installation Failed

```bash
# Upgrade pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall requirements
pip install -r requirements.txt --no-cache-dir
```

### Port Already in Use

The application uses Tkinter which doesn't require ports, but if using future web UI:

```bash
# Find process using port (e.g., 8000)
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

---

## Updating

### From Installer
1. Download new version installer
2. Run installer (will update existing installation)
3. Restart application

### From Source
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart application
```

---

## Getting Help

- **Documentation**: https://docs.dn-essences.com/qr-platform
- **GitHub Issues**: https://github.com/dn-essences/qr-platform/issues
- **Email Support**: support@dn-essences.com
- **FAQ**: [README.md](../README.md#troubleshooting)

---

**Last Updated**: June 30, 2026 | Version 1.0.0
