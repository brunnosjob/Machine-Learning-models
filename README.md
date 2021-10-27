# Machine-Learning-rh-preselecao
Esse é um repositório em que deposito scripts do projeto de machine learning que desenvolvi com o objetivo de auxiliar o processo seletivo a vaga de emprego de uma determinada empresa.
Em termos mais específicos, o modelo tem como objetivo classificar quais candidatos às vagas de emprego de uma dada empresa ficarão ao menos 2 anos na empresa. Dessa forma, o time de RH responsável pelo processo seletivo pode filtrar e reduzir os custos do processo e otimizar a eficiência de seleção de candidatos apropriados.

Um projeto como esse tem um importante impacto positivo na produção e nas finanças de uma empresa, haja visto que, quando a rotatividade de admissão e demissão é alta no curto espaço de tempo, o entrosamento e a continuidade dos objetivos da produção sofrem impactos negativos, afetando o financeiro, além dos custos do processo de admissão e demissão.

O presente documento apresenta o script em linguagem de programação, demonstrando as etapas e desenvolvimento do modelo de machine learning. A documentação com comentários detalhados expondo o passo a passo e as tomadas de decisões na construção de cada código e por cada função estará disponível na plataforma Medium, através do link https://br-cienciadedados.medium.com/ .

Para se aplicar o modelo, os seguintes dados são necessários na respectiva ordem:
1 - Vaga para qual se está aplicando
2 - Sexo
3 - Estado civil
4 - Motivo de saída da última empresa
5 - Fonte de inscrição para a vaga
6 - Pretensão salarial
7 - Projetos apresentados na empresa anterior
8 - Idade
9 - Meses ou anos de trabalho na última empresa

Após a obtenção dos dados, o método do OneHotEncoder é aplicado sobre as variáveis categóricas e a padronização é aplicada sobre todos os dados.
Por fim, o modelo de machine learning é aplicado.

O projeto conta com o script para a geração de um web app em que roda o modelo de machine learning a fim de testá-lo e disponibilizá-lo para interação de interessados.
