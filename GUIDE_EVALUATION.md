# 📋 Guia de Uso - Sistema de Avaliação Atualizado

## 🎯 Visão Geral

O sistema foi atualizado para gerenciar **dois tipos de avaliações**:

1. **Prova de Lógica** (07/03/2026) - Escala 0-10
   - Avaliação individual de cada candidato
   - Critério de desempate para seleção final

2. **Avaliação de Apresentação** (21/03/2026) - Escala 1-4
   - Avaliação em grupo (por equipe)
   - Com ajustes de contribuição individual

---

## 📊 Estrutura Atual

### Candidatos e Equipes
- **Total de Candidatos**: 49
- **Total de Equipes**: 5
- **Status**: Grupos já formados, pessoal que desistiu/não apareceu identificado

### Cronograma
- ✅ **07/03/2026**: Prova de Lógica (0-10)
- ⏳ **21/03/2026**: Apresentação das Equipes (com avaliação individual + em grupo)

---

## 🚀 Como Usar

### 1️⃣ Registrar Prova de Lógica (07/03)

**Local**: Menu Lateral → "Prova de Lógica" (aba 4)

**Passos**:
1. Clique em "Prova de Lógica"
2. Na seção superior, preencha:
   - **Candidato**: Selecione no dropdown
   - **Data da Prova**: Vem preenchida com 2026-03-07 (pode editar se necessário)
   - **Nota (0-10)**: Digite a nota de 0 a 10
   - **Observações**: Opcional (ex: "Faltou 1 questão", "Nota de desempate")
3. Clique em "Registrar Nota de Lógica"

**Para Editar**:
- Na tabela inferior, selecione a nota
- Clique em "Editar nota selecionada"
- Modifique os dados e clique em "Salvar"

**Para Remover**:
- Selecione a nota na tabela
- Clique em "Remover nota selecionada"
- Confirme a ação

---

### 2️⃣ Registrar Avaliação de Apresentação (21/03)

**Local**: Menu Lateral → "Avaliações (Apresentação)" (aba 5)

**Passos**:
1. Clique em "Avaliações (Apresentação)"
2. Na seção superior, preencha:
   - **Equipe**: Selecione a equipe a ser avaliada
   - **Sessão**: Selecione a sessão de apresentação
   - **Banca (nome)**: Nome do avaliador/banca
   - **Imersão (1–4)**: Nota de engajamento/aprofundamento
   - **Desenvolvimento (1–4)**: Nota de qualidade técnica
   - **Apresentação (1–4)**: Nota de clareza/comunicação
   - **Comentário**: Anotações adicionais da banca

3. Clique em "Registrar Avaliação de Apresentação"

4. **Diálogo de Contribuição Individual aparecerá**:
   - Para cada membro da equipe, ajuste:
     - **Peso** (0.1 a 1.2, padrão 1.0)
       - `1.0` = participação normal
       - `>1.0` = liderança/destaque
       - `<1.0` = participação abaixo do esperado
     - **Observações Internas**: Notas qualitativas sobre o membro
   - Clique em "Salvar Contribuições"

---

## 💡 Entendendo os Pesos de Contribuição

Os pesos aplicados a cada membro **não são notas públicas**. São apenas para análise interna da banca.

**Exemplos**:
- Membro liderou o projeto → peso 1.2
- Membro teve boa participação → peso 1.0
- Membro teve participação limitada → peso 0.8
- Membro mal se comportou/prejudicou → peso 0.5

**Cálculo Interno**:
```
Score Individual = (Nota da Equipe) × (Peso do Membro)
```

---

## 📈 Funcionalidades do Painel Administrativo

**Local**: Menu Lateral → "Admin (oculto)" (aba 9)

### Calcular Scores Ocultos
- Botão: "Calcular scores ocultos"
- Usa os pesos internos para gerar scores individuais
- Aplica penalidade de presença se configurado

### Recalcular Resumo por Equipe
- Mostra score final de cada equipe
- Considera presença e pesos internos
- Útil para ranking interno

