import pandas as pd
import random as rd
import numpy as np
from scipy.special import softmax
np.set_printoptions(precision=5)
import datetime
from tqdm import tqdm

SPORT = "tennis"
INPUT_DATA_PATH = f"DATA/raw/{SPORT}.csv"
OUTPUT_PATH = f"DATA/preprocessed/{SPORT}.csv"


COL_TO_KEEP = ["Date","Winner", "Loser", "AvgW", "AvgL", "Court", "Surface", "WRank","LRank", "WPts","LPts", "pl1_weight", "pl1_height", "pl1_hand", "pl2_weight", "pl2_height", "pl2_hand"]
DELTA_DATE = datetime.timedelta(days = 10) 

def execute(df):
    court_to_num = {
        "Outdoor":1,
        "Indoor":2
    }
    surface_to_num = {
        "Hard":1,
        "Grass":2,
        "Clay":3,
    }

    hands_to_num = {
        "Right-Handed":1,
        "Left-Handed":2
    }

    
    df = df[COL_TO_KEEP]
    df["Date"] = pd.to_datetime(df["Date"])
    print("df shape before drop : ", df.shape)
    df.dropna(inplace=True)
    print("df shape after drop : ", df.shape)
    df["Team1_end_state"] = np.random.choice(["w", "l"], df.shape[0])
    team1 = []
    team2 = []
    odds1 = []
    odds2 = []
    probs1 = []
    probs2 = []
    winner = []
    dates = []
    entropies1 = []
    entropies2 = []

    court = []
    surface = []

    rank1 = []
    pts1 = []
    weigth1 = []
    height1 = []
    hand1 = []

    rank2 = []
    pts2 = []
    weigth2 = []
    height2 = []
    hand2 = []

    for i_row, row in tqdm(df.iterrows()):
        odds = [row["AvgW"], row["AvgL"]]

        dates.append(row["Date"])
        court.append(court_to_num[row["Court"]])
        surface.append(surface_to_num[row["Surface"]])

        if row["Team1_end_state"] == "w":
            team1.append(row["Winner"])
            team2.append(row["Loser"])

            odds1.append(row["AvgW"])
            odds2.append(row["AvgL"])



            rank1.append(row["WRank"])
            pts1.append(row["WPts"])
            weigth1.append(row["pl1_weight"])
            height1.append(row["pl1_height"])
            hand1.append(hands_to_num[row["pl1_hand"]])

            rank2.append(row["LRank"])
            pts2.append(row["LPts"])
            weigth2.append(row["pl2_weight"])
            height2.append(row["pl2_height"])
            hand2.append(hands_to_num[row["pl2_hand"]])



            winner.append(1)
        else:
            team1.append(row["Loser"])
            team2.append(row["Winner"])

            odds1.append(row["AvgL"])
            odds2.append(row["AvgW"])

            rank2.append(row["WRank"])
            pts2.append(row["WPts"])
            weigth2.append(row["pl1_weight"])
            height2.append(row["pl1_height"])
            hand2.append(hands_to_num[row["pl1_hand"]])

            rank1.append(row["LRank"])
            pts1.append(row["LPts"])
            weigth1.append(row["pl2_weight"])
            height1.append(row["pl2_height"])
            hand1.append(hands_to_num[row["pl2_hand"]])

            winner.append(2)


    res = pd.DataFrame()
    res["Date"] = dates
    res["Surface"] = surface
    res["Court"] = court

    res["Team1"] = team1
    res["Odd1"] = odds1
    res["Rank1"] = rank1
    res["Pts1"] = pts1
    res["Weight1"] = weigth1
    res["Height1"] = height1
    res["Hand1"] = hand1
    

    res["Team2"] = team2
    res["Odd2"] = odds2
    res["Rank2"] = rank2
    res["Pts2"] = pts2
    res["Weight2"] = weigth2
    res["Height2"] = height2
    res["Hand2"] = hand2

    res["Winner"] = winner


    #save dataframe
    return res


if __name__ == "__main__":
    df = pd.read_csv(INPUT_DATA_PATH)
    res = execute(df)
    res.to_csv(OUTPUT_PATH,index=False)