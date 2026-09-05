-- Tabela principal de vendas
CREATE TABLE IF NOT EXISTS vendas (
    id                      SERIAL PRIMARY KEY,
    NM_CLIENTE              VARCHAR(150) NOT NULL,
    CD_VENDEDOR             VARCHAR(20) NOT NULL,
    CD_PRODUTO              VARCHAR(50) NOT NULL,
    NM_FAMILIA              VARCHAR(80) NOT NULL,
    NU_VOL_LIQ              NUMERIC(12, 2) NOT NULL CHECK (NU_VOL_LIQ >= 0),
    NU_ROB                  NUMERIC(14, 2) NOT NULL CHECK (NU_ROB >= 0),
    FL_CLIENTE_COBERTO      BOOLEAN NOT NULL DEFAULT false,
    DT_DIA                  DATE NOT NULL,
    DT_CRIACAO              TIMESTAMP NOT NULL DEFAULT now()
);

-- Índices para os padrões de consulta mais prováveis do agente
-- (filtrar por vendedor, por produto/família, e por período)
CREATE INDEX IF NOT EXISTS idx_vendas_vendedor ON vendas (CD_VENDEDOR);
CREATE INDEX IF NOT EXISTS idx_vendas_produto  ON vendas (CD_PRODUTO);
CREATE INDEX IF NOT EXISTS idx_vendas_familia  ON vendas (NM_FAMILIA);
CREATE INDEX IF NOT EXISTS idx_vendas_data     ON vendas (DT_DIA);
