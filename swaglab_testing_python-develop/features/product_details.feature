Feature: Ver detalles de los productos

Caracteristica:
Como usuario autenticado,
 quiero ver nombre, imagen, precio y descripción corta de cada producto,
 para entender mejor qué se ofrece.

  Background:
    Given el usuario navega a la página de SwagLabs
    When el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"

  Scenario Outline: Verificar detalles de un producto
    When el usuario hace clic en el producto "<producto>"
    Then debería ver el nombre "<nombre>", precio "<precio>" y descripción "<descripcion>"

    Examples:
      | producto               | nombre               | precio | descripcion                        |
      | Sauce Labs Backpack    | Sauce Labs Backpack  | $29.99 | carry.allTheThings()               |
      | Sauce Labs Bike Light  | Sauce Labs Bike Light| $9.99  | A red light for visibility