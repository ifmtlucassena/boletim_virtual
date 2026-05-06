# Turma

A classe `Turma` agrupa instâncias de `Aluno` e gera estatísticas conjuntas sobre o desempenho coletivo. Ela controla a capacidade máxima de estudantes e fornece operações de consulta sobre o conjunto.

---

## Métodos

### `adicionar_aluno(aluno) -> None`
Adiciona uma instância de `Aluno` à turma.
- Lança `TurmaLotadaError` se a turma já atingiu o limite máximo de alunos.

### `remover_aluno_por_nome(nome: str) -> None`
Remove o aluno com o nome informado da lista da turma.
- Busca pelo nome exato do aluno.
- Não lança exceção se o aluno não for encontrado.

### `calcular_media_turma() -> float`
Retorna a média das médias individuais de todos os alunos cadastrados.
- A média individual de cada aluno é calculada a partir das suas notas.
- Não pode ser chamado com turma sem alunos.

### `contar_alunos() -> int`
Retorna o número de alunos atualmente cadastrados na turma.
- Retorna `0` se a turma estiver vazia.
- Não lança exceções.

---

## Regras de Negócio

1. O limite máximo de alunos por turma é 40 (padrão).
2. O limite pode ser configurado no momento da criação da turma via parâmetro `limite`.
3. Tentar adicionar um aluno quando a turma já atingiu o limite lança `TurmaLotadaError`.
4. `calcular_media_turma` retorna a média das médias individuais, não a média de todas as notas somadas.
5. Turma sem alunos não pode ter média calculada.
6. A remoção por nome não produz erro caso o aluno não exista na lista.

---

## Cenários de Exceção

| Situação | Exceção lançada |
|---|---|
| Adicionar aluno em turma com 40 alunos (limite padrão) | `TurmaLotadaError` |
| Adicionar aluno em turma com limite personalizado já atingido | `TurmaLotadaError` |
