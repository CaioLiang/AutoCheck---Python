---------------- Removendo tabelas ----------------
DROP TABLE tb_login;
DROP TABLE tb_agendamento;
DROP TABLE tb_orcamento;
DROP TABLE tb_carro_diagnostico;
DROP TABLE tb_usuario_carro;
DROP TABLE tb_diagnostico;
DROP TABLE tb_usuario;
DROP TABLE tb_carro;
DROP TABLE tb_oficina;
DROP TABLE tb_pecas;

---------------- REMOVENDO SEQUENCES ----------------
DROP SEQUENCE tb_carro_id_carro_seq;
DROP SEQUENCE tb_diagnostico_id_diagnostico_seq;
DROP SEQUENCE tb_oficina_id_oficina_seq;
DROP SEQUENCE tb_orcamento_id_orcamento_seq;
DROP SEQUENCE tb_pecas_id_peca_seq;
DROP SEQUENCE tb_usuario_id_usuario_seq;
DROP SEQUENCE tb_usuario_carro_id_usuario_carro_seq;
DROP SEQUENCE tb_carro_diagnostico_id_carro_diagnostico_seq;

---------------- CRIANDO A TB_USUARIO --------------------
CREATE TABLE tb_usuario (
    id_usuario       INTEGER NOT NULL,
    nome_usuario     VARCHAR2(100) NOT NULL,
    cpf_usuario      VARCHAR2(11) NOT NULL,
    endereco_usuario VARCHAR2(100) NOT NULL,
    tel_usuario      VARCHAR2(11) NOT NULL
);

ALTER TABLE tb_usuario ADD CONSTRAINT tb_usuario_id_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE tb_usuario ADD CONSTRAINT tb_usuario_uc UNIQUE ( cpf_usuario );

---------------- CRIANDO A TB_LOGIN --------------------
CREATE TABLE tb_login (
    id_usuario    INTEGER NOT NULL,
    login_usuario VARCHAR2(100) NOT NULL,
    senha_usuario VARCHAR2(20) NOT NULL
);

ALTER TABLE tb_login ADD CONSTRAINT tb_login_id_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE tb_login ADD CONSTRAINT tb_login_uc UNIQUE ( login_usuario );

ALTER TABLE tb_login
    ADD CONSTRAINT tb_login_id_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES tb_usuario ( id_usuario );

---------------- CRIANDO A TB_CARRO --------------------
CREATE TABLE tb_carro (
    id_carro             INTEGER NOT NULL,
    chassi_carro         VARCHAR2(17) NOT NULL,
    marca_carro          VARCHAR2(50) NOT NULL,
    modelo_carro         VARCHAR2(50) NOT NULL,
    ano_fabricacao_carro VARCHAR2(4) NOT NULL,
    ano_modelo_carro     VARCHAR2(4) NOT NULL
);

ALTER TABLE tb_carro ADD CONSTRAINT tb_carro_id_carro_pk PRIMARY KEY ( id_carro );

ALTER TABLE tb_carro ADD CONSTRAINT tb_carro_uc UNIQUE ( chassi_carro );

---------------- CRIANDO A TB_USUARIO_CARRO --------------------
CREATE TABLE tb_usuario_carro (
    id_usuario_carro INTEGER NOT NULL,
    id_usuario       INTEGER NOT NULL,
    id_carro         INTEGER NOT NULL,
    ativo            CHAR(1) NOT NULL
);

ALTER TABLE tb_usuario_carro
    ADD CONSTRAINT chk_ativo CHECK ( ativo IN ( 'S', 'N' ) );

ALTER TABLE tb_usuario_carro ADD CONSTRAINT tb_usuario_carro_id_usuario_carro_pk PRIMARY KEY ( id_usuario_carro );

ALTER TABLE tb_usuario_carro
    ADD CONSTRAINT tb_usuario_carro_id_carro_fk FOREIGN KEY ( id_carro )
        REFERENCES tb_carro ( id_carro );

