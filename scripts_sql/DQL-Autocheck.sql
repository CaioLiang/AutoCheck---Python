SELECT * FROM tb_usuario;
SELECT * FROM tb_login;
SELECT * FROM tb_carro;
SELECT * FROM tb_pecas;
SELECT * FROM tb_oficina;
SELECT * FROM tb_diagnostico;
SELECT * FROM tb_usuario_carro;
SELECT * FROM tb_agendamento;
SELECT * FROM tb_orcamento;
SELECT * FROM tb_carro_diagnostico;

---------------- CLASSIFICACAO DE DADOS ----------------
SELECT * 
FROM tb_agendamento
ORDER BY data_hora_agendamento;

SELECT * 
FROM tb_orcamento
ORDER BY valor_final_orcamento DESC;

---------------- TIPO NUMÉRICO SIMPLES ----------------
SELECT COUNT(*) AS total_orcamentos
FROM tb_orcamento;

SELECT SUM(valor_final_orcamento) AS total_valor_final
FROM tb_orcamento;

---------------- FUNCAO DE GRUPO ----------------
SELECT id_usuario, COUNT(CASE WHEN ativo = 'S' THEN 1 END) AS posse_ativa, COUNT(CASE WHEN ativo = 'N' THEN 1 END) AS posse_inativa
FROM tb_usuario_carro 
GROUP BY id_usuario;

SELECT id_peca, COUNT(*) AS quantidade_usadas
FROM tb_orcamento
GROUP BY id_peca
ORDER BY id_peca;

---------------- SUB CONSULTA ----------------

---------------- JUNÇÃO DE TABELAS ----------------
