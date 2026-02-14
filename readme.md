
# 🧮 CalcHistory: The Calculator That Never Forgets

**CalcHistory** is a robust Python-based CLI (Command Line Interface) tool that performs basic arithmetic while maintaining a persistent log of your mathematical journey. No more forgetting what you calculated five minutes ago!

---

## 🚀 Features

* **Standard Operations:** Handles Addition, Subtraction, Multiplication, Division, and Modulus.
* **Persistent History:** Automatically saves every successful calculation to `History.txt`.
* **Safety First:** Includes "rock-solid" error handling for division by zero, invalid inputs, and missing history files.
* **Clean Slate:** Built-in functionality to wipe your history whenever you want to start fresh.

---

## 🛠️ How It Works

The application uses a dedicated `CalculatorWithHistory` class to manage both the math logic and the file I/O operations.

### Functionality Overview

| Feature | Description |
| --- | --- |
| **Perform Calculations** | Input expressions in the format `8 + 8`. |
| **View History** | Reads and displays the contents of `History.txt`. |
| **Clear History** | Wipes the `History.txt` file clean. |
| **Input Validation** | Guards against crashes from typos or bad formatting. |

---

## 📋 Installation & Usage

1. **Prerequisites:** Ensure you have **Python 3.x** installed.
2. **Clone the Repo:**
```bash
git clone https://github.com/yourusername/CalcHistory.git
cd CalcHistory

```


3. **Run the App:**
```bash
python main.py

```



### Example Usage

```text
Input format: 8 + 8 (Include spaces!)
Please Enter calculations: 10 * 5
Result: 50.0

```

---

## 📂 File Structure

* `main.py`: The core Python script containing the logic.
* `History.txt`: Created automatically on your first calculation to store your data.
* `README.md`: You are looking at it!

---

## 🛡️ Error Handling

This calculator is built to be resilient:

* **ZeroDivisionError:** Prevented with custom checks.
* **ValueError:** Handles cases where users enter text instead of numbers.
* **FileNotFoundError:** Gracefully notifies the user if the history log hasn't been created yet.

---

> **Note:** This project was developed with a focus on **DRY (Don't Repeat Yourself)** principles and clean file stream management using Python's `with` statement.

---