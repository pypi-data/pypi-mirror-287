# Command Stash Tool

A CLI tool for managing and organizing commands with support for saving, listing, exporting, importing, and backing up commands to AWS S3.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Setting Up](#setting-up)
    - [Commands](#commands)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Save commands with categories and descriptions.
- List saved commands with filtering options.
- Export commands to JSON or YAML files.
- Import commands from JSON or YAML files.
- Backup commands to an AWS S3 bucket.
- Restore commands from an AWS S3 bucket.

## Installation

### Using the Makefile

1. **Clone the repository**:

     ```bash
     git clone <repository-url>
     cd <repository-name>
     ```

2. **Run the setup command**:

The Makefile provides a convenient way to set up the project. Run the following command to install dependencies and set up the environment:

     ```bash
     make setup
     ```

     This command will:

     - Install dependencies using poetry.
     - Set up the virtual environment.
     - Install project-specific dependencies.

     If you prefer to set up the environment manually, please refer to the manual setup instructions in the original README.

## Usage

### Setting Up

Configure AWS: Create a config.yaml file in the root directory with the following structure:

```yaml
aws:
    region: your-aws-region
    bucket_name: your-s3-bucket-name
    bucket_privacy: private # or public-read
```

Set the commands file location (optional):

```bash
cmd_stash set-location <path-to-commands-file>
```

### Commands

Save a command:

```bash
cmd_stash save <category> <subcategory> <description> <command>
```

List commands:

```bash
cmd_stash list <category> [--subcategory <subcategory>] [--description <description>]
```

Export commands to a file:

```bash
cmd_stash export <file-path>
```

Import commands from a file:

```bash
cmd_stash import <file-path>
```

Create an S3 bucket:

```bash
cmd_stash create-bucket
```

Upload commands to S3:

```bash
cmd_stash upload
```

Download commands from S3:

```bash
cmd_stash download
```

Destroy the S3 bucket:

```bash
cmd_stash bucket-destroy
```

For more detailed usage instructions, please refer to the original README.

## Configuration

AWS Configuration: Ensure your config.yaml is correctly set up with your AWS region and bucket details.

Commands File: By default, commands are saved to commands.yaml in your home directory. You can change this location using the set-location command.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
