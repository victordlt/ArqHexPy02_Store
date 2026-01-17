from pydantic import BaseModel, Field, field_validator

class NombreProducto(BaseModel):
    valor: str = Field(..., description="Nombre del producto")

    #reglas de validacion
    @field_validator("valor")# Este método se ejecuta cada vez que se crea un objeto para validar el campo
    def validator_nombre(cls, v): #cls es obligatorio en la sintaxis pydantic, es como un self en una instancia
        if not v.strip(): # strip elimina espacios
            raise ValueError("El nombre no puede estar vacio")
        if len(v) > 50:
            raise ValueError("El nombre no puede exceder los 50 caracteres")
        return v
    
    #Esto define cuándo dos objetos NombreProducto son iguales
    def __eq__(self, other):
        return isinstance(other, NombreProducto) and self.valor == other.valor

    #Esto permite que al imprimir el objeto, muestre el valor.
    def __str__(self):
        return self.valor