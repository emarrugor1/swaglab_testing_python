Feature: Funcionalidad del carrito de compras en SwagLabs

Caracteristica:  Como usuario,
 quiero ver un indicador de cuántos productos tengo en el carrito,
 para llevar un control mientras navego el catálogo.


  Background:
    Given el usuario navega a la página de SwagLabs
    And el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"

  Scenario: Verificar visibilidad del ícono del carrito
    Then el ícono del carrito debe ser visible

  Scenario: Verificar que el contador se actualiza al agregar y quitar un producto
    When el usuario agrega "Sauce Labs Backpack" al carrito
    Then el contador del carrito debe mostrar "1"
    When el usuario elimina "Sauce Labs Backpack" del carrito
    Then el carrito debe estar vacío

  Scenario: Verificar que el carrito está vacío inicialmente
    Then el carrito debe estar vacío
