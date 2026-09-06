from bedrock_agentcore.memory import MemoryClient

from src.config import settings

def main() -> None:
    client = MemoryClient(region_name=settings.aws_region)

    memoria = client.create_memory(
        name="AgentSqlIaMemory",
        description="Memoria de curto rpazo do agente de faturamento",
    )

    print(f"Memoria criada com sucesso.")
    print(f"MEMORY ID: {memoria['id']}")

if __name__ == "__main__":
    main()