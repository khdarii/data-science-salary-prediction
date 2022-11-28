import glassdoor_scraper as gs
import pandas as pd

path = "~/git/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 20)

df.to_csv("glassdoor_jobs.csv", index=False)
