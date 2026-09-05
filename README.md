cat > README.md << 'EOF'
# Agente SQL com IA

Agente de IA que consulta um banco PostgreSQL via linguagem natural, usando
Strands Agents + Amazon Bedrock, com observabilidade via Langfuse, memória
via Bedrock AgentCore Memory, e deploy serverless na AWS (Lambda + API Gateway).

## Status do projeto

🚧 Em desenvolvimento — construído incrementalmente, fase por fase.

## Stack

- **Banco de dados:** PostgreSQL
- **Orquestração do agente:** Strands Agents (AWS)
- **Modelo de IA:** Amazon Bedrock (Claude)
- **Memória:** Amazon Bedrock AgentCore Memory
- **Observabilidade:** Langfuse
- **Armazenamento:** Amazon S3
- **Autenticação:** JWT (Amazon Cognito)
- **Deploy:** AWS Lambda + API Gateway

## Como rodar localmente

Instruções detalhadas serão adicionadas conforme cada fase for implementada.

## Como contribuir

Ver [CONTRIBUTING.md](./CONTRIBUTING.md) para o padrão de commits e branches.
EOF