### Recalcular Resumo Individual
- Mostra score de cada candidato
- Baseado em contribuição ajustada
- Excelente para identificar talento excepcional

### Exportar Avaliações (CSV)
- Exporta todos os dados de avaliação em CSV
- Útil para análise offline ou backup

---

## 📱 Dicas de Boas Práticas

### ✅ Faça
- ✅ Registre as notas de lógica assim que forem calculadas
- ✅ Use o campo de observações para contexto adicional
- ✅ Defina pesos de contribuição com cuidado e justiça
- ✅ Faça backup regularmente (botão "Backup DB" em Admin)
- ✅ Recalcule scores antes de tomar decisões finais

### ❌ Evite
- ❌ Registrar notas duplicadas (sistema avisa)
- ❌ Publicar weights/pesos individuais para alunos
- ❌ Editar dados sem registrar motivo
- ❌ Confundir score técnico com nota publicável

---

## 🔒 Segurança e Confidencialidade

- **Scores individuais** são **internos** e **confidenciais**
- **Pesos de contribuição** não são divulgados aos candidatos
- **Prova de Lógica** pode ser usada como critério de desempate
- Acesso ao painel Admin é protegido por PIN

---

## 📅 Calendário de Atividades

| Data | Atividade | Status |
|------|-----------|--------|
| 07/03/2026 | Prova de Lógica | ⏳ Registrar notas |
| 21/03/2026 | Apresentação das Equipes | ⏳ Aguardando |
| 21/03/2026 | Avaliação das Apresentações | ⏳ Registrar após evento |
| TBD | Análise de Scores | ⏳ Após todas avaliações |
| TBD | Decisão Final da Banca | ⏳ Análise de resultados |

---

## 🆘 Suporte/Problemas

### "Já existe nota registrada para este candidato"
- Um candidato já tem nota registrada para essa data
- Se quiser atualizar, clique em "Editar nota selecionada" na tabela
- Se quiser registrar para data diferente, mude a data

### "Candidato e data são obrigatórios"
- Preencha todos os campos obrigatórios antes de salvar

### Onde estão as notas registradas?
- **Prova de Lógica**: Tabela "Prova de Lógica" (lista completa com quem registrou)
- **Apresentação**: Tabela "Avaliações (Apresentação)" (notas da equipe)
- **Contribuição Individual**: Calculada via Admin → "Resumo Individual"

### Como editar avaliações já registradas?
1. Vá até a aba correspondente
2. Selecione o registro na tabela
3. Clique em "Editar..."
4. Modifique e salve

---

## 📊 Estrutura do Banco de Dados (Técnico)

### Tabela: `logic_scores`
```
id              - ID único
candidate_id    - FK para candidates
test_date       - Data da prova
score           - Nota (0-10)
notes           - Observações
registered_by   - Quem registrou
registered_at   - Data/hora do registro
```

### Tabela: `evaluations`
```
id                  - ID único
team_id             - FK para teams
judge               - Nome do avaliador
immersion           - Nota (1-4)
development         - Nota (1-4)
presentation        - Nota (1-4)
evaluation_type     - Tipo (PRESENTATION, LOGIC_TEST)
training_session_id - FK para training_sessions
... (mais campos)
```

### Tabela: `member_contribution`
```
id              - ID único
evaluation_id   - FK para evaluations
member_id       - FK para candidates
weight          - Peso (0.1-1.2)
note            - Observação interna
```

---

## 🎓 Notas Pedagógicas

Este sistema foi construído com base na filosofía:
- **Trabalho em Equipe**: Avaliações são primariamente em grupo
- **Justiça**: Pesos internos evitam "caronas"
- **Transparência**: Alunos veem notas de grupo, não pesos internos
- **Autonomia**: Sistema rastreia desenvolvimento ao longo do tempo

---

**Última atualização**: 17/03/2026
**Schema versão**: 12
**Total de candidatos**: 49
**Total de equipes**: 5
