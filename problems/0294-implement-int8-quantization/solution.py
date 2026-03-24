import numpy as np
import math
import numpy as np

def int8_quantize(x: list[float]) -> dict:
    arr = np.array(x, dtype=np.float32)

    maximum = np.max(np.abs(arr))

    if maximum == 0:
        scale = np.float32(1.0)
    else:
        scale = np.float32(maximum / np.float32(127.0))

    quantized = np.clip(np.round(arr / scale), -127, 127).astype(np.int32).tolist()

    result = {
        'quantized': quantized,
        'scale': round(float(scale), 6),
        'dequantized': [round(float(np.float32(q) * scale), 4) for q in quantized]
    }

    return result