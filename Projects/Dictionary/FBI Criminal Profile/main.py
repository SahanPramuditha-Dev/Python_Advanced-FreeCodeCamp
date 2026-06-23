from database import criminal_db

while True:
    print("\n===== CRIMINAL SEARCH SYSTEM =====")
    print("1. Search Criminal")
    print("2. Show All IDs")
    print("3. Show All Names")
    print("4. Filter by Risk Level")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ---------------- SEARCH ----------------
    if choice == "1":
        query = input("Search (name / offense / ID / case): ").lower()

        found = False

        for cid, data in criminal_db.items():
            if (
                query in cid.lower()
                or query in data["full_name"].lower()
                or query in data["offense_type"].lower()
                or query in data["case_id"].lower()
                or query in data["national_id"].lower()
            ):
                print("\n--- MATCH FOUND ---")
                print("ID:", cid)

                for key, value in data.items():
                    print(f"{key}: {value}")

                found = True

        if not found:
            print("No records found.")

    # ---------------- LIST IDS ----------------
    elif choice == "2":
        for cid in criminal_db:
            print(cid)

    # ---------------- LIST NAMES ----------------
    elif choice == "3":
        for cid, data in criminal_db.items():
            print(data["full_name"])
    

    elif choice == "4":
        level = input("Enter risk level (low / medium / high): ").lower()

        found = False

        for cid, data in criminal_db.items():
            if data["risk_level"].lower() == level:
                print("\n--- MATCH FOUND ---")
                print("ID:", cid)

                for key, value in data.items():
                    print(f"{key}: {value}")

                found = True

        if not found:
            print("No criminals found with that risk level.")

    # ---------------- EXIT ----------------
    elif choice == "5":
        print("System terminated.")
        break

    else:
        print("Invalid option.")