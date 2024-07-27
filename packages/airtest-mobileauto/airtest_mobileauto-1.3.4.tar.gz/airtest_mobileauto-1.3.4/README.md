# AirTest Mobile Automation

AirTest Mobile Automation is an object-oriented, multi-process control framework for mobile apps based on the AirTest framework. It is designed for stability and compatibility, making it ideal for automating tasks in games like Honor of Kings.

## Features

- **Enhanced Stability**: Includes connection status checks and automatic reconnection attempts to prevent errors after multiple failures.
- **Automated Operation**: Capable of fully automated processes with unattended operation. In case of errors, it automatically restarts the app or the control endpoint, such as Docker or an Android emulator.
- **Time Management**: Utilizes the UTC/GMT+08:00 time zone for task scheduling aligned with Chinese game refresh cycles.
- **Formatted Output**: Displays information in a formatted manner, e.g., `[MM-DD HH:MM:SS] info`.

## Modules

### Device Management (`deviceOB`)
Handles device management in an object-oriented approach, supporting various clients and control endpoints.

- **Clients**: Android (phones, BlueStacks, LDPlayer for Windows, Docker for Linux), iOS (iPhone and iPad with WebDriverAgent & tidevice).
- **Control Endpoints**: Windows, Mac, Linux.
- **Management Capabilities**: Open, close, and restart apps; manage devices.

### APP Management (`appOB`)
Manages the opening, closing, and restarting of apps.

### Tools (`DQWheel`)
- A utility for multi-process support based on the file system, including synchronization, broadcasting, file management, and enhanced time management.
- Utilizes files and dictionaries to store and retrieve image coordinates, reducing the time to locate element coordinates repeatedly. It also allows for selecting specific positions, such as the least proficient hero in Honor of Kings based on proficiency.

## Development Example
- An automation script for Honor of Kings is available as a development example.

## Contribution
Contributions are welcome! Please refer to our [contribution guidelines](CONTRIBUTING.md) for more information.

## Acknowledgements
This script was heavily inspired by the [WZRY_AirtestIDE@XRSec](https://github.com/XRSec/WZRY_AirtestIDE) project and serves as a primary reference for learning AirTest scripts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright
© 2024 cndaqiang. All rights reserved.