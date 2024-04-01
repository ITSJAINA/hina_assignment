import matplotlib.pyplot as plt

# Function to read CSV file
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            data.append(dict(zip(header, values)))
    return data

# Function to create subplots
def create_subplots(data):
    # Initialize counts dictionaries for each category
    vehicle_counts = {}
    weather_counts = {}
    economic_counts = {}

    # Count occurrences of each category
    for entry in data:
        vehicle_type = entry['Vehicle Type']
        weather = entry['Weather']
        economic_condition = entry['Economic Condition']

        vehicle_counts[vehicle_type] = vehicle_counts.get(vehicle_type, 0) + 1
        weather_counts[weather] = weather_counts.get(weather, 0) + 1
        economic_counts[economic_condition] = economic_counts.get(economic_condition, 0) + 1

    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Plot for Vehicle Type
    axs[0].bar(vehicle_counts.keys(), vehicle_counts.values())
    axs[0].set_title('Vehicle Type')

    # Plot for Weather
    axs[1].bar(weather_counts.keys(), weather_counts.values())
    axs[1].set_title('Weather')

    # Plot for Economic Condition
    axs[2].bar(economic_counts.keys(), economic_counts.values())
    axs[2].set_title('Economic Condition')

    plt.tight_layout()
    plt.show()

# Read data from CSV
data = read_csv('dt.csv')

# Create subplots
create_subplots(data)


