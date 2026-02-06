# Contribuindo com o Sistema de Processo Seletivo

Este guia foca em **colaboração entre múltiplos computadores**, **sincronização de dados** e **segurança**.

## 1) Revisão técnica do código atual (pontos de melhoria)

Com base na estrutura atual (`app.py`, `ui/dashboard.py`, `ui/dashboard_repository.py`):

- `app.py` concentra UI, regras de negócio, acesso a banco e migrações em um único arquivo grande.
  - Recomenda-se separar em camadas:
    - `core/` (regras de negócio)
    - `repositories/` (queries)
    - `services/` (casos de uso)
    - `ui/` (widgets/telas)
- O acesso ao SQLite é repetido com `sqlite3.connect(...)` em muitos pontos.
  - Centralizar em um módulo de conexão com `contextmanager` e configurações comuns (`foreign_keys=ON`, timeout, WAL).
- A estratégia de migração hoje está acoplada à inicialização em `init_db()`.
  - Para escala e auditoria, mover para migrações versionadas (ex.: `alembic` com SQLAlchemy ou scripts SQL ordenados).
- O dashboard (`ui/dashboard_repository.py`) usa queries diretas e sem tratamento para ausência de chave `process_status`.
  - Adicionar fallback seguro para evitar quebra ao carregar cards.
- A gravação de logs em arquivo texto (`audit.log`) é útil, mas sem rotação.
  - Adotar rotação (ex.: `logging.handlers.RotatingFileHandler`) e padronização de formato.

## 2) Colaboração entre máquinas

## Workflow recomendado (Git)

- `main`: sempre estável.
- branches curtas por tarefa (`feat/...`, `fix/...`, `docs/...`).
- Pull Requests pequenos, com checklist de:
  - impacto no modelo avaliativo;
  - impacto em segurança (LGPD);
  - necessidade de migração.

## Edição colaborativa em tempo real

- **VS Code Live Share**: ideal para pareamento técnico e revisão guiada.
- Alternativas:
  - JetBrains Code With Me;
  - Tmate/Tmux (terminal pair programming);
  - Tuple/Google Meet + compartilhamento de tela (quando o ambiente for restrito).

## Boas práticas de colaboração

- Definir `CONTRIBUTING` + padrão de commits (Conventional Commits).
- Padronizar formatação/lint em pre-commit (`black`, `ruff`, `isort`).
- Adotar revisão obrigatória de pelo menos 1 pessoa para mudanças em:
  - cálculo de notas;
  - exportação final;
  - status de processo seletivo.

## 3) Sincronização de banco entre múltiplos computadores

> Estado atual: SQLite local (`selection.db`) funciona muito bem para uso local/offline, mas **não é a melhor opção para escrita concorrente em múltiplas máquinas**.

## Estratégia A (recomendada para multiusuário): banco central

Migrar para PostgreSQL centralizado (VM, Docker server ou serviço gerenciado).

Vantagens:
- escrita concorrente robusta;
- controle transacional melhor;
- backups centralizados;
- auditoria e observabilidade mais simples.

Passos:
1. Introduzir camada de repositório desacoplada de SQLite.
2. Mapear schema atual em PostgreSQL.
3. Criar migração inicial + seed de configurações.
4. Publicar aplicação com `DATABASE_URL` por ambiente.

## Estratégia B (transição): SQLite + sincronização controlada

Se ainda não for possível migrar:

- Definir **um único nó escritor** (somente um computador faz gravações).
- Demais máquinas em modo leitura (relatórios/dashboard).
- Sincronização por snapshots versionados (backup com timestamp + checksum).
- Ativar `PRAGMA journal_mode=WAL` no escritor para reduzir lock.

> Evitar Dropbox/Drive sincronizando o mesmo `.db` simultaneamente em múltiplas máquinas.

## Estratégia C (offline-first avançado)

- Cada máquina grava localmente;
- eventos são serializados (event sourcing simplificado);
- um reconciliador central aplica regras de merge por data + origem + prioridade.

Útil quando há baixa conectividade, porém exige projeto adicional de resolução de conflitos.

## 4) Facilidade de setup em diferentes sistemas

## Ambiente padrão

- Python fixado (ex.: 3.11.x) com `pyenv` ou instalador oficial.
- Dependências por `venv` local e `requirements.txt`.
- Configurações de ambiente por arquivo `.env` (não versionar segredos).

## Script sugerido de bootstrap

Criar script `scripts/bootstrap.sh` com:
1. criação de venv;
2. instalação de dependências;
3. validação rápida (`python -m py_compile app.py ui/*.py`);
4. execução do app.

## Persistência por ambiente

- `selection.db` fora da raiz do repositório (ex.: pasta de dados local).
- Caminho do banco configurável por variável de ambiente (`SELECTION_DB_PATH`).
- Isso evita commits acidentais de banco real e facilita troca de máquina.

## 5) Segurança e integridade de dados

## Controles essenciais

- Não versionar bancos reais (`*.db`) com dados sensíveis.
- Criptografar backups (ex.: age/gpg) antes de mover entre máquinas.
- PIN administrativo: trocar padrão inicial imediatamente e registrar política de rotação.
- Princípio do menor privilégio para quem acessa exportações e área admin.

## Auditoria e rastreabilidade

- Log de auditoria estruturado com:
  - timestamp;
  - usuário/responsável;
  - ação;
  - entidade alterada.
- Assinar ou gerar hash de exportações finais para verificar integridade.

## Governança LGPD

- Minimizar dados pessoais nas telas compartilhadas.
- Mascarar campos sensíveis em sessões ao vivo.
- Definir janela de retenção e descarte de backups antigos.

## 6) Plano de execução em fases

1. **Fase 1 (rápida, 1-2 dias)**
   - Padronizar workflow Git + revisão + lint/format.
   - Remover bancos reais do versionamento.
   - Tornar caminho do banco configurável.

2. **Fase 2 (curto prazo, 1-2 semanas)**
   - Refatorar `app.py` em camadas.
   - Criar migrações versionadas.
   - Melhorar auditoria e backups.

3. **Fase 3 (médio prazo)**
   - Migrar para banco central (PostgreSQL).
   - Adicionar autenticação por usuário (não apenas PIN global).
   - Implementar observabilidade e rotina de restore testado.

---

Se quiser, no próximo passo posso transformar este plano em:
- checklist operacional de implantação;
- roadmap técnico com estimativa por tarefa;
- templates de PR e issue para o time.
