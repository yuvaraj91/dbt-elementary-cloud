{% macro check_undelivered_orders(args) %}
def test(model_df, ref, session):
    return model_df.filter(model_df['STATUS'] != 'delivered')
{% endmacro %}
