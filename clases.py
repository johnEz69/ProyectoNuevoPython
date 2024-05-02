
class Encargado:
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    @property
    def nombre(self):#retorna el atributo nombre de la clase encargado
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre):#cambia el nombre de la clase encargado
        self._nombre = nuevoNombre

    @property
    def dni(self):#retorna el dni 
        return self._dni

    @dni.setter
    def dni(self, nuevoDni):#cambia el dni por uno nuevo
        self._dni = nuevoDni

    def __eq__(self, other):#compara objetos
        return self.nombre == other.nombre and self.dni == other.dni

    def __str__(self):#
        return f"Nombre: {self.nombre}, DNI: {self.dni}"

    def __repr__(self):
        return f"Encargados:('{self.nombre}', '{self.dni}')"



### CLASE PROFESOR#############################

class Profesor:
    def __init__(self, nombre, materia, curso, division):
        self._nombre = nombre
        self._materia = materia
        self._curso = curso
        self._division = division

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, nuevaMateria):
        self._materia = nuevaMateria

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, nuevoCurso):
        self._curso=nuevoCurso


    @property
    def division(self):
       return self._division
        
    @division.setter
    def division(self,nuevaDivision):
        self._division=nuevaDivision
        
        
    def __eq__(self, other): #compara objetos
        return self.nombre == other.nombre and self.materia == other.materia and self.curso ==other.curso and self.division == other.division

    def __str__(self):#
        return f"Nombre: {self.nombre}, Materia: {self.materia}, Curso: {self.curso}, Division: {self.division}"
    
    def __repr__(self):
        return f"Profesores: ('{self.nombre}', '{self.materia}','{self.curso}','{self.division}')"








class Inscripciones:
    def __init__(self, fecha, nombre, dni, profesor, curso, division, nota):
        self._fecha = fecha
        self._nombre = nombre
        self._dni = dni
        self._profesor = profesor
        self._curso = curso
        self._division = division
        self._nota = nota

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nuevaFecha):
        self._fecha = nuevaFecha

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevoDni):
        self._dni = nuevoDni

    
    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, nuevoProfesor):
        self._profesor = nuevoProfesor

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, nuevoCurso):
        self._curso = nuevoCurso

    @property
    def division(self):
        return self._division

    @division.setter
    def division(self, nuevaDivision):
        self._division = nuevaDivision

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nuevaNota):
        self._nota = nuevaNota

 
    def __eq__(self, other):
        return (
            self.fecha == other.fecha
            and self.nombre == other.nombre
            and self.dni == other.dni
            and self.profesor == other.profesor
            and self.curso == other.curso
            and self.division == other.division
            and self.nota == other.nota
        )

    def __str__(self):
         return (f"Fecha: {self.fecha}, "
            f"Nombre: {self.nombre}, "
            f"DNI: {self.dni}, "
            f"Profesor: {self.profesor}, "
            f"Curso: {self.curso}, "
            f"División: {self.division}, "
            f"Nota: {self.nota}"
                )

    def __repr__(self):
          return (f"Inscripcion: ('{self.fecha}', '{self.nombre}', '{self.dni}','{self.profesor}', '{self.curso}' , '{self.division}', '{self.nota}'),")

      
    














     
