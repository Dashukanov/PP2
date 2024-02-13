import json

def main():
    with open("sample-data.json", "r") as file:
        data = json.load(file)

    print("Interface Status")
    print("=" * 80)
    print("{:<50}{:<20}{:<8}{:<8}".format("DN", "Description", "Speed", "MTU"))
    print("-" * 80)

    for entry in data["imdata"]:
        dn = entry["fvCEp"]["attributes"]["dn"]
        description = entry["fvCEp"]["attributes"].get("descr", "")
        speed = entry["fvCEp"]["attributes"].get("speed", "inherit")
        mtu = entry["fvCEp"]["attributes"].get("mtu", "")
        print("{:<50}{:<20}{:<8}{:<8}".format(dn, description, speed, mtu))

if __name__ == "__main__":
    main()