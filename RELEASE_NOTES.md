# Release Notes - V1.0.1

**Release Date:** July 3, 2026

**Release Type:** Bug Fix Release

## Overview

Version V1.0.1 is a critical production bug-fix release that resolves MongoDB configuration loading issues in packaged (PyInstaller) executables.

## Issues Fixed

### Critical
- **Fixed:** MongoDB configuration loading in packaged EXE
  - The application crashed with `ValueError: MONGODB_URI not found in .env` when running on external computers
  - Root cause: `.env` file was not included in the PyInstaller package
  - Solution: Implemented runtime detection and added `.env` to packaged executable

### Major
- **Fixed:** Application startup on external Windows PCs
  - The packaged EXE could not locate configuration files
  - Solution: Created `config/runtime.py` to detect dev vs PyInstaller mode and resolve paths correctly

### Improvements
- **Added:** Runtime environment detection (`config/runtime.py`)
  - Automatically detects whether running in development mode or as packaged EXE
  - Returns correct application root directory in both scenarios

- **Added:** Professional configuration error handling (`utils/message_dialog.py`)
  - User-friendly error dialogs instead of Python tracebacks
  - Clear instructions for users when configuration issues occur

- **Improved:** MongoDB connection error handling
  - Detailed error messages for connection failures
  - Timeout configuration for faster failure detection

- **Improved:** PyInstaller compatibility
  - `.env` file now included in packaged executable via `build.spec`
  - Automatic configuration discovery for both environments

## Changes Made

### New Files
- `config/runtime.py` - Runtime environment detection and path resolution
- `utils/message_dialog.py` - Professional error dialogs

### Modified Files
- `database/mongodb.py` - Updated to use runtime helper and error dialogs
- `build.spec` - Added `.env` to packaged data

### Compatibility
- ✅ Windows 10 support maintained
- ✅ Windows 11 support maintained
- ✅ Backward compatible with V1 data and configuration
- ✅ No breaking changes to APIs or services

## Testing Notes

### Development Mode
```bash
python app.py
```
- Loads `.env` from project root (unchanged behavior)
- All functionality works as before

### Packaged Mode (PyInstaller)
```bash
pyinstaller --clean --onefile --windowed --icon assets/icons/app_icon.ico --add-data ".env;." app.py
```
- `.env` is bundled inside executable
- Application works on any Windows PC without manual file copying
- Configuration errors show professional dialogs

## Known Limitations
- `.env` file must contain valid MongoDB credentials
- MongoDB Atlas IP whitelist must include user's IP address
- Application requires internet connection for MongoDB Atlas

## Version History
- **V1** (2026) - Initial release
- **V1.0.1** (2026) - Bug fix for .env configuration

## Support
For issues or questions, please contact the development team or create an issue on GitHub.
