from wata.geo.utils import utils, coord_trans

class GeoProcess:
    
    @staticmethod
    def WGS84_to_GCJ02(lat, lon):
        return coord_trans.WGS84_to_GCJ02(lat, lon)
    @staticmethod
    def WGS84_to_BD09(lat, lon):
        return coord_trans.WGS84_to_BD09(lat, lon)
    @staticmethod
    def WGS84_to_UTM(lat, lon):
        return coord_trans.WGS84_to_UTM(lat, lon)

    @staticmethod
    def GCJ02_to_WGS84(lat, lon):
        return coord_trans.GCJ02_to_WGS84(lat, lon)
    @staticmethod
    def GCJ02_to_BD09(lat, lon):
        return coord_trans.GCJ02_to_BD09(lat, lon)

    @staticmethod
    def BD09_to_GCJ02(lat, lon):
        return coord_trans.BD09_to_GCJ02(lat, lon)
    @staticmethod
    def BD09_to_WGS84(lat, lon):
        return coord_trans.BD09_to_WGS84(lat, lon)
    
    @staticmethod
    def UTM_to_WGS84(easting, northing, zone_number, zone_letter):
        return coord_trans.UTM_to_WGS84(easting, northing, zone_number, zone_letter)