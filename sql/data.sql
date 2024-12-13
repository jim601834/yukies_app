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
-- Data for Name: accounts; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.accounts (acct_name, acct_type, acct_category, acct_balance, acct_link, acct_pmt_method, acct_id, acct_subcategory, acct_location, acct_distance, comments) FROM stdin;
Dana	Provider	Medical	0.00	AZ Oncology Wilmot	\N	11	\N	\N	\N	\N
AZ Oncology Wilmot	Location	Medical	0.00	AZ Oncology	\N	13	\N	\N	\N	\N
Gin	Provider	Medical	0.00	AZ Oncology St Joseph	\N	14	\N	\N	\N	\N
Yurkanin	Provider	Medical	0.00	AZ Minimally Invasive	\N	47	\N	\N	\N	\N
Sonora Quest	Provider	Medical	0.00	\N	\N	49	\N	\N	\N	\N
St Joseph PT	Location	Medical	0.00	St Joseph	\N	18	\N	\N	\N	\N
Mayer	Provider	Medical	0.00	Coronado Internal Medicine	\N	21	\N	\N	\N	\N
Lui	Provider	Medical	0.00	SW Kidney	\N	25	\N	\N	\N	\N
Mayer RSRV	Reserve	Medical	0.00		\N	23	\N	\N	\N	\N
Chris PT	Provider	Medical	0.00	St Joseph PT	\N	17	\N	\N	\N	\N
Beer	Provider	Medical	0.00	SW Hand	\N	29	\N	\N	\N	\N
Bernstein	Provider	Medical	0.00	Urology Care	\N	30	\N	\N	\N	\N
Boiangiu	Provider	Medical	0.00	Pima Heart Glenn	\N	32	\N	\N	\N	\N
Perez	Provider	Medical	0.00	Pima Heart Camp Lowell	\N	36	\N	\N	\N	\N
Pima Heart Camp Lowell	Location	Medical	0.00	Pima Heart	\N	37	\N	\N	\N	\N
Faitelson	Provider	Medical	0.00	Pima Heart Glenn	\N	38	\N	\N	\N	\N
Winter	Provider	Medical	0.00	Pima Heart River	\N	39	\N	\N	\N	\N
Pima Heart River	Location	Medical	0.00	Pima Heart	\N	40	\N	\N	\N	\N
Davies	Provider	Medical	0.00	AZ Hearing	\N	41	\N	\N	\N	\N
Swingle	Provider	Medical	0.00	AZ Hearing	\N	43	\N	\N	\N	\N
Kaye	Provider	Medical	0.00	Tucson Eye Care	\N	44	\N	\N	\N	\N
David BMW	Provider	Services	0.00	Desert Tech	\N	99	\N	\N	\N	\N
Truly Nolen	Provider	Services	0.00	\N	\N	119	\N	\N	\N	\N
Pioneer Pest Control	Provider	Services	0.00	\N	\N	121	\N	\N	\N	\N
Hanger	Provider	Medical	0.00	\N	\N	53	\N	\N	\N	\N
Radiology LTD	Provider	Medical	0.00	\N	\N	54	\N	\N	\N	\N
Water Tech	Provider	Services	0.00	\N	\N	122	\N	\N	\N	\N
Jim Myers	Provider	Services	0.00	\N	\N	123	\N	\N	\N	\N
TEP	Provider	Utilities	0.00	\N	\N	110	\N	\N	\N	\N
Amerigas	Provider	Utilities	0.00	\N	\N	113	\N	\N	\N	\N
Cash	Cash	Payment Method	0.00	\N	\N	142	\N	\N	\N	\N
B of A 7660	Card	Payment Method	0.00	B of A	\N	116	\N	\N	\N	\N
B of A 4968	Card	Payment Method	0.00	B of A	\N	144	\N	\N	\N	\N
B of A 4666	Card	Payment Method	0.00	B of A	\N	145	\N	\N	\N	\N
Chase 3587	Check	Payment Method	0.00	\N	\N	148	\N	\N	\N	\N
ADE	Payee	Medical	0.00	\N	\N	98	\N	\N	\N	\N
Paypal 4139	Card	Payment Method	0.00	Synchrony Bank	\N	135	\N	\N	\N	\N
Chase Bella 2894	Card	Payment Method	0.00	JP Morgan Chase	\N	136	\N	\N	\N	\N
Verizon	Provider	Network	0.00	\N	\N	105	\N	\N	\N	\N
Reserve	Payee	Reserve	0.00	\N	\N	24	\N	\N	\N	\N
Transit	Payee	Transportation	0.00	\N	\N	9	\N	\N	\N	\N
B of A 2434	Checking	Payment Method	0.00	B of A	\N	143	\N	\N	\N	\N
AZ Minimally Invasive	Payee	Medical	0.00	\N	\N	48	\N	\N	\N	\N
AAA	Insurance	Transportation	0.00	\N	\N	126	\N	\N	\N	\N
Chevron	Payee	Transportation	0.00	\N	\N	128	\N	\N	\N	\N
Albertson's	Payee	Shopping	0.00	\N	\N	60	\N	\N	\N	\N
SW Kidney	Payee	Medical	0.00	\N	\N	26	\N	\N	\N	\N
Aqua Vita	Payee	Shopping	0.00	\N	\N	66	\N	\N	\N	\N
Urology Care	Payee	Medical	0.00	\N	\N	31	\N	\N	\N	\N
Pima Heart	Payee	Medical	0.00	\N	\N	34	\N	\N	\N	\N
AZ Hearing	Payee	Medical	0.00	\N	\N	42	\N	\N	\N	\N
Tucson Eye Care	Payee	Medical	0.00	\N	\N	45	\N	\N	\N	\N
Valley Sleep Center	Payee	Medical	0.00	\N	\N	35	\N	\N	\N	\N
Pima County	Payee	Government	0.00	\N	\N	93	\N	\N	\N	\N
State of Arizona	Payee	Government	0.00	\N	\N	94	\N	\N	\N	\N
Vivace	Payee	Eating Out	0.00	\N	\N	74	\N	\N	\N	\N
Fry's	Payee	Shopping	0.00	\N	\N	61	\N	\N	\N	\N
Basha's	Payee	Shopping	0.00	\N	\N	62	\N	\N	\N	\N
Sandyi	Payee	Shopping	0.00	\N	\N	64	\N	\N	\N	\N
TMC Wound Ctr	Provider	Medical	0.00	AZ Oncology	\N	19	\N	\N	\N	\N
Kinghorn	Payee	Services	0.00	\N	\N	97	\N	\N	\N	\N
Desert Tech	Payee	Services	0.00	\N	\N	100	\N	\N	\N	\N
Temco	Payee	Services	0.00	\N	\N	125	\N	\N	\N	\N
Tucson Water	Payee	Utilities	0.00	\N	\N	112	\N	\N	\N	\N
Caravan	Payee	Shopping	0.00	\N	\N	67	\N	\N	\N	\N
IRS	Payee	Government	0.00		\N	95	\N	\N	\N	\N
RAD	Provider	Utilities	0.00	\N	\N	124	\N	\N	\N	\N
Walgreen's	Payee	Medical	0.00	\N	\N	56	\N	\N	\N	\N
Banner Alvernon 3rd	Location	Medical	0.00	Banner	\N	7	\N	\N	\N	\N
Speedway	Payee	Car	0.00	\N	\N	129	\N	\N	\N	\N
QT	Payee	Car	0.00	\N	\N	127	\N	\N	\N	\N
Boden	Payee	Shopping	0.00	\N	\N	140	\N	\N	\N	\N
B of A 4131	Savings	Payment Method	0.00	B of A	\N	146	\N	\N	\N	\N
Sarnoff	Payee	Shopping	0.00	\N	\N	133	\N	\N	\N	\N
Lowe's	Payee	Shopping	0.00	\N	\N	134	\N	\N	\N	\N
CVS	Provider	Medical	0.00	\N	\N	55	\N	\N	\N	\N
Ace	Payee	Shopping	0.00	\N	\N	131	\N	\N	\N	\N
Walmart	Payee	Shopping	0.00	\N	\N	58	\N	\N	\N	\N
Trader Joe	Payee	Groceries	0.00	\N	\N	68	\N	\N	\N	\N
State Farm	Payee	Insurance	0.00	\N	\N	96	\N	\N	\N	\N
Takamatsu	Payee	Eating Out	0.00	\N	\N	75	\N	\N	\N	\N
Banner Campbell North	Location	Utilities	0.00	Banner	\N	8	\N	\N	\N	\N
Mariscos Chihuahua	Payee	Eating Out	0.00	\N	\N	77	\N	\N	\N	\N
B of A 2139	Checking	Payment Method	0.00	B of A	\N	115	\N	\N	\N	\N
Azure	Payee	Shopping	0.00	\N	\N	65	\N	\N	\N	\N
TMC One	Provider	Medical	0.00	AZ Oncology	\N	20	\N	\N	\N	\N
Rendezvous	Payee	Eating Out	0.00	\N	\N	78	\N	\N	\N	\N
Beyond Bread	Payee	Eating Out	0.00	\N	\N	79	\N	\N	\N	\N
Blanco	Payee	Eating Out	0.00	\N	\N	81	\N	\N	\N	\N
North	Payee	Eating Out	0.00	\N	\N	82	\N	\N	\N	\N
Pyramid 	Bank	Financial Institution	0.00	\N	\N	153	\N	\N	\N	\N
Jim	User		0.00	\N	\N	137	\N	\N	\N	\N
Yukie	User	\N	0.00	\N	\N	138	\N	\N	\N	\N
Bella	User	\N	0.00	\N	\N	139	\N	\N	\N	\N
Pima Heart Glenn	Location	Medical	0.00	Pima Heart	\N	33	\N	\N	\N	\N
Sahni	Provider	Medical	0.00	Valley Sleep Center	\N	46	\N	\N	\N	\N
David Pest	Provider	Services	0.00	Pioneer Pest Control	\N	120	\N	\N	\N	\N
Sunnova	Provider	Utilities	0.00	\N	\N	111	\N	\N	\N	\N
Medicare	Payee	Government	0.00	\N	\N	4	\N	\N	\N	\N
Medicare	Payee	Government	\N	\N	\N	4	\N	\N	\N	\N
Chris Ludwig	Provider	Services	0.00	Ludwig Klewer & Rudner	\N	165	\N	\N	\N	\N
SSA	Payor	Government	\N	\N	\N	14	\N	\N	\N	\N
AZ Oncology Camp Lowell	Location	Medical	\N	AZ Oncology	\N	17	\N	\N	\N	\N
AZ Oncology St Joseph	Location	Medical	\N	AZ Oncology	\N	18	\N	\N	\N	\N
AZ Oncology Rudasil	Location	Medical	\N	AZ Oncology	\N	19	\N	\N	\N	\N
AZ Oncology Swan	Location	Medical	\N	AZ Oncology	\N	20	\N	\N	\N	\N
B of A	Bank	Money	\N	\N	\N	21	\N	\N	\N	\N
Walmart RX	Payee	Medical	0.00	Walmart	\N	57	\N	\N	\N	\N
Coronado Internal Medicine	Payee	Medical	0.00	Signature	\N	22	\N	\N	\N	\N
Ford	Payee	Transportation	0.00	\N	\N	101	\N	\N	\N	\N
Transit	\N	Transportation	\N	\N	\N	9	\N	\N	\N	\N
Ludwig Klewer & Rudner	Payee	\N	0.00	\N	\N	166	\N	\N	\N	\N
Dehnert Dental	Payee	Medical	0.00	\N	\N	2	\N	\N	\N	\N
Water Tec	Payee	Services	\N	\N	\N	2	\N	\N	\N	\N
Z3M	\N	Transportation	\N	\N	\N	12	\N	\N	\N	\N
Dickman	\N	Groceries	\N	\N	\N	22	\N	\N	\N	\N
Altenbernd	Provider	Medical	\N	Banner Alevernon 3d	\N	23	\N	\N	\N	\N
Jabroun	Provider	Medical	\N	Banner Alevernon 3d	\N	24	\N	\N	\N	\N
Banner	Payee	Medical	\N	\N	\N	25	\N	\N	\N	\N
Insel	Providor	Medical	\N	Banner Campbell North	\N	26	\N	\N	\N	\N
Amazon	Provider	Shopping	0.00	\N	Chase 8370	130	\N	\N	\N	\N
Lee Lee	Payee	Shopping	0.00	\N	\N	63	\N	\N	\N	\N
Signature	Payee	Medical	0.00	\N	\N	159	\N	\N	\N	\N
St Joseph	Payee	Medical	\N	\N	\N	7	\N	\N	\N	\N
Safeway	Payee	Shopping	0.00	\N	\N	59	\N	\N	\N	\N
Walmart Market	Payee	Shopping	0.00	\N	\N	160	\N	\N	\N	\N
Home Depot	Payee	Shopping	0.00	\N	\N	132	\N	\N	\N	\N
Poetry	Payee	Shopping	0.00	\N	\N	141	\N	\N	\N	\N
Rural Metro	Payee	Utilities	\N	\N	\N	8	\N	\N	\N	\N
IBM	Payor	\N	\N	\N	\N	11	\N	\N	\N	\N
Pyramid Check	Checking	Payment Method	0.00	\N	\N	154	\N	\N	\N	\N
Abdelaziz	Provider	Network	0.00	AZ Oncology Wilmot	\N	10	\N	\N	\N	\N
JME	Payee	Network	\N	\N	\N	10	\N	\N	\N	\N
Pyramid Savings	Savings	Payment Method	0.00	\N	\N	157	\N	\N	\N	\N
Ally Bank	Payee	Money	\N	\N	\N	13	\N	\N	\N	\N
JP Morgan Chase	Bank	Money	0.00	\N	\N	151	\N	\N	\N	\N
Morgan Stanley	Investments	Money	0.00	\N	\N	152	\N	\N	\N	\N
Synchrony Bank	Bank	Money	0.00	\N	\N	150	\N	\N	\N	\N
Chase 8370	Card	Payment Method	0.00	JP Morgan Chase	\N	117	\N	\N	\N	\N
Firebirds	Payee	Eating Out	0.00	\N	\N	83	\N	\N	\N	\N
Frost	Payee	Eating Out	0.00	\N	\N	84	\N	\N	\N	\N
BJ's	Payee	Eating Out	0.00	\N	\N	87	\N	\N	\N	\N
Delhi Palace	Payee	Eating Out	0.00	\N	\N	88	\N	\N	\N	\N
Safron	Payee	Eating Out	0.00	\N	\N	89	\N	\N	\N	\N
Einstein	Payee	Eating Out	0.00	\N	\N	90	\N	\N	\N	\N
China Buffet	Payee	Eating Out	0.00	\N	\N	92	\N	\N	\N	\N
Miss Saigon	Payee	Eating Out	0.00	\N	\N	76	\N	\N	\N	\N
Locale	Payee	Eating Out	0.00	\N	\N	86	\N	\N	\N	\N
Raging Sage	Payee	Eating Out	0.00	\N	Cash	69	\N	\N	\N	\N
81	Payee	Eating Out	0.00	\N	\N	80	\N	\N	\N	\N
Wildflower	Payee	Eating Out	0.00	\N	\N	85	\N	\N	\N	\N
Starbucks	Payee	Eating Out	0.00	\N	\N	91	\N	\N	\N	\N
B of A Debit 0527	Debit	Payment Method	\N	B of  A 2139	\N	29	\N	\N	\N	\N
Yamato	Payee	Eating Out	\N		\N	30	\N	\N	\N	\N
Sher e Punjab	Payee	Eating out	\N	\N	\N	31	\N	\N	\N	\N
\.


