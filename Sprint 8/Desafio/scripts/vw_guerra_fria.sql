CREATE OR REPLACE VIEW pgdm_desafio.vw_guerra_fria AS
WITH filmes_paises AS (
  SELECT 
    f.id,
    f.id_imdb,
    df.titulo_principal,
    p.id_pais,
    p.nome_pais,
    f.data,
    d.ano,
    d.decada,
    f.votos_tmdb,
    f.media_tmdb,
    f.votos_imdb,
    f.media_imdb,
    f.orcamento,
    f.recebimento,
    d.periodo_historico,
    CASE
      WHEN p.id_pais = 58 THEN 'ocidente'
      WHEN p.id_pais = 53 THEN 'soviete'
      ELSE 'outro'
    END AS bloco_historico
  FROM 
    pgdm_desafio.fato_filmes_avaliacao f
  JOIN
    pgdm_desafio.dim_filmes df ON f.id_imdb = df.id_imdb
  CROSS JOIN 
    UNNEST(f.id_pais) AS t(id_pais_unnested)
  JOIN 
    pgdm_desafio.dim_pais p ON t.id_pais_unnested = p.id_pais
  JOIN 
    pgdm_desafio.dim_data d ON f.data = d.data
  WHERE 
    d.periodo_historico = 'guerra fria'
)
SELECT 
  id,
  id_imdb,
  titulo_principal,
  id_pais,
  nome_pais,
  data,
  ano,
  decada,
  votos_tmdb,
  media_tmdb,
  votos_imdb,
  media_imdb,
  orcamento,
  recebimento,
  periodo_historico,
  bloco_historico
FROM 
  filmes_paises
WHERE 
  bloco_historico IN ('ocidente', 'soviete');
