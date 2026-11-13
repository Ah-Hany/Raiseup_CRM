CREATE TABLE IF NOT EXISTS public.app_users
(
    id integer NOT NULL DEFAULT nextval('app_users_id_seq'::regclass),
    username character varying(100) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    password character varying(255) COLLATE pg_catalog."default" NOT NULL,
    role character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT app_users_pkey PRIMARY KEY (id),
    CONSTRAINT app_users_email_key UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.app_users
    OWNER to postgres;
