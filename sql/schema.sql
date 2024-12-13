--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: new_schema; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA new_schema;


ALTER SCHEMA new_schema OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: accounts; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.accounts (
    acct_name text,
    acct_type text,
    acct_category text,
    acct_balance numeric(10,2),
    acct_link text,
    acct_pmt_method text,
    acct_id integer NOT NULL,
    acct_subcategory text,
    acct_location jsonb,
    acct_distance numeric(5,1),
    comments character varying(100)
);

ALTER TABLE ONLY new_schema.accounts REPLICA IDENTITY FULL;


ALTER TABLE new_schema.accounts OWNER TO postgres;

--
-- Name: accounts_acct_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.accounts_acct_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.accounts_acct_id_seq OWNER TO postgres;

--
-- Name: accounts_acct_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.accounts_acct_id_seq OWNED BY new_schema.accounts.acct_id;


--
-- Name: accounts_with_top_level; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.accounts_with_top_level AS
 WITH RECURSIVE account_chain AS (
         SELECT accounts.acct_id,
            accounts.acct_name,
            accounts.acct_type,
            accounts.acct_category,
            accounts.acct_balance,
            accounts.acct_link,
            accounts.acct_pmt_method,
            accounts.acct_subcategory AS acct_xtra1,
            accounts.acct_location,
            accounts.acct_distance,
            accounts.comments,
            accounts.acct_name AS top_level_name
           FROM new_schema.accounts
          WHERE (accounts.acct_link IS NULL)
        UNION ALL
         SELECT a.acct_id,
            a.acct_name,
            a.acct_type,
            a.acct_category,
            a.acct_balance,
            a.acct_link,
            a.acct_pmt_method,
            a.acct_subcategory AS acct_xtra1,
            a.acct_location,
            a.acct_distance,
            a.comments,
            c.top_level_name
           FROM (new_schema.accounts a
             JOIN account_chain c ON ((a.acct_link = c.acct_name)))
        )
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM account_chain;


ALTER VIEW new_schema.accounts_with_top_level OWNER TO postgres;

--
-- Name: actions; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.actions (
    id integer NOT NULL,
    entry_date date,
    entry_time time without time zone,
    "account-name" character varying,
    amount numeric(10,2)
);


ALTER TABLE new_schema.actions OWNER TO postgres;

--
-- Name: actions_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.actions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.actions_id_seq OWNER TO postgres;

--
-- Name: actions_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.actions_id_seq OWNED BY new_schema.actions.id;


--
-- Name: automatic_transactions; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.automatic_transactions (
    id integer NOT NULL,
    transaction_name character varying(100),
    day_of_month integer,
    amount numeric(10,2),
    to_account character varying(50),
    from_account character varying(50),
    category character varying(50)
);


ALTER TABLE new_schema.automatic_transactions OWNER TO postgres;

--
-- Name: automatic_transactions_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.automatic_transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.automatic_transactions_id_seq OWNER TO postgres;

--
-- Name: automatic_transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.automatic_transactions_id_seq OWNED BY new_schema.automatic_transactions.id;


--
-- Name: budget; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.budget (
    id integer NOT NULL,
    category character varying NOT NULL,
    amount numeric(10,2),
    spent numeric(10,2),
    remaining numeric(10,2),
    display character varying
);


ALTER TABLE new_schema.budget OWNER TO postgres;

--
-- Name: budget_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.budget_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.budget_id_seq OWNER TO postgres;

--
-- Name: budget_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.budget_id_seq OWNED BY new_schema.budget.id;


--
-- Name: pmt_methods; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.pmt_methods (
    id integer NOT NULL,
    card_name character varying,
    statement_balance numeric,
    current_balance numeric,
    monthly_balance numeric,
    last_pmt_amount numeric,
    last_pmt_date character varying,
    closing_date date,
    payment_date date,
    valid_date date,
    "card number" character varying,
    "Type" character varying
);


ALTER TABLE new_schema.pmt_methods OWNER TO postgres;

--
-- Name: credit_card_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.credit_card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.credit_card_id_seq OWNER TO postgres;

--
-- Name: credit_card_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.credit_card_id_seq OWNED BY new_schema.pmt_methods.id;


--
-- Name: top_level_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.top_level_view AS
 WITH RECURSIVE account_chain AS (
         SELECT accounts.acct_id,
            accounts.acct_name,
            accounts.acct_type,
            accounts.acct_category,
            accounts.acct_balance,
            accounts.acct_link,
            accounts.acct_pmt_method,
            accounts.acct_subcategory AS acct_xtra1,
            accounts.acct_location,
            accounts.acct_distance,
            accounts.comments,
            accounts.acct_name AS top_level_name
           FROM new_schema.accounts
          WHERE (accounts.acct_link IS NULL)
        UNION ALL
         SELECT a.acct_id,
            a.acct_name,
            a.acct_type,
            a.acct_category,
            a.acct_balance,
            a.acct_link,
            a.acct_pmt_method,
            a.acct_subcategory AS acct_xtra1,
            a.acct_location,
            a.acct_distance,
            a.comments,
            c.top_level_name
           FROM (new_schema.accounts a
             JOIN account_chain c ON ((a.acct_link = c.acct_name)))
        )
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM account_chain;


ALTER VIEW new_schema.top_level_view OWNER TO postgres;

