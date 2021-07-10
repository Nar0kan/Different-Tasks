from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    # check if it's not the night time
    hour = int(time[0])*10 + int(time[1])
    minutes = int(time[3])*10 + int(time[4])
    
    if hour < 6:
        return "I don't see the sun!"
    elif hour >= 18 and minutes != 0:
        return "I don't see the sun!"

    # formula
    res = float((hour - 6) * 15 + minutes * 0.25)
    
    return res


if __name__ == '__main__':
    print(sun_angle("12:15"), sun_angle("18:01"))
