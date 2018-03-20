import pyqrcode
import time

# Replace this with your own path

PATH_TO_IMAGE = 'C:\\Users\\rupachak\\Documents\\Github\\QR Code Server\\static\\generated_qr\\'


def generate_and_save_png(content):
    qr_code = pyqrcode.create(content)
    filename = str(time.time()) + '.png'
    total_path = PATH_TO_IMAGE + filename
    qr_code.png(total_path,scale=10)
    return filename

