import os
import numpy as np
import soundfile as sf
import secrets

def xor_audio(input_path, output_folder, output_filename="output.wav", key=None):
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, output_filename)

    # Загрузка аудио и преобразование в int16
    data, samplerate = sf.read(input_path)
    if data.dtype != np.int16:
        data = (data * 32767).astype(np.int16)

    # Ключ
    if key is None or key == "":
        key = secrets.randbits(64)
        print(f"[ENCODE] Сгенерирован ключ: {key}")
        mode = "encode"
    else:
        key = int(key)
        print(f"[DECODE] Используется ключ: {key}")
        mode = "decode"

    # Инициализация генератора шума
    rng = np.random.default_rng(seed=key)
    noise = rng.integers(-32768, 32767, size=data.shape, dtype=np.int16)

    # Побитовая операция XOR
    result = np.bitwise_xor(data, noise)

    # Сохранение результата
    sf.write(output_path, result, samplerate, subtype="PCM_16")
    print(f"[{mode.upper()}] Файл сохранён в: {output_path}")

    return key if mode == "encode" else None

xor_audio('C:/Users/Давид 89307023143/Desktop/uh/original.wav', 'C:/Users/Давид 89307023143/Desktop/uh', 'bmp.wav', 8473666715916347842)