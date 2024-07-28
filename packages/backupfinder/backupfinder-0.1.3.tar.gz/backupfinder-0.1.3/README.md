# BackupFinder

**BackupFinder** is a Python tool for generating wordlists based on user-provided domain URLs. It helps in creating two types of wordlists:

1. **Log File Names**: Common log file names adjusted for the provided domain.
2. **Backup File Names**: Common backup file names customized with the domain.

## Features

- **Customizable Wordlists**: Generates wordlists for both log and backup files based on domain input.
- **Date-based Filenames**: Includes date-based variations for log filenames to account for different time granularities.
- **Easy to Use**: Simple command-line interface for quick generation of wordlists.

## Installation

You can install **BackupFinder** from PyPI using pip:

```
pip install backupfinder
```

## Usage

After installing the package, run the tool using:

```
backupfinder
```

### Example

When prompted, enter a URL such as `https://www.example.com`. The tool will generate two files:

- `custom_logfinder.txt`: Contains a list of common log file names adjusted for the domain.
- `custom_backupfinder.txt`: Contains a list of common backup file names adjusted for the domain.

### Inputs

- **URL**: Enter a domain URL such as `example.com` or `https://www.example.com`.

### Outputs

- **custom_logfinder.txt**: A text file with generated log file names.
- **custom_backupfinder.txt**: A text file with generated backup file names.

**BackupFinder** is a tool designed to aid in generating wordlists for security and auditing purposes. Use responsibly and ensure compliance with legal and ethical standards.
