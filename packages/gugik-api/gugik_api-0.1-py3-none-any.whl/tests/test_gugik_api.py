import pytest
import requests
from gugik_api.gugik_api import GUGiKAPI

def test_get_object_by_id():
    api = GUGiKAPI()
    response = api.get_object_by_id(request_type='GetParcelById', identifier='141201_1.0001.6509')
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.geom_wkb is not None

def test_get_object_by_xy():
    api = GUGiKAPI()
    response = api.get_object_by_xy(request_type='GetParcelByXY', coordinates='578919,371294')
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.geom_wkb is not None

def test_get_object_by_lat_lon():
    api = GUGiKAPI()
    response = api.get_object_by_lat_lon(request_type='GetParcelByXY', lat=50.06143, lon=19.93658)
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.geom_wkb is not None

def test_convert_to_lat_lon():
    api = GUGiKAPI()
    lat, lon = api.convert_to_lat_lon(578919, 371294)
    assert lat is not None
    assert lon is not None
    assert isinstance(lat, float)
    assert isinstance(lon, float)
    # Wartości spodziewane na podstawie narzędzia online
    expected_lat = 51.202911 
    expected_lon = 20.1299783 
    assert abs(lat - expected_lat) < 1e-6, f"Expected latitude {expected_lat}, but got {lat}"
    assert abs(lon - expected_lon) < 1e-6, f"Expected longitude {expected_lon}, but got {lon}"

def test_get_object_by_id_custom_format():
    api = GUGiKAPI()
    custom_format = 'teryt,id,region,county,geom_wkb'
    response = api.get_object_by_id(request_type='GetParcelById', identifier='141201_1.0001.6509', result_format=custom_format)
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.teryt is not None
    assert api.id is not None
    assert api.region is not None
    assert api.county is not None
    assert api.geom_wkb is not None

def test_get_object_by_xy_custom_format():
    api = GUGiKAPI()
    custom_format = 'teryt,id,region,county,geom_wkb'
    response = api.get_object_by_xy(request_type='GetParcelByXY', coordinates='578919,371294', result_format=custom_format)
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.teryt is not None
    assert api.id is not None
    assert api.region is not None
    assert api.county is not None
    assert api.geom_wkb is not None

def test_get_object_by_lat_lon_custom_format():
    api = GUGiKAPI()
    custom_format = 'teryt,id,region,county,geom_wkb'
    response = api.get_object_by_lat_lon(request_type='GetParcelByXY', lat=50.06143, lon=19.93658, result_format=custom_format)
    assert response is not None
    assert isinstance(response, bytes), "Response is not binary content"
    assert api.teryt is not None
    assert api.id is not None
    assert api.region is not None
    assert api.county is not None
    assert api.geom_wkb is not None

def test_get_object_by_id_invalid():
    api = GUGiKAPI()
    with pytest.raises(ValueError, match="No results returned for the given identifier"):
        api.get_object_by_id(request_type='GetParcelById', identifier='invalid_id')

def test_get_object_by_xy_invalid():
    api = GUGiKAPI()
    with pytest.raises(ValueError, match="No results returned for the given identifier"):
        api.get_object_by_xy(request_type='GetParcelByXY', coordinates='0,0')

def test_get_object_by_lat_lon_invalid():
    api = GUGiKAPI()
    with pytest.raises(ValueError, match="No results returned for the given identifier"):
        api.get_object_by_lat_lon(request_type='GetParcelByXY', lat=0.0, lon=0.0)
