import conducto as co

# Island Information:
# hawaii -> echo big island
# maui county:
#     maui -> echo valley isle
#     lanai -> echo pineapple isle
#     molokai -> echo friendly isle
#     kahoolawe -> echo target isle
# oahu -> echo gathering place
# kauai county:
#     kauai -> echo garden isle
#     niihau -> echo forbidden isle



def islands() -> co.Serial:
    with co.Serial() as pipeline:
        pipeline["hawaii"] = co.Exec("echo big island")
        with co.Parallel(name="maui_county") as maui_county:
            maui_county["maui"] = co.Exec("echo valley isle")
            maui_county["lanai"] = co.Exec("echo pineapple isle")
            maui_county["molokai"] = co.Exec("echo friendly isle")
            maui_county["kahoolawe"] = co.Exec("echo target isle")
        pipeline["oahu"] = co.Exec("echo gathering place")
        with co.Serial(name="kauai_county") as kauai_county:
            kauai_county["kauai"] = co.Exec("echo garden isle")
            kauai_county["niihau"] = co.Exec("echo forbidden isle")
    return pipeline

if __name__ == "__main__":
    co.main()