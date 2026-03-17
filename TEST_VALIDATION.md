# 🧪 Teste de Validação - Sistema de Avaliação v2.0

## 📋 Introdução

Este documento apresenta **testes práticos** que você pode executar para validar que o sistema está funcionando corretamente.

**Tempo estimado**: 10-15 minutos

---

## ✅ Teste 1: Validação do Banco de Dados

### Como executar
```bash
python test_migration.py
```

### Resultado esperado
```
==================================================
Teste de Migração do Banco de Dados
==================================================
✅ Versão do schema: 12
✅ Tabela 'logic_scores' encontrada
✅ Campo 'evaluation_type' encontrado
✅ Total de candidatos: 49
✅ Total de equipes: 5
✅ Migração validada com sucesso!
==================================================
```

### O que significa
- Schema foi migrado de v11 para v12 ✅
- Tabela logic_scores foi criada ✅
- Campo evaluation_type foi adicionado ✅
- Dados antigos preservados (49 candidatos, 5 equipes) ✅

---

## ✅ Teste 2: Iniciar a Aplicação

### Como executar
```bash
# Ativar ambiente virtual (se necessário)
.venv\Scripts\Activate.ps1

# Iniciar aplicação
python app.py
```

### O que procurar
1. ✅ Aplicação abre sem erros
2. ✅ Janela principal aparece
3. ✅ Menu lateral mostra:
   - "Prova de Lógica" (entre "Presença" e "Avaliações")
   - "Avaliações (Apresentação)" (não mais "Avaliações")

### Se houver erro
- Verifique se todas as dependências estão instaladas:
  ```bash
  pip install -r requirements.txt
  ```
- Verifique a versão do Python (≥3.7)
- Verifique se porta 5432+ está disponível

---

## ✅ Teste 3: Página "Prova de Lógica"

### Teste 3A: Carregá a página
1. Clique em "Prova de Lógica" no menu
2. Verifique se a página carrega sem erros

### Teste 3B: Registrar uma nota
**Dados de teste**:
- Candidato: Selecione qualquer um disponível
- Data: 2026-03-07 (valor padrão)
- Nota: 8.5
- Observações: "Teste de sistema"

**Passos**:
1. Selecione um candidato no dropdown
2. Deixe a data como está (2026-03-07)
3. Digite nota "8.5"
4. Digite observação "Teste de sistema"
5. Clique "Registrar Nota de Lógica"

**Resultado esperado**:
- ✅ Mensagem "Nota de lógica registrada para o candidato"
- ✅ Nota aparece na tabela inferior
- ✅ Campos se limpam para próximo registro

### Teste 3C: Editar a nota
1. Na tabela, clique sobre a nota que registrou
2. Clique "Editar nota selecionada"
3. Mude a nota para 7.5
4. Clique "Salvar"

**Resultado esperado**:
- ✅ Diálogo abre com dados preenchidos
- ✅ Mensagem "Nota atualizada"
- ✅ Tabela mostra novo valor (7.5)

### Teste 3D: Deletar a nota
1. Na tabela, clique sobre a nota editada
2. Clique "Remover nota selecionada"
3. Confirme a ação

**Resultado esperado**:
- ✅ Mensagem de confirmação aparece
- ✅ Nota é removida da tabela
- ✅ Tabela fica vazia ou mostra outros registros

---

## ✅ Teste 4: Página "Avaliações (Apresentação)"

### Teste 4A: Verificar nome da página
- ✅ Página chamada "Avaliações (Apresentação)" no menu
- ✅ Botão diz "Registrar Avaliação de Apresentação"

### Teste 4B: Visualizar avaliações existentes
1. Clique em "Avaliações (Apresentação)"
2. Verifique se tabela mostra avaliações anteriores

**Resultado esperado**:
- ✅ Tabela carrega com dados (se houver)
- ✅ Colunas: ID, Team, Sessão, Banca, Imersão, Desenv, Apres

### Teste 4C: Evitar duplicata
1. Selecione uma equipe + sessão que já tem avaliação
2. Tente registrar outra avaliação para mesma equipe+sessão
3. Clique "Registrar Avaliação"

**Resultado esperado**:
- ✅ Mensagem: "Já existe uma avaliação ativa para esta equipe nesta sessão"
- ✅ Avaliação NÃO é criada

---

## ✅ Teste 5: Diálogo de Contribuição Individual

### Dados para registrar
**Simulando apresentação de uma equipe**

### Teste 5A: Registrar avaliação completa
1. Vá para "Avaliações (Apresentação)"
2. Preencha o formulário:
   - **Equipe**: Selecione equipe que tem membros
   - **Sessão**: Selecione qualquer sessão (ou crie uma)
   - **Banca**: Digite "Teste Banca"
   - **Imersão**: 3
   - **Desenvolvimento**: 3
   - **Apresentação**: 3
   - **Comentário**: "Avaliação de teste"
3. Clique "Registrar Avaliação de Apresentação"

**Resultado esperado**:
- ✅ Mensagem: "Avaliação da equipe registrada (ID: X)"
- ✅ Mensagem: "Agora, insira as contribuições individuais"
- ✅ **Diálogo de Contribuição aparece**

### Teste 5B: Dentro do Diálogo de Contribuição
1. Verifique tabela com membros da equipe
2. Para cada membro:
   - Mude o peso (ex: 1.0 → 1.1)
   - Adicione observação (ex: "Liderou a implementação")
