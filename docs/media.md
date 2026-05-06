# Media

A classe `Media` concentra todos os cálculos matemáticos e validações de intervalo de notas do sistema. Ela não armazena estado — opera exclusivamente sobre os dados recebidos como parâmetro, funcionando como um serviço de cálculo reutilizável.

---

## Métodos

### `media_simples(notas: list) -> float`
Calcula e retorna a média aritmética simples da lista de notas recebida.
- Retorna a soma das notas dividida pela quantidade de elementos.
- Lança `ListaNotasVaziaError` se a lista estiver vazia.

### `validar_intervalo(nota: float) -> bool`
Verifica se uma nota está dentro do intervalo permitido [0.0, 10.0].
- Retorna `True` se a nota estiver dentro do intervalo (inclusive os extremos).
- Retorna `False` se a nota estiver fora do intervalo.
- Não lança exceções — apenas valida e retorna booleano.

### `verificar_discrepancia(notas: list) -> bool`
Verifica se existe discrepância alta entre as notas da lista.
- Retorna `True` se a diferença entre a maior e a menor nota for maior que 5.0.
- Retorna `False` se a diferença for menor ou igual a 5.0.
- Lança `ListaNotasVaziaError` se a lista estiver vazia.

---

## Regras de Negócio

1. O intervalo válido para notas é fechado: [0.0, 10.0].
2. `validar_intervalo` nunca lança exceção — apenas retorna `True` ou `False`.
3. `media_simples` com lista vazia lança `ListaNotasVaziaError`.
4. `verificar_discrepancia` com lista vazia lança `ListaNotasVaziaError`.
5. Discrepância é considerada alta quando `max(notas) - min(notas) > 5.0`.
6. Diferença exatamente igual a 5.0 não é considerada discrepância alta.

---

## Cenários de Exceção

| Situação | Exceção lançada |
|---|---|
| `media_simples([])` | `ListaNotasVaziaError` |
| `verificar_discrepancia([])` | `ListaNotasVaziaError` |
