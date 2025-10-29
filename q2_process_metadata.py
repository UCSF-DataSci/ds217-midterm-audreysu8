#!/usr/bin/env python3
# TODO: Add shebang line: #!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.


def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    dictionary = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                dictionary[key.strip()] = value.strip()
    return dictionary


def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    dictionary = {}
    if config["sample_data_rows"].isdigit() and int(config["sample_data_rows"]) > 0:
        dictionary["sample_data_rows"] = True
    else:
        dictionary["sample_data_rows"] = False
    if config["sample_data_min"].isdigit() and int(config["sample_data_min"]) >= 1:
        dictionary["sample_data_min"] = True
    else:
        dictionary["sample_data_min"] = False
    if config["sample_data_max"].isdigit() and int(config["sample_data_max"]) > int(config["sample_data_min"]):
        dictionary["sample_data_max"] = True
    else:
        dictionary["sample_data_max"] = False
    return dictionary

    


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # TODO: Parse config values (convert strings to int)
    sample_data_rows = int(config['sample_data_rows'])
    sample_data_min = int(config['sample_data_min'])
    sample_data_max = int(config['sample_data_max'])
    # TODO: Generate random numbers and save to file 

    # TODO: Use random module with config-specified range
    import random
    with open(filename, 'w') as file:
        for _ in range(sample_data_rows):
            number = random.randint(sample_data_min, sample_data_max)
            file.write(f"{number}\n")
    


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    dictionary = {}
    dictionary["mean"] = sum(data) / len(data)
    new = data.copy()
    new.sort()
    length = len(new)
    if length % 2 == 0:
        dictionary["median"] = (new[length // 2 - 1] + new[length // 2]) / 2
    else:
        dictionary["median"] = new[length // 2]
    dictionary["sum"] = sum(data)
    dictionary["count"] = len(data)
    return dictionary


if __name__ == '__main__':
    # TODO: Test your functions with sample data
    # Example:
    config = parse_config('q2_config.txt')
    validation = validate_config(config)
    generate_sample_data('data/sample_data.csv', config)
    print("Configuration:", config)
    print("Validation Results:", validation)
    # TODO: Read the generated file and calculate statistics
    with open('data/sample_data.csv', 'r') as file:
        data = [int(line.strip()) for line in file if line.strip().isdigit()]
    stats = calculate_statistics(data)
    # TODO: Save statistics to output/statistics.txt
    with open('output/statistics.txt', 'w') as file:
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")
    
