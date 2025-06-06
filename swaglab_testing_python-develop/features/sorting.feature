
Feature: Ordenamiento de productos en SwagLabs

Caracteristica :
 Como usuario,
 quiero poder ordenar los productos por nombre o precio,
 para encontrar más fácilmente lo que me interesa.


  Background:
    Given el usuario navega a la página de SwagLabs
    When el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"

  Scenario: Verificar ordenamiento A-Z
    Then los productos deben estar ordenados alfabéticamente de la A a la Z

  Scenario: Verificar ordenamiento Z-A
    Then los productos deben estar ordenados alfabéticamente de la Z a la A

  Scenario: Verificar ordenamiento por precio menor a mayor
    Then los productos deben estar ordenados por precio de menor a mayor

  Scenario: Verificar ordenamiento por precio mayor a menor
    Then los productos deben estar ordenados por precio de mayor a menor

