# Tạo QR code của Website với Python bằng thư viện QRcode


import qrcode
from PIL import Image
import os

def generate_qr_code(url, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(save_path)

if __name__ == "__main__":
    url = input("Nhập liên kết web mà bạn muốn chuyển sang mã QR: ")

    download_folder = os.path.expanduser("~") + "/Downloads/"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    save_path = os.path.join(download_folder, "qrcode.png")

    generate_qr_code(url, save_path)

    print(f"QR code của bạn đã được lưu tại: {save_path}")