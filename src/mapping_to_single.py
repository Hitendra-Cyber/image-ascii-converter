from src.constants import character_ramp

def map_brightness_char(brightness_value:int) -> str:
    if 0 > brightness_value or brightness_value > 255:
        raise Exception("Index error. Index provided is out of range of 0-255")
    if( 0 <= brightness_value < 28):
        return character_ramp[0]
    elif( 28 <= brightness_value < 56):
        return character_ramp[1]
    elif(56 <= brightness_value < 84):
        return character_ramp[2] 
    elif(84 <= brightness_value < 112):
        return character_ramp[3] 
    elif(112 <= brightness_value < 140):
        return character_ramp[4]
    elif(140 <= brightness_value < 168):
        return character_ramp[5]
    elif(168 <= brightness_value < 196):
        return character_ramp[6]
    elif(196 <= brightness_value < 220):
        return character_ramp[7]
    elif(224 <= brightness_value < 240):
        return character_ramp[8]
    else:
        return character_ramp[9]