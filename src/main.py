import pandas as pd
from __old.core import methods as m1
from __old.core import HelperTools as ht

from src.config import pdict


@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz = pd.read_csv("datasets/" + pdict["file_geodat_plz"], delimiter=";")

    df_lstat = pd.read_csv("datasets/" + pdict["file_lstations"], delimiter=",")
    df_lstat2 = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3 = m1.count_plz_occurrences(df_lstat2)

    df_residents = pd.read_csv("datasets/" + pdict["file_residents"], delimiter=",")
    gdf_residents2 = m1.preprop_resid(df_residents, df_geodat_plz, pdict)

    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)


if __name__ == "__main__":
    main()
