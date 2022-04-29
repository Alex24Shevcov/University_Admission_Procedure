N = int(input())

arr_candidates = []
dict_of_received = {"Engineering": [], "Chemistry": [], "Biotech": [], "Mathematics": [], "Physics": []}

with open("applicants.txt", "r") as file:
	for line in file.readlines():
		name, surename, phisics_score, chemistry_score,\
		mathematics_score, informatics_score,\
		special_score, priority_1, priority_2, priority_3 = line.split()
		arr_candidates.append((name, surename, phisics_score, chemistry_score, mathematics_score, informatics_score,
							   special_score, priority_1, priority_2, priority_3))


def sort_list_of_tuples(priority: str, arr_tuples: list) -> list:
	sorted_list_by_alphabet = sorted(arr_tuples, key=lambda x: (x[0], x[1]))
	if priority == "Engineering":
		sorted_list_by_scores = sorted(sorted_list_by_alphabet, key=lambda x: max(eval(f"({x[4]} + {x[5]}) / 2"), float(x[6])), reverse=True)
	elif priority == "Chemistry":
		sorted_list_by_scores = sorted(sorted_list_by_alphabet, key=lambda x: max(float(x[3]), float(x[6])), reverse=True)
	elif priority == "Biotech":
		sorted_list_by_scores = sorted(sorted_list_by_alphabet, key=lambda x: max(eval(f"({x[2]} + {x[3]}) / 2"), float(x[6])), reverse=True)
	elif priority == "Mathematics":
		sorted_list_by_scores = sorted(sorted_list_by_alphabet, key=lambda x: max(float(x[4]), float(x[6])), reverse=True)
	elif priority == "Physics":
		sorted_list_by_scores = sorted(sorted_list_by_alphabet, key=lambda x: max(eval(f"({x[2]} + {x[4]}) / 2"), float(x[6])), reverse=True)
	return sorted_list_by_scores


def step_first(arr_candidates, n_priority) -> list:
	matrix = [tup[:] for tup in arr_candidates]

	temp_dict_of_received = {"Engineering": [],
							 "Chemistry": [],
							 "Biotech": [],
							 "Mathematics": [],
							 "Physics": []}


	for tup in matrix:
		name = tup[0]
		surename = tup[1]
		phisics_score = tup[2]
		chemistry_score = tup[3]
		mathematics_score = tup[4]
		informatics_score = tup[5]
		special_score = tup[6]
		arr_facultyes = []
		arr_facultyes.append(tup[7])
		arr_facultyes.append(tup[8])
		arr_facultyes.append(tup[9])
		if arr_facultyes[n_priority] == "Engineering" and len(dict_of_received["Engineering"]) != N:
			temp_dict_of_received["Engineering"].append((name,
														 surename,
														 phisics_score,
														 chemistry_score,
														 mathematics_score,
														 informatics_score,
														 special_score,
														 arr_facultyes[0],
														 arr_facultyes[1],
														 arr_facultyes[2]))
		elif arr_facultyes[n_priority] == "Chemistry" and len(dict_of_received["Chemistry"]) != N:
			temp_dict_of_received["Chemistry"].append((name,
														 surename,
														 phisics_score,
														 chemistry_score,
														 mathematics_score,
														 informatics_score,
														 special_score,
														 arr_facultyes[0],
														 arr_facultyes[1],
														 arr_facultyes[2]))

		elif arr_facultyes[n_priority] == "Biotech" and len(dict_of_received["Biotech"]) != N:
			temp_dict_of_received["Biotech"].append((name,
														 surename,
														 phisics_score,
														 chemistry_score,
														 mathematics_score,
														 informatics_score,
														 special_score,
														 arr_facultyes[0],
														 arr_facultyes[1],
														 arr_facultyes[2]))

		elif arr_facultyes[n_priority] == "Mathematics" and len(dict_of_received["Mathematics"]) != N:
			temp_dict_of_received["Mathematics"].append((name,
														 surename,
														 phisics_score,
														 chemistry_score,
														 mathematics_score,
														 informatics_score,
														 special_score,
														 arr_facultyes[0],
														 arr_facultyes[1],
														 arr_facultyes[2]))

		elif arr_facultyes[n_priority] == "Physics" and len(dict_of_received["Physics"]) != N:
			temp_dict_of_received["Physics"].append((name,
														 surename,
														 phisics_score,
														 chemistry_score,
														 mathematics_score,
														 informatics_score,
														 special_score,
														 arr_facultyes[0],
														 arr_facultyes[1],
														 arr_facultyes[2]))


	arr_engineering = sort_list_of_tuples("Engineering", temp_dict_of_received["Engineering"])[:N]
	arr_chemistry = sort_list_of_tuples("Chemistry", temp_dict_of_received["Chemistry"])[:N]
	arr_biotech = sort_list_of_tuples("Biotech", temp_dict_of_received["Biotech"])[:N]
	arr_mathematics = sort_list_of_tuples("Mathematics", temp_dict_of_received["Mathematics"])[:N]
	arr_physics = sort_list_of_tuples("Physics", temp_dict_of_received["Physics"])[:N]

	for tup in arr_engineering + arr_chemistry + arr_biotech + arr_mathematics + arr_physics:
		if tup in matrix:
			matrix.remove(tup)

	for key, values in dict_of_received.items():
		i = 0
		try:
			while N - len(values) > 0:
				if key == "Engineering":
					dict_of_received[key].append(arr_engineering[i])
				elif key == "Chemistry":
					dict_of_received[key].append(arr_chemistry[i])
				elif key == "Biotech":
					dict_of_received[key].append(arr_biotech[i])
				elif key == "Mathematics":
					dict_of_received[key].append(arr_mathematics[i])
				elif key == "Physics":
					dict_of_received[key].append(arr_physics[i])
				i += 1
		except IndexError:
			...

	return matrix


def check_facultyes_and_condidates(dictionary: dict, arr_candidates: list) -> bool:
	if len(arr_candidates) == 0:
		return True

	for values in dictionary.values():
		if len(values) < N:
			return False
	return True


def show_and_write_to_file_enrollees(priority: str, arr_tuples: list):
	sorted_arr = sort_list_of_tuples(priority, arr_tuples)
	with open(f"{priority.lower()}.txt", "w") as file:
		for tup in sorted_arr:
			if priority == "Engineering":
				line = f"{tup[0]} {tup[1]} {max(eval(f'({tup[4]} + {tup[5]}) / 2'), float(tup[6]))}"
				file.write(line + "\n")
				print(line)
			elif priority == "Chemistry":
				line = f"{tup[0]} {tup[1]} {max(float(tup[3]), float(tup[6]))}"
				file.write(line + "\n")
				print(line)
			elif priority == "Biotech":
				line = f"{tup[0]} {tup[1]} {max(eval(f'({tup[2]} + {tup[3]}) / 2'), float(tup[6]))}"
				file.write(line + "\n")
				print(line)
			elif priority == "Mathematics":
				line = f"{tup[0]} {tup[1]} {max(float(tup[4]), float(tup[6]))}"
				file.write(line + "\n")
				print(line)
			elif priority == "Physics":
				line = f"{tup[0]} {tup[1]} {max(eval(f'({tup[2]} + {tup[4]}) / 2'), float(tup[6]))}"
				file.write(line + "\n")
				print(line)


i = 0
while not check_facultyes_and_condidates(dict_of_received, arr_candidates):
	arr_candidates = step_first(arr_candidates, i)
	i += 1

for key, arr_tuples in sorted(dict_of_received.items()):
	print(key)
	show_and_write_to_file_enrollees(key, arr_tuples)
	print()