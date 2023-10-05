from FBRef_scraper import FBRefScraper
import pandas as pd


def scrape_save_fixtures_multiple_seasons_leagues(
    season_start_years: list[int], league_names: list[str]
):
    df_all = pd.DataFrame()
    for league_name in league_names:
        for season_begin in season_start_years:
            fb = FBRefScraper(
                season_start_year=season_begin,
                season_end_year=season_begin + 1,
                league_name=league_name,
            )
            df = fb.scrape_fixtures_to_df()
            df_all = pd.concat([df_all, df], ignore_index=True)


season_start_years = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
"""
Scrapes the fixtures with meta info for all games of the regular season
"""
scrape_save_fixtures_multiple_seasons_leagues(season_start_years, ["Bundesliga"])

"""
Scrapes all the player stats, keeper stats, and lineups for the games in the seasons
This can of course also be used for individual seasons only
To not get blocked by fbref there needs to be 60s break every 20 games, to the scraping takes some time
"""
for season_start in season_start_years:
    fb = FBRefScraper(season_start, season_start + 1, "Bundesliga")
    fb.match_reports_to_csv()
