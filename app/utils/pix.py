import re
import crcmod

def _sanitize(txt: str) -> str:
    txt = txt.strip()
    # remove caracteres que podem quebrar padrão
    return re.sub(r"\s+", " ", txt)

def _emv(id_: str, value: str) -> str:
    value = "" if value is None else str(value)
    return f"{id_}{len(value):02d}{value}"

def _crc16(payload: str) -> str:
    crc16_func = crcmod.predefined.mkCrcFun("crc-ccitt-false")
    crc = crc16_func(payload.encode("utf-8"))
    return f"{crc:04X}"

def gerar_payload_pix(chave: str, nome: str, cidade: str, valor=None, txid="***") -> str:
    """
    Gera payload PIX (copia e cola) padrão EMV.
    valor=None -> doação livre.
    """
    chave = _sanitize(chave)
    nome = _sanitize(nome)[:25]
    cidade = _sanitize(cidade)[:15]
    txid = _sanitize(txid)[:25] or "***"

    # Merchant Account Information (GUI + chave)
    mai = (
        _emv("00", "BR.GOV.BCB.PIX") +
        _emv("01", chave)
    )
    mai = _emv("26", mai)

    payload = ""
    payload += _emv("00", "01")          # Payload Format Indicator
    payload += _emv("01", "12")          # Point of Initiation Method (12 = dinâmico / pode ser estático tb)
    payload += mai
    payload += _emv("52", "0000")        # Merchant Category Code
    payload += _emv("53", "986")         # BRL
    if valor is not None and str(valor).strip() != "":
        payload += _emv("54", f"{float(valor):.2f}")  # Transaction Amount
    payload += _emv("58", "BR")          # Country Code
    payload += _emv("59", nome)          # Merchant Name
    payload += _emv("60", cidade)        # Merchant City

    # Additional Data Field Template (TXID)
    adft = _emv("05", txid)
    payload += _emv("62", adft)

    # CRC16
    payload_sem_crc = payload + "6304"
    payload += _emv("63", _crc16(payload_sem_crc))

    return payload
