def checkDirection(deg):
    direction = ""
    if (deg >= 345 and deg < 361) or (deg >= 0 and deg < 15):
        direction = "С"
    elif (deg >= 15 and deg < 75):
        direction = "СВ"
    elif (deg >= 75 and deg < 105):
        direction = "В"
    elif (deg >= 105 and deg < 165):
        direction = "ЮВ"
    elif (deg >= 165 and deg < 195):
        direction = "Ю"
    elif (deg >= 195 and deg < 255):
        direction = "ЮЗ"
    elif (deg >= 255 and deg < 285):
        direction = "З"
    elif (deg >= 285 and deg < 345):
        direction = "СЗ"
    return direction