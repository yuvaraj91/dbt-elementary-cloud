# dbt-elementary-cloud

Trying out Elementary Data cloud free trial



# Local env setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The `profiles.yml` file contains the profile for this dbt project itself, and the extra Snowflake user for Elementary Data reporting.

To create the Snowflake user:

```sql
CREATE OR REPLACE USER elementary PASSWORD = '';
CREATE OR REPLACE ROLE ELEMENTARY_ROLE;
GRANT ROLE ELEMENTARY_ROLE TO USER elementary;
GRANT USAGE ON WAREHOUSE compute_wh TO ROLE ELEMENTARY_ROLE;
GRANT USAGE ON DATABASE local TO ROLE ELEMENTARY_ROLE;
GRANT USAGE ON SCHEMA local.elementary_report TO ROLE ELEMENTARY_ROLE;
GRANT SELECT ON ALL TABLES IN SCHEMA local.elementary_report TO ROLE ELEMENTARY_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA local.elementary_report TO ROLE ELEMENTARY_ROLE;
GRANT SELECT ON ALL VIEWS IN SCHEMA local.elementary_report TO ROLE ELEMENTARY_ROLE;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA local.elementary_report TO ROLE ELEMENTARY_ROLE;
```


# Installing the Elementary package to dbt

```bash
dbt deps
```

This will mostly create empty tables, that will be updated with artifacts, metrics and test results in future dbt executions:

```bash
dbt run --select elementary
```

# Loading sample data and running the models

```bash
dbt seed
dbt run
```

# Running the Elementary tests

```bash
dbt test
```

To view the report locally:

```bash
edr report
```
