import time

import faker

fake = faker.Faker()


def make_file():
    with open("100k.txt", "w") as file:
        for i in range(0, 100000):
            file.write(f"'{fake.name()}',\n")


if __name__ == "__main__":
    # Start measuring time
    start_time = time.perf_counter()

    # Make names
    make_file()

    # Calculate and display time elapsed
    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1000
    print("Elapsed time: {:.2f} milliseconds\n".format(elapsed))
