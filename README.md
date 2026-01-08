# Tool Center

A comprehensive collection of developer utilities and tools designed to streamline your development workflow. Built with vanilla HTML, JavaScript, and Tailwind CSS for maximum performance and simplicity.

## 🚀 Features

- **Client-Side Processing**: All tools run entirely in the browser. Your data never leaves your device.
- **Responsive Design**: Fully adapted for desktop, tablet, and mobile screens.
- **Zero Dependencies**: Lightweight implementation using CDN-hosted Tailwind CSS and FontAwesome.
- **Tool Request System**: Integrated feedback form to collect user requests for new tools.

## 🛠 Available Tools

### Data Formatting & Conversion
- **[JSON Formatter](json-formatter.html)**: Minify, beautify, and validate JSON data.
- **[XML Formatter](xml-formatter.html)**: Format and prettify XML structures.
- **[Base64 Encoder/Decoder](base64-encoder.html)**: Encode and decode data to/from Base64 format.
- **[URL Parser](url-parser.html)**: Parse URLs into their components (protocol, host, path, query params).
- **[Unix Timestamp Converter](timestamp-converter.html)**: Convert between Unix timestamps and human-readable dates.

### Security & Cryptography
- **[JWT Decoder](jwt-decoder.html)**: Decode, inspect, and verify JSON Web Tokens (JWT) signatures.
- **[MD5 Generator](md5-generator.html)**: Generate MD5 hashes from text input.

### Development & Design
- **[JSON Diff](json-diff.html)**: Compare two JSON objects and highlight differences.
- **[Color Picker](color-picker.html)**: Convert between Hex, RGB, and HSL color formats.
- **[Gradient Maker](gradient-maker.html)**: Create CSS gradients visually and copy the code.

## ⚙️ Administration

The project includes a lightweight admin interface for managing tool requests.

- **[Admin Panel](admin.html)**: View user-submitted tool requests (stored locally in `localStorage` for demo purposes).

## 💻 Tech Stack

- **HTML5**: Semantic structure.
- **Tailwind CSS**: Utility-first styling via CDN.
- **Vanilla JavaScript**: Core logic without heavy frameworks.
- **FontAwesome**: Icons and UI elements.
- **CryptoJS**: For cryptographic operations (MD5, HMAC, etc.).

## 📦 Usage

### Quick Start
You can access the live version directly at:  
👉 **[https://uxai2046.github.io/toolhub](https://uxai2046.github.io/toolhub)**

### Local Development
Since this is a static site, you can run it locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/uXAi2046/toolhub.github.io.git
   ```
2. Open `index.html` in your browser.
3. Or serve it using a simple HTTP server (e.g., Python):
   ```bash
   python3 -m http.server 8000
   ```

## 🤝 Contributing

Contributions are welcome! If you have a new tool idea:

1. Fork the repository.
2. Create a new HTML file for your tool (copy an existing one as a template).
3. Add your tool logic and update `index.html`.
4. Submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