--
-- Data for Name: actions; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.actions (id, entry_date, entry_time, "account-name", amount) FROM stdin;
\.


--
-- Data for Name: automatic_transactions; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.automatic_transactions (id, transaction_name, day_of_month, amount, to_account, from_account, category) FROM stdin;
\.


--
-- Data for Name: budget; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.budget (id, category, amount, spent, remaining, display) FROM stdin;
16	Grocery1	200.00	\N	\N	N
17	Grocery2	150.00	\N	\N	N
18	Grocery3	150.00	\N	\N	N
19	Drugs	0.00	\N	\N	N
8	Etc	453.31	\N	\N	Y
9	Contingency	0.00	\N	\N	Y
3	Utilities	287.06	\N	\N	Y
10	Insurance	530.01	\N	\N	Y
7	Transportation	130.00	\N	\N	Y
4	Medical	0.00	\N	\N	Y
15	Groceries	500.00	\N	\N	Y
2	Eating Out	180.00	\N	\N	Y
5	Network	219.63	\N	\N	Y
\.


--
-- Data for Name: persistent_state; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.persistent_state (id, state_key, state_value, last_updated) FROM stdin;
\.


--
-- Data for Name: pmt_methods; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.pmt_methods (id, card_name, statement_balance, current_balance, monthly_balance, last_pmt_amount, last_pmt_date, closing_date, payment_date, valid_date, "card number", "Type") FROM stdin;
5	PayPal 4139	0	0	0	0	\N	\N	\N	\N	\N	CC
2	B of A 4968	0	0	0	0	\N	2024-11-06	2024-11-05	\N	\N	CC
6	State Farm 1234	0	0	0	0	\N	\N	\N	\N	\N	CC
3	B of A 7660	0	0	503.67	0	\N	2024-10-28	2024-10-25	\N	\N	CC
4	Chase 8370	0	0	2032.0	0	\N	2024-09-24	2024-10-21	\N	\N	CC
1	B of A 4666	0	0	700.0	0	\N	2024-10-14	2024-11-11	\N	\N	CC
7	B of A 2139	\N	\N	0	\N	\N	\N	\N	\N	\N	CK
\.


