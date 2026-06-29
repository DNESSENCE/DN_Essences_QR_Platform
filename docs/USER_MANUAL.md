# User Manual

## D&N Essences QR Platform v1.0.0

Complete guide to using all features of the QR Platform.

### Table of Contents
1. [Getting Started](#getting-started)
2. [QR Generator](#qr-generator)
3. [History Management](#history-management)
4. [Analytics](#analytics)
5. [Settings](#settings)
6. [Tips & Best Practices](#tips--best-practices)
7. [Keyboard Shortcuts](#keyboard-shortcuts)

---

## Getting Started

### First Launch

1. **Application Opens** to Dashboard showing:
   - Total QR Codes generated
   - Total Scans and Exports
   - Customer and Product counts
   - Database connection status
   - Recent activity log

2. **Initial Setup** (if first time):
   - Go to Settings page
   - Update Company Name and Website
   - Configure export directory
   - Test database connection
   - Click "Save Settings"

3. **Creating Your First QR**:
   - Click "QR Generator" in sidebar
   - Select QR type
   - Enter value
   - Click "Generate"
   - Click "Save" to store

---

## QR Generator

### Step-by-Step QR Generation

#### 1. Select QR Type
- **Website**: Paste HTTPS URL (auto-converts to secure link)
- **Instagram**: Enter username (no @ symbol)
- **WhatsApp**: Enter phone number with country code (+1234567890)
- **Email**: Enter email address
- **Phone**: Enter phone number with country code

#### 2. Enter Value
- Type the specific value for your QR type
- Placeholder text shows expected format
- Real-time validation as you type

#### 3. Customize Options (Right Panel)

**Colors:**
- Foreground: Click to select QR color (default: black)
- Background: Click to select background (default: white)
- Recommended: Black on white for maximum scannability

**Size:**
- Scale from 4 (tiny) to 20 (very large)
- Affects QR code density
- Start with 10 for standard use

**Border:**
- Quiet zone around QR code (1-10)
- Recommended minimum: 2
- Prevents misscanning at edges

**Error Correction:**
- L (7%): Minimal corruption tolerance
- M (15%): Standard (recommended)
- Q (25%): High tolerance
- H (30%): Maximum tolerance (higher data density)

#### 4. Generate & Preview
- Click **Generate** button
- Preview appears in center panel
- Checks for errors in input
- Shows generation success/failure

#### 5. Save or Export

**Save to Database:**
- Stores QR permanently in MongoDB
- Creates scan/export tracking
- Enables later retrieval and management
- Click "Save" button

**Export to File:**
- Choose format: PNG, PDF, or SVG
- PNG: Best for web, email, documents
- PDF: Professional printing, batch exports
- SVG: Scalable for design apps
- Files saved to `exports/` directory with timestamp

### Tips for Better QR Codes

- **Contrast**: Always use high contrast colors
- **Size**: Larger is always safer (testing on mobile first)
- **Border**: Don't remove border zone
- **Format**: PNG for digital, PDF for print
- **Testing**: Always test with phone before deployment

---

## History Management

### Accessing History

1. Click **History** in sidebar
2. Page loads recent QR codes automatically
3. Shows: ID, Type, Data, Scan count, Export count, Creation date

### Search Functionality

1. Type in **Search box** at top
2. Searches across:
   - Raw user input (email, phone, etc.)
   - Formatted QR payload
   - User notes/tags
3. Press Enter or wait for auto-search

**Examples:**
- Search "instagram" finds all Instagram QRs
- Search "2024-01" finds QRs created in January 2024
- Search "sales" finds QRs tagged with sales notes

### Filtering

**By Type:**
- Use Type dropdown to filter
- Options: All, Website, Instagram, WhatsApp, Email, Phone
- Changes table instantly

**By Date Range:**
- Future feature: Will filter by creation date
- Currently sorted by newest first

### QR Code Actions

#### Select QR Code
- Click any row in table to select
- Selected row highlights
- Actions become available

#### Duplicate
- Click "Duplicate" button
- Creates exact copy with new ID
- Notes field shows "Duplicated from [original ID]"
- New QR appears in list

#### Delete
- Click "Delete" on selected QR
- Asks for confirmation
- Soft-deleted (recoverable)
- Disappears from active list

#### Restore
- Select from deleted QRs (if shown)
- Click "Restore"
- Returns to active list
- All data preserved

#### Export
- Click "Export" on selected QR
- Choose format (PNG/PDF/SVG)
- File saved with timestamp
- Opens save dialog

#### Refresh
- Click "Refresh" to reload list
- Pulls latest from database
- Useful after batch operations

---

## Analytics

### Dashboard Overview

**Analytics page displays:**
- QR activity time-series chart
- Engagement metrics card
- QR type distribution chart
- Top-performing QR codes table

### Time-Series Analysis

**Timeframe Selection:**
- **Daily**: Last 30 days (by calendar day)
- **Weekly**: Last 12 weeks
- **Monthly**: Last 12 months

**Metrics Tracked:**
- QR codes created
- Total scans
- Total exports

**Chart Shows:**
- X-axis: Time period
- Y-axis: Count
- Multiple lines: Different metrics

### Engagement Metrics

Shows four key statistics:
- **Total QR Codes**: All active QRs in database
- **Avg Scans/QR**: Average scans per single QR
- **Avg Exports/QR**: Average exports per single QR
- **Engagement Rate**: Overall platform engagement percentage

### Top Performers

**Metric Selection:**
- **Scans**: Shows QRs with most scan activity
- **Exports**: Shows QRs that are exported most

**Shows Top 10:**
- QR ID (first 8 characters)
- Type (Website, Instagram, etc.)
- Data (value, truncated)
- Total Scans
- Total Exports
- Creation Date

### Interpreting Results

**High Engagement**:
- Scans > 10 per QR = Strong interest
- Exports > 5 per QR = Reuse/sharing

**Low Engagement**:
- Few scans = Needs more distribution
- No exports = Limited secondary use

**Best Performers**:
- Focus future campaigns on types with high engagement
- Update outdated QRs with high potential

---

## Settings

### Application Settings

#### App Name
- Internal application title
- Shown in window title and branding
- Default: "D&N Essences QR Platform"

#### Company Name
- Your organization name
- Used in exports and metadata
- Default: "D&N Essences"

#### Company Website
- Your official website
- Included in PDF exports
- Default: "https://dn-essences.com"

#### Export Directory
- Where files are saved
- Default: "exports/" (creates in app directory)
- Change to backup location if preferred

### Database Settings

#### Connection Status
- Shows current MongoDB connection
- Format: "✅ Connected to DATABASE_NAME (X collections)"
- "❌ Disconnected" if offline

#### Test Connection
- Verifies MongoDB is accessible
- Shows success/failure message
- Useful for troubleshooting

#### Backup Database
- Initiates database backup
- Creates in `exports/backups/`
- Backup is JSON format
- Use periodically for disaster recovery

### Saving Settings

**Save Settings:**
- Changes all fields to new values
- Persists to `config/app_settings.json`
- Takes effect immediately

**Reset to Defaults:**
- Confirms action (can't undo easily)
- Restores all settings to factory defaults
- Database not affected

**Export Settings:**
- Saves current settings to JSON file
- Location: `exports/settings_backup.json`
- Share for consistent configuration across machines

**Import Settings:**
- Loads previously exported settings
- Replaces current configuration
- Useful for deploying to multiple computers

---

## Tips & Best Practices

### QR Code Generation

✅ **DO:**
- Test every QR with a real phone
- Use high-contrast colors
- Include adequate border space
- Generate at larger sizes (10+)
- Use PNG for maximum compatibility

❌ **DON'T:**
- Use low-contrast colors (light gray on white)
- Remove border completely
- Use tiny sizes (< 4) for print
- Modify QR after generation
- Rotate or skew QR codes

### Organization

✅ **DO:**
- Use consistent naming conventions
- Add notes with campaign/use
- Tag related QRs together
- Archive outdated QRs (don't delete)
- Review analytics monthly

❌ **DON'T:**
- Create duplicate entries
- Leave notes empty
- Generate QRs you don't need
- Permanently delete without backup
- Ignore engagement metrics

### Security

✅ **DO:**
- Keep MongoDB credentials secure
- Backup database regularly
- Use strong passwords
- Test connection regularly
- Monitor access logs

❌ **DON'T:**
- Share MongoDB URI in messages
- Hardcode credentials in code
- Leave backups in public folders
- Ignore connection warnings
- Use simple/default passwords

### Performance

✅ **DO:**
- Review history weekly
- Archive old QRs monthly
- Test on various devices
- Use PNG for fast delivery
- Monitor database size

❌ **DON'T:**
- Generate thousands of test QRs
- Leave deleted items unreviewed
- Use very large resolution exports unnecessarily
- Ignore database backups
- Mix old/new QRs in campaigns

---

## Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---|---|
| **QR Generator** | | |
| Generate QR | Enter | Enter |
| Clear Form | Ctrl+N | Cmd+N |
| Save QR | Ctrl+S | Cmd+S |
| Export QR | Ctrl+E | Cmd+E |
| | | |
| **History** | | |
| Refresh | F5 | Cmd+R |
| Search Focus | Ctrl+F | Cmd+F |
| Delete Selected | Delete | Delete |
| Duplicate | Ctrl+D | Cmd+D |
| | | |
| **Global** | | |
| Focus Search | Ctrl+/ | Cmd+/ |
| Go to Settings | Ctrl+, | Cmd+, |
| Refresh All | F5 | Cmd+R |
| Exit Application | Alt+F4 | Cmd+Q |

---

## Troubleshooting

### "MongoDB Connection Failed"
1. Check Settings → Test Connection
2. Verify internet connectivity
3. Check MongoDB URI in settings
4. Ensure IP is whitelisted in Atlas
5. Try disabling firewall temporarily

### "QR Code Failed to Generate"
1. Check input format for selected type
2. Verify special characters are allowed
3. Try simpler value first
4. Check application logs
5. Try restarting application

### "Export Failed"
1. Verify `exports/` directory exists
2. Check write permissions on folder
3. Ensure sufficient disk space
4. Try exporting to different format
5. Try different filename/location

### "Application Crashes"
1. Check Python version is 3.13+
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Clear application cache
4. Try updating to latest version
5. Report issue with error message

---

## Support & Resources

- **Documentation**: https://docs.dn-essences.com/qr-platform
- **GitHub Issues**: https://github.com/dn-essences/qr-platform/issues
- **Email**: support@dn-essences.com
- **FAQ**: See README.md troubleshooting section

---

**Version 1.0.0** | Last Updated: June 30, 2026
