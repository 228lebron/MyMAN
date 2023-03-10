USD_rate = 75
air_shipping_cost = 5
sea_shipping_cost = 1

PACKAGE_WEIGHTS = {
    'SOIC-8': 0.32,
    'SOIC-14': 0.55,
    'TO-92': 0.16,
    'SOD-523': 0.3
}

# fix криво заполненых брендов
brand_mapping = {
    "AD": "Analog Devices",
    "ADI": "Analog Devices",
    "ANALOG DEVICES": "Analog Devices",
    'TI': 'Texas Instruments',
    'Texas': 'Texas Instruments',
    'TEXAS': 'Texas Instruments',
    # add more
}