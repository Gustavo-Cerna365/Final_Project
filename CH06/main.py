import collections
from collections import deque

# ---------------------------------------------------------------------------
# PART 1 DATA: a small professional/social network
# ---------------------------------------------------------------------------
network = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "peggy": ["you", "maria"],   # cycle back to "you"!
    "anuj": [],
    "thom": ["diego"],
    "jonny": ["sam"],
    "maria": ["lee"],
    "diego": [],
    "sam": [],
    "lee": [],
}

# Which skill(s) each person has. Used by person_has_skill().
skills = {
    "you": ["project_management"],
    "alice": ["design"],
    "bob": ["sales"],
    "claire": ["marketing"],
    "peggy": ["finance"],
    "anuj": ["manufacturing"],
    "thom": ["design"],
    "jonny": ["sales"],
    "maria": ["manufacturing"],
    "diego": ["python"],
    "sam": ["python"],
    "lee": ["manufacturing"],
}


def person_has_skill(person, skill):
    return skill in skills.get(person, [])

def simple_hash(key, num_slots):
       return hash(key) % num_slots

class MiniHashTable:

    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.slots = [[] for _ in range(num_slots)]
        self.num_items = 0

    def insert(self, key, value):
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]

        for i in range(len(chain)):
            existing_key, existing_value = chain[i]
            if existing_key == key:
                chain[i] = (key, value)
                return

        chain.append((key, value))
        self.num_items += 1

    def get(self, key):
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]

        for existing_key, existing_value in chain:
            if existing_key == key:
                return existing_value

        return None

    def load_factor(self):
        return self.num_items / self.num_slots


def search(start_name, skill_to_find):
    search_queue = deque()
    search_queue.extend(network[start_name])  # Start with neighbors
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            searched.add(person) 
            print(f"Checking {person} for skill {skill_to_find}")
            if person_has_skill(person, skill_to_find):
                return True
            
            # Add neighbors without checking if they are in searched
            for neighbor in network[person]:
                search_queue.append(neighbor)

            print(f"Searched so far: {searched}")

    return False


# ---------------------------------------------------------------------------
# PART 2: shortest path (degree of separation), not just True/False
# ---------------------------------------------------------------------------

def search_shortest_path(start_name, skill_to_find):
    search_queue = deque((neighbor, 1) for neighbor in network[start_name])
    searched = set()
    
    while search_queue:
        person, distance = search_queue.popleft()
        
        if person not in searched:
            searched.add(person)  # Mark as searched immediately
            print(f"Checking {person} for skill {skill_to_find}, distance: {distance}")
            
            if person_has_skill(person, skill_to_find):
                return distance
            
            # Only add neighbors if they exist in the network
            for neighbor in network.get(person, []):
                if neighbor not in searched and neighbor not in [n[0] for n in search_queue]:
                    search_queue.append((neighbor, distance + 1))
                    print(f"Adding {neighbor} to search queue.")
    
    return -1


def search_with_path(start_name, skill_to_find):
    search_queue = deque(network[start_name])
    searched = set()
    came_from = {
        neighbor: start_name
        for neighbor in network[start_name]
    }

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            print(f"Checking {person} for skill {skill_to_find}")

            if person_has_skill(person, skill_to_find):
                path = [person]

                while path[-1] != start_name:
                    path.append(came_from[path[-1]])

                path.reverse()
                return path

            for neighbor in network[person]:
                if neighbor not in came_from:
                    came_from[neighbor] = person
                    search_queue.append(neighbor)

            searched.add(person)
            print(f"Added {person} to searched.")

    return []


# ---------------------------------------------------------------------------
# PART 3: topological sort mini-exercise
# ---------------------------------------------------------------------------
dependency_graph = {
    "create_repo_template": [],
    "write_starter_code": ["create_repo_template"],
    "write_tests": ["write_starter_code"],
    "create_classroom_assignment": ["write_starter_code", "write_tests"],
    "invite_students": ["create_classroom_assignment"],
    "grade_submissions": ["invite_students"],
}

proposed_order = [
    "create_repo_template",
    "write_starter_code",
    "write_tests",
    "create_classroom_assignment",
    "invite_students",
    "grade_submissions",
]


def is_valid_order(order, dep_graph):
    index_map = {step: index for index, step in enumerate(order)}

    for step, dependencies in dep_graph.items():
        for dependency in dependencies:
            if dependency in index_map and step in index_map:
                if index_map[dependency] >= index_map[step]:  # Step 3: Check the order
                    return False

    return True  # If all checks pass


def topological_sort(dep_graph):
    order = []  
    
    while len(order) < len(dep_graph):  
        found_step = False
        for step in dep_graph:  
            if step not in order:  
                if all(dep in order for dep in dep_graph[step]):
                    order.append(step)
                    found_step = True
                    break 

        if not found_step: 
            raise ValueError("Graph has a cycle or invalid dependencies.")

    return order 


if __name__ == "__main__":
    if __name__ == "__main__":
        print("Does anyone in my network know Python?",
          search("you", "python"))                     # Expect: True

        print("Does anyone know astronomy?",
          search("you", "astronomy"))                  # Expect: False

        print("Hops to nearest manufacturing contact:",
          search_shortest_path("you", "manufacturing")) # Expect: 2

        print("Hops to nearest python contact:",
          search_shortest_path("you", "python"))        # Expect: 3

        print("Hops to nonexistent skill:",
          search_shortest_path("you", "astronomy"))     # Expect: -1

        print("Path to manufacturing contact:",
          search_with_path("you", "manufacturing"))     # Expect: ['you', 'bob', 'anuj']
