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

COPY new_schema.accounts (acct_name, acct_type, acct_category, acct_balance, acct_link, acct_pmt_method, acct_id, acct_xtra1) FROM stdin;
AZ Vascular	Location	Medical	0.00	\N	\N	4	\N
Namanny	Provider	Medical	0.00	AZ Vascular	\N	3	\N
Banner Alvernon 3rd	Location	Medical	0.00	Banner	\N	7	\N
Insel	Provider	Medical	0.00	Banner Campbell North	\N	5	\N
Altenbernd	Provider	Medical	0.00	Banner Alvernon 3rd	\N	6	\N
Banner Campbell North	Location	Medical	0.00	Banner	\N	8	\N
Banner	Company	Medical	0.00	\N	\N	9	\N
AZ Oncology Wilmot	Location	Medical	0.00	AZ Oncology Wilmot	\N	12	\N
Dana	Provider	Medical	0.00	AZ Oncology Wilmot	\N	11	\N
AZ Oncology Wilmot	Location	Medical	0.00	AZ Oncology	\N	13	\N
AZ Minimally Invasive	Location	Medical	0.00	\N	\N	48	\N
Gin	Provider	Medical	0.00	AZ Oncology St Joseph	\N	14	\N
Yurkanin	Provider	Medical	0.00	AZ Minimally Invasive	\N	47	\N
Sonora Quest	Provider	Medical	0.00	\N	\N	49	\N
AZ Oncology	Company	Medical	0.00	\N	\N	16	\N
TMC	Provider	Medical	0.00	\N	\N	20	\N
St Joseph PT	Location	Medical	0.00	St Joseph	\N	18	\N
TMC Wound Ctr	Provider	Medical	0.00	TMC	\N	19	\N
Mayer	Provider	Medical	0.00	Coronado Internal Medicine	\N	21	\N
Walmart	Market	Food	0.00	\N	\N	58	\N
Lui	Provider	Medical	0.00	SW Kidney	\N	25	\N
SW Kidney	Location	Medical	0.00	\N	\N	26	\N
Mayer RSRV	Reserve	Medical	0.00		\N	23	\N
Reserve	\N	Reserve	0.00	\N	\N	24	\N
Azure	Markrt	Food	0.00	\N	\N	65	\N
Chris PT	Provider	Medical	0.00	St Joseph PT	\N	17	\N
SW Hand	Location	Medical	0.00	\N	\N	28	\N
Beer	Provider	Medical	0.00	SW Hand	\N	29	\N
Bernstein	Provider	Medical	0.00	Urology Care	\N	30	\N
Urology Care	location	Medical	0.00	\N	\N	31	\N
Boiangiu	Provider	Medical	0.00	Pima Heart Glenn	\N	32	\N
Pima Heart	Company	Medical	0.00	\N	\N	34	\N
Perez	Provider	Medical	0.00	Pima Heart Camp Lowell	\N	36	\N
Pima Heart Camp Lowell	Location	Medical	0.00	Pima Heart	\N	37	\N
Faitelson	Provider	Medical	0.00	Pima Heart Glenn	\N	38	\N
Winter	Provider	Medical	0.00	Pima Heart River	\N	39	\N
Pima Heart River	Location	Medical	0.00	Pima Heart	\N	40	\N
Davies	Provider	Medical	0.00	AZ Hearing	\N	41	\N
AZ Hearing	Company	Medical	0.00	\N	\N	42	\N
Swingle	Provider	Medical	0.00	AZ Hearing	\N	43	\N
Kaye	Provider	Medical	0.00	Tucson Eye Care	\N	44	\N
Tucson Eye Care	Location	Medical	0.00	\N	\N	45	\N
Valley Sleep Center	Company	Medical	0.00	\N	\N	35	\N
Pima County	Public	Government	0.00	\N	\N	93	\N
State of Arizona	Public	Government	0.00	\N	\N	94	\N
IRS	Public	Government	0.00	\N	\N	95	\N
Albertson's	Market	Food	0.00	\N	\N	60	\N
Fry's	Market	Food	0.00	\N	\N	61	\N
Basha's	Market	Food	0.00	\N	\N	62	\N
Lee Lee	Market	Food	0.00	\N	\N	63	\N
Sandyi	Market	Food	0.00	\N	\N	64	\N
Vivace	Restaurant	Dining	0.00	\N	\N	74	\N
State Farm		Insurance	0.00	\N	\N	96	\N
Takamatsu	Restaurant	Dining	0.00	\N	\N	75	\N
Kinghorn	Legal	Services	0.00	\N	\N	97	\N
ADE	\N	Services	0.00	\N	\N	98	\N
David BMW	Provider	Services	0.00	Desert Tech	\N	99	\N
Desert Tech	Location	Services	0.00	\N	\N	100	\N
Ford	Location	Services	0.00	\N	\N	101	\N
Truly Nolen	Provider	Services	0.00	\N	\N	119	\N
Pioneer Pest Control	Provider	Services	0.00	\N	\N	121	\N
Temco	Provider	Services	0.00	\N	\N	125	\N
Tucson Water	Provider	Utilities	0.00	\N	\N	112	\N
Dehnert	Provider	Medical	0.00	Dehnert Dental	\N	1	\N
Hanger	Provider	Medical	0.00	\N	\N	53	\N
Aqua Vita	Market	Food	0.00	\N	\N	66	\N
Caravan	Market	Food	0.00	\N	\N	67	\N
Trader Joe	Market	Food	0.00	\N	\N	68	\N
Miss Saigon	Restaurant	Dining	0.00	\N	\N	76	\N
Mariscos Chihuahua	Restaurant	Dining	0.00	\N	\N	77	\N
Rendezvous	Restaurant	Dining	0.00	\N	\N	78	\N
Beyond Bread	Restaurant	Dining	0.00	\N	\N	79	\N
Blanco	Restaurant	Dining	0.00	\N	\N	81	\N
North	Restaurant	Dining	0.00	\N	\N	82	\N
Firebirds	Restaurant	Dining	0.00	\N	\N	83	\N
Frost	Restaurant	Dining	0.00	\N	\N	84	\N
Locale	Restaurant	Dining	0.00	\N	\N	86	\N
BJ's	Restaurant	Dining	0.00	\N	\N	87	\N
Delhi Palace	Restaurant	Dining	0.00	\N	\N	88	\N
Safron	Restaurant	Dining	0.00	\N	\N	89	\N
Einstein	Restaurant	Dining	0.00	\N	\N	90	\N
China Buffet	Restaurant	Dining	0.00	\N	\N	92	\N
Dehnert Dental	Location	Medical	0.00	\N	\N	2	\N
Radiology LTD	Provider	Medical	0.00	\N	\N	54	\N
Walgreen's	Pharmacy	Medical	0.00	\N	\N	56	\N
AZ Oncology St Joseph	Location	Medical	0.00	AZ Oncology	\N	15	\N
Shafik	Provider	Medical	0.00	SW Hand	\N	27	\N
Water Tech	Provider	Services	0.00	\N	\N	122	\N
Jim Myers	Provider	Services	0.00	\N	\N	123	\N
RAD	Provider	Services	0.00	\N	\N	124	\N
AAA	Insurance	Services	0.00	\N	\N	126	\N
ADE	Provider	Services	0.00	\N	\N	118	\N
Verizon	Provider	Communication	0.00	\N	\N	105	\N
TEP	Provider	Utilities	0.00	\N	\N	110	\N
Amerigas	Provider	Utilities	0.00	\N	\N	113	\N
CVS	Pharmacy	Medical	0.00	\N	\N	55	\N
QT	\N	Gasoline	0.00	\N	\N	127	\N
Chevron	\N	Gasoline	0.00	\N	\N	128	\N
Speedway	\N	Gasoline	0.00	\N	\N	129	\N
Ace	\N	Retail	0.00	\N	\N	131	\N
Home Depot	\N	Retail	0.00	\N	\N	132	\N
Sarnoff	\N	Retail	0.00	\N	\N	133	\N
Lowe's	\N	Retail	0.00	\N	\N	134	\N
Boden	\N	Retail	0.00	\N	\N	140	\N
Poetry	\N	Retail	0.00	\N	\N	141	\N
Cash	Cash	Payment Method	0.00	\N	\N	142	\N
B of A 2139	Checking	Payment Method	0.00	B of A	\N	115	\N
B of A 2434	Checking	Payment Method	0.00	B of A	\N	143	\N
B of A 7660	Card	Payment Method	0.00	B of A	\N	116	\N
B of A 4968	Card	Payment Method	0.00	B of A	\N	144	\N
B of A 4666	Card	Payment Method	0.00	B of A	\N	145	\N
B of A 4131	Savings	Savings	0.00	\N	\N	146	\N
B of A		Financial Institution	0.00	\N	\N	147	\N
Paypal 4139	Card	Card	0.00	Synchrony Bank	\N	135	\N
Chase 8370	Card	Card	0.00	JP Morgan Chase	\N	117	\N
Chase Bella 2894	Card	Card	0.00	JP Morgan Chase	\N	136	\N
Chase 3587	Check	Payment Method	0.00	\N	\N	148	\N
B of A 	Bank	Financial Institution	0.00	\N	\N	149	\N
Synchrony Bank	Bank	Financial Institution	0.00	\N	\N	150	\N
JP Morgan Chase	Bank	Financial Institution	0.00	\N	\N	151	\N
Morgan Stanley	Investments	Financial Institution	0.00	\N	\N	152	\N
Pyramid 	Bank	Financial Institution	0.00	\N	\N	153	\N
Pyramid Saving	Savings	Savings	0.00	\N	\N	157	\N
Pyramid Check	Checking	Financial Institution	0.00	\N	\N	154	\N
US Bank	Card	Payment Method	0.00	\N	\N	155	\N
Abdelaziz	Provider	Medical	0.00	AZ Oncology Wilmot	\N	10	\N
Safeway	Market	Food	0.00	\N	\N	59	\N
Raging Sage	Coffee Shop	Dining	0.00	\N	Cash	69	\N
81	Restaurant	Dining	0.00	\N	\N	80	\N
Wildflower	Restaurant	Dining	0.00	\N	\N	85	\N
Starbucks	Restaurant	Dining	0.00	\N	\N	91	\N
Jim	User		0.00	\N	\N	137	\N
Yukie	User	\N	0.00	\N	\N	138	\N
Bella	User	\N	0.00	\N	\N	139	\N
Walmart RX	Pharmacy	Medical	0.00	Walmart	\N	57	\N
Coronado Internal Medicine	Location	Medical	0.00	Signature	\N	22	\N
Signature	Company	\N	0.00	\N	\N	159	\N
Pima Heart Glenn	Location	Medical	0.00	Pima Heart	\N	33	\N
Sahni	Provider	Medical	0.00	Valley Sleep Center	\N	46	\N
David Pest	Provider	Services	0.00	Pioneer Pest Control	\N	120	\N
Sunnova	Provider	Utilities	0.00	\N	\N	111	\N
Amazon	Provider	Retail	0.00	\N	\N	130	\N
Walmart RX	Pharmacy	Medical	0.00	\N	\N	161	\N
Walmart Market	Market	Food	0.00	\N	\N	160	\N
\N	\N	\N	0.00	\N	\N	162	\N
\N	\N	\N	0.00	\N	\N	163	\N
\N	\N	\N	0.00	\N	\N	164	\N
Chris Ludwig	Accountant	Services	0.00	Ludwig Klewer & Rudner	\N	165	\N
Ludwig Klewer & Rudner	PLLC	\N	0.00	\N	\N	166	\N
Olfactory Solutions	Technology	Services	0.00	\N	\N	167	\N
\N	\N	\N	\N	\N	\N	1	\N
Water Tec	RO Maintenance	Services	\N	\N	\N	2	\N
\N	\N	\N	\N	\N	\N	3	\N
\N	XXX	\N	\N	\N	\N	4	\N
\.


--
-- Name: accounts_acct_id_seq; Type: SEQUENCE SET; Schema: new_schema; Owner: postgres
--

SELECT pg_catalog.setval('new_schema.accounts_acct_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

