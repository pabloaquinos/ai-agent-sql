-- Tabela principal de vendas
CREATE TABLE IF NOT EXISTS vendas (
    id                      SERIAL PRIMARY KEY,
    nm_cliente              VARCHAR(150) NOT NULL,
    cd_vendedor             VARCHAR(20) NOT NULL,
    cd_produto              VARCHAR(50) NOT NULL,
    nm_familia              VARCHAR(80) NOT NULL,
    nu_vol_liq              NUMERIC(12, 2) NOT NULL CHECK (nu_vol_liq >= 0),
    nu_rob                  NUMERIC(14, 2) NOT NULL CHECK (nu_rob >= 0),
    fl_cliente_coberto      BOOLEAN NOT NULL DEFAULT false,
    dt_dia                  DATE NOT NULL,
    dt_criacao              TIMESTAMP NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_vendas_vendedor ON vendas (cd_vendedor);
CREATE INDEX IF NOT EXISTS idx_vendas_produto  ON vendas (cd_produto);
CREATE INDEX IF NOT EXISTS idx_vendas_familia  ON vendas (nm_familia);
CREATE INDEX IF NOT EXISTS idx_vendas_data     ON vendas (dt_dia);