--
-- Name: deposit_from_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.deposit_from_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = 'Payor'::text);


ALTER VIEW new_schema.deposit_from_view OWNER TO postgres;

--
-- Name: deposit_to_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.deposit_to_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Checking'::text, 'Savings'::text]));


ALTER VIEW new_schema.deposit_to_view OWNER TO postgres;

--
-- Name: pay_from_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.pay_from_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Card'::text, 'Checking'::text]));


ALTER VIEW new_schema.pay_from_view OWNER TO postgres;

--
-- Name: pay_to_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.pay_to_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Provider'::text, 'Payee'::text]));


ALTER VIEW new_schema.pay_to_view OWNER TO postgres;

--
-- Name: persistent_state; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.persistent_state (
    id integer NOT NULL,
    state_key character varying(100) NOT NULL,
    state_value character varying(255),
    last_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE new_schema.persistent_state OWNER TO postgres;

--
-- Name: persistent_state_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.persistent_state_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.persistent_state_id_seq OWNER TO postgres;

--
-- Name: persistent_state_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.persistent_state_id_seq OWNED BY new_schema.persistent_state.id;


--
-- Name: qlog; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.qlog (
    id integer NOT NULL,
    entry_date date,
    entry_time time without time zone,
    service_date date,
    category character varying,
    to_account character varying,
    amount money,
    from__account character varying,
    status character varying,
    comment character varying,
    image bytea,
    exec_time time without time zone,
    deduction character varying,
    t_code character varying,
    distance character varying
);


ALTER TABLE new_schema.qlog OWNER TO postgres;

--
-- Name: qlog_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.qlog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.qlog_id_seq OWNER TO postgres;

--
-- Name: qlog_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.qlog_id_seq OWNED BY new_schema.qlog.id;


--
-- Name: transfer_from_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.transfer_from_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Checking'::text, 'Savings'::text, 'Investment'::text]));


ALTER VIEW new_schema.transfer_from_view OWNER TO postgres;

--
-- Name: transfer_to_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.transfer_to_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Checking'::text, 'Savings'::text, 'Investment'::text, 'Card'::text, 'Mortgage'::text]));


ALTER VIEW new_schema.transfer_to_view OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: new_schema; Owner: postgres
--

CREATE TABLE new_schema.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE new_schema.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: new_schema; Owner: postgres
--

CREATE SEQUENCE new_schema.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE new_schema.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: new_schema; Owner: postgres
--

ALTER SEQUENCE new_schema.users_id_seq OWNED BY new_schema.users.id;


--
-- Name: withdraw_from_view; Type: VIEW; Schema: new_schema; Owner: postgres
--

CREATE VIEW new_schema.withdraw_from_view AS
 SELECT acct_id,
    acct_name,
    acct_type,
    acct_category,
    acct_balance,
    acct_link,
    acct_pmt_method,
    acct_xtra1,
    acct_location,
    acct_distance,
    comments,
    top_level_name
   FROM new_schema.top_level_view
  WHERE (acct_type = ANY (ARRAY['Checking'::text, 'Savings'::text]));


ALTER VIEW new_schema.withdraw_from_view OWNER TO postgres;

--
-- Name: accounts acct_id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.accounts ALTER COLUMN acct_id SET DEFAULT nextval('new_schema.accounts_acct_id_seq'::regclass);


--
-- Name: actions id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.actions ALTER COLUMN id SET DEFAULT nextval('new_schema.actions_id_seq'::regclass);


--
-- Name: automatic_transactions id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.automatic_transactions ALTER COLUMN id SET DEFAULT nextval('new_schema.automatic_transactions_id_seq'::regclass);


--
-- Name: budget id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.budget ALTER COLUMN id SET DEFAULT nextval('new_schema.budget_id_seq'::regclass);


--
-- Name: persistent_state id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.persistent_state ALTER COLUMN id SET DEFAULT nextval('new_schema.persistent_state_id_seq'::regclass);


--
-- Name: pmt_methods id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.pmt_methods ALTER COLUMN id SET DEFAULT nextval('new_schema.credit_card_id_seq'::regclass);


--
-- Name: qlog id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.qlog ALTER COLUMN id SET DEFAULT nextval('new_schema.qlog_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.users ALTER COLUMN id SET DEFAULT nextval('new_schema.users_id_seq'::regclass);


--
-- Name: actions actions_pk; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.actions
    ADD CONSTRAINT actions_pk PRIMARY KEY (id);


--
-- Name: automatic_transactions automatic_transactions_pkey; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.automatic_transactions
    ADD CONSTRAINT automatic_transactions_pkey PRIMARY KEY (id);


--
-- Name: budget budget_pk; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.budget
    ADD CONSTRAINT budget_pk PRIMARY KEY (id);


--
-- Name: pmt_methods credit_card_pk; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.pmt_methods
    ADD CONSTRAINT credit_card_pk PRIMARY KEY (id);


--
-- Name: persistent_state persistent_state_pkey; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.persistent_state
    ADD CONSTRAINT persistent_state_pkey PRIMARY KEY (id);


--
-- Name: persistent_state persistent_state_state_key_key; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.persistent_state
    ADD CONSTRAINT persistent_state_state_key_key UNIQUE (state_key);


--
-- Name: qlog qlog_pk; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.qlog
    ADD CONSTRAINT qlog_pk PRIMARY KEY (id);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

