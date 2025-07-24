# Convert Epoch

A simple Python utility that reads text from stdin and converts any 10-digit epoch timestamps to human-readable date/time format.

## Description

This program searches for 10-digit epoch timestamps (Unix timestamps) in text input and converts them to a readable format while preserving the rest of the text. It's useful for analyzing log files, debugging output, or any text that contains epoch timestamps.

## Features

- Reads from standard input (stdin)
- Automatically detects 10-digit epoch timestamps
- Converts timestamps to human-readable format: `Day Mon DD HH:MM:SS YYYY`
- Preserves original text structure
- Interactive mode - use Ctrl+D to end input

## Usage

### From File
```bash
cat logfile.txt | convert_epoch.py
```

### From Command Output
```bash
some_command | convert_epoch.py
```

## Example

**Input:**
```
User login at 1609459200 was successful
Error occurred at timestamp 1609462800
```

**Output:**
```
User login at Fri Jan 01 00:00:00 2021 was successful
Error occurred at timestamp Fri Jan 01 01:00:00 2021
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Convert-Epoch.git
cd Convert-Epoch
```

2. Make the script executable:
```bash
chmod +x convert_epoch.py
```

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## Notes

- Only detects exactly 10-digit numbers as epoch timestamps
- Uses local timezone for conversion
- Timestamps before 1970 or after 2038 may not work correctly on some systems

## License

This project is open source. Feel free to use and modify as needed.

## Contributing

Feel free to submit issues and pull requests to improve this utility.
