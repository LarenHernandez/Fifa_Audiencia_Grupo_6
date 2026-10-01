"""Fase 1: carga y validacion del CSV."""

from pathlib import Path
import pandas as pd
from Luken.excepciones import DatasetInvalidoError


class CargarCSV:
    """Lee un CSV y valida que tiene la estructura esperada."""

    COLUMNAS_ESPERADAS = ("country", "confederation", "population_share", "tv_audience_share", "gdp_weighted_share")

    def __init__(self, ruta, separador=","):
        self._ruta = Path(ruta)
        self._separador = separador

    @property
    def ruta(self):
        return self._ruta

    def cargar(self):
        if not self._ruta.exists():
            raise FileNotFoundError(f"No existe el fichero: {self._ruta}")
        df = pd.read_csv(self._ruta, sep=self._separador)
        self._validar(df)
        return df

    def _validar(self, df):
        if df.empty:
            raise DatasetInvalidoError("El dataset esta vacio")
        faltan = [c for c in self.COLUMNAS_ESPERADAS if c not in df.columns]
        if faltan:
            raise DatasetInvalidoError(f"Faltan columnas obligatorias: {faltan}")
