# Welcome to your new dbt project

## Using the Project

1. source .venv/bin/activate
2. navigate to simple_dbt_project directory
3. run `dbt debug` - approve push notification on DUO
4. Confirm raw tables (customers, events, orders, products) are in database raw schema
5. `dbt seed`
6. `dbt run`
7. (optional) `dbt test`

### Resources

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
