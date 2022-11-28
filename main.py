from raffle import Raffle

def main():
    donations_csv = "drawing_files/donations.csv"
    prizes_csv = "drawing_files/prizes.csv"
    raffle = Raffle(donations_csv=donations_csv, prizes_csv=prizes_csv)
    winners = raffle.draw_winners()
    for winner in winners:
        print(winner)
if __name__ == "__main__":
    main()
