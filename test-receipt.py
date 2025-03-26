import os

def compare_groceries(yolo_results_file, target_groceries_file):
    """
    Compares YOLO recognition results against a target grocery list.

    Args:
        yolo_results_file (str): Path to the YOLO results text file.
        target_groceries_file (str): Path to the target grocery list text file.

    Returns:
        tuple: (found_groceries, missing_groceries)
            found_groceries (list): List of groceries found in the YOLO results.
            missing_groceries (list): List of groceries from the target list that were not found.
            extra_detections (list): List of groceries detected by YOLO but not in the target list.
    """
    found_groceries = []
    missing_groceries = []
    extra_detections = []

    # Check if files exist
    if not os.path.exists(yolo_results_file):
        print(f"Error: YOLO results file not found at {yolo_results_file}")
        return [], [], []  # Return empty lists to avoid errors later

    if not os.path.exists(target_groceries_file):
        print(f"Error: Target groceries file not found at {target_groceries_file}")
        return [], [], []

    try:
        # Read YOLO results from the text file
        with open(yolo_results_file, 'r') as f:
            yolo_results = [line.strip().lower() for line in f]  # Read and lowercase

        # Read target groceries from the text file
        with open(target_groceries_file, 'r') as f:
            target_groceries = [line.strip().lower() for line in f]  # Read and lowercase

        # Find common groceries
        for grocery in target_groceries:
            if grocery in yolo_results:
                found_groceries.append(grocery)
            else:
                missing_groceries.append(grocery)

        # Find extra detections (items detected by YOLO but not in target list)
        for item in yolo_results:
            if item not in target_groceries:
                extra_detections.append(item)

        return found_groceries, missing_groceries, extra_detections

    except Exception as e:
        print(f"An error occurred: {e}")
        return [], [], []  # Return empty lists in case of any error


def main():
    """
    Main function to run the grocery comparison.  Prompts the user for the file names.
    """
    yolo_results_file = input("Enter the path to the YOLO results file: ")
    target_groceries_file = input("Enter the path to the target groceries file: ")

    found, missing, extra = compare_groceries(yolo_results_file, target_groceries_file)

    if found or missing or extra: # Only print if there is something to print
        print("\nComparison Results:")
        print("Found Groceries:", found)
        print("Missing Groceries:", missing)
        print("Extra Detections (Detected but not in target list):", extra)
    else:
        print("No groceries found or an error occurred.")



if __name__ == "__main__":
    main()