ALTER TABLE tb_usuario_carro
    ADD CONSTRAINT tb_usuario_carro_id_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES tb_usuario ( id_usuario );

---------------- CRIANDO A TB_DIAGNOSTICO --------------------
CREATE TABLE tb_diagnostico (
    id_diagnostico                 INTEGER NOT NULL,
    cod_falha_diagnostico          VARCHAR2(5),
    categoria_diagnostico          VARCHAR2(1) NOT NULL,
    descricao_diagnostico          VARCHAR2(100) NOT NULL,
    descricao_problema_diagnostico VARCHAR2(240) NOT NULL
);

ALTER TABLE tb_diagnostico ADD CONSTRAINT tb_diagnostico_id_diagnostico_pk PRIMARY KEY ( id_diagnostico );

---------------- CRIANDO A TB_CARRO_DIAGNOSTICO --------------------
CREATE TABLE tb_carro_diagnostico (
    id_carro_diagnostico INTEGER NOT NULL,
    id_diagnostico       INTEGER NOT NULL,
    id_carro             INTEGER NOT NULL
);

ALTER TABLE tb_carro_diagnostico ADD CONSTRAINT tb_carro_diagnostico_pk PRIMARY KEY ( id_carro_diagnostico );

ALTER TABLE tb_carro_diagnostico
    ADD CONSTRAINT tb_carro_diagnostico_id_carro_fk FOREIGN KEY ( id_carro )
        REFERENCES tb_carro ( id_carro );
        
ALTER TABLE tb_carro_diagnostico
    ADD CONSTRAINT tb_diagnostico_id_diagnostico_fk FOREIGN KEY ( id_diagnostico )
        REFERENCES tb_diagnostico ( id_diagnostico );

---------------- CRIANDO A TB_OFICINA --------------------
CREATE TABLE tb_oficina (
    id_oficina          INTEGER NOT NULL,
    unidade_oficina     VARCHAR2(100) NOT NULL,
    cep_oficina         VARCHAR2(8) NOT NULL,
    numero_oficina      VARCHAR2(100) NOT NULL,
    responsavel_oficina VARCHAR2(100) NOT NULL
);

ALTER TABLE tb_oficina ADD CONSTRAINT tb_oficina_id_oficina_pk PRIMARY KEY ( id_oficina );

---------------- CRIANDO A TB_AGENDAMENTO --------------------
CREATE TABLE tb_agendamento (
    id_carro_diagnostico        INTEGER NOT NULL,
    id_oficina                  INTEGER NOT NULL,
    disponibilidade_agendamento CHAR(1) NOT NULL,
    data_hora_agendamento       TIMESTAMP NOT NULL
);

ALTER TABLE tb_agendamento
    ADD CONSTRAINT chk_disponibilidade CHECK ( disponibilidade_agendamento IN ( 'S', 'N' ) );
    
ALTER TABLE tb_agendamento
    ADD CONSTRAINT tb_agendamento_id_oficina_fk FOREIGN KEY ( id_oficina )
        REFERENCES tb_oficina ( id_oficina );
        
ALTER TABLE tb_agendamento
    ADD CONSTRAINT tb_carro_diagnostico_id_carro_diagnostico_fkv1 FOREIGN KEY ( id_carro_diagnostico )
        REFERENCES tb_carro_diagnostico ( id_carro_diagnostico );
        
---------------- CRIANDO A TB_PECAS --------------------
CREATE TABLE tb_pecas (
    id_peca    INTEGER NOT NULL,
    nome_peca  VARCHAR2(100) NOT NULL,
    valor_peca NUMBER(9, 2) NOT NULL
);

ALTER TABLE tb_pecas ADD CONSTRAINT tb_pecas_id_peca_pk PRIMARY KEY ( id_peca );

