# Turbo AutoClicker

Optimized autoclicker for greatonlinetools.com/autoliker with minimal resource usage.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

## Usage

**Headless mode (recommended for overnight runs):**
```bash
python3 autoclicker.py --headless
```

**Visible mode (for testing):**
```bash
python3 autoclicker.py
```

## Features

- **Silent operation**: No logs printed to prevent overheating
- **Auto tab closing**: Instantly closes any popup windows/tabs
- **Resource optimized**: Minimal RAM/CPU usage with Chromium flags
- **Fast clicking**: Rapid button clicks on earn credits page
- **Headless support**: Run without visible browser window

## How it works

1. Opens https://greatonlinetools.com/autoliker/
2. Enters username: rubrastudios
3. Clicks search account
4. Navigates to dashboard
5. Clicks earn credits
6. Auto-clicks Like/Follow/Verify buttons
7. Instantly closes any new tabs/windows
8. Keeps only main tab open

## Stop

Press Ctrl+C to stop the script.
