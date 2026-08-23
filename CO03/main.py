def trace_enter(label, depth):
    indent = "  " * depth
    print(indent + "-> entering: " + str(label))


def trace_exit(label, depth):
    indent = "  " * depth
    print(indent + "<- exiting: " + str(label))

sample_structure = {
    "name": "root",
    "type": "folder",
    "contents": [
        {"name": "readme.txt", "type": "file", "size": 120},
        {
            "name": "docs",
            "type": "folder",
            "contents": [
                {"name": "notes.txt", "type": "file", "size": 200},
            ],
        },
        {"name": "empty_folder", "type": "folder", "contents": []},
    ],
}

# Exercise 1: Implementing Find File
def find_file(structure, target_name, current_path="", depth=0):
    new_path = current_path + "/" + structure["name"]
    trace_enter(new_path, depth)

    if structure["type"] == "file":
        if structure["name"] == target_name:
            trace_exit(new_path + " (FOUND!)", depth)
            return new_path
        trace_exit(new_path, depth)
        return None

    if structure["type"] == "folder":
        for item in structure["contents"]:
            result = find_file(item, target_name, new_path, depth + 1)
            if result is not None: 
                trace_exit(new_path, depth)
                return result

        trace_exit(new_path + " (NOT FOUND)", depth)  # Added for clarity
    return None

#Exercise 2: Implementing Count Files
def count_files(structure, depth=0):
    trace_enter(structure["name"], depth)

    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return 1

    if structure["type"] == "folder":
        total = 0
        for item in structure["contents"]:
            total += count_files(item, depth + 1)  # Sum counts
        trace_exit(structure["name"], depth)
        return total  # Return the total count

    trace_exit(structure["name"], depth)
    return 0


# Exercise 3: Implement Total Size

def total_size(structure, depth=0):
    trace_enter(structure["name"], depth)

    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return structure["size"]

    if structure["type"] == "folder":
        running_total = 0
        for item in structure["contents"]:
            running_total += total_size(item, depth + 1)
        trace_exit(structure["name"], depth)
        return running_total

    trace_exit(structure["name"], depth)
    return 0

# Implementing print tree with depth

def print_tree_with_depth(structure, depth=0):
    print("  " * depth + structure["name"]) 

    if structure["type"] == "folder":
        for item in structure["contents"]:
            print_tree_with_depth(item, depth + 1)  

# Test Cases
if __name__ == "__main__":
    print("Find File:")
    print(find_file(sample_structure, "notes.txt"))

    print("\nCount Files:")
    print(count_files(sample_structure))

    print("\nTotal Size:")
    print(total_size(sample_structure))

    print("\nFile Tree:")
    print_tree_with_depth(sample_structure)
