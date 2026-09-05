# Guia de Contribuição

## Estratégia de branches

- `main`: sempre estável/funcional. Nunca commitamos direto aqui em features grandes.
- `feat/<nome-curto>`: uma branch por funcionalidade nova (ex: `feat/agente-strands`).
- `fix/<nome-curto>`: correção de bug.
- `chore/<nome-curto>`: tarefas de manutenção (infra, configs, dependências).
- `docs/<nome-curto>`: apenas documentação.

Fluxo: criar branch → commitar → abrir Pull Request para `main` → revisar (mesmo sozinho, revisar o diff antes de mergear) → squash merge → apagar a branch.

## Padrão de commits (Conventional Commits)

Formato: `<tipo>(<escopo opcional>): <descrição curta no imperativo>`

Tipos usados neste projeto:

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação apenas |
| `chore` | Configuração, infra, dependências |
| `refactor` | Mudança de código sem alterar comportamento |
| `test` | Adição/ajuste de testes |
| `security` | Correção ou hardening relacionado a segurança |

Exemplos:
chore(infra): sobe postgres local via docker compose
feat(db): cria tabela de vendas e usuario somente-leitura
feat(agent): implementa guardrail de validacao de sql
