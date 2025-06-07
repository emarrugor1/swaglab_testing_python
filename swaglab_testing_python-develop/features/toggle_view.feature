Feature: Alternar vista de productos

  Como usuario en SwagLabs
  Quiero poder alternar entre la vista de grilla y lista
  Para visualizar los productos según mi preferencia

  Background:
    Given el usuario ha iniciado sesión exitosamente

  Scenario: Cambiar de vista y mantener orden
    When el usuario aplica el ordenamiento por precio de menor a mayor
    And el usuario alterna la vista de productos
    Then la vista debe cambiar correctamente
    And el orden de productos debe mantenerse
    And el botón debe reflejar la vista activa
