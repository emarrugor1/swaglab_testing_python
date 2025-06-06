Feature: Iniciar sesión en SwagLabs

Caracteristica :
Como usuario autenticado,
 quiero ver todos los productos disponibles en una grilla,
 para poder decidir cuál comprar.

  Scenario: Usuario inicia sesión exitosamente
    Given el usuario navega a la página de SwagLabs
    When el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"
    Then debería ser redirigido al inventario

