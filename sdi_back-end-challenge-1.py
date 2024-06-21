def calculate_optimized_cost(seats):
    # Define the capacities and costs of each car type
    car_types = [
        {'capacity': 5, 'cost': 5000, 'name': 'small'},
        {'capacity': 10, 'cost': 8000, 'name': 'medium'},
        {'capacity': 15, 'cost': 12000, 'name': 'large'}
    ]
    
    all_combinations = []

    # Check all combinations of cars
    for large in range((seats // car_types[2]['capacity']) + 1):
        for medium in range((seats // car_types[1]['capacity']) + 1):
            remaining_seats = seats - large * car_types[2]['capacity'] - medium * car_types[1]['capacity']
            if remaining_seats < 0:
                continue
            small = (remaining_seats + car_types[0]['capacity'] - 1) // car_types[0]['capacity']
            total_cost = large * car_types[2]['cost'] + medium * car_types[1]['cost'] + small * car_types[0]['cost']
            all_combinations.append((total_cost, {'small': small, 'medium': medium, 'large': large}))
    
    # Sort combinations by total cost (ascending) and by number of large cars (descending)
    all_combinations.sort(key=lambda x: (x[0], -x[1]['large']))
    
    return all_combinations

if __name__ == "__main__":
    while True:
        try:
            seats = int(input("Enter the number of seats (Enter -1 to End):"))
            if seats == -1:
                break
            if seats < 0:
                raise ValueError("Number of seats must be a positive integer.")
            
            # Calculate optimized cost and get car count
            all_combinations = calculate_optimized_cost(seats)
            
            # Print the result
            if all_combinations:
                print(f"Total cost for {seats} seat(s) is ${all_combinations[0][0]}")
                best_option = all_combinations[0][1]
                print(f"Type of Car:")
                if best_option['large'] > 0:
                    print(f"  {best_option['large']} Large")
                if best_option['medium'] > 0:
                    print(f"  {best_option['medium']} Medium")
                if best_option['small'] > 0:
                    print(f"  {best_option['small']} Small")   
                
                
            else:
                print("No valid combinations found for the given number of seats.")
        
        except ValueError as e:
            print(f"Error: {e}")