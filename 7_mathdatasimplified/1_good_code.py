#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


Baixando os dados crus
======================
Neste script estamos baixando os Dados desde um Drive.
Construimos uma função de tal maneira que o código seja
mais limpo (ou seja, mais legível).
"""
import zipfile

import gdown
from pydantic import BaseModel


class RawLocation(BaseModel):
    url: str
    zip_path: str



def get_raw_data(raw_location: RawLocation) -> None:
    gdown.download(raw_location.url, raw_location.zip_path, quiet=False)
    with zipfile.ZipFile(raw_location.zip_path, "r") as zip_ref:
        zip_ref.extractall(".")



if __name__ == "__main__":
    raw_location = RawLocation(
        url="https://drive.google.com/uc?id=1jI1cmxqnwsmC-vbl8dNY6b4aNBtBbKy3",
        zip_path="Twitter.zip"
    )
    get_raw_data(raw_location=raw_location)
