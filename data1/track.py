import zipfile
import os

data0 = "D:\\Gry\\Steam Games\\steamapps\\common\\Dying Light 2\\ph\\source\\data0.pak"
data1 = "D:\\Gry\\Steam Games\\steamapps\\common\\Dying Light 2\\ph\\source\\data1.pak"
dataen = "D:\\Gry\\Steam Games\\steamapps\\common\\Dying Light 2\\ph\\source\\data_lang\\dataen.pak"

def zip_info(zip_file):
    if not zip_file.endswith(('.zip', '.pak')):
        raise ValueError("File must have a .zip or .pak extension")
    with zipfile.ZipFile(zip_file, 'r') as z:
        for file in z.infolist():
            crc = file.CRC
            size = file.file_size
            filename = file.filename
            folder, name = os.path.split(filename)
            txt_name = f"{os.path.splitext(name)[0]}.txt"
            if folder and not os.path.exists(folder):
                os.makedirs(folder)
            with open(os.path.join(folder, txt_name), 'w') as f:
                f.write(f"CRC: {crc}\nSize: {size} bytes")


zip_info(data1)

            
