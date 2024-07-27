import requests
from enum import Enum
from pyproj import Transformer


class ResultFormat(Enum):
    GEOM_WKB = "geom_wkb"
    GEOM_WKT = "geom_wkt"
    GEOM_EXTENT = "geom_extent"
    TERYT = "teryt"
    ID = "id"
    FUNCTION = "function"
    VOIVODESHIP = "voivodeship"
    COUNTY = "county"
    COMMUNE = "commune"
    REGION = "region"
    PARCEL = "parcel"


class GUGiKAPI:
    BASE_URL = "https://uldk.gugik.gov.pl/"

    def __init__(self):
        self.session = requests.Session()
        self.geom_wkb = None
        self.geom_wkt = None
        self.geom_extent = None
        self.teryt = None
        self.id = None
        self.function = None
        self.voivodeship = None
        self.county = None
        self.commune = None
        self.region = None
        self.parcel = None

    def _parse_response(self, response, result_format):
        """Pomocnicza metoda do parsowania odpowiedzi."""
        if response.content.startswith(b"-1"):
            raise ValueError("No results returned for the given identifier")

        content_str = response.content.decode("utf-8")
        result_fields = result_format.split(",")
        content_values = content_str.split("|")

        for key, value in zip(result_fields, content_values):
            if key in ResultFormat._value2member_map_:
                setattr(self, key, value.strip())

        return response.content

    def get_object_by_id(self, request_type, identifier, result_format="geom_wkb"):
        """
        Pobierz informacje o obiekcie przez identyfikator.

        :param request_type: Typ żądania (GetParcelById, GetBuildingById, GetRegionById, GetRegionByNameOrId, GetCommuneById, GetCountyById, GetVoivodeshipById)
        :param identifier: Identyfikator obiektu
        :param result_format: Format wyniku (np. 'teryt,id,region,county,geom_wkb')
        :return: Binary content response
        """
        if isinstance(result_format, ResultFormat):
            result_format = result_format.value

        params = {"request": request_type, "id": identifier, "result": result_format}
        response = self.session.get(self.BASE_URL, params=params)
        response.raise_for_status()

        return self._parse_response(response, result_format)

    def get_object_by_xy(self, request_type, coordinates, result_format="geom_wkb"):
        """
        Pobierz informacje o obiekcie przez współrzędne.

        :param request_type: Typ żądania (GetParcelByXY, GetBuildingByXY, GetRegionByXY, GetCommuneByXY, GetCountyByXY, GetVoivodeshipByXY)
        :param coordinates: Współrzędne punktu w formacie 'X,Y' lub 'X,Y,SRID'
        :param result_format: Format wyniku (np. 'teryt,id,region,county,geom_wkb')
        :return: Binary content response
        """
        if isinstance(result_format, ResultFormat):
            result_format = result_format.value

        params = {"request": request_type, "xy": coordinates, "result": result_format}
        response = self.session.get(self.BASE_URL, params=params)
        response.raise_for_status()

        return self._parse_response(response, result_format)

    def get_object_by_lat_lon(
        self, request_type, lat, lon, srid="4326", result_format="geom_wkb"
    ):
        """
        Pobierz informacje o obiekcie przez szerokość i długość geograficzną.

        :param request_type: Typ żądania (GetParcelByXY, GetBuildingByXY, GetRegionByXY, GetCommuneByXY, GetCountyByXY, GetVoivodeshipByXY)
        :param lat: Szerokość geograficzna (latitude)
        :param lon: Długość geograficzna (longitude)
        :param srid: Opcjonalny układ współrzędnych (domyślnie '4326')
        :param result_format: Format wyniku (np. 'teryt,id,region,county,geom_wkb')
        :return: Binary content response
        """
        coordinates = f"{lon},{lat},{srid}"
        return self.get_object_by_xy(request_type, coordinates, result_format)

    def convert_to_lat_lon(self, x, y, from_srid="2180", to_srid="4326"):
        """
        Konwertuj współrzędne z jednego układu odniesienia na inny.

        :param x: Współrzędna X
        :param y: Współrzędna Y
        :param from_srid: SRID układu źródłowego (domyślnie '2180')
        :param to_srid: SRID układu docelowego (domyślnie '4326')
        :return: Krotka (longitude, latitude)
        """
        transformer = Transformer.from_crs(
            f"epsg:{from_srid}", f"epsg:{to_srid}", always_xy=True
        )
        lon, lat = transformer.transform(x, y)
        return lat, lon


# Przykład użycia:
if __name__ == "__main__":
    from ll_convert import decimal_to_dms
    api = GUGiKAPI()

    # Pobierz działkę przez identyfikator z domyślnym formatem wyniku
    try:
        parcel_info = api.get_object_by_id(
            request_type="GetParcelById", identifier="141201_1.0001.6509"
        )
        print("Parcel Info:", parcel_info)
        print("geom_wkb:", api.geom_wkb)
        print("geom_wkt:", api.geom_wkt)
        print("geom_extent:", api.geom_extent)
        print("teryt:", api.teryt)
        print("id:", api.id)
        print("function:", api.function)
        print("voivodeship:", api.voivodeship)
        print("county:", api.county)
        print("commune:", api.commune)
        print("region:", api.region)
        print("parcel:", api.parcel)
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Pobierz działkę przez współrzędne z domyślnym formatem wyniku
    try:
        parcel_info = api.get_object_by_xy(
            request_type="GetParcelByXY", coordinates="578919,371294"
        )
        print("Parcel Info by XY:", parcel_info)
        print("geom_wkb:", api.geom_wkb)
        print("geom_wkt:", api.geom_wkt)
        print("geom_extent:", api.geom_extent)
        print("teryt:", api.teryt)
        print("id:", api.id)
        print("function:", api.function)
        print("voivodeship:", api.voivodeship)
        print("county:", api.county)
        print("commune:", api.commune)
        print("region:", api.region)
        print("parcel:", api.parcel)
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Pobierz działkę przez szerokość i długość geograficzną z domyślnym formatem wyniku
    try:
        parcel_info = api.get_object_by_lat_lon(
            request_type="GetParcelByXY", lat=51.202911849030386, lon=20.129978380644378
        )
        print("Parcel Info by Lat Lon:", parcel_info)
        print("geom_wkb:", api.geom_wkb)
        print("geom_wkt:", api.geom_wkt)
        print("geom_extent:", api.geom_extent)
        print("teryt:", api.teryt)
        print("id:", api.id)
        print("function:", api.function)
        print("voivodeship:", api.voivodeship)
        print("county:", api.county)
        print("commune:", api.commune)
        print("region:", api.region)
        print("parcel:", api.parcel)
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Konwersja współrzędnych z EPSG:2180 do EPSG:4326 za pomocą pyproj
    x, y = 578919, 371294
    lat, lon = api.convert_to_lat_lon(x, y)
    print(f"Converted coordinates using pyproj: lat={lat}, lon={lon}")
    print(decimal_to_dms(lat, lon))
