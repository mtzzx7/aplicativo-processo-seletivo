# 🧠 Sistema de Processo Seletivo – Robot One 2026

## 📌 Visão Geral

Este projeto é um **sistema desktop em Python** desenvolvido para gerenciar o **processo seletivo da equipe de robótica Robot One**, alinhado a competições como **OBR, TBR e CCBB**.

O sistema **não é apenas um app de notas**.  
Ele implementa um **modelo pedagógico e avaliativo específico**, baseado em:

- Trabalho em equipe  
- Autonomia dos alunos  
- Avaliação contínua  
- Justiça interna sem exposição pública  

⚠️ **Qualquer alteração deve respeitar esse modelo.**

---

## 🎯 Objetivo do Sistema

1. Centralizar o processo seletivo em um único aplicativo  
2. Avaliar **equipes** de forma oficial  
3. Permitir uma **avaliação individual justa**, porém **oculta**  
4. Fornecer dados confiáveis para decisão final da banca  
5. Automatizar importação, avaliação e exportação de resultados  

---

## 🧩 Funcionalidades Implementadas

- Importação de inscrições via **Excel**
- Cadastro e gerenciamento de **candidatos**
- Criação e gerenciamento de **equipes**
- Controle de **sessões de avaliação**
- Registro de **presença**
- Avaliação por **equipe**
- Camada de **pesos internos individuais**
- Diário de bordo por equipe
- Dashboard de métricas
- Exportação de dados para **CSV**
- Backup automático do banco
- Proteção por **PIN** para área administrativa

---

## ❌ O QUE ESTE SISTEMA NÃO FAZ (E NÃO DEVE FAZER)

🚫 Não envia e-mails diretamente aos alunos  
🚫 Não exibe ranking individual  
🚫 Não expõe pesos internos  
🚫 Não avalia aluno individualmente de forma pública  
🚫 Não contradiz o edital publicado  

> **Se alguma alteração quebrar uma dessas regras, ela está incorreta.**

---

## 🏗️ Arquitetura Geral

- **Linguagem:** Python 3  
- **Interface:** PySide6  
- **Banco de dados:** SQLite  
- **Persistência:** Local (offline)  

### Fluxo Geral

Formulário de Inscrição
↓
Excel de Respostas
↓
Importação no App
↓
Formação de Equipes
↓
Avaliação por Sessões
↓
Cálculo Interno
↓
Excel Final + Comunicação Interna

## 📊 Modelo Avaliativo (CRÍTICO)

### 🔹 Avaliação Oficial (Pública)

- Unidade: **Equipe**
- Escala curta (exemplo atual): **1 a 4**
- Critérios:
  - Imersão
  - Desenvolvimento
  - Apresentação

⚠️ **Reflete o edital e não deve ser alterada.**

---

### 🔹 Avaliação Interna (Oculta)

- Unidade: **Indivíduo**
- Forma: **peso multiplicador**
- Faixa recomendada:
  - Mínimo: `0.8`
  - Padrão: `1.0`
  - Máximo: `1.2`

```python
score_individual = nota_equipe * peso_individual

Essa camada existe para:

Evitar efeito “carona”

Reconhecer liderança

Tornar a decisão final mais justa

⚠️ Nunca expor esses valores aos alunos.

👥 Fluxo Correto de Avaliação (UX Esperado)

Selecionar Equipe

Selecionar Sessão

Registrar nota da equipe

Sistema carrega apenas os membros daquela equipe

Ajustar pesos individuais (opcional)

Registrar observações internas

🚫 O avaliador não escolhe aluno solto fora da equipe.

🗄️ Estrutura de Dados (Resumo)

Tabelas principais:

candidates

teams

team_members

evaluations

attendance

diary_entries

attachments

internal_weights

settings

Relacionamentos:

Avaliação → Equipe

Candidato → Equipe

Peso interno → Avaliação + Candidato

📤 Exportação de Resultados

O Excel final deve conter:

Nome do aluno

Equipe

Score interno final

Status:

Aprovado

Lista de espera

Não aprovado

⚠️ O ranking é interno
⚠️ O status é o único dado comunicável

📧 Comunicação por E-mail

O sistema envia e-mails apenas para técnicos / coordenação

Nunca diretamente para alunos

Conteúdo:

Excel final anexado

Resumo do processo

Confirmação de encerramento

Isso garante:

LGPD

Segurança institucional

Proteção da banca

🔐 Segurança e Ética

Banco local

Sem API pública

PIN para funções administrativas

Logs de auditoria

Backup manual e automático

🧠 Evoluções Permitidas

✔️ Melhorias de UX
✔️ Dashboards analíticos
✔️ Relatórios internos
✔️ Normalização de pesos
✔️ Automação de e-mails internos

🚫 Evoluções Proibidas

❌ Ranking público
❌ Avaliação individual visível
❌ Transformar o processo em prova
❌ Exposição de notas individuais

⚠️ Aviso Importante para Desenvolvedores e IAs

Este sistema resolve um problema real, institucional e pedagógico.

Antes de alterar qualquer coisa:

Leia o edital

Entenda o modelo de equipe

Compreenda por que a avaliação individual é oculta

Preserve a autonomia dos alunos

Se a mudança:

Facilita nota

Expõe alunos

Cria competição tóxica

➡️ Ela está errada.

✅ Conclusão

Este sistema:

Já funciona

Já é confiável

Já respeita o edital

O foco agora é:

Refinar, não reinventar.


Se quiser, no próximo passo eu posso:
- Criar um **README curto só para IA**
- Gerar um **CHECKLIST de PR**
- Criar um **diagrama visual (Mermaid / Draw.io)**
- Escrever um **CONTRIBUTING.md**
- Preparar o **fluxo de e-mail automático**

