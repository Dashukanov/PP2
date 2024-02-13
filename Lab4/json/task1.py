import json

def main():
    with open("C:\\Users\\admin\\Desktop\\repos\\PP2\\PP2-3\\Lab4\\json\\sample-data.json", "r") as file:
        data = json.load(file)

    print("Interface Status")
    print("=" * 80)
    print("{:<50}{:<20}{:<8}{:<8}".format("DN", "Description", "Speed", "MTU"))
    print("-" * 80)

    for entry in data["imdata"]:
        dn = entry["l1PhysIf"]["attributes"]["dn"]
        description = entry["l1PhysIf"]["attributes"].get("descr", "")
        speed = entry["l1PhysIf"]["attributes"].get("speed", "inherit")
        mtu = entry["l1PhysIf"]["attributes"].get("mtu", "")
        print("{:<50}{:<20}{:<8}{:<8}".format(dn, description, speed, mtu))

if __name__ == "__main__":
    main()


