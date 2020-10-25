# oito-rainhas
Projeto de resolução do problema das oito rainhas utilizando algoritmo genético. 

[![Run on Repl.it](https://repl.it/badge/github/MiniMarvin/oito-rainhas)](https://repl.it/github/MiniMarvin/oito-rainhas)

'''
```
genótipo - [bool] / 3 bits por rainha (representa o board todo)
fenótipo - pega 3 bits e 
```

```
crossfill
aaa|aaaaaaa
bbb|bbbbbbb

aaa|bbbbbbb
bbb|aaaaaaa
```

# Especificação Mini-projeto – 8 rainhas

## Primeira parte:
Representação (genótipo): string de bits
Recombinação: “cut-and-crossfill” crossover
Probabilidade de Recombinação: 90%
Mutação: troca de genes
Probabilidade de Mutação: 40%
Seleção de pais: ranking - Melhor de 2 de 5 escolhidos aleatoriamente
Seleção de sobreviventes: substituição do pior
Tamanho da população: 100
Número de filhos gerados: 2
Inicialização: aleatória
Condição de término: Encontrar a solução, ou 10.000 avaliações de fitness
Fitness?

## Segunda parte:
Implementar possíveis melhorias mudando:
Representação
Recombinação 
Mutação
Seleção de pais – roleta?
Seleção de sobreviventes: geracional ou substituição do pior
Tamanho da população: 10? 30? 50? 70? 120? 200?
O fitness pode ser melhorado?


## Segunda parte de fato
A melhorar:
1. Representação - colocar digitos
2. Recombinaçao - aquela do caminho ciclo lá
3. Mutação - permutação
4. Testar roleta (opcional)
5. Seleção de sobreviventes (opcional)
6. fitness - ver depois

## O que precisa no relatório
Avaliação do Projeto

O objetivo é avaliar se as modificações propostas para a solução do problema das 8 rainhas foram eficientes e eficazes e porque essas alterações levaram a melhora/piora.
Para cada implementação devem ser feitas 30 execuções e analisar
* Em quantas execuções o algoritmo convergiu (no/30 execuções);
* Em que iteração o algoritmo convergiu (média e desvio padrão);
* Número de indivíduos que convergiram por execução;
* Fitness médio alcançado nas 30 execuções (média e desvio padrão);
* Análise adicional: Quantas iterações são necessárias para toda a população convergir?