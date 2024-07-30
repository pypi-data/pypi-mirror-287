import pandas as pd

from ..constants import MEAN_95CI, N_ONLY, N_WITH_COL_PROP, N_WITH_ROW_PROP
from ..row import RowDefinition, RowDefinitions
from ..table import Table


class FbgTable(Table):
    def __init__(self, main_df: pd.DataFrame = None):
        super().__init__(colname="fbg", main_df=main_df, title="FBG (mmol/L) categories")

    @property
    def row_definitions(self) -> RowDefinitions:
        df_tmp = self.main_df.copy()
        row_defs = RowDefinitions(reverse_rows=False)
        row0 = RowDefinition(
            title=self.title,
            label=self.default_sublabel,
            condition=(df_tmp["gender"].notna()),
            columns={"F": (N_ONLY, 2), "M": (N_ONLY, 2), "All": (N_ONLY, 2)},
            drop=False,
        )
        row_defs.add(row0)

        columns = {
            "F": (N_WITH_COL_PROP, 2),
            "M": (N_WITH_COL_PROP, 2),
            "All": (N_WITH_ROW_PROP, 2),
        }
        row_defs.add(
            RowDefinition(
                colname=self.colname,
                label="Not fasted",
                condition=(self.main_df["fasting_fbg_hrs"] < 8.0),
                columns=columns,
                drop=True,
            )
        )

        columns = {
            "F": (MEAN_95CI, 2),
            "M": (MEAN_95CI, 2),
            "All": (MEAN_95CI, 2),
        }
        row_mean = RowDefinition(
            colname=self.colname,
            label="Mean (95% CI)",
            condition=(self.main_df[self.colname].notna()),
            columns=columns,
            drop=False,
        )
        columns = {
            "F": (N_WITH_COL_PROP, 2),
            "M": (N_WITH_COL_PROP, 2),
            "All": (N_WITH_ROW_PROP, 2),
        }

        row_defs.add(
            RowDefinition(
                colname=self.colname,
                label="<6.1",
                condition=(self.main_df[self.colname] < 6.1),
                columns=columns,
                drop=True,
            )
        )
        row_defs.add(
            RowDefinition(
                colname=self.colname,
                label="6.1-6.9",
                condition=(self.main_df[self.colname] >= 6.1)
                & (self.main_df[self.colname] < 7.0),
                columns=columns,
                drop=True,
            )
        )
        row_defs.add(
            RowDefinition(
                colname=self.colname,
                label="7.0 and above",
                condition=(self.main_df[self.colname] >= 7.0),
                columns=columns,
                drop=True,
            )
        )
        row_defs.add(
            RowDefinition(
                colname=self.colname,
                label="not measured",
                condition=(self.main_df[self.colname].isna()),
                columns=columns,
                drop=True,
            )
        )

        row_defs.add(row_mean)
        return row_defs
