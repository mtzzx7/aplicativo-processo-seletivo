# Changelog - Sistema de Avaliação v2.0

## Data: 17/03/2026

### Mudanças Implementadas

#### 1. **Nova Página: Prova de Lógica**
- **Local**: Menu lateral → "Prova de Lógica" (nova aba #4)
- **Objetivo**: Registrar notas individuais de cada candidato na prova de lógica (07/03/2026)
- **Escala**: 0 a 10
- **Funcionalidade**: 
  - Registrar nota de lógica por candidato
  - Editar notas já registradas
  - Deletar notas se necessário
  - Visualizar histórico de todas as notas registradas
- **Uso como Desempate**: A prova de lógica será usada como critério de desempate quando necessário

#### 2. **Página de Avaliações Renomeada**
- **Antes**: "Avaliações"
- **Agora**: "Avaliações (Apresentação)" (aba #5)
- **Objetivo**: Deixar mais claro que trata-se da avaliação de apresentação (21/03/2026)
- **Nota**: Mantém a mesma funcionalidade de registro de notas em grupo (Imersão, Desenvolvimento, Apresentação)

#### 3. **Nova Tabela no Banco de Dados: `logic_scores`**
```sql
CREATE TABLE logic_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    test_date TEXT NOT NULL,
    score REAL NOT NULL,
    notes TEXT,
    registered_by TEXT,
    registered_at TEXT,
    FOREIGN KEY(candidate_id) REFERENCES candidates(id)
)
```

#### 4. **Novo Campo em `evaluations`**
- Campo: `evaluation_type TEXT DEFAULT 'PRESENTATION'`
- **Futura expansão**: Permitirá diferenciar entre diferentes tipos de avaliação
- **Atual**: Todas as avaliações existentes e novas são do tipo 'PRESENTATION'

#### 5. **Atualização da Configuração**
- Arquivo: `config.toml`
- Seção `[logic_test]` adicionada com:
  - `enabled = true`
  - `test_date = "2026-03-07"`
  - `weight_as_tiebreaker = true`

### Como Usar

#### **Registrar Prova de Lógica**
1. Navegue até "Prova de Lógica" no menu lateral
2. Selecione o candidato
3. Data vem preenchida automaticamente (2026-03-07)
4. Digite a nota de 0 a 10
5. Adicione observações se necessário
6. Clique em "Registrar Nota de Lógica"

#### **Registrar Avaliação de Apresentação (21/03)**
1. Navegue até "Avaliações (Apresentação)"
2. Selecione a equipe e a sessão
3. Digite o nome da banca
4. Registre as notas de:
   - Imersão (1-4)
   - Desenvolvimento (1-4)
   - Apresentação (1-4)
5. Adicione comentários se necessário
6. Clique em "Registrar Avaliação de Apresentação"
7. Um diálogo aparecerá para registrar **pesos de contribuição individual**

#### **Pesos de Contribuição Individual (Apresentação)**
- Cada membro recebe um peso (0.1 a 1.2, padrão 1.0)
- Isso permite ajustar o score da equipe para análise interna
- **Exemplo**: Se um membro teve pouca participação, pode receber peso 0.7
- Esses pesos são **internos** e não são divulgados aos alunos

### Status de Grupos

De acordo com a sua informação:
- ✅ Grupos já estão formados
- ✅ Pessoal que desistiu ou não compareceu já foi identificado
- ⏳ Prova de Lógica: 07/03/2026 (pode registrar as notas agora)
- ⏳ Apresentação das Equipes: 21/03/2026 (registrar quando ocorrer)

### Índices das Páginas (Referência)
```
0 - Inscrições
1 - Equipes
2 - Sessões de Treinamento
3 - Presença
4 - Prova de Lógica         ⭐ NOVO
5 - Avaliações (Apresentação)
6 - Diário de Bordo
7 - Sobre
8 - Dashboard
9 - Admin (oculto)
```

### Banco de Dados
- **Schema versão antigo**: v11
- **Schema versão novo**: v12 (com tabela `logic_scores`)
- **Migração**: Automática ao iniciar a aplicação

### Próximos Passos Sugeridos
1. Registrar todas as notas da prova de lógica (07/03)
2. No dia 21/03, registrar as avaliações de apresentação por equipe
3. Para cada avaliação, definir os pesos de contribuição individual
4. Usar o painel Admin para calcular scores finais quando necessário
5. Dashboard mostrará resumo de avaliações completo

---
**Observação**: O sistema mantém histórico completo de todas as avaliações. Qualquer alteração em notas deve ser feita através da edição de registros existentes, com rastreamento automático de mudanças.
