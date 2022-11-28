from csv import DictReader
import csv
import datetime
import os
import random
import math


class Raffle:
    def __init__(self, donations_csv, prizes_csv):
        self.donations = donations_csv
        self.prizes = prizes_csv

    def draw_winners(self):
        prizes = self.get_prizes(self.prizes)
        donations = self.get_donations(self.donations)
        raffle_tickets = self.raffle_tickets(donations)
        winners = []
        for prize in prizes:
            winner = random.choice(raffle_tickets)
            winner_name = donations[winner - 1]
            winner = dict([(prize["prize"], winner_name["name"])])
            winners.append(winner)
            self.raffle_winners_audit(winner)
        return winners

    def raffle_tickets(self, donations):
        raffle_tickets = []
        for index, donation in enumerate(donations, start=1):
            donation_amount = int(donation["donation_amount"])
            num_tickets = math.trunc(donation_amount / 5)

            for i in range(num_tickets):
                raffle_tickets.append(index)

        random.shuffle(raffle_tickets)
        self.raffle_tickets_audit(raffle_tickets)
        return raffle_tickets

    def get_donations(self, donations):

        with open(donations, "r") as file:
            reader = DictReader(file)
            list_of_donations = list(reader)

        return list_of_donations

    def get_prizes(self, prizes):
        with open(prizes, "r") as file:
            list_of_prizes = list(csv.DictReader(file))
        return list_of_prizes

    def raffle_tickets_audit(self, tickets):
        audit_file = "audit/raffle_tickets_audit.csv"
        if not os.path.exists(audit_file):
            print(f"creating: {audit_file}")
            headers = ["raffle_tickets_order", "time_stamp"]
            with open(audit_file, mode="a", newline="") as csv_file:
                w = csv.DictWriter(csv_file, fieldnames=headers)
                w.writeheader()

        with open(audit_file, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([tickets,datetime.datetime.now(datetime.timezone.utc)])

    def raffle_winners_audit(self, winners):
        audit_file = "audit/raffle_winners_audit.csv"
        if not os.path.exists(audit_file):
            print(f"creating: {audit_file}")
            headers = ["prize", "winner_name", "time_stamp"]
            with open(audit_file, mode="a", newline="") as csv_file:
                w = csv.DictWriter(csv_file, fieldnames=headers)
                w.writeheader()

        with open(audit_file, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in winners.items():
                writer.writerow(
                    [key, value, datetime.datetime.now(datetime.timezone.utc)]
                )

