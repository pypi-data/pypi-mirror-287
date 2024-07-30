import base64
import json
from .errors import *

async def encode(
    value: any,
    cycles: int
) -> any:
    try:
        value = json.dumps(value)
        text = str(value)
    except:
        raise ConvertError("Value cannot be converted")
    
    for _ in range(cycles):
        text = text.encode()
        text = base64.b64encode(text).decode()
    return text

async def decode(
    text: str,
    cycles: int
) -> any:
    for _ in range(cycles):
        text = text.encode()
        text = base64.b64decode(text).decode()
    value = json.loads(text)
    return value
