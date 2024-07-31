import polars as pl
import duckdb
import sys
import re
from loguru import logger
from .utilities import clean_check

logger.remove()
logger.add(sys.stdout, colorize=True, format='<level>{level}</level> | <cyan>{function}</cyan> | <level>{message}</level>')


class PipelineText:
    def __init__(self, mode: str = ''):
        self.mode = mode

    @staticmethod
    def clean_text(data: pl.DataFrame, col: str = 'item_name') -> pl.DataFrame:
        regex = "[\(\[\<\"].*?[\)\]\>\"]"
        return data.with_columns(
            pl.col(col).map_elements(
                lambda x: re.sub(regex, "", x).lower().rstrip('.').strip(), return_dtype=pl.String
            )
            .alias(f'{col.lower()}_clean')
        )

    def run(self, data):
        # load data
        query = f"""select * from data"""
        df = duckdb.sql(query).pl()
        logger.info(f'[Data] Base Data {self.mode}: {df.shape}')

        # clean check
        dict_check = clean_check(df)['null']
        drop_null_col = [i for i, v in dict_check.items() if v == df.shape[0]]

        df = (
            df
            .pipe(PipelineText.clean_text)
            .drop(drop_null_col)
            .select(pl.all().name.prefix(f'{self.mode}_'))
            .drop_nulls()
        )
        logger.info(f'[Data] Join Data {self.mode}: {df.shape}')
        return df
