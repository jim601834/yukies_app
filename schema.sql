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
    acct_xtra1 text
);


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
-- Name: accounts acct_id; Type: DEFAULT; Schema: new_schema; Owner: postgres
--

ALTER TABLE ONLY new_schema.accounts ALTER COLUMN acct_id SET DEFAULT nextval('new_schema.accounts_acct_id_seq'::regclass);


--
-- Name: my_publication; Type: PUBLICATION; Schema: -; Owner: postgres
--

CREATE PUBLICATION my_publication FOR ALL TABLES WITH (publish = 'insert, update, delete, truncate');


ALTER PUBLICATION my_publication OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

