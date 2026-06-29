# D&N Essences QR Platform

A professional desktop application for generating, managing, and analyzing QR codes. Built with Python 3.13, CustomTkinter, and MongoDB Atlas.

## Features

✨ **QR Code Generation**
- Support for 5 QR types: Website, Instagram, WhatsApp, Email, Phone
- Customizable colors, size, border, and error correction
- Real-time preview with HighDPI support
- One-click export to PNG, PDF, or SVG

📊 **History & Management**
- Complete QR code history with filtering and search
- Duplicate, restore, and permanently delete QR codes
- Track scans and exports per QR code
- Sort by creation date, type, or engagement metrics

📈 **Analytics & Reporting**
- Daily, weekly, and monthly statistics
- QR type distribution charts
- Engagement metrics (avg scans/exports per QR)
- Top-performing QR codes by metric

⚙️ **Settings & Configuration**
- Customize application name and company details
- Configure default QR parameters
- Database connection testing and backup
- Import/export settings

🗄️ **MongoDB Integration**
- Cloud-based data storage via MongoDB Atlas
- Automatic index creation for optimal performance
- Soft-delete functionality for data recovery
- Real-time statistics and analytics

## System Requirements

- **OS**: Windows 10/11, macOS 10.14+, Linux
- **Python**: 3.13 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Display**: 1024x768 minimum resolution
- **Internet**: Required for MongoDB Atlas connection

## Installation

### Option 1: Standalone Executable (Windows)

1. Download `DN_Essences_QR_Platform.exe` from the releases page
2. Run the installer
3. Follow the installation wizard
4. Launch the application from Start Menu or Desktop shortcut

### Option 2: From Source

1. Clone the repository
   ```bash
   git clone https://github.com/dn-essences/qr-platform.git
   cd qr-platform
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Configure MongoDB
   ```bash
   # Set environment variable with your MongoDB URI
   export MONGODB_URI="mongodb+srv://user:password@cluster.mongodb.net/qr_platform"
   ```

5. Run the application
   ```bash
   python app.py
   ```

## Configuration

### Environment Variables

```bash
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/database_name
```

### Application Settings

Settings are stored in `config/app_settings.json`:

```json
{
  "theme": "dark",
  "app_name": "D&N Essences QR Platform",
  "company_name": "D&N Essences",
  "company_website": "https://dn-essences.com",
  "qr_default_foreground": "black",
  "qr_default_background": "white",
  "qr_default_size": 10,
  "qr_default_border": 2,
  "export_format": "png",
  "export_directory": "exports"
}
```

## Usage Guide

### Generating QR Codes

1. Navigate to **QR Generator** page
2. Select QR type from dropdown
3. Enter the value (URL, username, phone, etc.)
4. Customize colors, size, and border if needed
5. Click **Generate** to preview
6. Click **Save** to store in database or **Export** to save as image

### Viewing History

1. Go to **History** page
2. Use search bar to find specific QR codes
3. Filter by type using dropdown
4. Click on any QR code to select it
5. Use toolbar to duplicate, delete, or restore QR codes

### Analyzing Performance

1. Open **Analytics** page
2. Select timeframe (Daily, Weekly, Monthly)
3. Choose metric to track (Scans, Exports)
4. View charts and top-performing QR codes
5. Engagement metrics show overall platform activity

### Configuring Settings

1. Navigate to **Settings** page
2. Update app name, company info, and export directory
3. Click **Test Connection** to verify MongoDB
4. Click **Backup Database** to create backup
5. Click **Save Settings** to persist changes

## Troubleshooting

### MongoDB Connection Failed
- Verify MongoDB URI environment variable is set correctly
- Check internet connection
- Ensure MongoDB cluster allows connections from your IP
- Run "Test Connection" from Settings page

### High DPI Display Issues
- The application uses CustomTkinter which automatically handles HighDPI scaling
- If text appears blurry, try updating graphics drivers

### QR Code Export Fails
- Check that `exports/` directory is writable
- Ensure sufficient disk space available
- Verify PDF/PNG dependencies are installed

## Architecture

### MVC Pattern
- **Models**: Data structures (`models/`)
- **Views**: UI components (`ui/`)
- **Controllers**: Business logic orchestration (`controllers/`)
- **Services**: Database and export operations (`services/`)

### Key Components
- `app.py` - Application entry point
- `database/mongodb.py` - MongoDB connection management
- `services/` - Business logic (QR, Export, History, Analytics, Settings)
- `controllers/` - UI orchestration
- `ui/` - CustomTkinter UI components
- `config/` - Application configuration

## Tech Stack

- **Frontend**: CustomTkinter (Modern Tkinter)
- **Backend**: Python 3.13
- **Database**: MongoDB Atlas
- **QR Generation**: qrcode[pil]
- **PDF Export**: ReportLab
- **Image Processing**: Pillow

## Dependencies

Core:
- customtkinter>=5.0 - Modern Tkinter replacement
- pymongo>=4.0 - MongoDB driver
- qrcode[pil]>=7.0 - QR code generation
- reportlab>=4.0 - PDF generation
- Pillow>=9.0 - Image processing

Development:
- pyinstaller - Executable generation
- pytest - Unit testing

## Development

### Running Tests
```bash
pytest tests/
```

### Building Executable
```bash
pyinstaller build.spec
```

### Code Style
- Python 3.13 syntax
- Type hints on all functions
- PEP 8 formatting
- Docstrings on all classes/methods

## Support

For issues, questions, or feature requests:
- GitHub Issues: https://github.com/dn-essences/qr-platform/issues
- Email: support@dn-essences.com
- Documentation: https://docs.dn-essences.com/qr-platform

## License

Proprietary License - D&N Essences
All rights reserved. See LICENSE file for details.

## Changelog

### Version 1.0.0 (Initial Release)
- ✨ QR code generation for 5 types
- 📊 Complete history management
- 📈 Analytics and reporting
- ⚙️ Configurable settings
- 🔒 MongoDB Atlas integration
- 🎨 Professional UI with dark theme
- 📤 Export to PNG/PDF/SVG
- 💾 Database backup and restore

## Credits

**Development**: D&N Essences Development Team
**Framework**: CustomTkinter
**Database**: MongoDB Atlas
**Icons**: Icons from assets library

---

**Version 1.0.0** | Last Updated: June 2026 | [License](LICENSE) | [Changelog](CHANGELOG.md)