3. Clique "Salvar Contribuições"

**Resultado esperado**:
- ✅ Tabela mostra todos os membros
- ✅ Campos de peso e observação são editáveis
- ✅ Mensagem: "Contribuições finalizadas" ou similar
- ✅ Diálogo fecha
- ✅ Volta para página de avaliações

---

## ✅ Teste 6: Painel Administrativo

### Teste 6A: Acessar Admin
1. Clique em "Admin (oculto)" no menu
2. Insira PIN administrativo (padrão: 1234)

**Resultado esperado**:
- ✅ Página Admin carrega
- ✅ Vê tabela de avaliações
- ✅ Vê pesos entre 0-1

### Teste 6B: Calcular Scores Ocultos
1. Clique "Calcular scores ocultos"
2. Wait para processamento

**Resultado esperado**:
- ✅ Mensagem de sucesso
- ✅ Scores ocultos calculados na tabela

### Teste 6C: Resumo por Equipe
1. Clique "Recalcular Resumo por equipe"

**Resultado esperado**:
- ✅ Tabela abaixo mostra resumo
- ✅ Colunas: Equipe ID, Nome, AVG hidden, Presença (%), Score Final

---

## 🐛 Testes de Validação (Error Handling)

### Teste 7A: Nota inválida (fora do range)
1. Vá para "Prova de Lógica"
2. Tente inserir nota 11 (máximo é 10)
3. Clique "Registrar Nota de Lógica"

**Resultado esperado**:
- ❌ Aviso: "Nota deve estar entre 0 e 10"
- ✅ Nota NÃO é registrada

### Teste 7B: Candidato não selecionado
1. Vá para "Prova de Lógica"
2. Deixe candidato vazio
3. Clique "Registrar Nota de Lógica"

**Resultado esperado**:
- ❌ Aviso: "Selecione um candidato"
- ✅ NÃO permite registrar

### Teste 7C: Duplicata de candidato na mesma data
1. Registre nota para candidato X em 2026-03-07
2. Tente registrar outra nota para candidato X em 2026-03-07
3. Clique "Registrar Nota de Lógica"

**Resultado esperado**:
- ❌ Aviso: "Já existe nota registrada para este candidato na data..."
- ✅ NÃO permite registrar duplicata

---

## 📊 Verificação de Dados

### Teste 8A: Backup está funcionando
1. Vá para Admin
2. Clique "Backup DB"
3. Verifique se arquivo foi criado

**Resultado esperado**:
- ✅ Arquivo `backup_selection_YYYYMMDD_HHMMSS.db` criado
- ✅ Arquivo contém cópia do banco

### Teste 8B: Exportar dados
1. Vá para Admin
2. Clique "Exportar avaliações (CSV)"
3. Escolha local para salvar

**Resultado esperado**:
- ✅ Arquivo CSV é gerado
- ✅ Contém todas as avaliações
- ✅ Pode ser aberto em Excel/LibreOffice

---

## 🎯 Sumário de Teste

### Checklist Final
```
[✅] Teste 1: Migração do DB validada
[✅] Teste 2: Aplicação inicia sem erros
[✅] Teste 3: Prova de Lógica funciona
  [✅] 3A: Página carrega
  [✅] 3B: Registra nota
  [✅] 3C: Edita nota
  [✅] 3D: Deleta nota
[✅] Teste 4: Avaliações (Apresentação) funciona
  [✅] 4A: Nome correto
  [✅] 4B: Visualiza dados
  [✅] 4C: Evita duplicata
[✅] Teste 5: Contribuição Individual funciona
  [✅] 5A: Registra avaliação
  [✅] 5B: Diálogo abre e funciona
[✅] Teste 6: Admin funciona
  [✅] 6A: Acessa com PIN
  [✅] 6B: Calcula scores
  [✅] 6C: Resumo por equipe
[✅] Teste 7: Validações funcionam
  [✅] 7A: Rejeita fora de range
  [✅] 7B: Rejeita candidato vazio
  [✅] 7C: Evita duplicata
[✅] Teste 8: Recursos Admin
  [✅] 8A: Backup funciona
  [✅] 8B: Export CSV funciona
```

---

## ✨ Se Tudo Passou

🎉 **Parabéns!** Seu sistema está funcionando perfeitamente!

Próximas ações recomendadas:
1. ✅ Registar as notas da prova de lógica (07/03)
2. ✅ Aguardar apresentação (21/03)
3. ✅ Registrar avaliações de apresentação
4. ✅ Fazer análise final com Admin

---

## 🆘 Se Algo Falhou

Verifique:
1. **Erro de banco de dados**: Execute `python init_db.py`
2. **Dependências faltando**: `pip install -r requirements.txt`
3. **Porta ocupada**: Verifique processo Python rodando
4. **Arquivo corrompido**: Delete `selection.db` e recrie

---

## 📞 Próximos Passos

Após validar tudo:
1. Leia [GUIDE_EVALUATION.md](./GUIDE_EVALUATION.md) para instruções completas
2. Faça backup do DB
3. Comece a registrar dados reais
4. Use Admin panel para monitorar status

---

**Bom teste! 🧪✅**

Data: 17/03/2026
Tempo estimado: 10-15 minutos
Dificuldade: Fácil
