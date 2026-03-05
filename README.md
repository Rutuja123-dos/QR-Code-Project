# 📱 Professional QR Code Generator

A Python-based utility to generate high-quality, customized QR codes. This project was developed to bridge the gap between physical networking and digital professional profiles by creating a scannable link to my LinkedIn.

## 🚀 Features
* **Custom Styling:** Adjusts border size, box size, and versioning.
* **Error Correction:** Uses `ERROR_CORRECT_H` (High) to ensure the QR remains scannable even if slightly damaged or covered.
* **Image Generation:** Utilizes the `Pillow` library to render the final QR as a `.png` file.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** * `qrcode`: For generating the matrix.
    * `Pillow (PIL)`: For image processing and saving. 

## 📂 Project Structure
* `Qr code.py`: The main script containing the logic.
* `linkedin.png`: The generated output linking to my professional profile.

## ⚙️ How to Run
1. Install the required dependencies:
   pip install qrcode[pil]
2. Run the script:
   python "Qr code.py"
## 👤 Author
Rutuja Wagh
