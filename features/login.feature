Feature: Inicio de sesión en Swaglab
  Como usuario estándar
  Quiero iniciar sesión en la aplicación
  Para acceder a las funcionalidades

  Scenario: Inicio de sesión exitoso con usuario estándar
    Given que estoy en la página de inicio de sesión de Swaglab
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And hago clic en el botón de login
    Then debo ver la página principal de productos

