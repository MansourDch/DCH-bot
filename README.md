# DCH-bot

A Towns Protocol bot for distributed communication and automation.

## Overview

DCH-bot is a bot application built on the Towns Protocol, designed to facilitate distributed communication and enable automated processes within the Towns network.

## Features

- 🤖 Automated message handling
- 💬 Towns Protocol integration
- 🔐 Secure communication
- 🚀 Easy deployment and configuration

## Prerequisites

- Node.js 16.0 or higher
- npm 7.0 or higher
- Basic understanding of Towns Protocol

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MansourDch/DCH-bot.git
cd DCH-bot
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file with your configuration:
```bash
cp .env.example .env
# Edit .env with your settings
```

## Usage

```bash
npm start
```

## Development

```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Run tests
npm test
```

## Project Structure

```
DCH-bot/
├── src/
│   ├── index.ts
│   ├── bot.ts
│   └── utils/
├── config/
├── tests/
├── package.json
├── tsconfig.json
└── README.md
```

## Configuration

Create a `.env` file in the root directory:

```
TOWNS_BOT_NAME=DCH-bot
TOWNS_BOT_ADDRESS=your_address_here
TOWNS_PRIVATE_KEY=your_private_key_here
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Towns Protocol Documentation](https://docs.towns.com)
- [GitHub - Towns Protocol](https://github.com/towns-protocol)

## Support

For issues and questions, please open an issue on GitHub.
