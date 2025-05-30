# language: es
Característica: Inicio de sesión en Swaglab
  Como usuario estándar
  Quiero iniciar sesión en la aplicación
  Para acceder a las funcionalidades

  Escenario: Inicio de sesión exitoso con usuario estándar
    Dado que estoy en la página de inicio de sesión de Swaglab
    Cuando ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    Y hago clic en el botón de login
    Entonces debo ver la página principal de productos
