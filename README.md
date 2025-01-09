![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# Projet Secu Houtrique Thomas

## Type safety & pep8
Code conforme à PEP 8 et 100% statiquement typé.

## build image docker
```bash
 docker build -t secu:latest .
```

## Execution du programme (Docker)
```
docker run -it secu:latest python3 main.py
```

## Installation des modules
```bash
python3 -m pip install -r requirements.txt
```

### Éxecution du script
```bash
python3 main.py
```

### Unittest
```bash
python3 test_unit.py
```