from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    """
        Check if it's not the night time. If so - return sun angle. If not - return message "I don't see the sun!".
    """
    hour = int(time[0])*10 + int(time[1])
    minutes = int(time[3])*10 + int(time[4])
    
    if hour < 6:
        return "I don't see the sun!"
    elif hour >= 18 and minutes != 0:
        return "I don't see the sun!"

    # formula
    result = float((hour - 6) * 15 + minutes * 0.25)
    return result

if __name__ == '__main__':
    print(sun_angle("12:15")) # 93.75
    print(sun_angle("12:00")) # 90.0
    print(sun_angle("16:20")) # 155.0
    print(sun_angle("18:01")) # I don't see the sun!