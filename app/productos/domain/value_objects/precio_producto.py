from pydantic import BaseModel, Field, field_validator

class PrecioProducto(BaseModel):
    valor: int = Field(..., description="Nombre del producto")

    #reglas de validacion
    @field_validator("valor")# Este método se ejecuta cada vez que se crea un objeto para validar el campo
    def validator_precio_positivo(cls, v): #cls es obligatorio en la sintaxis pydantic, es como un self en una instancia
        if v < 0:
            raise ValueError("El precio no puede ser negativo")
        return v
    
    #Esto define cuándo dos objetos PrecioProducto son iguales
    def __eq__(self, other):
        return isinstance(other, PrecioProducto) and self.valor == other.valor

    #Esto permite que al imprimir el objeto, muestre el valor.
    def __str__(self):
        return f"{self.valor:.2f}" # parseamos la salida a 2 decimales.