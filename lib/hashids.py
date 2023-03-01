"""
Cifrado y descrifado de ID por medio de Hashids
"""
from typing import Any
import re
from hashids import Hashids

from config.settings import SALT

hashids = Hashids(SALT, min_length=8)
hashid_regexp = re.compile("[0-9a-zA-Z]{8,16}")


def cifrar_id(un_id: int) -> str:
    """Cifrar ID"""
    return hashids.encode(un_id)


def descifrar_id(un_id_hasheado: str) -> Any:
    """Descifrar ID"""
    if hashid_regexp.match(un_id_hasheado):
        solicitud_id = hashids.decode(un_id_hasheado)
        if len(solicitud_id) == 1:
            return solicitud_id[0]
    return None

def decrypt_id(un_id_hasheado: str) -> Any:
    result = re.match("[0-9a-zA-Z]{8,16}", un_id_hasheado)
    solicitud_id = hashids.decode(un_id_hasheado)
    if len(solicitud_id) == 1:
        return  solicitud_id[0]
    