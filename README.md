# boletim_virtual

Sistema de gestão de notas escolares desenvolvido com TDD (Test-Driven Development). O projeto cobre o ciclo Red/Green/Refactor para as entidades Aluno, Turma, Média e Classificador de Desempenho.

## Informações Acadêmicas

- **Curso:** Tecnologia em Sistemas para Internet
- **Disciplina:** Teste de Software
- **Docente:** Orlando Pereira Santana Junior
- **Discentes:** Wilgner Alexandre de Castro Mendes, Valéria Alves de Sousa, Lucas de Sena Diniz Santos, Andrey Viana Sena Mello

## Tecnologias

- Python 3.11+
- pytest
- pytest-cov

## Estrutura de Pastas

```
boletim_virtual/
├── src/
│   ├── __init__.py                     # Exporta todas as classes e exceções
│   ├── aluno.py                        # Classe Aluno
│   ├── media.py                        # Classe Media
│   ├── turma.py                        # Classe Turma
│   ├── classificador_desempenho.py     # Classe ClassificadorDesempenho
│   └── exceptions.py                   # Exceções customizadas
├── tests/
│   ├── __init__.py
│   ├── test_aluno.py
│   ├── test_media.py
│   ├── test_turma.py
│   └── test_classificador_desempenho.py
├── docs/                               # Documentação do projeto
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Como Instalar e Executar

```bash
pip install -r requirements.txt
```

Rodar os testes:
```bash
pytest
```

Rodar com cobertura:
```bash
pytest --cov=src --cov-report=term-missing
```

## Status

![Etapa Atual](https://img.shields.io/badge/Etapa%20Atual-2%20%E2%80%94%20Configura%C3%A7%C3%A3o%20do%20Projeto-blue)
![Testes](https://img.shields.io/badge/Testes-24%20coletados-brightgreen)
![Cobertura](https://img.shields.io/badge/Cobertura-0%25%20(stubs)-lightgrey)
![Python](https://img.shields.io/badge/Python-3.11%2B-yellow)
![pytest](https://img.shields.io/badge/Framework-pytest-blue)

> 🚧 Estrutura inicial criada. Implementação via TDD iniciará na Etapa 3.

## Cronograma

| Etapa | Descrição                                        | Entregável                                      | Prazo  |
|-------|--------------------------------------------------|-------------------------------------------------|--------|
| 1     | Levantamento de Requisitos                       | `docs/requisitos.md`                            | 23/04  |
| 2     | Configuração do Projeto                          | Repositório criado + estrutura vazia            | 30/04  |
| 3     | Implementação com TDD (parte 1 e 2)              | Commits Red/Green/Refactor + código completo    | 14/05  |
| 4     | Documentação e Análise dos Benefícios            | `docs/analise_beneficios.md`                    | 21/05  |
| 5     | README final e Organização do GitHub             | README finalizado + slides                      | 28/05  |
| 6     | Apresentação ao vivo para a turma                | Apresentação de 15 min (demonstração + análise) | 4–25/06|
