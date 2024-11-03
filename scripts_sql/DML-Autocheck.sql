-- Inserindo dados fictícios na tb_usuario
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Ana Silva', '11111111111', 'Rua A, 123', '11987654321');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Bruno Costa', '22222222222', 'Rua B, 234', '11987654322');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Carlos Souza', '33333333333', 'Rua C, 345', '11987654323');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Daniela Lima', '44444444444', 'Rua D, 456', '11987654324');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Eduardo Pereira', '55555555555', 'Rua E, 567', '11987654325');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Fernanda Martins', '66666666666', 'Rua F, 678', '11987654326');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Gabriel Alves', '77777777777', 'Rua G, 789', '11987654327');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Helena Rocha', '88888888888', 'Rua H, 890', '11987654328');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Igor Fonseca', '99999999999', 'Rua I, 901', '11987654329');
INSERT INTO tb_usuario (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('Julia Teixeira', '10101010101', 'Rua J, 101', '11987654330');

-- Inserindo dados fictícios na tb_login
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (1, 'ana_silva', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (2, 'bruno_costa', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (3, 'carlos_souza', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (4, 'daniela_lima', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (5, 'eduardo_pereira', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (6, 'fernanda_martins', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (7, 'gabriel_alves', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (8, 'helena_rocha', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (9, 'igor_fonseca', 'senha123');
INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES (10, 'julia_teixeira', 'senha123');

-- Inserindo dados fictícios na tb_carro
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('ABC12345678901234', 'Toyota', 'Corolla', '2020', '2021');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('BCD23456789012345', 'Honda', 'Civic', '2019', '2019');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('CDE34567890123456', 'Ford', 'Focus', '2018', '2019');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('DEF45678901234567', 'Chevrolet', 'Cruze', '2021', '2022');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('EFG56789012345678', 'Hyundai', 'Elantra', '2020', '2020');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('FGH67890123456789', 'Volkswagen', 'Golf', '2019', '2020');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('GHI78901234567890', 'BMW', '320i', '2021', '2021');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('HIJ89012345678901', 'Audi', 'A4', '2018', '2019');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('IJK90123456789012', 'Nissan', 'Sentra', '2020', '2020');
INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('JKL01234567890123', 'Mitsubishi', 'Lancer', '2017', '2018');

-- Inserindo dados fictícios na tb_pecas
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Filtro de óleo', 30.50);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Pastilha de freio', 120.00);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Correia dentada', 90.75);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Bateria 60Ah', 280.99);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Velas de ignição', 50.20);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Radiador', 350.80);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Amortecedor', 230.00);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Disco de freio', 180.00);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Filtro de ar', 20.00);
INSERT INTO tb_pecas (nome_peca, valor_peca) VALUES ('Cabo de vela', 45.00);

-- Inserindo dados fictícios na tb_oficina
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina Auto Center', '12345678', '123', 'João Silva');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina CarTech', '87654321', '456', 'Maria Santos');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina Mecânica Top', '13579246', '789', 'Carlos Costa');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina Turbo Motors', '24681357', '321', 'Patrícia Souza');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina Rápida', '11223344', '654', 'Roberto Lima');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Auto Mecânica', '22334455', '987', 'André Almeida');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina Premium', '33445566', '432', 'Juliana Fernandes');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Mecânica Geral', '44556677', '765', 'Ricardo Alves');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Oficina do Bairro', '55667788', '109', 'Fernanda Ribeiro');
INSERT INTO tb_oficina (unidade_oficina, cep_oficina, numero_oficina, responsavel_oficina) VALUES ('Centro Automotivo', '66778899', '210', 'Marcos Pinheiro');

-- Inserindo dados fictícios na tb_diagnostico
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0010', 'E', 'Falha no circuito A', 'Problema no circuito de comando de válvulas');
INSERT INTO tb_diagnostico (categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('M', 'Sensor de fluxo de ar baixo', 'Medida baixa no sensor de fluxo de ar');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0171', 'C', 'Sistema muito pobre', 'Mistura de combustível pobre detectada');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0300', 'E', 'Falha de ignição aleatória', 'Falha aleatória de ignição em múltiplos cilindros');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0420', 'E', 'Eficiência do catalisador baixa', 'Baixa eficiência no sistema de catalisador');
INSERT INTO tb_diagnostico (categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('T', 'Sensor de velocidade do veículo', 'Falha detectada no sensor de velocidade');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0700', 'T', 'Falha no sistema de transmissão', 'Erro geral no sistema de transmissão');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P1101', 'E', 'Fluxo de ar fora do intervalo', 'Valor do fluxo de ar fora do intervalo esperado');
INSERT INTO tb_diagnostico (categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('E', 'Falha no sistema de controle do motor', 'Erro geral no sistema de controle do motor');
INSERT INTO tb_diagnostico (categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('C', 'Mistura pobre em marcha lenta', 'Mistura de combustível pobre em marcha lenta detectada');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0012', 'E', 'Válvula de controle de fase com falha', 'Problema no tempo de abertura/fechamento da válvula');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0128', 'M', 'Temperatura do motor abaixo do esperado', 'O motor não atinge a temperatura ideal de operação');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0301', 'E', 'Falha de ignição no cilindro 1', 'Detecção de falha de ignição específica no cilindro 1');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0340', 'E', 'Falha no sensor de posição do comando de válvulas', 'Erro na leitura do sensor de posição do comando de válvulas');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0455', 'C', 'Vazamento no sistema de recuperação de vapores', 'Detectado vazamento no sistema de emissões evaporativas');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0506', 'T', 'RPM do motor muito baixo', 'O motor opera em uma faixa de RPM muito abaixo do normal');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P0705', 'T', 'Sensor de posição da transmissão com falha', 'Problema na leitura do sensor de posição da transmissão');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P1130', 'E', 'Sensor de oxigênio fora do intervalo', 'Sensor de oxigênio está apresentando leituras inconsistentes');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P2279', 'C', 'Vazamento no sistema de admissão', 'Detectado vazamento de ar no sistema de admissão');
INSERT INTO tb_diagnostico (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('P2189', 'C', 'Mistura rica em marcha lenta', 'Mistura de combustível rica em marcha lenta detectada');


-- Inserindo dados fictícios na tb_usuario_carro
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (1, 1, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (1, 2, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (2, 3, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (2, 4, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (3, 5, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (3, 6, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (4, 7, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (4, 8, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (5, 9, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (5, 10, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (6, 1, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (6, 2, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (7, 3, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (7, 4, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (8, 5, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (8, 6, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (9, 7, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (9, 8, 'N');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (10, 9, 'S');
INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES (10, 10, 'N');

-- Inserindo dados fictícios na tb_carro_diagnostico
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (1, 1);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (2, 3);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (3, 2);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (4, 6);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (5, 10);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (6, 8);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (7, 4);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (8, 7);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (9, 9);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (10, 5);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (11, 1);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (12, 3);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (13, 2);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (14, 6);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (15, 10);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (16, 8);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (17, 4);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (18, 7);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (19, 9);
INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES (20, 5);

-- Inserindo dados fictícios na tb_agendamento
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (4, 1, 'N', TO_TIMESTAMP('2024-11-03 11:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (2, 2, 'S', TO_TIMESTAMP('2024-11-02 14:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (7, 3, 'N', TO_TIMESTAMP('2024-11-04 10:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (1, 4, 'S', TO_TIMESTAMP('2024-11-01 09:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (1, 5, 'N', TO_TIMESTAMP('2024-11-01 10:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (3, 6, 'S', TO_TIMESTAMP('2024-11-02 15:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (10, 7, 'N', TO_TIMESTAMP('2024-11-06 14:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (5, 8, 'S', TO_TIMESTAMP('2024-11-03 13:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (7, 9, 'N', TO_TIMESTAMP('2024-11-09 12:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (6, 10, 'S', TO_TIMESTAMP('2024-11-04 08:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (2, 11, 'N', TO_TIMESTAMP('2024-11-07 09:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (8, 12, 'S', TO_TIMESTAMP('2024-11-05 11:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (9, 13, 'N', TO_TIMESTAMP('2024-11-05 12:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (10, 14, 'S', TO_TIMESTAMP('2024-11-06 15:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (6, 15, 'N', TO_TIMESTAMP('2024-11-09 10:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (4, 16, 'S', TO_TIMESTAMP('2024-11-08 14:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (3, 17, 'N', TO_TIMESTAMP('2024-11-07 11:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (8, 18, 'S', TO_TIMESTAMP('2024-11-10 13:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (9, 19, 'N', TO_TIMESTAMP('2024-11-10 15:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_agendamento (id_oficina, id_carro_diagnostico, disponibilidade_agendamento, data_hora_agendamento) VALUES (5, 20, 'S', TO_TIMESTAMP('2024-11-08 16:00:00', 'YYYY-MM-DD HH24:MI:SS'));

-- Inserindo dados fictícios na tb_orcamento
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (1, 1, 350.75, 200.00, TO_TIMESTAMP('2024-10-01 08:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (2, 2, 320.00, 180.00, TO_TIMESTAMP('2024-10-02 09:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (3, 3, 400.00, 220.00, TO_TIMESTAMP('2024-10-03 10:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (4, 4, 350.00, 150.00, TO_TIMESTAMP('2024-10-04 11:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (5, 5, 1900.00, 130.00, TO_TIMESTAMP('2024-10-05 14:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (6, 6, 450.00, 300.00, TO_TIMESTAMP('2024-10-06 08:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (7, 7, 500.00, 250.00, TO_TIMESTAMP('2024-10-07 13:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (8, 8, 280.00, 200.00, TO_TIMESTAMP('2024-10-08 15:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (9, 9, 330.00, 150.00, TO_TIMESTAMP('2024-10-09 09:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (10, 10, 260.00, 160.00, TO_TIMESTAMP('2024-10-10 12:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (11, 6, 480.00, 250.00, TO_TIMESTAMP('2024-10-11 10:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (12, 8, 320.00, 160.00, TO_TIMESTAMP('2024-10-12 09:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (13, 2, 350.00, 200.00, TO_TIMESTAMP('2024-10-13 14:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (14, 3, 280.00, 150.00, TO_TIMESTAMP('2024-10-14 11:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (15, 4, 600.00, 300.00, TO_TIMESTAMP('2024-10-15 08:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (16, 1, 280.00, 120.00, TO_TIMESTAMP('2024-10-16 10:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (17, 5, 180.00, 100.00, TO_TIMESTAMP('2024-10-17 09:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (18, 9, 190.00, 80.00, TO_TIMESTAMP('2024-10-18 12:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (19, 10, 170.00, 70.00, TO_TIMESTAMP('2024-10-19 13:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO tb_orcamento (id_carro_diagnostico, id_peca, valor_final_orcamento, valor_mao_obra_orcamento, data_hora_orcamento) VALUES (20, 7, 400.00, 200.00, TO_TIMESTAMP('2024-10-20 14:30:00', 'YYYY-MM-DD HH24:MI:SS'));