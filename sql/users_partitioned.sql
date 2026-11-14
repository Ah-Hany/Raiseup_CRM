CREATE TABLE IF NOT EXISTS public.users_partitioned
(
    id integer,
    username character varying(250) COLLATE pg_catalog."default",
    email character varying(200) COLLATE pg_catalog."default",
    password character varying(20) COLLATE pg_catalog."default",
    created_at timestamp without time zone,
    updated_at timestamp without time zone
) PARTITION BY RANGE (created_at);

ALTER TABLE IF EXISTS public.users_partitioned
    OWNER to postgres;

-- Partitions SQL

CREATE TABLE public.users_2020 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2020-01-01 00:00:00') TO ('2021-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2020
    OWNER to postgres;
CREATE TABLE public.users_2021 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2021-01-01 00:00:00') TO ('2022-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2021
    OWNER to postgres;
CREATE TABLE public.users_2022 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2022-01-01 00:00:00') TO ('2023-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2022
    OWNER to postgres;
CREATE TABLE public.users_2023 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2023-01-01 00:00:00') TO ('2024-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2023
    OWNER to postgres;
CREATE TABLE public.users_2024 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2024-01-01 00:00:00') TO ('2025-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2024
    OWNER to postgres;
CREATE TABLE public.users_2025 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2025-01-01 00:00:00') TO ('2026-01-01 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2025
    OWNER to postgres;
CREATE TABLE public.users_2026 PARTITION OF public.users_partitioned
    FOR VALUES FROM ('2026-01-01 00:00:00') TO ('2026-12-31 00:00:00')
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_2026
    OWNER to postgres;
