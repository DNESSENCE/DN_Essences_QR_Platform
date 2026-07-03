# Build Instructions - D&N Essences Smart QR Platform V1.0.1

This document provides step-by-step instructions for building and packaging the application for distribution.

## Prerequisites

- Python 3.13 or later
- PyInstaller (included in requirements.txt)
- Windows 10 or Windows 11
- `.env` file configured with valid MongoDB Atlas credentials

## Setup

### 1. Clone or Download Repository

```bash
git clone https://github.com/DNESSENCE/DN_Essences_QR_Platform.git
cd DN_Essences_QR_Platform
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file in the project root with your MongoDB Atlas credentials:

```env
MONGODB_URI=mongodb+srv://username:password@cluster-name.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=qr_platform
```

**⚠️ Important:** Keep `.env` secure. Never commit to version control.

### 5. Test Development Build

```bash
python app.py
```

The application should start without errors and connect to MongoDB.

## Building the Executable

### Method 1: Using build.spec (Recommended)

The `build.spec` file is pre-configured with all necessary PyInstaller settings.

```bash
pyinstaller build.spec --clean
```

### Method 2: Command Line (Manual)

If you prefer to build without the spec file:

```bash
pyinstaller ^
  --clean ^
  --onefile ^
  --windowed ^
  --icon assets/icons/app_icon.ico ^
  --name "DN_Essences_QR_Platform" ^
  --add-data ".env;." ^
  app.py
```

### Build Options Explained

| Option | Purpose |
| ------ | ------- |
| `--clean` | Remove previous build artifacts |
| `--onefile` | Create single executable (easier distribution) |
| `--windowed` | Hide console window on Windows |
| `--icon` | Set application icon |
| `--add-data ".env;."` | **CRITICAL:** Include .env in executable |
| `--name` | Set output executable name |

## Output

After successful build:

```text
dist/
  └── DN_Essences_QR_Platform.exe
build/
  └── (build artifacts)
DN_Essences_QR_Platform.spec
  └── (build specification)
```

The executable is located in the `dist/` directory.

## Distribution

### Packaging for Release

1. **Create release directory:**

   ```bash
   mkdir release
   cd dist
   copy DN_Essences_QR_Platform.exe ..\release\
   cd ..\release
   ```

2. **Create installer (optional):**
   - Use NSIS (Nullsoft Scriptable Install System) for professional installer
   - Or distribute EXE directly

3. **Create README for end users:**

   ```text
   D&N Essences Smart QR Platform V1.0.1
   
   System Requirements:
   - Windows 10 or Windows 11
   - 100 MB free disk space
   - Internet connection (for MongoDB)
   
   Installation:
   1. Download DN_Essences_QR_Platform.exe
   2. Run the executable
   3. Application will start automatically
   
   Troubleshooting:
   - Ensure you have a valid internet connection
   - Check that MongoDB Atlas is accessible from your location
   - Contact support if issues persist
   ```

### Testing Packaged Build

Before distribution, test the EXE on a clean Windows machine:

1. Copy `dist/DN_Essences_QR_Platform.exe` to a test machine
2. Run the executable
3. Verify MongoDB connection
4. Test all major features (QR generation, export, history)

## Troubleshooting

### Build Fails

**Problem:** PyInstaller fails to build

```text
ModuleNotFoundError: No module named 'module_name'
```

**Solution:**

- Add missing module to `hiddenimports` in build.spec
- Rebuild with `--clean` flag

### `.env` Not Found

**Problem:** Application shows "Configuration Error" dialog

```text
MongoDB configuration file (.env) could not be found
```

**Solution:**

- Verify `.env` exists in project root before building
- Verify build.spec includes `('.env', '.')` in datas
- Rebuild with updated spec file

### Connection Timeout

**Problem:** Application hangs or shows connection error

```text
Failed to connect to MongoDB Atlas
```

**Solution:**

- Verify MongoDB URI in `.env` is correct
- Check MongoDB Atlas IP whitelist includes your IP
- Ensure internet connection is active
- Verify firewall allows MongoDB connections

## Version Information

- **Application:** D&N Essences Smart QR Platform
- **Version:** V1.0.1
- **Release Type:** Bug Fix Release
- **Platform:** Windows 10/11
- **Python:** 3.13+
- **GUI Framework:** CustomTkinter
- **Database:** MongoDB Atlas

## Support

For build issues or questions:

1. Check this guide
2. Review RELEASE_NOTES.md
3. Check GitHub Issues
4. Contact development team

## Changelog

### V1.0.1

- Fixed .env configuration loading in packaged executables
- Added runtime environment detection
- Improved error handling with professional dialogs
- Enhanced PyInstaller compatibility

### V1

- Initial release
