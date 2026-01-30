from datetime import datetime, timedelta


def make_commits(start_date: datetime, days: int):
    current_date = start_date

    for _ in range(days):
        text_date = current_date.strftime("%d.%m.%Y г.")

        with open("test.txt", "a", encoding="utf-8") as f:
            f.write(f"{text_date}\n")

        current_date += timedelta(days=1)


def main():
    start_date = datetime(2000, 1, 1)
    days = 31

    make_commits(start_date, days)


if __name__ == "__main__":
    main()
