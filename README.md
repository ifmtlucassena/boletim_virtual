# boletim_virtual

Sistema de gestão de notas escolares desenvolvido com TDD (Test-Driven Development). O projeto simula um contexto escolar, onde é possível cadastrar alunos, registrar notas, calcular médias, organizar turmas e classificar o desempenho acadêmico.

O objetivo principal da atividade foi praticar o ciclo Red/Green/Refactor, usando testes automatizados para guiar a implementação das entidades `Aluno`, `Turma`, `Media` e `ClassificadorDesempenho`.

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

```text
boletim_virtual/
├── src/
│   ├── __init__.py                     # Exporta as classes e exceções principais
│   ├── aluno.py                        # Classe Aluno
│   ├── media.py                        # Classe Media
│   ├── turma.py                        # Classe Turma
│   ├── classificador_desempenho.py     # Classe ClassificadorDesempenho
│   └── exceptions.py                   # Exceções customizadas do domínio
├── tests/
│   ├── __init__.py
│   ├── test_aluno.py
│   ├── test_media.py
│   ├── test_turma.py
│   └── test_classificador_desempenho.py
├── docs/
│   ├── aluno.md
│   ├── media.md
│   ├── turma.md
│   ├── classificador_desempenho.md
│   └── analise_beneficios.md           # Reflexão sobre TDD e benefícios do processo
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Como Instalar e Executar

Instalar as dependências:

```bash
pip install -r requirements.txt
```

Rodar os testes:

```bash
pytest
```

Rodar os testes com cobertura:

```bash
pytest --cov=src --cov-report=term-missing
```

## Documentação

- [Classe Aluno](docs/aluno.md)
- [Classe Media](docs/media.md)
- [Classe Turma](docs/turma.md)
- [Classe ClassificadorDesempenho](docs/classificador_desempenho.md)
- [Etapa 4 - Documentação e Análise dos Benefícios](docs/analise_beneficios.md)

## Resumo dos Resultados

Resultado atual da suíte de testes:

- **Testes coletados:** 24
- **Testes passando:** 24
- **Cobertura total:** 92%
- **Comando utilizado:** `pytest --cov=src --cov-report=term-missing`

## Status

![Etapa Atual](https://img.shields.io/badge/Etapa%20Atual-5%20%E2%80%94%20README%20final-blue)
![Testes](https://img.shields.io/badge/Testes-24%20passando-brightgreen)
![Cobertura](https://img.shields.io/badge/Cobertura-92%25-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11%2B-yellow)
![pytest](https://img.shields.io/badge/Framework-pytest-blue)

> Etapa 5 concluída: README atualizado, documentação organizada e resultados dos testes registrados.

## Cronograma

| Etapa | Descrição                                        | Entregável                                      | Prazo  |
|-------|--------------------------------------------------|-------------------------------------------------|--------|
| 1     | Levantamento de Requisitos                       | `docs/requisitos.md`                            | 23/04  |
| 2     | Configuração do Projeto                          | Repositório criado + estrutura vazia            | 30/04  |
| 3     | Implementação com TDD (parte 1 e 2)              | Commits Red/Green/Refactor + código completo    | 14/05  |
| 4     | Documentação e Análise dos Benefícios            | `docs/analise_beneficios.md`                    | 21/05  |
| 5     | README final e Organização do GitHub             | README finalizado + slides                      | 28/05  |
| 6     | Apresentação ao vivo para a turma                | Apresentação de 15 min (demonstração + análise) | 11-25/06 |
