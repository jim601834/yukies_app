import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem

def create_pandas_model(df: pd.DataFrame) -> QStandardItemModel:
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(df.columns.tolist())
    for row in df.itertuples(index=False):
        items = [QStandardItem(f"{cell:.2f}" if isinstance(cell, (int, float)) else str(cell)) for cell in row]
        model.appendRow(items)
    return model