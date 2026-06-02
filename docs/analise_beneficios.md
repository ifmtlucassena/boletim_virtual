# Etapa 4 - Documentação e Análise dos Benefícios

Nesta etapa, registramos uma reflexão sobre como foi desenvolver o projeto `boletim_virtual` usando TDD. O projeto é simples, mas serviu para entendermos melhor como os testes ajudam a organizar o código e a evitar erros durante a implementação.

Durante o desenvolvimento, trabalhamos com branches, pull requests, revisões de código e merges. Cada parte do sistema foi sendo feita aos poucos, seguindo a ideia do ciclo Red, Green e Refactor: primeiro escrever ou ajustar os testes, depois implementar o necessário para eles passarem e, por fim, melhorar o código quando fosse preciso.

## 10. Evolução do código: como o design emergiu dos testes

No início, o projeto tinha apenas a estrutura básica: classes criadas, arquivos de teste e algumas regras de negócio documentadas. Muitos métodos ainda estavam vazios, com `pass`, então o comportamento real ainda precisava ser implementado.

Com os testes, fomos entendendo melhor o papel de cada classe. A classe `Aluno` ficou responsável por guardar as notas de um estudante, adicionar notas válidas, limpar a lista e informar a quantidade de notas. A classe `Media` ficou responsável pelos cálculos, como média simples, validação de intervalo e verificação de discrepância entre notas.

A classe `Turma` passou a organizar os alunos, controlar limite, remover aluno pelo nome e calcular a média geral da turma. Já a classe `ClassificadorDesempenho` ficou com a regra de classificação: aprovado, recuperação ou reprovado, de acordo com a média.

Assim, o design do projeto foi surgindo aos poucos. Os testes ajudaram a separar melhor as responsabilidades e evitar que uma classe ficasse fazendo coisa demais. Mesmo sendo um sistema pequeno, essa separação deixou o código mais fácil de entender.

## 11. Bugs encontrados pelos testes antes da integração

Os testes ajudaram a encontrar problemas antes de juntarmos tudo nas branches principais. No começo, vários testes falhavam porque os métodos ainda não tinham implementação. Isso fazia parte do processo, mas também mostrava claramente o que ainda precisava ser feito.

Alguns exemplos de problemas que os testes ajudaram a evitar:

- calcular média com lista vazia;
- aceitar notas menores que 0 ou maiores que 10;
- deixar métodos como `limpar_notas` e `get_quantidade_notas` sem comportamento real;
- permitir adicionar alunos acima do limite da turma;
- classificar uma média nula como se fosse uma média válida;
- retornar um resumo sem as informações principais do aluno.

Esses casos são simples, mas são justamente o tipo de erro que pode passar despercebido quando a implementação é feita direto, sem teste antes.

Também percebemos que os testes precisam ser reais. Se um teste fica apenas com `pass`, ele aparece como aprovado, mas não garante nada. Isso foi uma lição importante para o grupo: não basta ter arquivos de teste, eles precisam verificar o comportamento esperado.

## 12. Comparativo: como seria sem TDD vs. com TDD

Sem TDD, provavelmente teríamos começado implementando as classes e só depois tentado testar alguns casos. Isso poderia fazer com que algumas regras ficassem esquecidas, principalmente os casos de erro, como nota inválida, lista vazia ou média nula.

Com TDD, tivemos que pensar primeiro no comportamento esperado. Antes de escrever a implementação final, já tínhamos uma ideia mais clara do que cada método deveria fazer. Isso ajudou a evitar improvisos e deixou o código mais direcionado.

Outra diferença foi na segurança para alterar o código. Quando fazíamos algum ajuste, os testes ajudavam a mostrar se alguma regra tinha quebrado. Sem testes, dependeríamos mais de testar manualmente ou apenas confiar que a mudança estava correta.

De forma geral, com TDD o processo ficou um pouco mais trabalhoso no início, mas mais organizado depois. Para um projeto pequeno, isso já fez diferença; em um projeto maior, provavelmente faria ainda mais.

## 13. Lições aprendidas pelo grupo

Aprendemos que TDD ajuda a pensar melhor antes de implementar. Escrever os testes nos obrigou a transformar as regras de negócio em exemplos concretos, como "nota acima de 10 deve gerar erro" ou "média 7 deve ser aprovado".

Também vimos que nomes de testes bem escritos ajudam bastante. Eles deixam claro o que o sistema deveria fazer e servem como uma documentação do comportamento esperado.

Outra lição foi a importância de revisar o código antes de juntar as partes. As branches e os pull requests ajudaram a organizar o trabalho do grupo, mas também mostraram que precisamos ter cuidado para manter tudo sincronizado.

Por fim, percebemos que TDD não resolve tudo sozinho. Ele ajuda bastante, mas depende de testes bem escritos e de uma boa revisão do grupo. Para as próximas etapas, queremos manter os testes mais completos e garantir que a versão final do projeto tenha todos os comportamentos realmente verificados.
