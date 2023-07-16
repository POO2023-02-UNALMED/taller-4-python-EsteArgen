from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    
    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    def listadoAsignaturas(self, **kwargs):
        for key in kwargs:
            if self._asignaturas is None:
                self._asignaturas = []
            self._asignaturas.append(Asignatura(kwargs[key]))

    def agregarAlumno(self, alumno, lista = None):
        if(lista is None):
            lista = []
            lista.append(alumno)
        else:
            lista.append(alumno)
        
        if self.listadoAlumnos is None:
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + lista

        
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
