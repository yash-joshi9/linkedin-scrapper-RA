"""Example to scrape a list of Companies, and put overviews in csv form"""

from scrape_linkedin import CompanyScraper
import pandas as pd



from scrape_linkedin import ProfileScraper

with ProfileScraper(cookie="AQEDATZKyKEAJVq1AAABeoKbgtYAAAF6pqgG1k0Ar1SxUkb4V6rWZJyg3UwJ9DXE2nLFHHcfe0kVgkI_GbZl3X7l7VI6wtW6hdJxSBlVUK6oEN84_XYNfl-tOVzU0q_hT7NWk3aLY-MdwDLaa6hbNgi2") as scraper:
    profile = scraper.scrape(user='yash-j')
print(profile.to_dict())