---------------- CRIANDO A TB_ORCAMENTO --------------------
CREATE TABLE tb_orcamento (
    id_orcamento             INTEGER NOT NULL,
    id_carro_diagnostico     INTEGER NOT NULL,
    id_peca                  INTEGER NOT NULL,
    valor_final_orcamento    NUMBER(9, 2) NOT NULL,
    valor_mao_obra_orcamento NUMBER(9, 2) NOT NULL,
    data_hora_orcamento      TIMESTAMP NOT NULL
);

ALTER TABLE tb_orcamento ADD CONSTRAINT tb_orcamento_id_diagnostico_pk PRIMARY KEY ( id_orcamento );

ALTER TABLE tb_orcamento ADD CONSTRAINT tb_diagnostico_uc UNIQUE ( id_carro_diagnostico );

ALTER TABLE tb_orcamento
    ADD CONSTRAINT tb_orcamento_id_peca_fk FOREIGN KEY ( id_peca )
        REFERENCES tb_pecas ( id_peca );
        
ALTER TABLE tb_orcamento
    ADD CONSTRAINT tb_carro_diagnostico_id_carro_diagnostico_fk FOREIGN KEY ( id_carro_diagnostico )
        REFERENCES tb_carro_diagnostico ( id_carro_diagnostico );

---------------- CRIANDO AS SEQUENCES --------------------
CREATE SEQUENCE tb_carro_id_carro_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_carro_id_carro_trg BEFORE
    INSERT ON tb_carro
    FOR EACH ROW
    WHEN ( new.id_carro IS NULL )
BEGIN
    :new.id_carro := tb_carro_id_carro_seq.nextval;
END;
/

CREATE SEQUENCE tb_carro_diagnostico_id_carro_diagnostico_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_carro_diagnostico_id_carro_diagnostico_trg BEFORE
    INSERT ON tb_carro_diagnostico
    FOR EACH ROW
    WHEN ( new.id_carro_diagnostico IS NULL )
BEGIN
    :new.id_carro_diagnostico := tb_carro_diagnostico_id_carro_diagnostico_seq.nextval;
END;
/

CREATE SEQUENCE tb_diagnostico_id_diagnostico_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_diagnostico_id_diagnostico_trg BEFORE
    INSERT ON tb_diagnostico
    FOR EACH ROW
    WHEN ( new.id_diagnostico IS NULL )
BEGIN
    :new.id_diagnostico := tb_diagnostico_id_diagnostico_seq.nextval;
END;
/

CREATE SEQUENCE tb_oficina_id_oficina_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_oficina_id_oficina_trg BEFORE
    INSERT ON tb_oficina
    FOR EACH ROW
    WHEN ( new.id_oficina IS NULL )
BEGIN
    :new.id_oficina := tb_oficina_id_oficina_seq.nextval;
END;
/

CREATE SEQUENCE tb_orcamento_id_orcamento_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_orcamento_id_orcamento_trg BEFORE
    INSERT ON tb_orcamento
    FOR EACH ROW
    WHEN ( new.id_orcamento IS NULL )
BEGIN
    :new.id_orcamento := tb_orcamento_id_orcamento_seq.nextval;
END;
/

CREATE SEQUENCE tb_pecas_id_peca_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_pecas_id_peca_trg BEFORE
    INSERT ON tb_pecas
    FOR EACH ROW
    WHEN ( new.id_peca IS NULL )
BEGIN
    :new.id_peca := tb_pecas_id_peca_seq.nextval;
END;
/

CREATE SEQUENCE tb_usuario_id_usuario_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_usuario_id_usuario_trg BEFORE
    INSERT ON tb_usuario
    FOR EACH ROW
    WHEN ( new.id_usuario IS NULL )
BEGIN
    :new.id_usuario := tb_usuario_id_usuario_seq.nextval;
END;
/

CREATE SEQUENCE tb_usuario_carro_id_usuario_carro_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tb_usuario_carro_id_usuario_carro_trg BEFORE
    INSERT ON tb_usuario_carro
    FOR EACH ROW
    WHEN ( new.id_usuario_carro IS NULL )
BEGIN
    :new.id_usuario_carro := tb_usuario_carro_id_usuario_carro_seq.nextval;
END;
/