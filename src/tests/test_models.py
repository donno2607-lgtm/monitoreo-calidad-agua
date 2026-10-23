
import unittest
from src.models import SensorPH, SensorTurbidez
from src.exceptions import SensorMalfunctionException, WaterQualityAlertException

class TestSensores(unittest.TestCase):

    def setUp(self):
        self.sensor_ph = SensorPH("PH-01", "Zona A")
        self.sensor_turb = SensorTurbidez("TURB-01", "Zona A")

    def test_datos_sensor(self):
        self.assertEqual(self.sensor_ph.id_sensor, "PH-01")
        self.assertEqual(self.sensor_ph.ubicacion, "Zona A")

    def test_falla_hardware(self):
        self.sensor_ph._activo = False
        with self.assertRaises(SensorMalfunctionException):
            self.sensor_ph.leer_valor()

    def test_lectura_general(self):
        try:
            val = self.sensor_ph.leer_valor()
            self.assertIsInstance(val, float)
        except WaterQualityAlertException:
            pass

if __name__ == "__main__":
    unittest.main()
