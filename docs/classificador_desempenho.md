# ClassificadorDesempenho

A classe `ClassificadorDesempenho` determina o status acadêmico do aluno com base em sua média e formata a saída para exibição. Ela não armazena estado — recebe a média como parâmetro e aplica as regras de classificação a cada chamada.

---

## Métodos

### `definir_situacao(media: float) -> str`
Classifica o aluno com base na média recebida e retorna uma string com a situação.
- Retorna `"APROVADO"` se média >= 7.0.
- Retorna `"RECUPERACAO"` se média >= 4.0 e < 7.0.
- Retorna `"REPROVADO"` se média < 4.0.
- Lança `StatusInconclusivoError` se a média for `None`.

### `pode_realizar_exame(media: float) -> bool`
Indica se o aluno tem direito a realizar o exame de recuperação.
- Retorna `True` apenas se a situação for `"RECUPERACAO"` (média entre 4.0 e 6.9).
- Retorna `False` para situações `"APROVADO"` ou `"REPROVADO"`.

### `formatar_resumo(nome: str, media: float) -> str`
Retorna uma string formatada com o nome do aluno, sua média e sua situação acadêmica.
- A string deve conter as três informações: nome, média e situação.
- O formato exato da string é definido pela implementação.

### `atingiu_criterio_aprovacao(media: float) -> bool`
Verifica se o aluno atingiu a média mínima para aprovação direta.
- Retorna `True` se média >= 7.0.
- Retorna `False` caso contrário.

---

## Regras de Negócio

1. Média >= 7.0 resulta em situação `"APROVADO"`.
2. Média entre 4.0 e 6.9 (inclusive em ambos os extremos) resulta em situação `"RECUPERACAO"`.
3. Média abaixo de 4.0 resulta em situação `"REPROVADO"`.
4. Média nula (`None`) impede a classificação e lança `StatusInconclusivoError`.
5. Apenas alunos em `"RECUPERACAO"` podem realizar o exame final.
6. O critério de aprovação direta é média >= 7.0, sem exceções.
7. `formatar_resumo` deve conter nome, média e situação na string retornada.

---

## Cenários de Exceção

| Situação | Exceção lançada |
|---|---|
| `definir_situacao(None)` | `StatusInconclusivoError` |
