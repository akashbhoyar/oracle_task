from flask import Flask, render_template
import pandas as pd
import oracledb

app = Flask(__name__)

# Establish MySQL connection
# Connect to the Oracle database
conn = oracledb.connect("team13_akash/team13_akash@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/orcl")
c = conn.cursor()


# Define SQL query
query = "select * from cdi_import"

# Execute query and get DataFrame
emp = pd.read_sql(query, conn)

# Close MySQL connection
conn.close()

# Convert DataFrame to HTML table
html_table = emp.to_html(classes="table table-striped", index=False)

@app.route("/")
def index():
    return render_template("index.html", table=html_table)

if __name__ == "__main__":
    app.run(debug=True)
