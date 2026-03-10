def show_data(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_data(name="Ly", age=24, city="Madrid")