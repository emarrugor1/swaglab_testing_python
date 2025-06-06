1) Crear entorno virtual de python: 

```bash
python3 -m venv venv
source venv/bin/activate
```

2) Instalar dependencias:

```bash
pip install -r requirements.txt
```

3) Ejecutar test y generar resultados de Allure:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results features/ --tags @tag
```
4) Visualizar los resultados de Allure:

```bash
allure serve allure-results
```