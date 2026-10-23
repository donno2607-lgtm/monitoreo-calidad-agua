from typing import List, Dict, Any
from src.models import Sensor
from src.exceptions import SensorMalfunctionException, WaterQualityAlertException

class GestorSensores:
    def __init__(self):
        self._coleccion_sensores: List[Sensor] = []

    def agregar_sensor(self, sensor: Sensor) -> None:
        if isinstance(sensor, Sensor):
            self._coleccion_sensores.append(sensor)
        else:
            raise TypeError("Objeto no válido para el gestor.")

    def recolectar_datos_masivos(self) -> List[Dict[str, Any]]:
        resultados = []
        
        for sensor in self._coleccion_sensores:
            registro = {
                "id": sensor.id_sensor,
                "ubicacion": sensor.ubicacion,
                "estado": "OK",
                "lectura": None,
                "mensaje": "Normal"
            }

            try:
                valor = sensor.leer_valor()
                registro["lectura"] = valor
            except WaterQualityAlertException as e:
                registro["estado"] = "ALERTA"
                registro["mensaje"] = str(e)
            except SensorMalfunctionException as e:
                registro["estado"] = "FALLO"
                registro["mensaje"] = str(e)
            except Exception as e:
                registro["estado"] = "ERROR"
                registro["mensaje"] = str(e)

            resultados.append(registro)

        return resultados