--
-- Data for Name: qlog; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.qlog (id, entry_date, entry_time, service_date, category, to_account, amount, from__account, status, comment, image, exec_time, deduction, t_code, distance) FROM stdin;
22	2024-10-11	16:30:43	2024-10-11	Payment Method	B of A 2139	$2,800.00	SSA	\N		\N	\N	false	Transfer	\N
31	2024-10-12	22:31:55	2024-10-12	Medical	Pima Heart	$30.00	B of A 4666	\N		\N	\N	false	Pay	\N
32	2024-10-12	22:34:01	2024-10-12	Medical	Signature	$20.00	B of A 4968	\N		\N	\N	false	Pay	\N
78	2024-10-20	15:32:49	2024-10-20	Payment Method	B of A 7660	$400.00	B of A 2139	\N		\N	\N	false	Transfer	\N
79	2024-10-20	15:33:22	2024-10-20	Medical	ADE	$900.00	B of A 7660	\N		\N	\N	true	Pay	\N
46	2024-10-15	10:31:56	2024-10-15	Transportation	Ford	$255.00	B of A 4666	\N		\N	\N	false	Pay	\N
5	2024-10-11	13:34:37	2024-10-11	Payment Method	B of A 2139	$66.00	B of A 2434	\N		\N	\N	false	Pay	\N
47	2024-10-15	10:33:42	2024-10-15	Transportation	Chevron	$41.00	B of A 4666	\N		\N	\N	false	Pay	\N
7	2024-10-11	13:41:01	2024-10-11	Medical	ADE	$99.00	B of A 2139	\N		\N	\N	false	Pay	\N
35	2024-10-13	00:28:05	2024-10-13	Eating Out	Beyond Bread	$45.00	B of A 4968	\N		\N	\N	false	Pay	\N
9	2024-10-11	13:53:05	2024-10-11	Medical	AZ Minimally Invasive	$0.00	B of A 4968	\N		\N	\N	false	Pay	\N
45	2024-10-15	10:18:09	2024-10-15	Transportation	QT	$45.00	B of A 7660	\N		\N	\N	false	Pay	\N
43	2024-10-15	07:44:43	2024-10-15	Eating Out	Einstein	$10.00	B of A 7660	\N		\N	\N	false	Pay	\N
41	2024-10-15	01:26:17	2024-10-15	Eating Out	BJ's	$56.00	B of A 7660	\N		\N	\N	false	Pay	\N
13	2024-10-11	14:05:49	2024-10-11	Medical	AZ Minimally Invasive	$66.00	B of A 2434	\N		\N	\N	false	Pay	\N
15	2024-10-11	14:11:35	2024-10-11	Utilities	Amerigas	$33.00	Chase Bella 2894	\N		\N	\N	false	Pay	\N
16	2024-10-11	14:14:36	2024-10-11	Payment Method	B of A 4131	$33.00	B of A 2434	\N		\N	\N	false	Pay	\N
44	2024-10-15	10:00:01	2024-10-15	Groceries	Walmart Market	$60.00	B of A 4666	\N		\N	\N	false	Pay	\N
2	2024-10-11	13:15:59	2024-10-11	Groceries	Albertson's	$55.00	B of A 4968	\N		\N	\N	false	Pay	\N
3	2024-10-11	13:20:09	2024-10-11	Groceries	Ace	$99.00	B of A 7660	\N		\N	\N	false	Pay	\N
40	2024-10-14	23:59:35	2024-10-14	Groceries	Ace	$230.00	B of A 4968	\N		\N	\N	false	Pay	\N
48	2024-10-20	10:41:03	2024-10-20	Shopping	Ace	$24.94	B of A 7660	\N		\N	\N	false	Pay	\N
25	2024-10-12	15:36:55	2024-10-12	Medical	AZ Minimally Invasive	$56.98	B of A 4666	\N		\N	\N	false	Pay	\N
26	2024-10-12	15:59:41	2024-10-12	Payment Method	B of A 2434	$345.00	B of A 4131	\N		\N	\N	false	Pay	\N
23	2024-10-11	18:22:08	2024-10-11	Payment Method	B of A 2434	$111.00	B of A 2139	\N		\N	\N	false	Deposit	\N
36	2024-10-14	22:33:24	2024-10-14	Medical	ADE	$500.00	B of A 2139	\N		\N	\N	true	Pay	\N
37	2024-10-14	23:39:29	2024-10-14	Network	Verizon	$700.00	B of A 4666	\N		\N	\N	false	Pay	\N
38	2024-10-14	23:44:50	2024-10-14	Network	Verizon	$350.00	B of A 7660	\N		\N	\N	false	Pay	\N
39	2024-10-14	23:48:50	2024-10-14	Network	Verizon	$300.00	B of A 7660	\N		\N	\N	false	Pay	\N
42	2024-10-15	01:31:36	2024-10-15	Medical	Signature	$356.00	B of A 7660	\N		\N	\N	true	Pay	\N
49	2024-10-20	11:03:23	2024-10-20	Shopping	Albertson's	$56.00	B of A 7660	\N		\N	\N	false	Pay	\N
50	2024-10-20	11:04:21	2024-10-20	Medical	AZ Hearing	$345.00	B of A 7660	\N		\N	\N	true	Pay	\N
51	2024-10-20	11:10:25	2024-10-20	Medical	ADE	$67.00	B of A 7660	\N		\N	\N	true	Pay	\N
52	2024-10-20	11:25:55	2024-10-20	Medical	AZ Minimally Invasive	$135.00	B of A 7660	\N		\N	\N	true	Pay	\N
53	2024-10-20	11:40:27	2024-10-20	Utilities	Amerigas	$354.00	B of A 7660	\N		\N	\N	false	Pay	\N
54	2024-10-20	11:44:28	2024-10-20	Shopping	Azure	$87.67	B of A 7660	\N		\N	\N	false	Pay	\N
55	2024-10-20	11:51:54	2024-10-20	Medical	Pima Heart	$30.00	B of A 7660	\N		\N	\N	true	Pay	\N
56	2024-10-20	11:55:11	2024-10-20	Shopping	Ace	$44.00	B of A 7660	\N		\N	\N	false	Pay	\N
59	2024-10-20	12:13:22	2024-10-20	Shopping	Amazon	$556.00	B of A 7660	\N		\N	\N	false	Pay	\N
60	2024-10-20	12:13:45	2024-10-20	Utilities	Amerigas	$456.00	B of A 7660	\N		\N	\N	false	Pay	\N
61	2024-10-20	12:14:27	2024-10-20	Money	B of A	$300.00	B of A 2139	\N		\N	\N	false	Transfer	\N
62	2024-10-20	12:46:01	2024-10-20	Money	B of A	$66.00	B of A 2139	\N		\N	\N	false	Transfer	\N
63	2024-10-20	13:15:54	2024-10-20	Money	B of A	$44.00	B of A 2139	\N		\N	\N	false	Transfer	\N
64	2024-10-20	13:21:21	2024-10-20	Money	B of A	$90.00	B of A 2139	\N		\N	\N	false	Transfer	\N
65	2024-10-20	13:27:28	2024-10-20	Money	B of A	$50.00	B of A 2139	\N		\N	\N	false	Transfer	\N
66	2024-10-20	13:30:05	2024-10-20	Money	B of A	$55.00	B of A 2139	\N		\N	\N	false	Transfer	\N
67	2024-10-20	13:38:37	2024-10-20	Money	B of A	$60.00	B of A 2139	\N		\N	\N	false	Transfer	\N
68	2024-10-20	13:42:22	2024-10-20	Money	B of A	$70.00	B of A 2139	\N		\N	\N	false	Transfer	\N
69	2024-10-20	13:48:27	2024-10-20	Payment Method	B of A 7660	$80.00	B of A 2139	\N		\N	\N	false	Transfer	\N
70	2024-10-20	13:49:03	2024-10-20	Payment Method	B of A 7660	$75.00	B of A 2139	\N		\N	\N	false	Transfer	\N
71	2024-10-20	13:49:32	2024-10-20	Payment Method	B of A 7660	$400.00	B of A 2139	\N		\N	\N	false	Transfer	\N
72	2024-10-20	13:56:10	2024-10-20	Payment Method	B of A 7660	$700.00	B of A 2139	\N		\N	\N	false	Transfer	\N
73	2024-10-20	14:32:36	2024-10-20	Payment Method	B of A 7660	$867.00	B of A 2139	\N		\N	\N	false	Transfer	\N
75	2024-10-20	15:22:45	2024-10-20	Payment Method	B of A 7660	$45.99	B of A 2139	\N		\N	\N	false	Transfer	\N
76	2024-10-20	15:28:03	2024-10-20	Payment Method	B of A 7660	$100.00	B of A 2139	\N		\N	\N	false	Transfer	\N
77	2024-10-20	15:28:59	2024-10-20	Medical	AZ Hearing	$191.98	B of A 7660	\N		\N	\N	true	Pay	\N
80	2024-10-20	15:40:44	2024-10-20	Payment Method	B of A 7660	$1,700.00	B of A 2139	\N		\N	\N	false	Transfer	\N
81	\N	\N	2024-10-20	\N	AZ Hearing	$500.00	B of A 7660	\N		\N	\N	true	Pay	\N
82	\N	\N	2024-10-20	\N	AZ Hearing	$123.00	B of A 7660	\N		\N	\N	true	Pay	\N
83	\N	\N	2024-10-20	\N	AZ Hearing	$123.00	B of A 4666	\N		\N	\N	true	Pay	\N
84	\N	\N	2024-10-20	\N	Vivace	$123.00	B of A 4666	\N		\N	\N	false	Pay	\N
85	\N	\N	2024-10-20	\N	Basha's	$100.00	B of A 4666	\N		\N	\N	false	Pay	\N
86	\N	\N	2024-10-20	\N	Azure	$135.00	B of A 7660	\N		\N	\N	false	Pay	\N
87	\N	\N	2024-10-20	\N	Albertson's	$321.00	B of A 7660	\N		\N	\N	false	Pay	\N
88	\N	\N	2024-10-20	\N	81	$123.00	B of A 7660	\N		\N	\N	false	Pay	\N
89	\N	\N	2024-10-20	\N	State Farm	$321.00	B of A 7660	\N		\N	\N	false	Pay	\N
91	\N	\N	2024-10-21	\N	AZ Hearing	$555.00	B of A 7660	\N		\N	\N	true	Pay	\N
92	\N	\N	2024-10-21	\N	B of A 7660	$2,877.00	B of A 2139	\N		\N	\N	false	Transfer	\N
93	\N	\N	2024-10-21	\N	B of A 4666	$7,846.00	B of A 2139	\N		\N	\N	false	Transfer	\N
94	\N	\N	2024-10-21	\N	Blanco	$67.00	B of A 7660	\N		\N	\N	false	Pay	\N
95	\N	\N	2024-10-21	\N	Amazon	$34.00	Chase 8370	\N		\N	\N	false	Pay	\N
96	\N	\N	2024-10-21	\N	AZ Hearing	$354.00	Chase 8370	\N		\N	\N	true	Pay	\N
97	\N	\N	2024-10-21	\N	AZ Hearing	$777.00	Chase 8370	\N		\N	\N	true	Pay	\N
98	\N	\N	2024-10-21	\N	ADE	$567.00	Chase 8370	\N		\N	\N	true	Pay	\N
58	2024-10-20	12:00:09	2024-10-20	Eating Out	China Buffet	$18.95	B of A 7660	\N		\N	\N	false	Pay	\N
74	2024-10-20	15:21:49	2024-10-20	Eating Out	81	$45.99	B of A 7660	\N		\N	\N	false	Pay	\N
99	\N	\N	2024-10-21	\N	Beyond Bread	$36.00	B of A 7660	\N		\N	\N	false	Pay	\N
100	\N	\N	2024-10-21	\N	81	$55.67	B of A 7660	\N		\N	\N	false	Pay	\N
101	\N	\N	2024-10-21	\N	ADE	$345.00	B of A 7660	\N		\N	\N	true	Pay	\N
102	\N	\N	2024-10-21	\N	81	$456.00	B of A 2139	\N		\N	\N	false	Pay	\N
103	\N	\N	2024-10-21	\N	AZ Minimally Invasive	$300.00	Chase 8370	\N		\N	\N	true	Pay	\N
104	\N	\N	2024-10-21	\N	ADE	$435.00	B of A 4666	\N		\N	\N	true	Pay	\N
105	\N	\N	2024-10-21	\N	Amerigas	$221.00	B of A 4666	\N		\N	\N	false	Pay	\N
106	\N	\N	2024-10-21	\N	AZ Minimally Invasive	$321.00	B of A 2434	\N		\N	\N	true	Pay	\N
107	\N	\N	2024-10-21	\N	ADE	$44.00	B of A 4666	\N		\N	\N	true	Pay	\N
108	2024-10-22	19:28:17	2024-10-22	Medical	ADE	$54.00	Chase 8370	\N		\N	\N	true	Pay	\N
109	2024-10-27	14:11:57	2024-10-25	Eating Out	Blanco	$56.00	B of A 4666	\N		\N	\N	false	Pay	\N
110	2024-11-21	06:15:35	2024-11-21	Medical	AZ Minimally Invasive	$60.00	Paypal 4139	\N		\N	\N	true	Pay	\N
111	2024-12-08	18:19:42	2024-12-08	Shopping	Amazon	$44.00	Chase 8370	\N		\N	\N	false	Pay	\N
112	2024-12-08	18:20:32	2024-12-07	Eating Out	Beyond Bread	$66.00	B of A 7660	\N		\N	\N	false	Pay	\N
113	2024-12-08	18:21:04	2024-12-08	Eating Out	Einstein	$112.00	B of A 7660	\N		\N	\N	false	Pay	\N
114	2024-12-08	18:21:50	2024-12-08	Shopping	Albertson's	$109.00	Chase 8370	\N		\N	\N	false	Pay	\N
115	2024-12-08	18:22:43	2024-12-08	Medical	SW Hand	$223.00	B of A 7660	\N		\N	\N	true	Pay	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: new_schema; Owner: postgres
--

COPY new_schema.users (id, name, password) FROM stdin;
1	Yukie	Bella
2	Jim	Sasuke
3	Bella	Bella
\.


--
-- Name: accounts_acct_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.accounts_acct_id_seq', 31, true);


--
-- Name: actions_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.actions_id_seq', 1, false);


--
-- Name: automatic_transactions_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.automatic_transactions_id_seq', 1, false);


--
-- Name: budget_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.budget_id_seq', 19, true);


--
-- Name: credit_card_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.credit_card_id_seq', 12, true);


--
-- Name: persistent_state_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.persistent_state_id_seq', 1, false);


--
-- Name: qlog_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.qlog_id_seq', 115, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.users_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

