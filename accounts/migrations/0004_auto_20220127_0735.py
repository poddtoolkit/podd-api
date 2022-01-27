# Generated by Django 4.0.1 on 2022-01-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_domain_code_alter_domain_name"),
    ]

    operations = [
        migrations.RunSQL(
            """
create or replace function inherit_authority_down(src_id bigint)
    returns table
            (
                id bigint
            )
as
$$
with RECURSIVE cte as (
    select id, 0 as depth, ARRAY [id] as path
    from accounts_authority
    where id = src_id

    union all

    select a.id, depth + 1, a.id || path
    from accounts_authority a,
         accounts_authority_inherits aih,
         cte
    where a.id = aih.from_authority_id
      and aih.to_authority_id = cte.id
      and not path @> Array [a.id]
)
select distinct id
from cte;

$$ language sql stable;
            """,
            """
drop function inherit_authority_down(src_id bigint);
            """,
        )
    ]