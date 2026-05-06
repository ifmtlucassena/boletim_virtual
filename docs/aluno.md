# Aluno

A classe `Aluno` gerencia os dados de identificação e as notas de cada estudante. Ela é responsável por armazenar, validar e expor as notas lançadas, garantindo que apenas valores dentro do intervalo permitido sejam aceitos.

---

## Métodos

### `adicionar_nota(nota: float) -> None`
Adiciona uma nota à lista interna do aluno.
- Aceita apenas valores numéricos entre 0.0 e 10.0 (inclusive).
- Lança `NotaInvalidaError` se a nota estiver fora do intervalo [0.0, 10.0].
- Lança `NotaInvalidaError` se o valor passado não for numérico.

### `get_notas() -> list`
Retorna a lista com todas as notas adicionadas ao aluno.
- Retorna lista vazia `[]` caso nenhuma nota tenha sido adicionada.
- Não lança exceções.

### `limpar_notas() -> None`
Remove todas as notas da lista interna do aluno.
- Após a chamada, `get_notas()` deve retornar `[]`.
- Não lança exceções.

### `get_quantidade_notas() -> int`
Retorna o número total de notas registradas para o aluno.
- Retorna `0` caso a lista esteja vazia.
- Não lança exceções.

---

## Regras de Negócio

1. O intervalo válido para notas é fechado: [0.0, 10.0].
2. Nota igual a 0.0 é válida.
3. Nota igual a 10.0 é válida.
4. Qualquer nota abaixo de 0.0 é inválida.
5. Qualquer nota acima de 10.0 é inválida.
6. Valores não numéricos (string, None, etc.) são inválidos.
7. A lista de notas começa vazia ao criar o aluno.
8. `limpar_notas` zera completamente a lista, independente do estado anterior.

---

## Cenários de Exceção

| Situação | Exceção lançada |
|---|---|
| `adicionar_nota(-1.0)` | `NotaInvalidaError` |
| `adicionar_nota(10.1)` | `NotaInvalidaError` |
| `adicionar_nota("oito")` | `NotaInvalidaError` |
| `adicionar_nota(None)` | `NotaInvalidaError` |
