def get_temp_color(temp_c):
    if temp_c <= -30:
        return "#003366"  # Deep Blue
    elif temp_c <= -20:
        return "#4A90E2"  # Ice Blue
    elif temp_c <= -10:
        return "#B3DFFD"  # Light Blue
    elif temp_c <= 0:
        return "#E6F7FF"  # Pale Grayish Blue
    elif temp_c <= 10:
        return "#D1F2D3"  # Light Green
    elif temp_c <= 20:
        return "#FFFACD"  # Soft Yellow
    elif temp_c <= 30:
        return "#FFCC80"  # Light Orange
    elif temp_c <= 40:
        return "#FF7043"  # Deep Orange
    else:
        return "#D32F2F"  # Bright Red

def get_wind_color(wind_kph):
    if wind_kph <= 10:
        return "#E0F7FA"  # Light Cyan
    elif wind_kph <= 20:
        return "#B2EBF2"  # Pale Blue
    elif wind_kph <= 40:
        return "#4DD0E1"  # Soft Teal
    elif wind_kph <= 60:
        return "#0288D1"  # Bright Blue
    else:
        return "#01579B"  # Deep Navy Blue

def get_cloud_color(cloud):
    if cloud <= 10:
        return "#FFF9C4"  # Light Yellow
    elif cloud <= 30:
        return "#FFF176"  # Soft Yellow
    elif cloud <= 60:
        return "#E0E0E0"  # Light Gray
    elif cloud <= 90:
        return "#9E9E9E"  # Gray
    else:
        return "#616161"  # Dark Gray