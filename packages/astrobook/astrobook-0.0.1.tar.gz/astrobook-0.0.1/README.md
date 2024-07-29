**Author:** [Behrouz Safari](https://behrouzz.github.io/)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# astrobook
*Educational tools for the astronomical book*


## Installation

Install the latest version:

    pip install astrobook

Requirements are *numpy*, *pandas*, *scipy*, *requests* and *matplotlib*.


## Examples

Retrieve data from SIMBAD:

```python
from astrobook import sql2df

df = sql2df('SELECT TOP 10 main_id, ra, dec FROM basic', api='simbad')
```

Get names, description an number of rows of tables of IRSA

```python
from astrobook import sql2df

query = """
SELECT table_name, description, irsa_nrows
FROM TAP_SCHEMA.tables
WHERE irsa_nrows IS NOT NULL
ORDER BY irsa_nrows DESC
"""

df = sql2df(query, api='irsa')
```


See more at [astrodatascience.net](https://behrouzz.github.io/astrodatascience/)
