from QRCraft import generate_qr_code, save_qr_image

# Generate QR code for an integer
int_qr = generate_qr_code(123456, mode='integer')
save_qr_image(int_qr, 'int_qr_code.png')
