def decimal_to_dms(lat, lon):
    def convert(decimal):
        degrees = int(decimal)
        minutes = int((decimal - degrees) * 60)
        seconds = (decimal - degrees - minutes / 60) * 3600
        return degrees, minutes, seconds

    lat_deg, lat_min, lat_sec = convert(abs(lat))
    lon_deg, lon_min, lon_sec = convert(abs(lon))

    lat_hemisphere = "N" if lat >= 0 else "S"
    lon_hemisphere = "E" if lon >= 0 else "W"

    lat_dms = f"{lat_deg}°{lat_min}'{lat_sec:.2f}\"{lat_hemisphere}"
    lon_dms = f"{lon_deg}°{lon_min}'{lon_sec:.2f}\"{lon_hemisphere}"

    return lat_dms, lon_dms


if __name__ == "__main__":
    # Przykład użycia:
    lat = 51.202911849030386
    lon = 20.129978380644378
    lat_dms, lon_dms = decimal_to_dms(lat, lon)
    print(f"Latitude in DMS: {lat_dms}")
    print(f"Longitude in DMS: {lon_dms}")
