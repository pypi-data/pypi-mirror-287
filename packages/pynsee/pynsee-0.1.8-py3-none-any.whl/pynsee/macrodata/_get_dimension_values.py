# -*- coding: utf-8 -*-
# Copyright : INSEE, 2021

import xml.etree.ElementTree as ET
import pandas as pd
import os

from pynsee.utils._get_temp_dir import _get_temp_dir
from pynsee.utils._request_insee import _request_insee
from pynsee.utils.save_df import save_df

@save_df(day_lapse_max=90)
def _get_dimension_values(cl_dimension, update=False, silent=True, insee_date_test=None):

    INSEE_sdmx_link_codelist = "https://www.bdm.insee.fr/series/sdmx/codelist/FR1"
    INSEE_api_link_codelist = "https://api.insee.fr/series/BDM/V1/codelist/FR1"

    INSEE_sdmx_link_codelist_dimension = INSEE_sdmx_link_codelist + "/" + cl_dimension
    INSEE_api_link_codelist_dimension = INSEE_api_link_codelist + "/" + cl_dimension

    results = _request_insee(
            sdmx_url=INSEE_sdmx_link_codelist_dimension,
            api_url=INSEE_api_link_codelist_dimension,
        )

    # create temporary directory
    dirpath = _get_temp_dir()

    dimension_file = os.path.join(dirpath, "dimension_file")

    with open(dimension_file, "wb") as f:
        f.write(results.content)

    root = ET.parse(dimension_file).getroot()

    if os.path.exists(dimension_file):
        os.remove(dimension_file)

    list_values = []

    id = next(iter(root[1][0][0].attrib.values()))
    name_fr = root[1][0][0][0].text
    name_en = root[1][0][0][1].text

    dataset = {"id": [id], "name_fr": [name_fr], "name_en": [name_en]}

    dt = pd.DataFrame(dataset, columns=["id", "name_fr", "name_en"])

    list_values.append(dt)

    data = root[1][0][0]

    n_values = len(data)

    def extract_name_fr(data, i):
        try:
            name_fr = data[i][0].text
        except:
            name_fr = None
        finally:
            return name_fr

    def extract_name_en(data, i):
        try:
            name_en = data[i][1].text
        except:
            name_en = None
        finally:
            return name_en

    def extract_id(data, i):
        try:
            id = data[i].attrib.values()
        except:
            id = None
        finally:
            return id

    for i in range(2, n_values):

        id = next(iter(extract_id(data, i)))
        name_fr = extract_name_fr(data, i)
        name_en = extract_name_en(data, i)

        dataset = {"id": [id], "name_fr": [name_fr], "name_en": [name_en]}

        dt = pd.DataFrame(dataset, columns=["id", "name_fr", "name_en"])

        list_values.append(dt)

    df_dimension_values = pd.concat(list_values)

    return df_dimension_values
