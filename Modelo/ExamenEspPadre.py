from Modelo.Examen import Examen
from Modelo.EstudiantePadre import EstudiantePadre

class ExamenEspPadre(Examen, EstudiantePadre):
    def __init__(self, est_id, fecha):
        EstudiantePadre.__init__(self, est_id)
        Examen.__init__(self, fecha)
