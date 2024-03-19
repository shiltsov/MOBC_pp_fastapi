--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: app_user_logs; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.app_user_logs (
    id integer NOT NULL,
    ip character varying,
    request text,
    request_date date
);


ALTER TABLE public.app_user_logs OWNER TO "user";

--
-- Name: app_user_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.app_user_logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.app_user_logs_id_seq OWNER TO "user";

--
-- Name: app_user_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.app_user_logs_id_seq OWNED BY public.app_user_logs.id;


--
-- Name: app_user_votes; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.app_user_votes (
    id integer NOT NULL,
    ip character varying,
    rating integer,
    vote_date date,
    CONSTRAINT app_user_votes_rating_check CHECK ((rating >= 1)),
    CONSTRAINT app_user_votes_rating_check1 CHECK ((rating <= 5))
);


ALTER TABLE public.app_user_votes OWNER TO "user";

--
-- Name: app_user_votes_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.app_user_votes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.app_user_votes_id_seq OWNER TO "user";

--
-- Name: app_user_votes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.app_user_votes_id_seq OWNED BY public.app_user_votes.id;


--
-- Name: app_user_logs id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.app_user_logs ALTER COLUMN id SET DEFAULT nextval('public.app_user_logs_id_seq'::regclass);


--
-- Name: app_user_votes id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.app_user_votes ALTER COLUMN id SET DEFAULT nextval('public.app_user_votes_id_seq'::regclass);


--
-- Data for Name: app_user_logs; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.app_user_logs (id, ip, request, request_date) FROM stdin;
1	127.0.0.4	мама мыла раму	2024-03-18
2	127.0.1.2	мама пила водку	2024-03-18
3	127.0.2.1	папа ел омлет	2024-03-18
4	127.0.3.4	брат пил отвар	2024-03-18
5	127.0.5.7	рома курил табак	2024-03-18
6	127.0.5.1	варган играл громко	2024-03-18
7	127.0.0.4	мама мыла раму	2024-03-18
8	127.0.1.2	мама пила водку	2024-03-18
9	127.0.2.1	папа ел омлет	2024-03-18
10	127.0.3.4	брат пил отвар	2024-03-18
11	127.0.5.7	рома курил табак	2024-03-18
12	127.0.5.1	варган играл громко	2024-03-18
\.


--
-- Data for Name: app_user_votes; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.app_user_votes (id, ip, rating, vote_date) FROM stdin;
1	127.0.0.4	5	2024-03-18
2	127.0.1.5	5	2024-03-18
3	127.0.1.1	5	2024-03-18
4	127.0.2.1	4	2024-03-18
5	127.0.0.3	4	2024-03-18
6	127.0.1.9	3	2024-03-18
7	127.0.0.4	5	2024-03-18
8	127.0.3.5	1	2024-03-18
9	127.0.4.1	5	2024-03-18
10	127.0.5.1	2	2024-03-18
11	127.0.5.3	4	2024-03-18
12	127.0.5.9	3	2024-03-18
13	127.0.6.5	1	2024-03-18
14	127.0.6.1	5	2024-03-18
15	127.0.6.1	2	2024-03-18
16	127.0.6.3	4	2024-03-18
17	127.0.6.9	5	2024-03-18
18	127.0.0.4	5	2024-03-18
19	127.0.1.5	5	2024-03-18
20	127.0.1.1	5	2024-03-18
21	127.0.2.1	4	2024-03-18
22	127.0.0.3	4	2024-03-18
23	127.0.1.9	3	2024-03-18
24	127.0.0.4	5	2024-03-18
25	127.0.3.5	1	2024-03-18
26	127.0.4.1	5	2024-03-18
27	127.0.5.1	2	2024-03-18
28	127.0.5.3	4	2024-03-18
29	127.0.5.9	3	2024-03-18
30	127.0.6.5	1	2024-03-18
31	127.0.6.1	5	2024-03-18
32	127.0.6.1	2	2024-03-18
33	127.0.6.3	4	2024-03-18
34	127.0.6.9	5	2024-03-18
\.


--
-- Name: app_user_logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.app_user_logs_id_seq', 12, true);


--
-- Name: app_user_votes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.app_user_votes_id_seq', 34, true);


--
-- Name: app_user_logs app_user_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.app_user_logs
    ADD CONSTRAINT app_user_logs_pkey PRIMARY KEY (id);


--
-- Name: app_user_votes app_user_votes_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.app_user_votes
    ADD CONSTRAINT app_user_votes_pkey PRIMARY KEY (id);


--
-- Name: ix_app_user_logs_request_date; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_app_user_logs_request_date ON public.app_user_logs USING btree (request_date);


--
-- Name: ix_app_user_votes_rating; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_app_user_votes_rating ON public.app_user_votes USING btree (rating);


--
-- Name: ix_app_user_votes_vote_date; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_app_user_votes_vote_date ON public.app_user_votes USING btree (vote_date);


--
-- PostgreSQL database dump complete
--

