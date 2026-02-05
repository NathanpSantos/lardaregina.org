def _tlv(tag: str, value: str) -> str:
    length = str(len(value)).zfill(2)
    return f"{tag}{length}{value}"

def _crc16(payload: str) -> str:
    # CRC-16/CCITT-FALSE
    poly = 0x1021
    crc = 0xFFFF
    for ch in payload:
        crc ^= (ord(ch) << 8)
        for _ in range(8):
            crc = ((crc << 1) ^ poly) if (crc & 0x8000) else (crc << 1)
            crc &= 0xFFFF
    return f"{crc:04X}"

def gerar_payload_pix(chave: str, nome: str, cidade: str, valor: str | None = None) -> str:
    # Nome até 25 e cidade até 15 (padrão EMV)
    nome = (nome or "LAR DA REGINA")[:25]
    cidade = (cidade or "GUARULHOS")[:15]

    gui = _tlv("00", "br.gov.bcb.pix")
    key = _tlv("01", chave)
    merchant_account = _tlv("26", gui + key)

    payload = ""
    payload += _tlv("00", "01")          # Payload Format Indicator
    payload += _tlv("01", "12")          # Point of Initiation Method (dinâmico)
    payload += merchant_account
    payload += _tlv("52", "0000")        # MCC
    payload += _tlv("53", "986")         # BRL
    if valor:
        payload += _tlv("54", valor)     # Valor opcional (ex: "25.00")
    payload += _tlv("58", "BR")
    payload += _tlv("59", nome)
    payload += _tlv("60", cidade)
    payload += _tlv("62", _tlv("05", "***"))  # Additional Data Field Template

    payload_crc = payload + "6304"
    crc = _crc16(payload_crc)
    return payload_crc + crc
