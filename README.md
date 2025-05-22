# 🔢 Advanced Number System Converter

A powerful Python utility for converting numbers between different number systems, including support for fractional numbers and bases from 2 to 36.

## 📋 Table of Contents

1. [Features](#-features)
2. [Technology Stack](#-technology-stack)
3. [Installation](#-installation)
4. [Usage](#-usage)
5. [Project Structure](#-project-structure)
6. [Examples](#-examples)
7. [Contributing](#-contributing)
8. [Contact](#-contact)

---

## ✨ Features

- **Multi-Base Support**: Convert numbers between any base from 2 to 36
- **Fractional Numbers**: Handle decimal points and fractional parts
- **High Precision**: Configurable precision for fractional conversions
- **Case-Insensitive**: Accepts both uppercase and lowercase letters for bases > 10
- **Input Validation**: Robust error handling for invalid inputs
- **Comprehensive Testing**: Includes multiple example conversions

---

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **Built-in Libraries**: No external dependencies required
- **Type Hints**: Modern Python type annotations for better code clarity

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone <your-repository-url>
cd <repository-name>
```

2. **No Additional Dependencies Required**

The project uses only Python standard library, so no additional installation is needed.

---

## 🔍 Usage

### Basic Usage

```python
from number_sys_conv import convert_base_fractional

# Convert binary to decimal
result = convert_base_fractional("101.101", 2, 10)
print(result)  # Output: 5.625

# Convert decimal to binary
result = convert_base_fractional("0.5", 10, 2)
print(result)  # Output: 0.1

# Convert hexadecimal to decimal
result = convert_base_fractional("1A.8", 16, 10)
print(result)  # Output: 26.5
```

### Function Parameters

```python
convert_base_fractional(
    number_str: str,    # Input number as string
    from_base: int,     # Source base (2-36)
    to_base: int,       # Target base (2-36)
    precision: int = 10 # Precision for fractional part
) -> str
```

---

## 📁 Project Structure

```plaintext
project/
│
├── number_sys_conv.py    # Main conversion module
├── main-1.ipynb          # Jupyter notebook with examples
└── README.md            # Project documentation
```

---

## 📝 Examples

### 1. Binary to Decimal Conversion
```python
result = convert_base_fractional("101.101", 2, 10)
# 101.101 (binary) = 5.625 (decimal)
```

### 2. Decimal to Binary Conversion
```python
result = convert_base_fractional("0.5", 10, 2)
# 0.5 (decimal) = 0.1 (binary)
```

### 3. Hexadecimal to Decimal Conversion
```python
result = convert_base_fractional("1A.8", 16, 10)
# 1A.8 (hex) = 26.5 (decimal)
```

### 4. Custom Precision
```python
result = convert_base_fractional("0.1", 10, 2, precision=20)
# Converts with 20 decimal places of precision
```

---

## 💡 Implementation Details

The converter uses a two-step process:
1. **To Decimal**: Converts the input number to decimal (base 10)
2. **From Decimal**: Converts the decimal number to the target base

### Key Features:
- Handles both integer and fractional parts
- Supports bases from 2 to 36 (using 0-9 and A-Z)
- Configurable precision for fractional parts
- Robust error handling for invalid inputs

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a Pull Request

---

## 📧 Contact

[Your Name]  
[Your GitHub Profile] | [Your Email]

---

> This project is designed for educational and practical purposes. It provides a robust solution for number system conversions with support for fractional numbers and various bases. 