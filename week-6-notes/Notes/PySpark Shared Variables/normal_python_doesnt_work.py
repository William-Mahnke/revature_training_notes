# driver_counter = 0

# def increment_on_worker(_):
#     global driver_counter
#     driver_counter += 1

# sc.parallelize(range(1, 11), 4).foreach(
#     increment_on_worker
# )

# print(driver_counter)
# # Driver value normally stays 0